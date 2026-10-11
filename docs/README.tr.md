<p align="center">
  <img src="../assets/readme/hero.png" width="100%" alt="Harika Claude Modları">
</p>

<h1 align="center">Harika Claude Modları</h1>

<p align="center"><b>Claude Code modlarının ve değiştirdikleri daha derin davranışların kanıt derecelendirmeli dizini.</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-506-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="../LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
  <a href="https://wh000wh000.github.io/awesome-claude-mods/"><img src="https://img.shields.io/badge/site-searchable-1f6feb" alt="site"></a>
</p>

<p align="center"><sub><a href="../README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.pt-BR.md">Português</a> · <a href="README.ru.md">Русский</a> · <a href="README.it.md">Italiano</a> · <a href="README.ar.md">العربية</a> · <a href="README.hi.md">हिन्दी</a> · <b>Türkçe</b> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.pl.md">Polski</a> · <a href="README.nl.md">Nederlands</a> · <a href="README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **Güncel dizin** · Son senkronizasyon: `2026-10-11T21:12:49+08:00` (UTC+8)
> · Kayıtlar: **506** · Son güncellemede eklenenler: **0** · Uygulama dilleri: **12**

<sub>Aşağıdaki her kayıt otomatik olarak toplandı, filtrelendi ve yeniden kontrol edildi. Burada ücretli yerleştirme yoktur.</sub>

<a id="featured"></a>

## Anın seçkileri

<sub>Her kategoriden bir giriş; kanıt derecesine ve yıldızlara göre sıralanır, her güncellemede yeniden hesaplanır. Bu bir sıralamadır, onay değildir; her seçki aşağıdaki tam kartına bağlantı verir. Ekran görüntüsü veya kayıt yayınlayan projeler tercih edilir, böylece şerit görsel kalır.</sub>

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
<sub>Hayalet belirteçleri bul. Onları düzelt. Sıkıştırmadan sağ çık. Bağlam kalitesinin bozulmasını önle.</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo">
<b>🧵 <a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b>
<sub>⭐74325 · TypeScript · 👁️ observed</sub>
<sub>🌊 Özgün agent harness. Akıllı çok oyunculu sürüleri dağıtın, otonom iş akışlarını koordine edin ve konuşmaya dayalı AI sistemleri oluşturun. Uyarlanabilir bellek,…</sub>
</td>
<td width="50%" valign="top">
<b>📰 <a href="https://news.ycombinator.com/item?id=49925102">Claude Code Mods</a></b>
<sub>⭐6 · 👁️ observed</sub>
</td>
</tr>
</table>

## İçerik

- [Claude Code modu nedir](#claude-code-modu-nedir)
- [Kayıtlar nasıl derecelendiriliyor](#kayıtlar-nasıl-derecelendiriliyor)
- [Resmî: Anthropic'ın kendi depoları ve sürüm notları](#resmî-anthropicın-kendi-depoları-ve-sürüm-notları) — **15**
- [Modlar: mod yeteneği kullanılarak oluşturulanlar](#modlar-mod-yeteneği-kullanılarak-oluşturulanlar) — **381**
- [DSH ve Cordis eklenti ekosistemleri](#dsh-ve-cordis-eklenti-ekosistemleri) — **99**
- [Yazılar, tartışmalar ve videolar](#yazılar-tartışmalar-ve-videolar) — **11**
- [Uygulama diline göre projeler](#uygulama-diline-göre-projeler)

## Claude Code modu nedir

Claude Code, 2.1.287 sürümünde **modlar** kazandı: bir eklentinin değiştirebileceğinden daha derin davranışları değiştirebilen ve kendi arayüzünü çizebilen uzantılar.

Bir mod, istemin çevresine **satır, şerit, bölme veya kart** çizmek için `ui.render` öğesine bağlanabilir, `$.ui.selection()` ile en son seçtiğiniz metni okuyabilir, `agent.spawn` ile ekip arkadaşları oluşturabilir ve bir `Client` bölgesinin sahibi olabilir. Çizim yapamayan bir mod yalnızca kendisi başarısız olur — `ui.fault`, tek bir bozuk modun oturumu devre dışı bırakmasını önler.

Bu liste modları, bunların üzerine kurulduğu eklenti ve hook yüzeyini ve DSH ile Cordis karşılıklarını kapsar. Daha geniş Claude Code ekosistemini özellikle **kapsamaz**: bir istem paketi mod değildir.

## Kayıtlar nasıl derecelendiriliyor

Bu alandaki listelerin çoğu, nelerin dahil olduğunu belirtmekle yetinir. Bu liste ise gerçekte ne kadarının doğrulandığını açıklar ve buna göre filtreleme yapmanıza olanak tanır. Bir derece, projenin kalitesini değil kanıtı tanımlar — hakkında henüz kimsenin yazmadığı, iyi geliştirilmiş bir mod yine de `inferred` olarak kalır.

| Derece                                                                                          | Anlamı                                                                                                                                                                                                           |
| ----------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `doğrudan Anthropic tarafından yayımlandı`                                                      | Doğrudan Anthropic tarafından yayımlandı veya resmî değişiklik günlüğünden okundu.                                                                                                                               |
| `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor`                        | Kendi metni mod yüzeyinin bir parçasından — `ui.render`, `ui.fault`, `agent.spawn`, `$.ui.selection()`, bir bölme, şerit veya kart — söz ediyor; yani yazar, gerçek API üzerine geliştirdiği bir şeyi açıklıyor. |
| `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` | Kendisini bir mod, eklenti veya hook olarak tanımlıyor, ancak metninde özellikle mod yüzeyinden söz edilmiyor. Gerçek, ancak doğrulanmamış.                                                                      |
| `yalnızca terminoloji eşleşmesine dayanıyor`                                                    | Yalnızca terminoloji eşleşmesine dayanıyor. İnanıldığı için değil, filtrenin denetlenebilir olması için dahil edildi.                                                                                            |

<a id="official"></a>

## Resmî: Anthropic&#x27;ın kendi depoları ve sürüm notları

Anthropic'ın kendi Claude Code depoları ve mod kapsamını tanımlayan sürümler. Özetlenmek yerine kaynaktan okuyun.

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></b> · ⭐150151 · TypeScript · ✅ official · 0 天</summary>

##### 📝 Özet

Claude Code terminalinizde çalışan, kod tabanınızı anlayan ve rutin görevleri yerine getirerek, karmaşık kodu açıklayarak ve git iş akışlarını doğal dil komutlarıyla yöneterek daha hızlı kod yazmanıza yardımcı olan aracı bir kodlama aracıdır.

<sub>🔧 Kodda kullanıldığı bulundu: `feed.xml`</sub>

##### 📌 Temel bilgiler

| Alan     | Değer                                                      |
| -------- | ---------------------------------------------------------- |
| Kategori | `Resmî: Anthropic&#x27;ın kendi depoları ve sürüm notları` |
| Kanıt    | `doğrudan Anthropic tarafından yayımlandı`                 |
| Dil      | TypeScript                                                 |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **150151** |
| Son gönderme   | 2026-10-10 |
| İlk listelenme | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b> · ⭐9473 · TypeScript · ✅ official · 1 天</summary>

##### 📝 Özet

Kaynak projede herhangi bir açıklama yayımlanmadı.

##### 📌 Temel bilgiler

| Alan     | Değer                                                      |
| -------- | ---------------------------------------------------------- |
| Kategori | `Resmî: Anthropic&#x27;ın kendi depoları ve sürüm notları` |
| Kanıt    | `doğrudan Anthropic tarafından yayımlandı`                 |
| Dil      | TypeScript                                                 |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **9473**   |
| Son gönderme   | 2026-10-09 |
| İlk listelenme | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-python">anthropics/claude-agent-sdk-python</a></b> · ⭐8248 · Python · ✅ official · 1 天</summary>

##### 📝 Özet

Kaynak projede herhangi bir açıklama yayımlanmadı.

##### 📌 Temel bilgiler

| Alan     | Değer                                                      |
| -------- | ---------------------------------------------------------- |
| Kategori | `Resmî: Anthropic&#x27;ın kendi depoları ve sürüm notları` |
| Kanıt    | `doğrudan Anthropic tarafından yayımlandı`                 |
| Dil      | Python                                                     |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **8248**   |
| Son gönderme   | 2026-10-09 |
| İlk listelenme | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-security-review">anthropics/claude-code-security-review</a></b> · ⭐6342 · Python · ✅ official · 241 天</summary>

##### 📝 Özet

An AI-powered security review GitHub Action using Claude to analyze code changes for security vulnerabilities.

##### 📌 Temel bilgiler

| Alan     | Değer                                                      |
| -------- | ---------------------------------------------------------- |
| Kategori | `Resmî: Anthropic&#x27;ın kendi depoları ve sürüm notları` |
| Kanıt    | `doğrudan Anthropic tarafından yayımlandı`                 |
| Dil      | Python                                                     |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **6342**   |
| Son gönderme   | 2026-02-11 |
| İlk listelenme | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-typescript">anthropics/claude-agent-sdk-typescript</a></b> · ⭐1797 · Shell · ✅ official · 1 天</summary>

##### 📝 Özet

Kaynak projede herhangi bir açıklama yayımlanmadı.

##### 📌 Temel bilgiler

| Alan     | Değer                                                      |
| -------- | ---------------------------------------------------------- |
| Kategori | `Resmî: Anthropic&#x27;ın kendi depoları ve sürüm notları` |
| Kanıt    | `doğrudan Anthropic tarafından yayımlandı`                 |
| Dil      | Shell                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **1797**   |
| Son gönderme   | 2026-10-09 |
| İlk listelenme | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/model-cards">anthropics/model-cards</a></b> · ⭐25 · ✅ official · 309 天</summary>

##### 📝 Özet

Supplementary materials for Claude Model Cards

##### 📌 Temel bilgiler

| Alan     | Değer                                                      |
| -------- | ---------------------------------------------------------- |
| Kategori | `Resmî: Anthropic&#x27;ın kendi depoları ve sürüm notları` |
| Kanıt    | `doğrudan Anthropic tarafından yayımlandı`                 |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **25**     |
| Son gönderme   | 2025-12-05 |
| İlk listelenme | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.287 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Özet

Claude Modları eklendi: eklentiler artık daha derin davranışları değiştirebilir. Sizi kollayan ve sizin veya Claude'nin gözden kaçırabileceği şeyleri işaretleyen yerleşik bir mod olan You should know eklendi. `/plugin enable cc-plugin-you-should-know@builtin` ile etkinleştirin (telemetrinin açık olduğu birinci taraf oturumları için)

##### 📌 Temel bilgiler

| Alan     | Değer                                                      |
| -------- | ---------------------------------------------------------- |
| Kategori | `Resmî: Anthropic&#x27;ın kendi depoları ve sürüm notları` |
| Kanıt    | `doğrudan Anthropic tarafından yayımlandı`                 |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| İlk listelenme | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.288 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Özet

Modlar için `$.ui.selection()` eklendi: tam ekran modunda en son seçtiğiniz metni, seçim tek bir döküm satırının içindeyse o satırı döndürür. Bir görünüm Claude Code yeniden başlatılmadan önce çizildiğinde, bir modun düğmesine basılmasının bazen farklı bir düğmenin eylemini çalıştırması düzeltildi. Bir eklenti veya mod istemin üzerinde satırlar gösterirken arka plan görevleri iletişim kutusu açıldığında tam ekran oturumlarının "unrecoverable interface error" ile kapanması düzeltildi. Yalnızca güncel olmayan kayıtlı bir ayarı okuduğunda `claude plugin test`'in modları uzaktan kapatılmış olarak bildirmesi düzeltildi

##### 📌 Temel bilgiler

| Alan     | Değer                                                      |
| -------- | ---------------------------------------------------------- |
| Kategori | `Resmî: Anthropic&#x27;ın kendi depoları ve sürüm notları` |
| Kanıt    | `doğrudan Anthropic tarafından yayımlandı`                 |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| İlk listelenme | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.289 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Özet

Birleşik kabuk komutunun iç içe bir bölümündeki deny veya ask kuralının, yönetilen makinelerde kullanıcı tarafından yüklenen bir modun onayını korumaması düzeltildi. Yükseltme sonrasındaki ilk oturumda yüklü modların yüklenmemesi düzeltildi. Ekip arkadaşları için `agent.spawn`, eklenti kancası olayları genelinde tek bir aracı kimliği ve `$.agent.list()` içinde boşta ve bekliyor durumları eklendi. Bir modun `ui.render` kancasının yazdığı bir değer çizilirken bir satırın hata vermesi sonucunda oturumların "unrecoverable interface error" ile sona ermesi düzeltildi; motor artık kendi satırını çiziyor. Bir modun bölmesindeki veya bandındaki sağa hizalı içeriğin kapatma işaretinin veya `\[-\]`'ün altında çizilmesi düzeltildi

##### 📌 Temel bilgiler

| Alan     | Değer                                                      |
| -------- | ---------------------------------------------------------- |
| Kategori | `Resmî: Anthropic&#x27;ın kendi depoları ve sürüm notları` |
| Kanıt    | `doğrudan Anthropic tarafından yayımlandı`                 |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| İlk listelenme | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.290 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Özet

Bir modun `turn.step` kancasının sonucuna `serverToolUses` eklendi: araç, danışman olan API tarafından kendisinin çalıştırdığı çağrıları; her birinin kimliği, adı, girdisi, başlangıç ve bitiş zamanlarıyla birlikte çağırır. Bir modun `tool.check` kancasının okuduğu soruya ve karara `ceiling` eklendi; bir araç için kuruluşun gerektirdiği onayın adı belirtildi. Eklenti kancalarının tür tanımlarına `ThemeKey` ve `Color` türleri eklendi; böylece bir düzenleyici, bir modun çiziminin adlandırabileceği tema renklerini listeler. `claude plugin validate` öğesine eklendi: bir modun bir geçiş sitesinde kaydettiği her kanca, bir `.catch` içerip içermediğiyle birlikte listelenir (`--json` altında `gatingHooks`). Bir modun `turn.step` sonucu düzeltildi

##### 📌 Temel bilgiler

| Alan     | Değer                                                      |
| -------- | ---------------------------------------------------------- |
| Kategori | `Resmî: Anthropic&#x27;ın kendi depoları ve sürüm notları` |
| Kanıt    | `doğrudan Anthropic tarafından yayımlandı`                 |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| İlk listelenme | 2026-10-06 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.292 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Özet

Eklendi: `prompt.autocomplete`, bir modun istem kutusunun otomatik tamamlama listesine kendi satırlarını eklemek için bağlandığı bir olay; modlar için `$.model.complete` öğesine istem önbellekleme eklendi: `prompt` ve `system` metin blokları alır ve bir blok üzerindeki `cache: true`, isteği o noktaya kadar önbelleğe alır; `agent.spawn` mod kancasına, çalıştırmaları ve indeksleriyle birlikte iş akışı ajanları eklendi, böylece bir mod onları reddedebilir; Write, Edit, NotebookEdit ve LSP satırları ile tekli Read, Grep ve Glob satırları düzeltildi, bir modun çağrıyı neden reddettiği gizleniyordu: satır artık nedeni gösteriyor; bir modun reddeden `config.set`, `state.set`, `env.set` veya `agent.spawn` kancası düzeltildi afte

##### 📌 Temel bilgiler

| Alan     | Değer                                                      |
| -------- | ---------------------------------------------------------- |
| Kategori | `Resmî: Anthropic&#x27;ın kendi depoları ve sürüm notları` |
| Kanıt    | `doğrudan Anthropic tarafından yayımlandı`                 |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| İlk listelenme | 2026-10-07 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.293 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Özet

Modlar için `$.tool.register`'e `isDeferred` eklendi: `false`, aracın şemasını araç aramasının arkasında olmak yerine başlangıçtan itibaren istemde listeler `classic.*` olaylarındaki bir modun kancalarının, eklenti kancaları çalışanı yeniden başlatılırken atlanması düzeltildi; bu durum ayar kancalarının onlarsız yanıt vermesine yol açıyordu `$.session.append` çağıran modlarda `claude plugin test`'ün başarısız olması düzeltildi; testler yeni `mock.session` ile eklenen satırları geri okuyabilir

##### 📌 Temel bilgiler

| Alan     | Değer                                                      |
| -------- | ---------------------------------------------------------- |
| Kategori | `Resmî: Anthropic&#x27;ın kendi depoları ve sürüm notları` |
| Kanıt    | `doğrudan Anthropic tarafından yayımlandı`                 |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| İlk listelenme | 2026-10-08 |

</details>

<details>
<summary><b>Bu kategoride daha fazlası</b> <sub>· 3</sub></summary>

- [Claude Code 2.1.295 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Modlar için `$.ui.notify` eklendi: kendi bildirim ayarınız üzerinden yerel bir…
- [Claude Code 2.1.296 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - `UserPromptSubmit` hook&#x27;u veya modun `prompt.submit` hook&#x27;u sırasında Esc ya da…
- [riffkit/skill](https://github.com/riffkit/skill) - Official Riffkit skill — riff a winning TikTok into your own short video from…

</details>

<a id="mods"></a>

## Modlar: mod yeteneği kullanılarak oluşturulanlar

Buradaki her giriş, Claude Code'un 2.1.287 sürümünde kazandığı yeteneğin kullanıldığına dair kanıt gösterir: `ui.render` üzerinden çizim yapar, bir bölmeye, banda veya karta sahip olur, `$.ui.selection()` okur, `agent.spawn` ile ekip arkadaşları oluşturur ya da açıkça mod olduğunu belirtir.

<details>
<summary>🧩 <b><a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b> · ⭐2534 · Python · 👁️ observed · 0 天</summary>

##### 📝 Özet

Hayalet belirteçleri bul. Onları düzelt. Sıkıştırmadan sağ çık. Bağlam kalitesinin bozulmasını önle.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Modlar: mod yeteneği kullanılarak oluşturulanlar`                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |
| Dil      | Python                                                                   |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **2534**   |
| Son gönderme   | 2026-10-10 |
| İlk listelenme | 2026-10-11 |

🏷 `agentskills` · `claude-code` · `claude-code-mod` · `claude-code-skill` · `claude-plugin` · `codex` · `context-engineering` · `context-window`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer animation"><br><sub>animasyonlu kayıt</sub></td>
</tr></table>

<sub>Yeniden dağıtıma izin veren bir lisans belirtilmediği için varlığa upstream deposundan doğrudan bağlantı veriliyor.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/awesome-claude-code-mods">karanb192/awesome-claude-code-mods</a></b> · ⭐484 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Özet

GitHub üzerinden taranan, her modun ağ üzerinden okuyabileceği, yazabileceği, çalıştırabileceği veya gönderebileceği şeylerle birlikte herkese açık Claude Code modlarının (işlev hooks'ları) topluluk kataloğu. https://mods.aidojo.si/'a göz atın

<sub>🔧 Kodda kullanıldığı bulundu: `data/seeds.txt`, `data/duplicates.txt`, `README.md`, `data/repos.txt`</sub>

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Modlar: mod yeteneği kullanılarak oluşturulanlar`                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |
| Dil      | JavaScript                                                               |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **484**    |
| Son gönderme   | 2026-10-11 |
| İlk listelenme | 2026-10-04 |

🏷 `anthropic` · `awesome` · `awesome-list` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/cache-tax">karanb192/cache-tax</a></b> · ⭐127 · TypeScript · 👁️ observed · 7 天</summary>

##### 📝 Özet

Molalar sırasında Claude Code'un prompt önbelleğini sıcak tutun ve soğuk gönderimden önce tahmini maliyeti gösterin.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Modlar: mod yeteneği kullanılarak oluşturulanlar`                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |
| Dil      | TypeScript                                                               |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **127**    |
| Son gönderme   | 2026-10-04 |
| İlk listelenme | 2026-10-10 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `function-hooks` · `prompt-caching`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/karanb192--cache-tax/9ba5b1dbc9440791.png" width="100%" alt="karanb192/cache-tax screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/karanb192--cache-tax/e1a7cdd41b0efd1b.gif" width="100%" alt="karanb192/cache-tax animation"><br><sub>animasyonlu kayıt · <a href="https://raw.githubusercontent.com/karanb192/cache-tax/main/docs/assets/cache-cost-explainer.mp4">Videoyu aç</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/awss1i/assay">awss1i/assay</a></b> · ⭐104 · HTML · 👁️ observed · 0 天</summary>

##### 📝 Özet

Web sayfaları için aracı-yerel bir QA CLI. Deterministik, yazılacak test yok, LLM yok.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Modlar: mod yeteneği kullanılarak oluşturulanlar`                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |
| Dil      | HTML                                                                     |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **104**    |
| Son gönderme   | 2026-10-10 |
| İlk listelenme | 2026-10-10 |

🏷 `agentic-ai` · `ai-agents` · `browser-automation` · `claude-code` · `claude-code-mod` · `cli` · `code-generation` · `developer-tools`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hellosverre/claude-skins">hellosverre/claude-skins</a></b> · ⭐93 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Özet

Claude Code için görünümler: simgeli araç satırları, diff, tablo ve Mermaid grafik kartları, kullanım bandı ve on beş tema. /skin bunları canlı olarak değiştirir.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Modlar: mod yeteneği kullanılarak oluşturulanlar`                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |
| Dil      | TypeScript                                                               |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **93**     |
| Son gönderme   | 2026-10-10 |
| İlk listelenme | 2026-10-10 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hellosverre--claude-skins/e70c992c52ca2e70.gif" width="100%" alt="hellosverre/claude-skins animation"><br><sub>animasyonlu kayıt</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NahumLitvin/prismantis">NahumLitvin/prismantis</a></b> · ⭐74 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Özet

Renkli, temalandırılabilir Claude Code yanıtları: 15 temada tablolar, kod, diyagramlar, grafikler ve araç satırları; kopyalama düğmeleriyle. Bir Claude Code modu.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Modlar: mod yeteneği kullanılarak oluşturulanlar`                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |
| Dil      | TypeScript                                                               |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **74**     |
| Son gönderme   | 2026-10-11 |
| İlk listelenme | 2026-10-11 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `markdown` · `mermaid` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/f6e44059e77434b4.png" width="100%" alt="NahumLitvin/prismantis screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/9df6377936558503.gif" width="100%" alt="NahumLitvin/prismantis animation"><br><sub>animasyonlu kayıt</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/scasella/claude-flightdeck">scasella/claude-flightdeck</a></b> · ⭐66 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Özet

Terminalinize canlı bir aracı panosu yerleştiren bir Claude Code modu: bağlam ve maliyet, danışman zaman çizelgesi, her izin kontrolü, alt aracı kartları ve kulvarlar.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Modlar: mod yeteneği kullanılarak oluşturulanlar`                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |
| Dil      | TypeScript                                                               |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **66**     |
| Son gönderme   | 2026-10-02 |
| İlk listelenme | 2026-10-10 |

🏷 `agent-observability` · `agent-visualization` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/scasella--claude-flightdeck/8c83ca6b4347b2f9.gif" width="100%" alt="scasella/claude-flightdeck screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/scasella--claude-flightdeck/8c83ca6b4347b2f9.gif" width="100%" alt="scasella/claude-flightdeck animation"><br><sub>animasyonlu kayıt</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/claude-code-mods">karanb192/claude-code-mods</a></b> · ⭐40 · JavaScript · 👁️ observed · 7 天</summary>

##### 📝 Özet

Claude Mod'ları ve bunları oluşturmak için araçlar: önce bir builder skill, ardından mod'lar

<sub>🔧 Kodda kullanıldığı bulundu: `plugins/mod-builder/skills/mod-builder/references/migrate.md`, `plugins/mod-builder/skills/mod-builder/references/nouns.md`</sub>

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Modlar: mod yeteneği kullanılarak oluşturulanlar`                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |
| Dil      | JavaScript                                                               |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **40**     |
| Son gönderme   | 2026-10-03 |
| İlk listelenme | 2026-10-04 |

🏷 `claude` · `claude-code` · `claude-code-plugin` · `claude-mods` · `function-hooks` · `prompt-caching`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/henrik-thevibe/Claude-Fables">henrik-thevibe/Claude-Fables</a></b> · ⭐32 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Özet

Çalışırken Claude Code’un küçük bir çizgi film oluşturmasını izleyin.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Modlar: mod yeteneği kullanılarak oluşturulanlar`                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |
| Dil      | TypeScript                                                               |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **32**     |
| Son gönderme   | 2026-10-02 |
| İlk listelenme | 2026-10-10 |

🏷 `ai-narration` · `claude` · `claude-code` · `claude-code-plugin` · `claude-mod` · `claude-mods` · `developer-tools` · `fun`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/henrik-thevibe--claude-fables/283c6335f0455468.png" width="100%" alt="henrik-thevibe/Claude-Fables screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/henrik-thevibe--claude-fables/630db5cb89b1339d.gif" width="100%" alt="henrik-thevibe/Claude-Fables animation"><br><sub>animasyonlu kayıt</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/oikon48/prompt-rail">oikon48/prompt-rail</a></b> · ⭐27 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Özet

Claude Code oturumunuzun istemleri için bir şerit: okumak için üzerine gelin, atlamak için tıklayın (işlev kancaları / Mods).

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Modlar: mod yeteneği kullanılarak oluşturulanlar`                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |
| Dil      | TypeScript                                                               |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **27**     |
| Son gönderme   | 2026-10-03 |
| İlk listelenme | 2026-10-04 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `function-hooks`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/oikon48--prompt-rail/d6ee96dd984886df.png" width="100%" alt="oikon48/prompt-rail screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/oikon48--prompt-rail/87309761ea9d1f19.gif" width="100%" alt="oikon48/prompt-rail animation"><br><sub>animasyonlu kayıt</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/iamumeransari/claude-show-your-work">iamumeransari/claude-show-your-work</a></b> · ⭐24 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Özet

Claude Code, görüntüleri gösterir ve videoları doğrudan terminalinizde oynatır: ekran görüntüleri, Playwright kayıtları ve senkronize önce/sonra QA. Ghostty ve kitty.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Modlar: mod yeteneği kullanılarak oluşturulanlar`                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |
| Dil      | TypeScript                                                               |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **24**     |
| Son gönderme   | 2026-10-11 |
| İlk listelenme | 2026-10-11 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/iamumeransari--claude-show-your-work/9ee7df00aee28636.jpg" width="100%" alt="iamumeransari/claude-show-your-work screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/iamumeransari--claude-show-your-work/adcbff13953c23f1.gif" width="100%" alt="iamumeransari/claude-show-your-work animation"><br><sub>animasyonlu kayıt</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NovusEdge/glowup">NovusEdge/glowup</a></b> · ⭐23 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Özet

Claude Code için bir yenilenme: canlı kokpit paneli, paylaşılabilir temalar ve Claude'in ne yaptığını canlandıran piksel evcil hayvanı

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Modlar: mod yeteneği kullanılarak oluşturulanlar`                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |
| Dil      | TypeScript                                                               |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **23**     |
| Son gönderme   | 2026-10-11 |
| İlk listelenme | 2026-10-11 |

🏷 `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `developer-tools` · `eye-candy` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/52396333a085f3d5.gif" width="100%" alt="NovusEdge/glowup screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/4905ed24c2c755ad.gif" width="100%" alt="NovusEdge/glowup animation"><br><sub>animasyonlu kayıt</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/augiefra/claude-mods">augiefra/claude-mods</a></b> · ⭐11 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Özet

Claude Code modu: belirtecin üstündeki tek bir bantta token cinsinden bağlam, saate göre 5 saatlik ve haftalık limitler, istem önbelleği geri sayımı, oturum maliyeti ve çalışan ajanlar.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Modlar: mod yeteneği kullanılarak oluşturulanlar`                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |
| Dil      | JavaScript                                                               |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **11**     |
| Son gönderme   | 2026-10-11 |
| İlk listelenme | 2026-10-04 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `claude-code-plugins` · `claude-code-statusline`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/augiefra--claude-mods/5e1358adde3e377d.png" width="100%" alt="augiefra/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/augiefra--claude-mods/27f137c61fc42d0c.gif" width="100%" alt="augiefra/claude-mods animation"><br><sub>animasyonlu kayıt</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/furqan-khan07/pixelband">furqan-khan07/pixelband</a></b> · ⭐10 · TypeScript · 👁️ observed · 7 天</summary>

##### 📝 Özet

Claude Code isteminizin üzerinde, Claude çalışırken tepki veren animasyonlu piksel sanatı. Yedi sahne veya kendi görüntünüz ya da GIF'iniz. Sıfır token.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Modlar: mod yeteneği kullanılarak oluşturulanlar`                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |
| Dil      | TypeScript                                                               |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **10**     |
| Son gönderme   | 2026-10-04 |
| İlk listelenme | 2026-10-10 |

🏷 `animation` · `ascii-art` · `claude` · `claude-code` · `claude-mods` · `pixel-art` · `plugin` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/furqan-khan07--pixelband/a2bacbca880dcd7d.gif" width="100%" alt="furqan-khan07/pixelband screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/furqan-khan07--pixelband/53dd07a5a38530b0.gif" width="100%" alt="furqan-khan07/pixelband animation"><br><sub>animasyonlu kayıt</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Arunjay4213/claude-mods">Arunjay4213/claude-mods</a></b> · ⭐8 · TypeScript · 👁️ observed · 25 天</summary>

##### 📝 Özet

Mod olarak oluşturulmuş Claude Code oturum izleyicileri: bağlam penceresi, plan kotası tüketim hızı, tur başına maliyet

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Modlar: mod yeteneği kullanılarak oluşturulanlar`                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |
| Dil      | TypeScript                                                               |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **8**      |
| Son gönderme   | 2026-09-15 |
| İlk listelenme | 2026-10-04 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `developer-tools` · `function-hooks` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Arunjay4213/claude-mods/main/docs/demo.gif" width="100%" alt="Arunjay4213/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Arunjay4213/claude-mods/main/docs/demo.gif" width="100%" alt="Arunjay4213/claude-mods animation"><br><sub>animasyonlu kayıt</sub></td>
</tr></table>

<sub>Yeniden dağıtıma izin veren bir lisans belirtilmediği için varlığa upstream deposundan doğrudan bağlantı veriliyor.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/nogu66/md-prompt">nogu66/md-prompt</a></b> · ⭐7 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Özet

Siz yazarken Markdown, Claude Code'un istem kutusuna çizilir. Çitli kod, çiti kapatmadan önce bile sözdizimi vurgulanmış bir karta dönüşür.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Modlar: mod yeteneği kullanılarak oluşturulanlar`                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |
| Dil      | TypeScript                                                               |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **7**      |
| Son gönderme   | 2026-10-03 |
| İlk listelenme | 2026-10-10 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `function-hooks`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nogu66--md-prompt/b729912bc80aeee4.png" width="100%" alt="nogu66/md-prompt screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nogu66--md-prompt/408107e3aa381332.gif" width="100%" alt="nogu66/md-prompt animation"><br><sub>animasyonlu kayıt</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/arasovic/claude-code-mods">arasovic/claude-code-mods</a></b> · ⭐6 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Özet

Claude Code için Mods: terminal kullanıcı arayüzüne canlı bölmeler ve davranış ekleyen işlev kancası eklentileri

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Modlar: mod yeteneği kullanılarak oluşturulanlar`                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |
| Dil      | TypeScript                                                               |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **6**      |
| Son gönderme   | 2026-10-10 |
| İlk listelenme | 2026-10-04 |

🏷 `ai-agents` · `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-mods` · `claude-code-plugin` · `claude-code-plugins`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/arasovic--claude-code-mods/a8e330d8ce6f7bad.png" width="100%" alt="arasovic/claude-code-mods screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/helenkwok/gsd-status-mod">helenkwok/gsd-status-mod</a></b> · ⭐6 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Özet

Claude Code için canlı GSD panosu: yol haritası, çatalları gösteren ajan ağacı, bağlam ve maliyet, iş akışları ve .planning için markdown okuyucu. Salt okunur.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Modlar: mod yeteneği kullanılarak oluşturulanlar`                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |
| Dil      | TypeScript                                                               |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **6**      |
| Son gönderme   | 2026-10-11 |
| İlk listelenme | 2026-10-11 |

🏷 `agents` · `claude-code` · `claude-code-mod` · `claude-code-plugin` · `dashboard` · `gsd` · `markdown-reader` · `planning`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/helenkwok--gsd-status-mod/4626cb34617b7732.png" width="100%" alt="helenkwok/gsd-status-mod screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/helenkwok--gsd-status-mod/a31036b15398e820.gif" width="100%" alt="helenkwok/gsd-status-mod animation"><br><sub>animasyonlu kayıt</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/markneonin/paneline">markneonin/paneline</a></b> · ⭐6 · TypeScript · 👁️ observed · 4 天</summary>

##### 📝 Özet

Activity, Files, Agents, Context ve MCP sekmelerini içeren bir yan bölme, prompt'un üstünde bir durum satırı, yeniden biçimlendirilmiş bir chat, terminalde Mermaid diyagramları, tablolar ve kod ile diff panelleri ekleyen Claude Code mod'u (plugin). Renkler hem /color hem de /theme (dark, light ve diğerleri) ayarlarını izler.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Modlar: mod yeteneği kullanılarak oluşturulanlar`                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |
| Dil      | TypeScript                                                               |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **6**      |
| Son gönderme   | 2026-10-06 |
| İlk listelenme | 2026-10-10 |

🏷 `ai-agents` · `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mod` · `claude-code-mods`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/markneonin--paneline/e7976a2ea941fd17.png" width="100%" alt="markneonin/paneline screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Shuffzord/RoadRaven">Shuffzord/RoadRaven</a></b> · ⭐6 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Özet

Kendi kendini izleyen planınız. Claude Code ve herhangi bir MCP ana bilgisayarının canlı olarak güncel tuttuğu yerel masaüstü yol haritası ağacı. Düz JSON, bulut yok.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Modlar: mod yeteneği kullanılarak oluşturulanlar`                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |
| Dil      | TypeScript                                                               |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **6**      |
| Son gönderme   | 2026-10-10 |
| İlk listelenme | 2026-10-11 |

🏷 `ai-agents` · `bun` · `claude-code` · `claude-code-mod` · `claude-code-plugin` · `desktop-app` · `electrobun` · `local-first`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Shuffzord/RoadRaven/master/screenshots/events.png" width="100%" alt="Shuffzord/RoadRaven screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

<sub>Yeniden dağıtıma izin veren bir lisans belirtilmediği için varlığa upstream deposundan doğrudan bağlantı veriliyor.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/leopiney/wolfbud-claude-mod">leopiney/wolfbud-claude-mod</a></b> · ⭐5 · TypeScript · 👁️ observed · 2 天</summary>

##### 📝 Özet

Claude Code için sesli çalışma arkadaşı. ElevenLabs konuşma AI'sı tarafından desteklenen 3D bir kurtla düşüncelerinizi konuşun; anlaştığınızda istemi Claude'e gönderir ve Claude tamamlandığında konuşur.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Modlar: mod yeteneği kullanılarak oluşturulanlar`                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |
| Dil      | TypeScript                                                               |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **5**      |
| Son gönderme   | 2026-10-08 |
| İlk listelenme | 2026-10-10 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin` · `claude-mods`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/leopiney/wolfbud-claude-mod/main/assets/banner.png" width="100%" alt="leopiney/wolfbud-claude-mod screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

<sub>Yeniden dağıtıma izin veren bir lisans belirtilmediği için varlığa upstream deposundan doğrudan bağlantı veriliyor.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/HMarzban/claude-mod">HMarzban/claude-mod</a></b> · ⭐4 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Özet

Bir sonraki Claude Code mesajınızın maliyetini görün: istemin üzerinde istem önbelleği geri sayımını, yeniden ısıtma fiyatını, oturum maliyetini, bağlamı ve 5 saatlik/haftalık kullanım sınırlarını gösteren canlı bir bant.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Modlar: mod yeteneği kullanılarak oluşturulanlar`                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |
| Dil      | TypeScript                                                               |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **4**      |
| Son gönderme   | 2026-10-11 |
| İlk listelenme | 2026-10-11 |

🏷 `anthropic` · `claude` · `claude-ai` · `claude-code` · `claude-code-plugin` · `claude-mod` · `cost-tracking` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hmarzban--claude-mod/680a1325dcf966ff.gif" width="100%" alt="HMarzban/claude-mod screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hmarzban--claude-mod/680a1325dcf966ff.gif" width="100%" alt="HMarzban/claude-mod animation"><br><sub>animasyonlu kayıt</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/dominicrico/jev-router">dominicrico/jev-router</a></b> · ⭐3 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Özet

Claude Code eklentisi: otomatik Claude model yönlendirmesi. Her istem, adım ve alt agent için Haiku, Sonnet veya Opus'u ve akıl yürütme çabasını seçer; çaba sınırı, istem önbelleği koruması, durum bandı ve kıyaslamalar.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Modlar: mod yeteneği kullanılarak oluşturulanlar`                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |
| Dil      | TypeScript                                                               |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **3**      |
| Son gönderme   | 2026-10-10 |
| İlk listelenme | 2026-10-09 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-marketplace` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dominicrico--jev-router/e9ab68584ed9c404.jpg" width="100%" alt="dominicrico/jev-router screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dominicrico--jev-router/2a6620c49438b369.gif" width="100%" alt="dominicrico/jev-router animation"><br><sub>animasyonlu kayıt</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/FynnXland/fynn-mods">FynnXland/fynn-mods</a></b> · ⭐3 · TypeScript · 👁️ observed · 1 天</summary>

##### 📝 Özet

Claude Code için altı mod: animasyonlu Clawd maskotu, kullanım limiti ve prompt-cache çubukları, gönderim öncesi mesaj denetleyicisi, hızlı yanıtlar, yapılacaklar kuyruğu ve maliyet defteri. Terminal ve masaüstü uygulaması, İngilizce/Almanca.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Modlar: mod yeteneği kullanılarak oluşturulanlar`                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |
| Dil      | TypeScript                                                               |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **3**      |
| Son gönderme   | 2026-10-09 |
| İlk listelenme | 2026-10-07 |

🏷 `ai-coding-assistant` · `claude` · `claude-ai` · `claude-code` · `claude-code-marketplace` · `claude-code-mods` · `claude-code-plugin` · `claude-code-plugins`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/fynnxland--fynn-mods/46068e3739e61a25.gif" width="100%" alt="FynnXland/fynn-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/fynnxland--fynn-mods/46068e3739e61a25.gif" width="100%" alt="FynnXland/fynn-mods animation"><br><sub>animasyonlu kayıt</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/mertkayacs/ultramod">mertkayacs/ultramod</a></b> · ⭐3 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Özet

Claude Code için en iyi hepsi bir arada mod paketi: kullanım sınırları ve bağlam HUD'si, rm -rf ve git reset --hard için geri alma özellikli bir koruma, .env ve gizli bilgi koruması ve her tur için bir makbuz. On mod, tek kurulum.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Modlar: mod yeteneği kullanılarak oluşturulanlar`                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |
| Dil      | TypeScript                                                               |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **3**      |
| Son gönderme   | 2026-10-10 |
| İlk listelenme | 2026-10-09 |

🏷 `ai-agents` · `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/mertkayacs--ultramod/0f9d8b2253819dc8.gif" width="100%" alt="mertkayacs/ultramod screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/mertkayacs--ultramod/1537defa7233d7f2.gif" width="100%" alt="mertkayacs/ultramod animation"><br><sub>animasyonlu kayıt</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/mthli/cc-shorts">mthli/cc-shorts</a></b> · ⭐3 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Özet

Claude Code'unuzda YouTube Shorts oynatın 💃

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Modlar: mod yeteneği kullanılarak oluşturulanlar`                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |
| Dil      | TypeScript                                                               |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **3**      |
| Son gönderme   | 2026-10-02 |
| İlk listelenme | 2026-10-10 |

🏷 `claude-mods` · `youtube-shorts`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/mthli--cc-shorts/ef652fff732c023d.png" width="100%" alt="mthli/cc-shorts screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/chenyuxiaojin/cyxj-notch">chenyuxiaojin/cyxj-notch</a></b> · ⭐2 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Özet

Claude Code için macOS çentik gösterge paneli: kullanım sınırları, açık oturumlar, görev ilerlemesi, istem önbelleği geri sayımı ve yapılacaklar — dahil edilen beş Claude Code modu tarafından beslenir.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Modlar: mod yeteneği kullanılarak oluşturulanlar`                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |
| Dil      | TypeScript                                                               |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **2**      |
| Son gönderme   | 2026-10-11 |
| İlk listelenme | 2026-10-10 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `developer-tools` · `dynamic-island` · `macos` · `menu-bar`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/chenyuxiaojin--cyxj-notch/61834d73bebe8659.gif" width="100%" alt="chenyuxiaojin/cyxj-notch screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/chenyuxiaojin--cyxj-notch/61834d73bebe8659.gif" width="100%" alt="chenyuxiaojin/cyxj-notch animation"><br><sub>animasyonlu kayıt</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Christandoh/context-cache">Christandoh/context-cache</a></b> · ⭐2 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Özet

Claude Code mod: context usage, session / weekly / Fable limits and prompt-cache temperature above the prompt

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Modlar: mod yeteneği kullanılarak oluşturulanlar`                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |
| Dil      | TypeScript                                                               |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **2**      |
| Son gönderme   | 2026-10-11 |
| İlk listelenme | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/christandoh--context-cache/3cdd3b2c5a09da7d.png" width="100%" alt="Christandoh/context-cache screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/CodyAMaughan/meme-factory">CodyAMaughan/meme-factory</a></b> · ⭐2 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Özet

Fabrikadan yeni çıktı. Bir Claude Code modu: bir meme isteyin, çalışmaya devam edin. Taslaklar bir yan panelde hazırlanır; seçin, yeniden düzenleyin, onaylayın ve Slack'e gönderin.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Modlar: mod yeteneği kullanılarak oluşturulanlar`                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |
| Dil      | JavaScript                                                               |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **2**      |
| Son gönderme   | 2026-10-10 |
| İlk listelenme | 2026-10-09 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `developer-tools` · `fun` · `meme-generator` · `memes` · `slack`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/codyamaughan--meme-factory/7417dc8940c4a087.png" width="100%" alt="CodyAMaughan/meme-factory screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/codyamaughan--meme-factory/8c9d44287267796f.gif" width="100%" alt="CodyAMaughan/meme-factory animation"><br><sub>animasyonlu kayıt</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/estruyf/claude-stats-mod">estruyf/claude-stats-mod</a></b> · ⭐2 · JavaScript · 👁️ observed · 8 天</summary>

##### 📝 Özet

Kullanım limitlerinizi ve harcamalarınızı istemin üzerindeki bantta gösteren bir Claude Code modu.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Modlar: mod yeteneği kullanılarak oluşturulanlar`                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |
| Dil      | JavaScript                                                               |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **2**      |
| Son gönderme   | 2026-10-02 |
| İlk listelenme | 2026-10-10 |

🏷 `claude` · `claude-code` · `claude-mod` · `claude-mods`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/estruyf/claude-stats-mod/main/assets/desktop.png" width="100%" alt="estruyf/claude-stats-mod screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

<sub>Yeniden dağıtıma izin veren bir lisans belirtilmediği için varlığa upstream deposundan doğrudan bağlantı veriliyor.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/i-harsha-reddy/naruto-mod">i-harsha-reddy/naruto-mod</a></b> · ⭐2 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Özet

Claude Code için piksel sanatlı bir Naruto yardımcısı: Claude çalışırken gerçekleştirilen 20 ninja, 60 jutsu

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Modlar: mod yeteneği kullanılarak oluşturulanlar`                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |
| Dil      | TypeScript                                                               |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **2**      |
| Son gönderme   | 2026-10-10 |
| İlk listelenme | 2026-10-11 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `naruto` · `pixel-art`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/i-harsha-reddy--naruto-mod/c4048227757840cb.gif" width="100%" alt="i-harsha-reddy/naruto-mod screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/i-harsha-reddy--naruto-mod/c4048227757840cb.gif" width="100%" alt="i-harsha-reddy/naruto-mod animation"><br><sub>animasyonlu kayıt</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/lorenzh/rabe">lorenzh/rabe</a></b> · ⭐2 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Özet

Claude Code'un arka planda ne çalıştırdığını görün: alt ajanlar, Codex işleri, kabuklar, izleyiciler, cron işleri ve iş akışları.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Modlar: mod yeteneği kullanılarak oluşturulanlar`                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |
| Dil      | TypeScript                                                               |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **2**      |
| Son gönderme   | 2026-10-11 |
| İlk listelenme | 2026-10-09 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/lorenzh--rabe/1c67cab3774edaee.gif" width="100%" alt="lorenzh/rabe screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/lorenzh--rabe/1c67cab3774edaee.gif" width="100%" alt="lorenzh/rabe animation"><br><sub>animasyonlu kayıt</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/macleodlabs-ai/claudeflow">macleodlabs-ai/claudeflow</a></b> · ⭐2 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Özet

MacLeod Labs tarafından geliştirilen Claude Code modları: streams, bir oturumun iç içe geçmiş çalışmalarını renk kodlu akışlara ayırır

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Modlar: mod yeteneği kullanılarak oluşturulanlar`                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |
| Dil      | TypeScript                                                               |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **2**      |
| Son gönderme   | 2026-10-11 |
| İlk listelenme | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/macleodlabs-ai/claudeflow/main/assets/hero.jpg" width="100%" alt="macleodlabs-ai/claudeflow screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

<sub>Yeniden dağıtıma izin veren bir lisans belirtilmediği için varlığa upstream deposundan doğrudan bağlantı veriliyor.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/MankhongGarden/claude-code-mods-field-notes">MankhongGarden/claude-code-mods-field-notes</a></b> · ⭐2 · TypeScript · 👁️ observed · 1 天</summary>

##### 📝 Özet

Windows üzerindeki Claude Code modları hakkında birinci gün saha notları: bağlam/kota yakıt çubuğu, Thai UI modu, Matrix önyükleme introsu ve güvenli güncelleyici; ayrıca nelerin başarısız olduğu ve nedenleri (bölmeler, istemin üzerindeki bantlar, Windows Terminal'de Thai).

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Modlar: mod yeteneği kullanılarak oluşturulanlar`                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |
| Dil      | TypeScript                                                               |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **2**      |
| Son gönderme   | 2026-10-09 |
| İlk listelenme | 2026-10-07 |

🏷 `anthropic` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `claude-mods` · `developer-tools` · `function-hooks`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/mankhonggarden--claude-code-mods-field-notes/832ffcdb7bad9007.png" width="100%" alt="MankhongGarden/claude-code-mods-field-notes screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary><b>Bu kategoride daha fazlası</b> <sub>· 347</sub></summary>

- [rashedInt32/glass](https://github.com/rashedInt32/glass) - Bir mod olarak Claude Code.
- [xuanji86/claude-agentpane](https://github.com/xuanji86/claude-agentpane) - Claude Code için bir yan panel: bir oturumun çalıştırdığı alt aracılar, her…
- [letswritetw/claude-mod-open-todos](https://github.com/letswritetw/claude-mod-open-todos) - Claude Desktop (Code sekmesi) kenar çubuğu paneli: tüm Claude Code…
- [letswritetw/claude-mod-token-usage](https://github.com/letswritetw/claude-mod-token-usage) - Claude Desktop (Code sekmesi) giriş kutusunun üstündeki kullanım çubuğu: 5h /…
- [omarcevi/claudemods](https://github.com/omarcevi/claudemods) - Tek bir pazardan kurulabilen topluluk Claude modları, eklentileri ve becerileri.
- [eighteyes/cactus](https://github.com/eighteyes/cactus) - Konuşmalı ajanlarla çalışan insanlar için karar kuyruğu CLI/TUI.
- [xuanji86/claude-statuspane](https://github.com/xuanji86/claude-statuspane) - Claude Code için kayan durum kartı — model, bağlam, hız sınırları, maliyet, dal…
- [xuanji86/claude-mdview](https://github.com/xuanji86/claude-mdview) - Claude Code.
- [atomashevic/claude-latex-math](https://github.com/atomashevic/claude-latex-math) - Claude Code mod that typesets the LaTeX math in Claude.
- [charimsma/dopa-mode](https://github.com/charimsma/dopa-mode) - Claude Code için havai fişekler: her tuş vuruşu, araç çağrısı, commit ve…
- [ha-ptt0601/cc-mods](https://github.com/ha-ptt0601/cc-mods) - Küçük Claude Code modülleri (işlev kancası eklentileri): session-switcher ve…
- [ice-lfernandes/claude-code-mods](https://github.com/ice-lfernandes/claude-code-mods) - Altı Claude Code modu: plan sınırları ve istemin üstünde bağlam, izin istemleri…
- [NarenDawar/narens-claude-toolkit](https://github.com/NarenDawar/narens-claude-toolkit) - Naren.
- [neteye-platform/cc-split-diff-view](https://github.com/neteye-platform/cc-split-diff-view) - Edit ve Write farklarını yan yana iki sütunda çizen Claude Code modu.
- [testy-cool/awesome-claude-code-mods](https://github.com/testy-cool/awesome-claude-code-mods) - Eklenti pazaryeri olarak kurulabilen, derlenmiş bir Claude Code modları…
- [xsyetopz/dotclaude](https://github.com/xsyetopz/dotclaude) - Harness mühendisliğine takıntılı bir Rustacean tarafından tasarlanmış, son…
- [ArgonQQ/sipp](https://github.com/ArgonQQ/sipp) - 💧 Claude Code için pasif-agresif bir su içme hatırlatıcısı.
- [herman925/925-cc-plugins](https://github.com/herman925/925-cc-plugins) - Herman.
- [patitow/claude-mod-cost-visibility](https://github.com/patitow/claude-mod-cost-visibility) - Claude Code modu: istemin üzerinde canlı maliyet, bağlam ve plan kota…
- [rbartoli/agent-usage-guard](https://github.com/rbartoli/agent-usage-guard) - Alt ajanların çoğalmasını, yoğun bağlamlı istemleri ve yeniden deneme…
- [shimo4228/harness-scope](https://github.com/shimo4228/harness-scope) - Genel becerilerinizi, aracıları, kuralları ve araçlarınızı adlandırılmış…
- [simplecore-inc/claude-mods](https://github.com/simplecore-inc/claude-mods) - Claude Code eklentileri (modlar): birkaç Claude hesabı arasında geçiş yapın…
- [Singh-AP/awesome-claude-mods](https://github.com/Singh-AP/awesome-claude-mods) - 🧩 Test edilmiş, tek komutla kurulabilen Claude Code modları: YOLO modu için…
- [smukh/roll-credits](https://github.com/smukh/roll-credits) - Kodlama oturumunuz için film tarzı jenerik.
- [yodakeisuke/claudelingo](https://github.com/yodakeisuke/claudelingo) - Claude Code ile çalışırken yabancı bir dil öğrenin.
- [alaturqua/tower-mods](https://github.com/alaturqua/tower-mods) - Claude Code mods for running many sessions across many repos from one control…
- [alexlifexyz/p3c-guard](https://github.com/alexlifexyz/p3c-guard) - Agent Java yazarken Alibaba Java kuralını (p3c) ihlal eden kod diske…
- [andrewbakercloudscale/claude-code-cost-sidebar](https://github.com/andrewbakercloudscale/claude-code-cost-sidebar) - Claude Code için canlı maliyet, token ve bağlam kullanımı kenar çubuğu: oturum…
- [aosmcleod/next-up-mod](https://github.com/aosmcleod/next-up-mod) - Claude Code modu: Claude.
- [BjoernSchotte/ccmod-amp](https://github.com/BjoernSchotte/ccmod-amp) - Claude Code içinde internet radyosu: cliamp kenar çubuğu, mini oynatıcı…
- [Bocskay-Botond/claude-code-mods](https://github.com/Bocskay-Botond/claude-code-mods) - Fun, useful Claude Code mods: a pixel critter above your prompt, a tools menu…
- [chrisluo5311/squad-chat](https://github.com/chrisluo5311/squad-chat) - Claude pişiriyor. Ekibinizle sohbet edin.
- [crebot51/jack-mods](https://github.com/crebot51/jack-mods) - jack.
- [danielpg95/modster-hunter](https://github.com/danielpg95/modster-hunter) - Bir Claude Code modu: Claude çalışırken boşta duran bir oyunda piksel sanatlı…
- [darkomarijaan/nexus-mod](https://github.com/darkomarijaan/nexus-mod) - Hepsi bir arada Claude Code modu: canlı HUD, güvenlik korumaları.
- [DarkVelours/claude-code-galactic-battle](https://github.com/DarkVelours/claude-code-galactic-battle) - Claude Code.
- [Davron2004/slash-coverage](https://github.com/Davron2004/slash-coverage) - Her Claude Code ajanının bağlamında hangi dosyaların olduğunu ve her birinden…
- [drakulavich/cogload](https://github.com/drakulavich/cogload) - Aklınızı serin tutun. Claude Code günleriniz için bir termometre: diskinizde…
- [EgonLeitner/dashband](https://github.com/EgonLeitner/dashband) - Claude Code için istem alt bilgisinde ve istemin üzerinde istem önbelleğini…
- [ElirazKed/claude-code-pr-watch](https://github.com/ElirazKed/claude-code-pr-watch) - Claude Code modu: bir oturumun açtığı veya gönderdiği GitHub PR.
- [enhki/claude-mods](https://github.com/enhki/claude-mods) - Terminal ve masaüstü uygulaması için küçük Claude Code modları.
- [ewxgwy1987/claude-code-mods](https://github.com/ewxgwy1987/claude-code-mods) - Her biri kendi deposunda bulunan Claude Code modları koleksiyonu: usage-meter…
- [ewxgwy1987/claude-code-progress-board](https://github.com/ewxgwy1987/claude-code-progress-board) - Claude Code modu: görevler, alt ajanlar, iş akışı çalıştırmaları, hedef ve araç…
- [ewxgwy1987/claude-code-session-toc](https://github.com/ewxgwy1987/claude-code-session-toc) - Claude Code modu: tüm oturumun konulara ve kategorilere göre gruplandırılmış…
- [ewxgwy1987/claude-code-usage-meter](https://github.com/ewxgwy1987/claude-code-usage-meter) - Claude Code modu: plan hız sınırlarını, bağlam doluluğunu, oturum maliyetini ve…
- [Exdenta/ambient-spanish](https://github.com/Exdenta/ambient-spanish) - Ajan yanıtlarına İspanyolca kelimeler ekleyen Claude CLI becerisi + modu.
- [FrBmt-BIGetNouf/alarum-claude-mod](https://github.com/FrBmt-BIGetNouf/alarum-claude-mod) - Alarum.me&#x27;yi Claude kodunuza CLI veya Desktop&#x27;a gömün.
- [FrBmt-BIGetNouf/floatee-claude-mod](https://github.com/FrBmt-BIGetNouf/floatee-claude-mod) - Your Floatee backlog above Claude Code.
- [GoneTone/cc-askpass](https://github.com/GoneTone/cc-askpass) - A Claude Code mod that lets Claude run commands that need sudo, instead of…
- [gonzalonicolasr/claude-code-nerv](https://github.com/gonzalonicolasr/claude-code-nerv) - Claude Code için Evangelion tarzı kenar çubuğu: bağlam, kota, etkinlik, PR.
- [gregdotca/ccmod-the-machine](https://github.com/gregdotca/ccmod-the-machine) - Onu Person of Interest dizisindeki The Machine olarak yeniden biçimlendiren bir…
- [HyunjunJeon/claude-workflow-mods](https://github.com/HyunjunJeon/claude-workflow-mods) - dag-workflow: canlı DAG bölmesiyle alt agent.
- [ibrahimkobeissy/claude-mods](https://github.com/ibrahimkobeissy/claude-mods) - Claude Code için açık kaynaklı modlar: bölmeler, durum satırları, bildirimler…
- [jonyfs/astrolabe](https://github.com/jonyfs/astrolabe) - 🧭 Claude Code mod: oturum durumu, canlı Spec Kit ilerlemesi ve kullanım…
- [kongyo2/context-view](https://github.com/kongyo2/context-view) - Bağlam penceresi, istemin üzerinde tek satır olarak;
- [kyledarling-io/claude-code-desktop-hud](https://github.com/kyledarling-io/claude-code-desktop-hud) - Claude Code Desktop için canlı görev HUD.
- [m4cd4r4/clear-resume](https://github.com/m4cd4r4/clear-resume) - Claude Code için ücretsiz, açık kaynaklı bir eklenti.
- [Mechazawa/claude-inline-images](https://github.com/Mechazawa/claude-inline-images) - Claude Code mod that shows images inline in Ghostty and kitty.
- [meganemura/pull-request-pane](https://github.com/meganemura/pull-request-pane) - Oturumun GitHub pull request.
- [NotRedFox/NotRedFoxs-Claude-skills](https://github.com/NotRedFox/NotRedFoxs-Claude-skills) - Claude Code becerileri: belge doğrulayıcı, kod denetçisi, hata anıları günlüğü…
- [pepperonas/loc-today](https://github.com/pepperonas/loc-today) - Claude Code modu: tüm oturumlarda Claude tarafından bugün yazılan kod satırları…
- [pepperonas/path-links](https://github.com/pepperonas/path-links) - Claude Code modu: yanıtlardaki tıklanabilir yollar — klasörü açmak için…
- [peterlimg/auto-effort](https://github.com/peterlimg/auto-effort) - Claude Code modu: Jev ile istem başına /effort seçer.
- [rezzminator/buddy](https://github.com/rezzminator/buddy) - Claude Code arkadaş eklentisi: isteminizin üzerinde kurallarınızı hatırlayan ve…
- [roma-vibe/jev-governor](https://github.com/roma-vibe/jev-governor) - Claude Code mod: Jev-guided model/effort routing, verbatim context compaction…
- [samfrmr/barmkin-mod](https://github.com/samfrmr/barmkin-mod) - Claude Code modları: Claude Code için güvenlik katmanı — gizli bilgilerin…
- [Sennjen/claude-sdlc](https://github.com/Sennjen/claude-sdlc) - Claude Code plugin&#x27;i ve mod&#x27;u: hook ile zorunlu kılınan insan onayı kapıları ve…
- [SeongGwangJu/k-mods](https://github.com/SeongGwangJu/k-mods) - Harika Claude Code modları koleksiyonu | 클로드 코드 모드 모음집.
- [soulrocha/Claude-code-hero-journey](https://github.com/soulrocha/Claude-code-hero-journey) - 🦀 Claude Code için rahat bir RPG HUD modu.
- [tanujarun/it-speaks](https://github.com/tanujarun/it-speaks) - Konuşuyor: Claude.
- [timoncool/givememod](https://github.com/timoncool/givememod) - İsteğe bağlı Claude Code modları — konuşmanızı okuyup size uygun modu oluşturan…
- [timoncool/slapbox](https://github.com/timoncool/slapbox) - 🍑 Hata yaptığında Claude.
- [TroyJLorents-GH/mod-squad](https://github.com/TroyJLorents-GH/mod-squad) - Claude Code modları: canlı bölmeler, maliyet farkındalıklı model yönlendirme ve…
- [valeryia-piatrova/token-hamster](https://github.com/valeryia-piatrova/token-hamster) - 🐹 Claude Code modu ve eklentisi: kullanım monitörü, token izleyici ve durum…
- [vumichien/claude-code-mods-kit](https://github.com/vumichien/claude-code-mods-kit) - Üç ücretsiz Claude Code modu: .env değerlerini araç sonuçlarından gizleyin…
- [y-hirakaw/claude-code-mods](https://github.com/y-hirakaw/claude-code-mods) - Claude Code modları. touch-map: Claude tarafından listelenen, okunan…
- [0xnicholasy/claude-mods](https://github.com/0xnicholasy/claude-mods) - 0xnicholasy.
- [akixi-maison/usage-mods](https://github.com/akixi-maison/usage-mods) - Claude Code modu: kullanım ilerleme çubukları (bağlam, 5s, 7g) ve istemin…
- [alan-oliv/claude-mods](https://github.com/alan-oliv/claude-mods) - Claude Code modları: istemin üzerinde oturum istatistik kartları.
- [Aler1x/claude-cat](https://github.com/Aler1x/claude-cat) - Claude Code isteminin üzerinde animasyonlu bir braille kedisi.
- [alinaqi/mixture-of-models-claude-mod](https://github.com/alinaqi/mixture-of-models-claude-mod) - Claude Code modu: ucuz işleri bir alt Claude Code aracılığıyla GLM/Kimi.
- [aloki-alok/omni-cat](https://github.com/aloki-alok/omni-cat) - Claude Code isteminizin üzerinde, bir OmniDimension ses ajanı test çağrısı…
- [ambervdberg/smartcompact](https://github.com/ambervdberg/smartcompact) - Bağlam penceresini küçük tutmak için sıkıştırma işlemini uygun bir anda seçen…
- [an80sPWNstar/claude-mods](https://github.com/an80sPWNstar/claude-mods) - Claude Code için Claude modları: token-meter.
- [anderson-spider/claude-mods](https://github.com/anderson-spider/claude-mods) - anderson-spider tarafından geliştirilen Claude Code eklenti pazaryeri.
- [andras-gyarmati/claude-quota-band](https://github.com/andras-gyarmati/claude-quota-band) - Claude Code modu: planınızın 5 saatlik ve haftalık kullanımını istemin üzerinde…
- [androidZzT/claude-trading-mods](https://github.com/androidZzT/claude-trading-mods) - Terminalden piyasayı izlemek için Claude Code modları: trendler ve sektör ısı…
- [angomedia/claude-mods](https://github.com/angomedia/claude-mods) - Claude Code için modlar.
- [arslan-charyyev/claude-mods](https://github.com/arslan-charyyev/claude-mods) - Özel Claude Code modlarım.
- [Ashley-Pettit/lgtm-flash](https://github.com/Ashley-Pettit/lgtm-flash) - LGTM Lines gemisi her kod değişikliğinden sonra yanınızdan geçer — bir Claude…
- [Ashley-Pettit/villager-hp](https://github.com/Ashley-Pettit/villager-hp) - Your Claude usage limits as an animated villager health card, with a weekly…
- [AskTinNguyen/ather-mods](https://github.com/AskTinNguyen/ather-mods) - S2 ekibi için Claude Code modları (ather marketplace).
- [Atanur/deskfit](https://github.com/Atanur/deskfit) - Claude çalışırken kısa antrenmanlar: günlük hedef, seriler, rozetler ve isteğe…
- [atharv6f/waypoint](https://github.com/atharv6f/waypoint) - Claude Code isteminin yanında plan, görev ve ajan ilerlemesi — bir Claude Code…
- [aycandv/claude-usage-meter](https://github.com/aycandv/claude-usage-meter) - Claude Code için kullanım panosu: modele göre harcama.
- [barneym/claude-context-bar](https://github.com/barneym/claude-context-bar) - Claude Code modu: istemin üstünde canlı bağlam penceresi dökümü.
- [bastianfuchs/claude-code-cache-warm](https://github.com/bastianfuchs/claude-code-cache-warm) - Claude Code mod that shows the prompt-cache countdown in the footer and keeps…
- [benjaminr/nowplaying](https://github.com/benjaminr/nowplaying) - Claude Code için Now Playing modu: istemin üzerinde kapak görseli, kontroller…
- [bitcars/ctx-bar](https://github.com/bitcars/ctx-bar) - ctx-bar: a Claude Code mod that keeps the context window visible at all times.
- [broening/claude-mods](https://github.com/broening/claude-mods) - Claude Code için modlar: önbellek saati, patlama yarıçapı, öneriler, iş…
- [Carismarkus/clowl](https://github.com/Carismarkus/clowl) - Claude Code.
- [cGradying/claude-code-cockpit](https://github.com/cGradying/claude-code-cockpit) - Tek bir eklenti olarak yüklenen ve varsayılan olarak sessiz çalışan tek…
- [chamonkey-crypto/claude-mods](https://github.com/chamonkey-crypto/claude-mods)
- [ChaseWNorton/claude-doom](https://github.com/ChaseWNorton/claude-doom) - İçinde Freedoom bulunan orijinal Doom motoru, Claude Code içinde oynanabilir.
- [christian-engels/claude-footprint](https://github.com/christian-engels/claude-footprint) - Claude Code modu: kaynaklarıyla birlikte her tur ve oturum için tahmini…
- [chshin84/claude-mods](https://github.com/chshin84/claude-mods) - Claude Code 단어 사전 패널과 상태 표시줄 플러그인.
- [cldotdev/claude-todo-list](https://github.com/cldotdev/claude-todo-list) - Bir konuşmadaki açık maddelerin güncel listesini tutan ve bunu istemin üzerinde…
- [comertial/claude-pending-changes](https://github.com/comertial/claude-pending-changes) - Review every file Claude touches, like a pull request, without leaving the…
- [comertial/comertial-mods](https://github.com/comertial/comertial-mods) - Gerçek Mühendisler için Claude Code modları.
- [crisguitar/claude-mods](https://github.com/crisguitar/claude-mods)
- [d3nims/d3nim-claude-mods](https://github.com/d3nims/d3nim-claude-mods) - d3nim 팀専용 Claude Code modları (usage-meter: 파란 불꽃 / 테리어 사용량 밴드).
- [danielgillaspia01-web/claude-mods](https://github.com/danielgillaspia01-web/claude-mods)
- [davep-s20/claude-mods](https://github.com/davep-s20/claude-mods)
- [davidparys/claude-mods](https://github.com/davidparys/claude-mods) - Claude Code modları: kural koruyucu, düzeltmelerinizi kalıcı kurallar olarak…
- [davidurco/cc-tamagotchi](https://github.com/davidurco/cc-tamagotchi) - Claude Code içinde yaşayan bir Tamagotchi: yumurtadan çıkar, Claude.
- [Demo-0416/claude-code-mods](https://github.com/Demo-0416/claude-code-mods) - Bir eklenti pazarı olarak Claude Code modları.
- [derekwden-droid/message-timestamps](https://github.com/derekwden-droid/message-timestamps) - Claude Code modu: terminalde ve masaüstü uygulamasında her istem ve yanıtın…
- [devohmycode/ccmods](https://github.com/devohmycode/ccmods) - İşlev kancaları olarak yazılmış Claude Code modları ve bunları sunan pazar…
- [dot-agi/arrester](https://github.com/dot-agi/arrester) - Claude Code modu: bir guard araç çağrısını engelledikten sonra aynı hedefe…
- [dot-agi/downrange](https://github.com/dot-agi/downrange) - Claude Code modu: gerçek çıktından okunan ilerleme ve tahmini varış süreleriyle…
- [dot-agi/high-command](https://github.com/dot-agi/high-command) - Claude Code modu: ekip arkadaşlarından, adlandırılmış alt ajanlardan ve diğer…
- [dot-agi/sandbox-tuner](https://github.com/dot-agi/sandbox-tuner) - Claude Code modu: sandbox engellemelerini açıklar ve tekrarlanan engellemeleri…
- [dricosnyman/claude-favourites](https://github.com/dricosnyman/claude-favourites) - Claude Code için favoriler: komutlarınız ve becerileriniz için tek tıklamalı…
- [Egrn/claude-code-mutedit](https://github.com/Egrn/claude-code-mutedit) - Hey, susturdum! Farkı bırak, ritmi kes; artık düzenleme yok, daha az kredi.
- [Eiyuo/Claude-Mods](https://github.com/Eiyuo/Claude-Mods)
- [elec100-design/claude-mods](https://github.com/elec100-design/claude-mods) - claude için modlar.
- [EmanueleNene/claude-mods](https://github.com/EmanueleNene/claude-mods) - Claude Code modları: delete-guard (dosya silme işlemlerini onaylar) ve…
- [eric1hua/claudemods-desktop-statusline](https://github.com/eric1hua/claudemods-desktop-statusline) - Masaüstü uygulamasında ve terminalde istemin üzerinde bir bant olarak abonelik…
- [ErnestTramp/claude-critters](https://github.com/ErnestTramp/claude-critters) - Claude Code mod: your background agents as pixel critters, one sprite per model.
- [FeidaWang/edit-replay](https://github.com/FeidaWang/edit-replay) - Edit Replay: step through the file edits Claude made in the last turn, one diff…
- [Flo0806/fh-claude-mods](https://github.com/Flo0806/fh-claude-mods) - Claude Mod Marketplace.
- [floheissler/cc-worktree-radar](https://github.com/floheissler/cc-worktree-radar) - İstemin üzerinde paralel dallarınızın ve çalışma ağaçlarınızın canlı radarı…
- [gaius-codius/ostrakon](https://github.com/gaius-codius/ostrakon) - Çalışma sırasında düşünceleri yakalamak, bunları projeler ve makineler arasında…
- [GarvitNangru/claude-code-mods](https://github.com/GarvitNangru/claude-code-mods) - Claude Code için modlar ve görünümler: Claude.
- [Gat0rRex/claude-mods](https://github.com/Gat0rRex/claude-mods) - Claude Code modları (işlev kancası eklentileri): bağlam bandı, açık uçlar…
- [gauravruhela07/claude-mods](https://github.com/gauravruhela07/claude-mods) - Yedi Claude Code modu: savvy-progress, skins, filetree, cache-tax…
- [GeckoKing9/claude-code-copy-button](https://github.com/GeckoKing9/claude-code-copy-button) - Claude Code yanıtlarındaki her kod bloğunda Ctrl+tıklamayla bağlantı kopyalama…
- [Gersom/gersom-claude-mods](https://github.com/Gersom/gersom-claude-mods) - Claude Code modları: usage-meter gibi kanca eklentileri.
- [Gharib89/claude-mods](https://github.com/Gharib89/claude-mods) - Tek bir marketplace üzerinden yüklenen Claude Code modları.
- [gomymy64/claude-code-mods-cheatsheet](https://github.com/gomymy64/claude-code-mods-cheatsheet)
- [gotzastory/my-mods](https://github.com/gotzastory/my-mods) - Claude Code modları: context-bar-plus (bağlam çubuğu, kota, alt ajan modları).
- [hahahahahahahahah6/mod-audit](https://github.com/hahahahahahahahah6/mod-audit) - Claude Code Modları için statik tedarik zinciri denetçisi — yerel, çevrimdışı…
- [hb03/claude-mods](https://github.com/hb03/claude-mods) - Claude Code için Almanca modlar: bağlam/önbellek bildirimleri, talimatlarla…
- [Hsiang-LinC/vault-jot](https://github.com/Hsiang-LinC/vault-jot) - Claude Code mod: capture ideas into an Obsidian vault inbox from any session.
- [Huuuuung/think-meter](https://github.com/Huuuuung/think-meter) - Claude Code modu: her yanıtın ne kadar sürdüğü, Claude.
- [huynl-96/claude-mods](https://github.com/huynl-96/claude-mods) - Claude Code modları: streamer-mode, ekranınızı paylaşırken özel panelleri…
- [hyperbola-bear/claude-mods](https://github.com/hyperbola-bear/claude-mods) - claude modlarım için.
- [icedevil2001/auto-continue](https://github.com/icedevil2001/auto-continue) - Claude Code modu: 5 saatlik kullanım sınırının dolmasını bekler ve sizin için…
- [icedevil2001/claude-mods](https://github.com/icedevil2001/claude-mods) - Claude Code için küçük modlar; 5 saatlik sınırdan sonra otomatik devam ile…
- [im-adarsh/claude-mods](https://github.com/im-adarsh/claude-mods)
- [imsungbin/quackpit-mod](https://github.com/imsungbin/quackpit-mod) - Claude Code isteminizin üzerinde bir kokpit. Ördek göstergeleri okur.
- [jakerains/claudemods](https://github.com/jakerains/claudemods) - Küçük Claude Code modları: bağlam ve plan kullanımı göstergeleri, istem…
- [jasonwblock/sdlc-tracker](https://github.com/jasonwblock/sdlc-tracker) - SDLC Tracker: a Claude Code mod with a side pane showing where each work item…
- [jduerrmann/agent-crew](https://github.com/jduerrmann/agent-crew) - Her alt ajan, dokunduğu dosyalar ve oturumunuzun kullanımı ile maliyeti için…
- [jessetsai1024/claude-ctx-panel](https://github.com/jessetsai1024/claude-ctx-panel) - Kenar çubuğunda bağlam kullanım paneli: toplam, kategoriler, tur başına büyüme…
- [jessetsai1024/claude-files](https://github.com/jessetsai1024/claude-files) - Kenar çubuğunda dosya listesi: bu konuşmada hangi dosyalar oluşturuldu…
- [jessetsai1024/claude-maomao](https://github.com/jessetsai1024/claude-maomao) - Girdi kutusunun üzerinde koşup zıplayan 8-bit tarzı 毛毛.
- [jessetsai1024/claude-prompts](https://github.com/jessetsai1024/claude-prompts) - Kenar çubuğunda “sorduğum sorular”: kullanıcının bu konuşmada yazdığı her…
- [jessetsai1024/claude-timeline](https://github.com/jessetsai1024/claude-timeline) - Kenar çubuğunda zaman çizelgesi: bu turda zaman nereye harcandı.
- [jessetsai1024/claude-tokens](https://github.com/jessetsai1024/claude-tokens) - Kenar çubuğunda token alışverişi: ana konuşma her seferinde Anthropic.
- [jessetsai1024/claude-whisper](https://github.com/jessetsai1024/claude-whisper) - claude code.
- [jimmysteinmetz/b-sides](https://github.com/jimmysteinmetz/b-sides) - Yeni eğik çizgi komutları ve yan bölmeler gibi Claude Code için küçük modlar.
- [jjjung0921/claude-mods](https://github.com/jjjung0921/claude-mods)
- [jkf87/mod-guide](https://github.com/jkf87/mod-guide) - 6 dilde, aranabilir bir mod diziniyle birlikte Claude Code modları.
- [KaiC5504/clawd-bar](https://github.com/KaiC5504/clawd-bar) - Clawd, Claude Code prompt.
- [kajidog/cc-mods-tts](https://github.com/kajidog/cc-mods-tts) - Claude Code.
- [kbrdn1/claude-crosstalk](https://github.com/kbrdn1/claude-crosstalk) - Claude Code oturumlarınız arasındaki konuşmaları okumak ve bu konuşmalara…
- [ke11/claude-mods](https://github.com/ke11/claude-mods) - Claude Code mods. PixBar: a pixel creature above your prompt that moves with…
- [Khanthtutzin/subagent-crew](https://github.com/Khanthtutzin/subagent-crew) - Claude Code modu: istemin üzerinde piksel Claude maskotları olarak çalışan alt…
- [kkatsuyoshi/claude-mods](https://github.com/kkatsuyoshi/claude-mods) - claude modları.
- [KKK12142/claude-mods](https://github.com/KKK12142/claude-mods) - Claude Code modları (usage-meter, ...).
- [krishna-goutham-tls/cc-mods](https://github.com/krishna-goutham-tls/cc-mods) - İki Claude Code modu: sohbetin yanında bir dosya bölmesi olan folio ve durum…
- [kuehn-lars/cc-graph](https://github.com/kuehn-lars/cc-graph) - cc-graph: a live graph oh what Claude Code knows.
- [leonidb/claude-code-mods](https://github.com/leonidb/claude-code-mods) - Claude Code.
- [LordMordelon/claude-mods](https://github.com/LordMordelon/claude-mods) - Angel (Vremia) projeleri için Claude Code modları.
- [Lucas-CX/awesome-claude-mods](https://github.com/Lucas-CX/awesome-claude-mods) - Topluluk tarafından derlenmiş bir Claude Code Modları rehberi: kullanım…
- [M-i-k-e-l/agent-state](https://github.com/M-i-k-e-l/agent-state) - Claude.
- [malinfossum/mango-buddy](https://github.com/malinfossum/mango-buddy) - Claude Code isteminizin üstünde tüylü siyah bir kedi.
- [MarcusJellinghaus/claude-mode-gate](https://github.com/MarcusJellinghaus/claude-mode-gate) - Değiştirilebilir izin profillerine sahip bir Claude Code modu: güvenli bir…
- [MDmubarak786/claude-mods](https://github.com/MDmubarak786/claude-mods) - Claude Code için topluluk modları: Claude Code içinde çalışan korumalar…
- [michaelblaess/turbo-mod](https://github.com/michaelblaess/turbo-mod) - Claude Code için yan panel: Claude.
- [micke-dahlgren/token-range-monitor](https://github.com/micke-dahlgren/token-range-monitor) - Claude Code mod: projects what will be left of your weekly and 5-hour Claude…
- [mmedum/glimt](https://github.com/mmedum/glimt) - Claude Code için sessiz bir yan bölme: bu oturumun ne yaptığı, planı, ajanları…
- [mmedum/nuet](https://github.com/mmedum/nuet) - Claude Code dökümündeki her istemin ve her yanıtın üzerinde, kendi saat…
- [mmedum/spor](https://github.com/mmedum/spor) - Claude Code&#x27;un katlayarak gizlediği şeyleri geri getirir: Claude&#x27;in okuduğu…
- [mrsono0/ctx-footer](https://github.com/mrsono0/ctx-footer) - Claude Code modu: istem altbilgisi mod yuvasında bağlam penceresi kullanımını…
- [muellerei/enable-todo-tools](https://github.com/muellerei/enable-todo-tools) - Oturum başlangıcında CLAUDE_CODE_ENABLE_TODO_TOOLS ayarlayarak, bunları devre…
- [muellerei/task-line](https://github.com/muellerei/task-line) - Claude Code modu: istemin üzerinde görev listesi başına bir satır;
- [nachtgold/claude-code-connect-four](https://github.com/nachtgold/claude-code-connect-four) - Claude Code içinde bir AI.
- [naoanao/agent-cross-check](https://github.com/naoanao/agent-cross-check) - Claude Code modu: başka bir kodlama ajanı deponuza commit yaptığında Claude…
- [naoanao/shared-repo-guard](https://github.com/naoanao/shared-repo-guard) - Birden çok AI ajanının paylaştığı depolar için Claude Code modu: gizli…
- [nerevar48/nerevar-mods](https://github.com/nerevar48/nerevar-mods) - Claude Code mods marketplace.
- [nu0ma/query-guard](https://github.com/nu0ma/query-guard) - Claude Code.
- [OG-Matcha/tessera](https://github.com/OG-Matcha/tessera) - Claude Code, Windows ve CJK öncelikli tek bir mod: herhangi bir terminalde…
- [onk3sh/fix-on-edit](https://github.com/onk3sh/fix-on-edit)
- [Open01277/claude-mods](https://github.com/Open01277/claude-mods)
- [osaki42/awesome-claude-mods](https://github.com/osaki42/awesome-claude-mods) - Sizin için yaptıklarına göre sıralanmış en iyi Claude Code Modları.
- [pablodiazjorge/impact-radius](https://github.com/pablodiazjorge/impact-radius) - Riskli kabuk komutlarını.
- [Para-FR/claude-code-mods-fr](https://github.com/Para-FR/claude-code-mods-fr) - Claude Code için iki Claude Modu: garde-du-corps.
- [Paradox07127/claude-utopia](https://github.com/Paradox07127/claude-utopia) - Ajan telemetrisi, zaman çizelgesi panoları, mmrun çapraz model incelemesi ve…
- [paragpandyareal/swear-slap](https://github.com/paragpandyareal/swear-slap) - Claude Code.
- [paulosergio-jnr/claude-code-mods](https://github.com/paulosergio-jnr/claude-code-mods) - Claude Code Mods repo.
- [paulpc2/claude-code-mods](https://github.com/paulpc2/claude-code-mods) - Claude Code modları: usage-both, istemin üzerinde 5 saatlik ve haftalık…
- [philarete173/claude_mods](https://github.com/philarete173/claude_mods) - Claude masaüstü uygulamasının Code sekmesi için gerçek zamanlı oturum…
- [PhilRoli/traintracker-claude](https://github.com/PhilRoli/traintracker-claude) - Claude Code mod: pause sessions before your TrainTracker train arrives.
- [pompeitech/affreschi](https://github.com/pompeitech/affreschi) - Vesuvius tasarım sistemi temalı, pompeitech arayüzü için Claude Code modları.
- [pradyb/claude-mods](https://github.com/pradyb/claude-mods) - Claude Code için modifikasyonlar: safety-guard yıkıcı komutları ve gizli…
- [qazwsx1121/Claude-Code-mods](https://github.com/qazwsx1121/Claude-Code-mods)
- [rafagomes/claude-code-mods](https://github.com/rafagomes/claude-code-mods) - Claude Code için modlar: oturum içinde çalışan işlev kancası eklentileri…
- [rajib2k5/claude-market-watch](https://github.com/rajib2k5/claude-market-watch) - Claude Code modu: canlı hisse senedi şeridi, /quote bölmesi, fiyat uyarıları…
- [ramtinJ95/claude-mods](https://github.com/ramtinJ95/claude-mods) - Claude Code mods, published as one plugin marketplace.
- [ray-amjad/memory-fork](https://github.com/ray-amjad/memory-fork) - Claude Code mod: keeps auto-memory up to date in the background after every turn.
- [RedRoosterKey/claude-code-ssh-usage-band](https://github.com/RedRoosterKey/claude-code-ssh-usage-band) - Claude Code modu: istemin üzerindeki bir satırda SSH ana bilgisayarı, RAM ve…
- [Risdon8/push-ups](https://github.com/Risdon8/push-ups) - Claude Code modu: Claude çalışırken yapılacak şınavlar. Jeton yok.
- [robinade/claude-mods-ko](https://github.com/robinade/claude-mods-ko) - Claude Code modu Korece sürümünün 6 çeşidi: varsayım kaydı, kolay dil, fikir…
- [saadk408/stepline](https://github.com/saadk408/stepline) - Claude Code modu: plan modunda onayladığınız planı prompt.
- [saksham10arora-dotcom/awesome-claude-mods](https://github.com/saksham10arora-dotcom/awesome-claude-mods) - Özenle seçilmiş Claude Code modları listesi.
- [saksham10arora-dotcom/claude-frugal](https://github.com/saksham10arora-dotcom/claude-frugal) - Maliyetsiz mod: yardımcı ajanlar Haiku üzerinde çalışır;
- [saksham10arora-dotcom/claude-lofi](https://github.com/saksham10arora-dotcom/claude-lofi) - Oturumu takip eden bir lofi müzikleri: sakinlik, odaklanma, akış ve testlerin…
- [saksham10arora-dotcom/claude-teach-me](https://github.com/saksham10arora-dotcom/claude-teach-me) - Claude kod yazarken öğrenin: kodu değiştiren bir turdan sonra, tam o…
- [saksham10arora-dotcom/claude-vhs](https://github.com/saksham10arora-dotcom/claude-vhs) - Claude.
- [sam-ruff/account-switcher-claude-code-mod](https://github.com/sam-ruff/account-switcher-claude-code-mod) - A mod for claude code that allows you to switch between accounts.
- [samaphp/session-links](https://github.com/samaphp/session-links) - Oturumunuzun bahsettiği her bağlantı, istemin hemen üzerindeki tek satırda.
- [sawzhang/hello-mod](https://github.com/sawzhang/hello-mod) - Claude Code işlev kancalarının最小演示：istem üzerinde gerçek zamanlı…
- [sebastian1747/claude-mod-simple-usage-bar](https://github.com/sebastian1747/claude-mod-simple-usage-bar) - Claude Code modu: 5 saatlik, haftalık ve Fable limitlerini istemin üzerinde…
- [SeitaHigashi/claude-terminal-image](https://github.com/SeitaHigashi/claude-terminal-image) - Claude Code mod: show an image (PNG, JPEG, GIF, WebP, BMP) in a terminal pane…
- [SentientNr6/claude-mods](https://github.com/SentientNr6/claude-mods) - Claude için bir eklenti koleksiyonu.
- [shahsanket2107/clarvis](https://github.com/shahsanket2107/clarvis) - Clarvis: Claude Code için resmî olmayan bir Avengers hayran modu.
- [shengyy/ccoverhead](https://github.com/shengyy/ccoverhead) - İstemin üzerinde bağlamı, büyümeyi, kotayı, önbelleği, yerel maliyeti ve ajan…
- [shezis/claude-model-router](https://github.com/shezis/claude-model-router) - Claude Code modu: basit turları ve alt ajanları daha ucuz modellere…
- [sidhantunnithan/jindan-cc-marketplace](https://github.com/sidhantunnithan/jindan-cc-marketplace) - Kişisel Claude Code modları.
- [speti4/doom-pane](https://github.com/speti4/doom-pane) - The original DOOM in a Claude Code pane with nothing to install: the engine…
- [steven-ngle/blade-of-commits](https://github.com/steven-ngle/blade-of-commits) - Dans eden pixel-art Malenia ile Claude Code için tek tıkla commit mesajları.
- [su-record/claude-mods](https://github.com/su-record/claude-mods) - Kişisel Claude Code modları.
- [takiguchi-yu/claude-mods](https://github.com/takiguchi-yu/claude-mods) - Yerel olarak kullanılan Claude Code modları deposu.
- [Tanish-Dev/claude-usage-band](https://github.com/Tanish-Dev/claude-usage-band) - Clawd Meter — Claude Code modu; Claude plan kullanımınızı.
- [tartinerlabs/claude-code-mods](https://github.com/tartinerlabs/claude-code-mods)
- [TFoxik/claude-model-router](https://github.com/TFoxik/claude-model-router) - A Claude Code mod that picks the model and effort for each kind of work, and…
- [TheBabaYaga/claude-session-flow](https://github.com/TheBabaYaga/claude-session-flow) - Her istemi, Claude.
- [theishandubey/claude-mods](https://github.com/theishandubey/claude-mods) - Modlardan oluşan bir Claude Code eklenti pazaryeri: Claude Code içinde bantlar…
- [Tora29/my-claude-tools](https://github.com/Tora29/my-claude-tools) - Claude Mods.
- [trietsch/claude-customizations](https://github.com/trietsch/claude-customizations) - Claude Code için özelleştirmeler.
- [tunglt1810/claude-gadgets](https://github.com/tunglt1810/claude-gadgets) - Bazı Claude modları.
- [TurboKach/cc-language-improve](https://github.com/TurboKach/cc-language-improve) - Yazarken isteminizin İngilizcesini denetleyen Claude Code modu.
- [tusharck/mods-for-claude](https://github.com/tusharck/mods-for-claude) - Her biri sizin için oluşturulmasını sağlayan kopyala-yapıştır istemi içeren…
- [ulttla/claude-mod-repo](https://github.com/ulttla/claude-mod-repo) - Claude Code modları: istemin üzerinde bağlam ve plan limiti ölçer ve yeni…
- [VaitaR/claude-code-limits](https://github.com/VaitaR/claude-code-limits) - Claude Code modu: istemin üstünde tek satırda 5h/7d kotası, bağlam penceresi…
- [VAlux/claude-session-progress](https://github.com/VAlux/claude-session-progress) - Claude Code modu: uzun süren görevler için animasyonlu ilerleme bandı ve…
- [Vansitha/clawd-watch](https://github.com/Vansitha/clawd-watch) - Üç küçük Claude Code modu: alt ajanlarınızın ne zaman tamamlanacağını görün…
- [varunmoka7/image-shrinker](https://github.com/varunmoka7/image-shrinker) - Claude onları okumadan önce büyük ekran görüntülerini küçültür;
- [varunmoka7/layman](https://github.com/varunmoka7/layman) - &quot;Kayboldum&quot; deyin, Claude son yanıtını günlük ifadelerle yeniden açıklasın.
- [varunmoka7/next-steps-autopilot](https://github.com/varunmoka7/next-steps-autopilot) - İstem kutusunun üzerinde önerilen sonraki istemleri gösterir.
- [varunmoka7/side-chat](https://github.com/varunmoka7/side-chat) - Çalışmanızın yanındaki bir bölmede Claude.
- [Victormartinsilva/MODS-CLAUDECODE](https://github.com/Victormartinsilva/MODS-CLAUDECODE) - Tek adımlı kurulum ve Portekizce video rehberi içeren Claude Code modları…
- [vihrea1337/headroom](https://github.com/vihrea1337/headroom) - Claude Code için hız sınırı geri sayımları ve tüketim hızı tahmini.
- [Wasif-ZA/claude-mods](https://github.com/Wasif-ZA/claude-mods)
- [wukonigcom/quanta-costa](https://github.com/wukonigcom/quanta-costa) - 🧾 Claude Code eklentisi: Claude Pro/Max kullanım limitleriniz, hız tahmini…
- [xinhuagu/oh-my-claude-mods](https://github.com/xinhuagu/oh-my-claude-mods) - Claude Code için modlar. agent-crew: alt aracılarınızı rol, model, mevcut araç…
- [yeonwooook/claude-study-latex](https://github.com/yeonwooook/claude-study-latex) - Claude.
- [YohanGarcia/agent-taskboard](https://github.com/YohanGarcia/agent-taskboard) - Claude Code için canlı görev panosu: oluşturmadan önce planlayın, her görevi…
- [yuntaengtaeng/snitch](https://github.com/yuntaengtaeng/snitch) - Claude Code modu, Claude.
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - Durdurulamaz Anthropic PBC ekibinden (bağlantısı yoktur), kodlama…
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) - Neler olduğunu gösteren bir Claude Code eklentisi - bağlam kullanımı, etkin…
- [sirmalloc/ccstatusline](https://github.com/sirmalloc/ccstatusline) - 🚀 Claude Code CLI için powerline desteği, temalar ve daha fazlasını içeren…
- [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) - Claude Code.
- [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) - Claude Code.
- [Owloops/claude-powerline](https://github.com/Owloops/claude-powerline) - Claude Code için güzel, vim tarzı powerline.
- [persiyanov/herdr-reviewr](https://github.com/persiyanov/herdr-reviewr) - Kodlama aracınızın diff.
- [devswha/herdr-web-ui](https://github.com/devswha/herdr-web-ui) - Browser and phone client for herdr: chat and live terminal for every agent…
- [uppinote20/claude-dashboard](https://github.com/uppinote20/claude-dashboard) - Bağlam kullanımı, API hız sınırları ve maliyet takibiyle Claude Code için…
- [a86582751/dsh-nexttavern](https://github.com/a86582751/dsh-nexttavern) - DeepSeek Harness için uzun biçimli rol yapma agent.
- [L-Forster/open-jet](https://github.com/L-Forster/open-jet) - An offline coding agent for local models.
- [backstabslash/goccc](https://github.com/backstabslash/goccc) - Fast, zero-dependency cost calculator and customizable statusline for Claude…
- [kylesnowschwartz/tail-claude-hud](https://github.com/kylesnowschwartz/tail-claude-hud) - Claude Code oturumları için terminal statusline.
- [arturogarrido/claudinho](https://github.com/arturogarrido/claudinho) - ⚽ Takip ettiğiniz müsabaka için canlı futbol skorları, fikstürler ve puan…
- [WormAlien/hub-cc](https://github.com/WormAlien/hub-cc) - Claude Code için Windows ve macOS üzerinde yerel kontrol düzlemi: sabit bir uç…
- [philoserf/claude-code-config](https://github.com/philoserf/claude-code-config) - ~/.claude içinde sürümlendirilen kişisel Claude Code yapılandırması…
- [ashafizullah/claude-code-muslim-mods](https://github.com/ashafizullah/claude-code-muslim-mods) - Claude Code içinde namaz vakitleri, Hicri tarih, zikirler, günlük ayet, sünnet…
- [livlign/ccbit](https://github.com/livlign/ccbit) - Claude Code için oturum farkındalığına sahip durum satırı.
- [GoSlowPoke168/claude-statusline](https://github.com/GoSlowPoke168/claude-statusline) - Claude Code için iki satırlı truecolor durum satırı.
- [proDreams/dsh-tidewatch](https://github.com/proDreams/dsh-tidewatch) - A floating peak/off-peak tide card for DeepSeek Harness: i18n (en/zh/ru)…
- [pierrebelin/claude-code-toolkit](https://github.com/pierrebelin/claude-code-toolkit) - .NET DDD/Clean Architecture için taşınabilir Claude Code araç seti: katı TDD…
- [jcdendrite/claude-config](https://github.com/jcdendrite/claude-config) - Taşınabilir Claude Code genel yapılandırması: özel beceriler, PreToolUse…
- [mutlumehmet/claude-plugins](https://github.com/mutlumehmet/claude-plugins) - Her gün kullandığım Claude Code eklentileri: herkesin makinesinde çalışacak…
- [chaybits/ai-session-usage](https://github.com/chaybits/ai-session-usage) - Claude Code and ChatGPT (Codex) subscription limits in one card: a KDE Plasma 6…
- [frsorrentino/fable-director](https://github.com/frsorrentino/fable-director) - Claude Code için token yönetimi: en üst model yönlendirir, yürütme en ucuz…
- [jeancarlo-javier/claude-status-bar](https://github.com/jeancarlo-javier/claude-status-bar) - Claude Code için canlı iş akışı aşaması durum satırı.
- [rootstudioyaml/sprag](https://github.com/rootstudioyaml/sprag) - Claude Code ve Codex token harcamasını azaltın: aramaları ve test…
- [tedserbinski/claude-code-statusline](https://github.com/tedserbinski/claude-code-statusline) - Claude Code için basit ve kullanışlı durum satırı kurulumu.
- [aquahitt/claude-code-limit-alerts](https://github.com/aquahitt/claude-code-limit-alerts) - Claude Code için kullanım sınırı uyarıları: macOS bildirimleri, uygulama içi…
- [crosscountryridinggirlwonder916/claude-statusline](https://github.com/crosscountryridinggirlwonder916/claude-statusline) - Display Claude Code statusline with rate limits, current directory, and Git…
- [fbincon/claude-code-statusline](https://github.com/fbincon/claude-code-statusline) - Linux, WSL, Windows ve macOS için yapılandırılabilir Claude Code durum satırı;
- [JairoTorregrosa/claude-statusline](https://github.com/JairoTorregrosa/claude-statusline) - Claude Code için hızlı Rust durum satırı — önce yük, önbelleğe alınmış git…
- [jsh135790/claude-code-capsule-panel](https://github.com/jsh135790/claude-code-capsule-panel) - Claude Code için canlı kullanım panosu — Catppuccin kapsül tarzı bir yan…
- [jv-k/claude-gauge](https://github.com/jv-k/claude-gauge) - Claude Code için bir durum satırı ve token satırı: bağlam, tempo…
- [kyllian330/claude-statusline](https://github.com/kyllian330/claude-statusline) - Model, bağlam, sınırlar, git bilgileri ve oturum süresi dahil olmak üzere…
- [Ma1achy/claude-statusline](https://github.com/Ma1achy/claude-statusline) - Claude Code için her şeyi kurcalamaya uygun, kullanıcı dostu durum satırı…
- [Obednal97/claude-statusline-kit](https://github.com/Obednal97/claude-statusline-kit) - Çok satırlı Claude Code durum satırı: harcama, bağlam yüzdesi, git ve etkin…
- [salvanya/claude_code_statusline](https://github.com/salvanya/claude_code_statusline) - claude code için kullanışlı bilgiler içeren durum satırı.
- [tc3oliver/claude-team-kit](https://github.com/tc3oliver/claude-team-kit) - Yerel aracı ekipleri. Kontrol altında.
- [yedidya-buildfy/claude-addons](https://github.com/yedidya-buildfy/claude-addons) - Claude Code eklentileri: sekme durumunda renkli nokta izleyicisi + yerleşik GSD…
- [akhilnalliboina/claude-usage-statusline](https://github.com/akhilnalliboina/claude-usage-statusline) - macOS ve Linux için Claude Code kullanım durum satırı, herdr yükleyici…
- [andkirby/claude-statusline](https://github.com/andkirby/claude-statusline) - Claude Code için özel durum satırı — kullanım yüzdesi, bağlam boyutu, maliyet…
- [AsyrafHussin/claude-code-statusline](https://github.com/AsyrafHussin/claude-code-statusline) - Claude Code için sade ve bilgilendirici bir durum satırı — projeyi, git…
- [BedirYilmaz/claude-crt-hud-mod](https://github.com/BedirYilmaz/claude-crt-hud-mod) - Claude CRT HUD modu: terminalde ve masaüstündeki Code sekmesinde Claude Code…
- [bunderlog/claude-plugins](https://github.com/bunderlog/claude-plugins) - baloo içeren Claude Code eklenti pazaryeri: beceriler, değişiklikleri projenin…
- [ctfbio/claude-code-statusline](https://github.com/ctfbio/claude-code-statusline) - Profesyonel düzeyde Claude Code durum satırı: oturum süresi, ECB döviz…
- [cvrt-gmbh/claude-statusline](https://github.com/cvrt-gmbh/claude-statusline) - Claude Code için abonelik farkındalıklı durum satırı.
- [dave-net-positive/Claude_Code_PII_Redactor](https://github.com/dave-net-positive/Claude_Code_PII_Redactor) - Mod that detects and redacts PII in Claude Code before it reaches the model.
- [diegorv/koko.claude-statusline](https://github.com/diegorv/koko.claude-statusline) - Claude Code için zengin bir terminal durum satırı — Bun + TypeScript, çalışma…
- [ejklock/claude-mermaid-render](https://github.com/ejklock/claude-mermaid-render) - Transkriptte Mermaid diyagramlarını güzelce oluşturan Claude Code eklentisi…
- [fbandres/ccmods](https://github.com/fbandres/ccmods) - Mods for Claude Code: live panes, gauges and more, installable as plugins.
- [filtercoffeeway/claude-kit](https://github.com/filtercoffeeway/claude-kit) - Claude Code için araçlar, beceriler ve aracılar — model, dal, PR, bağlam…
- [FunDrivenDev/claude-plugins](https://github.com/FunDrivenDev/claude-plugins) - Public Claude Code plugins: a context-budget status line.
- [giribboy77-arch/claude-statusline](https://github.com/giribboy77-arch/claude-statusline) - Claude Code özel durum satırı (model, efor, bağlam, önbellek, kullanım sınırı).
- [hardtomakeanadress/claude-code-deepseek-cost](https://github.com/hardtomakeanadress/claude-code-deepseek-cost) - Claude Code için gerçek DeepSeek API harcaması: oturum dökümlerini DeepSeek…
- [hieuvo/claude-imgview](https://github.com/hieuvo/claude-imgview) - Görüntüleri Claude Code içinde önizleyin: resmi açmak için bir yanıtın…
- [HiramAA/claude-desktop-mods](https://github.com/HiramAA/claude-desktop-mods) - Claude Code ve WSL ile Windows içindeki Claude Desktop için modlar: istemin…
- [ihororlovskyi/claude-statusline](https://github.com/ihororlovskyi/claude-statusline) - Ajan paneli satırları içeren Claude Code durum satırı.
- [izahamyatim/claude-plugin-fizzy](https://github.com/izahamyatim/claude-plugin-fizzy) - 🚀 Gerçek zamanlı ekip görünürlüğü için Claude.
- [kernastra/claudecode](https://github.com/kernastra/claudecode) - Oluşturduğum ve paylaşmak istediğim Claude Code becerileri, modları ve diğer…
- [konnichiwab/claude-code-config](https://github.com/konnichiwab/claude-code-config) - Claude Code ayar menüsü, durum satırı ve yapılandırma.
- [Leechlike-intangibleasset343/claude-code-statusline](https://github.com/Leechlike-intangibleasset343/claude-code-statusline) - Track Claude Code status with a compact dashboard showing context, cost…
- [mgstegmaier/claude-plugins](https://github.com/mgstegmaier/claude-plugins) - Ev yapımı, kafessiz claude eklentileri, becerileri, modları ve daha fazlası.
- [msinclair-sudo/claude-code-setup](https://github.com/msinclair-sudo/claude-code-setup) - Claude Code ortam yükleyicisi: skills, statusline, hooks, permissions ve isteğe…
- [muemadennis/claude-code-command-center](https://github.com/muemadennis/claude-code-command-center) - Claude Code Live Dashboard 2026: Track Costs, Tokens &amp; Git Branch Status.
- [OpenClawFarm/claude-statusline](https://github.com/OpenClawFarm/claude-statusline) - Claude Code için HUD tarzı durum satırı — ağ durumu, TPS, bağlam, kotalar ve…
- [oshnilia/claude-plugins](https://github.com/oshnilia/claude-plugins) - Claude.
- [pirncedark/afu-claude-statusline](https://github.com/pirncedark/afu-claude-statusline) - Claude Code için renkli çok satırlı durum çubuğu.
- [rainyfei/claude-statusline-win](https://github.com/rainyfei/claude-statusline-win) - Windows (PowerShell) için Claude Code durum satırı: kullanım çubukları, tempo…
- [roy651/cc-plugins](https://github.com/roy651/cc-plugins) - Claude Code için Bearings and Glossary modu.
- [satoramoto/awesome-claude](https://github.com/satoramoto/awesome-claude) - Paylaşılan bileşen kiti, playground ve Storybook ile Claude Code yapılandırması…
- [Sofia-D4L/claude-conf](https://github.com/Sofia-D4L/claude-conf) - Przenośna konfiguracja Claude Code (statusline + instalator).
- [SohamShirsat/claude-cockpit](https://github.com/SohamShirsat/claude-cockpit) - A small dashboard for Claude Code: context %, cache countdown, 5-hour &amp; weekly…
- [speti4/claude-statusline](https://github.com/speti4/claude-statusline) - Custom terminal status bar for Claude Code: model, directory, git state…
- [thaiquangquy/claude.me](https://github.com/thaiquangquy/claude.me) - Taşınabilir Claude Code yapılandırması: CLAUDE.md, ayarlar, durum satırı…
- [Tina0529/claude-session-radar](https://github.com/Tina0529/claude-session-radar) - Claude Code masaüstü (macOS) modu: tıklayarak gidilebilen oturum bildirimleri…
- [unlocked-spark/claude-code-earshot](https://github.com/unlocked-spark/claude-code-earshot) - Claude Code için ekran okuyucu yardımcı modu (Unlocked Spark Foundation).
- [viplav-artha/claude-code-lessons](https://github.com/viplav-artha/claude-code-lessons) - Claude Code hakkında uygulamalı ve doğrulanmış kapsamlı inceleme — CLAUDE.md…
- [vladimir-ks/ai-agile-claude-code-statusline](https://github.com/vladimir-ks/ai-agile-claude-code-statusline) - Claude Code için gerçek zamanlı maliyet takibi ve oturum izleme durum satırı.
- [warodan/vscode-claude-code-patch](https://github.com/warodan/vscode-claude-code-patch) - Claude Code skill (VS Code, Windows): image previews and open buttons under…
- [ymoud/claude-code-statusline](https://github.com/ymoud/claude-code-statusline) - Klasörü, git dalını, modeli, bağlam penceresi kullanımını ve plan kullanım…
- [YoniYon00/claude-feedback-rings](https://github.com/YoniYon00/claude-feedback-rings) - Context Rot Detector 2026 - Claude Code Ajanları için Proaktif AI Bellek ve Hız…
- [zhuyansen/awesome-claude-code-hooks](https://github.com/zhuyansen/awesome-claude-code-hooks) - Claude Code kancaları, alt ajanları ve durum satırları: türe göre düzenlenmiş…
- [tronschell/statusline.sh](https://github.com/tronschell/statusline.sh) - Claude Code durum satırları için görsel oluşturucu.
- [Magnus-Gille/tokenatlas](https://github.com/Magnus-Gille/tokenatlas) - Gerçek zamanlı belirteç kullanımını ve tahmini enerji tüketimini gösteren…
- [Apparux/cc-fusion](https://github.com/Apparux/cc-fusion) - Claude Code durum satırı: CCometixLine görünümü + Claude HUD işlevselliği.

</details>

<a id="dsh-cordis"></a>

## DSH ve Cordis eklenti ekosistemleri

DeepSeek Harness ve Cordis aynı yere farklı bir yönden ulaşır: onlar için eklenti, mod mekanizmasıdır; dolayısıyla oradaki bir eklenti, buradaki bir moda denktir.

<details>
<summary>🧵 <b><a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b> · ⭐74325 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Özet

🌊 Özgün agent harness. Akıllı çok oyunculu sürüleri dağıtın, otonom iş akışlarını koordine edin ve konuşmaya dayalı AI sistemleri oluşturun. Uyarlanabilir bellek, kendi kendine öğrenen zekâ, federasyon, vektör RAG entegrasyonu ve yerel Claude Code / Codex / Hermes ile daha birçok entegre özelliğe sahiptir

<sub>🔧 Kodda kullanıldığı bulundu: `plugins/ruflo-swarm/README.md`, `plugins/ruflo-swarm/hooks/model/members.ts`, `v3/docs/validation/mod-api-coverage-2026-10.md`, `plugins/ruflo-swarm/hooks/register.ts`</sub>

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                    |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |
| Dil      | TypeScript                                                               |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **74325**  |
| Son gönderme   | 2026-10-11 |
| İlk listelenme | 2026-10-04 |

🏷 `agentic-ai` · `agentic-framework` · `agentic-workflow` · `agents` · `ai-agents` · `ai-assistant` · `ai-skills` · `autonomous-agents`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/2ca82c9c9a7fca31.gif" width="100%" alt="ruvnet/ruflo animation"><br><sub>animasyonlu kayıt</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/nexu-io/open-design">nexu-io/open-design</a></b> · ⭐100497 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

🎨 En iyi DeepSeek Harness Tasarım Eklentisi. Açık kaynaklı Claude Design alternatifi. 🖥️ Yerel öncelikli masaüstü uygulaması. 🖼️ Kodlama aracınız tasarım motoruna dönüşür: prototipler, açılış sayfaları, panolar, slaytlar, görseller ve videolar — gerçek dosyalar, HTML/PDF/PPTX/MP4 dışa aktarma. 🤖 BYOK üzerinden Claude Code / Codex / Cursor / DeepSeek Harness / OpenCode ve 20’den fazla CLI.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | TypeScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **100497** |
| Son gönderme   | 2026-10-11 |
| İlk listelenme | 2026-10-04 |

🏷 `agent-skills` · `ai-design` · `byok` · `claude-code-for-design` · `claude-design` · `codex-design` · `coding-agents` · `cursor-design`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nexu-io--open-design/a1049df34322d3ce.png" width="100%" alt="nexu-io/open-design screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/morluto/rea">morluto/rea</a></b> · ⭐87809 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

Uygulama davranışından yerel ikili dosyalara kadar her şeyi ajanlarla tersine mühendislik yöntemiyle analiz edin.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | TypeScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **87809**  |
| Son gönderme   | 2026-10-11 |
| İlk listelenme | 2026-10-05 |

🏷 `agent-skills` · `ai-agents` · `binary-analysis` · `claude-code` · `cli` · `codex` · `cordis` · `ctf`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--rea/f46ca8b1518ae39f.png" width="100%" alt="morluto/rea screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/tt-a1i/archify">tt-a1i/archify</a></b> · ⭐81879 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

Herhangi bir fikri, planı veya kod tabanını güzel ve etkileşimli bir diyagrama dönüştürün. Claude Code, Codex ve daha fazlası için bir araç becerisi.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | JavaScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **81879**  |
| Son gönderme   | 2026-10-11 |
| İlk listelenme | 2026-10-04 |

🏷 `agent-skills` · `ai-agents` · `architecture-diagram` · `claude-code` · `claude-skills` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tt-a1i--archify/71b7d4b2427db202.png" width="100%" alt="tt-a1i/archify screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/esengine/DeepSeek-Reasonix">esengine/DeepSeek-Reasonix</a></b> · ⭐35759 · Go · 🔎 inferred · 0 天</summary>

##### 📝 Özet

Karmaşık yazılım mühendisliği görevleri için güvenilir bir kodlama aracısı.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | Go                                                                                              |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **35759**  |
| Son gönderme   | 2026-10-11 |
| İlk listelenme | 2026-10-06 |

🏷 `agent` · `agent-framework` · `ai-agent` · `ai-coding` · `cli` · `coding-agent` · `deepseek` · `developer-tools`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/zhu1090093659/dsh-web">zhu1090093659/dsh-web</a></b> · ⭐8626 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

DeepSeek Harness (DSH) Web eklenti toplama ekosistemi · Her şey bir eklentidir, Creative Workshop üzerinden dağıtılır｜｜DeepSeek Harness (DSH) Web Plugin Aggregation Ecosystem · Everything is a plugin, distributed via the Creative Workshop

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | TypeScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **8626**   |
| Son gönderme   | 2026-10-10 |
| İlk listelenme | 2026-10-04 |

🏷 `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-web` · `dsh-web-ui`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zhu1090093659--dsh-web/5153c3c61827ebb8.jpg" width="100%" alt="zhu1090093659/dsh-web screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-market/dsh-market">dsh-market/dsh-market</a></b> · ⭐6146 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

DeepSeek Harness içindeki eklenti pazarı — göz atın, arayın, tek tıklamayla kurun · DSH görsel eklenti pazarı

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | TypeScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **6146**   |
| Son gönderme   | 2026-10-11 |
| İlk listelenme | 2026-10-11 |

🏷 `deepseek-harness` · `dsh-plugin` · `marketplace`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dsh-market--dsh-market/06b60aace017dab8.png" width="100%" alt="dsh-market/dsh-market screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/MeteorNOX/DeepSeek-Balance-Whale-Widget">MeteorNOX/DeepSeek-Balance-Whale-Widget</a></b> · ⭐4478 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

DeepSeek Harness（DSH）arayüzünün sağ alt köşesinde yaşayan, DeepSeek hesabınızın bakiyesini takip etmenize yardımcı olan küçük bir balina kızı. Pofuduk ve sevimli; sürükleyip kenara yapışmayı, sola yapışınca ters dönmeyi ve sayı kaydırma animasyonunu destekler. Arayüzle birlikte otomatik olarak etkinleşir; dsh kurulumunuzla doğrudan başlatmanız önerilir.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | JavaScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **4478**   |
| Son gönderme   | 2026-10-11 |
| İlk listelenme | 2026-10-11 |

🏷 `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-plugin` · `dsh-plugins` · `floating-widget`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/meteornox--deepseek-balance-whale-widget/c17efbb95a7522ee.png" width="100%" alt="MeteorNOX/DeepSeek-Balance-Whale-Widget screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ccch1mneyyy/dsh-TUI">ccch1mneyyy/dsh-TUI</a></b> · ⭐4285 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

DSH için resmî olarak en çok önerilen TUI eklentisi — yüksek performans, düşük kaynak kullanımı, sevimli piksel balina ve akıcı fare etkileşimi. npm ile tek komutla kurulum. / DSH 官方首推的 TUI 插件，高性能低占用，可爱像素鲸鱼，流畅鼠标交互，npm 一键安装

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | TypeScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **4285**   |
| Son gönderme   | 2026-10-11 |
| İlk listelenme | 2026-10-10 |

🏷 `claude-code` · `coding-agent` · `deepseek` · `deepseek-harness` · `dsh-plugin` · `ink` · `react` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ccch1mneyyy--dsh-tui/18fd45f8f1eaca04.png" width="100%" alt="ccch1mneyyy/dsh-TUI screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-tauri/deepseek-harness-desktop">dsh-tauri/deepseek-harness-desktop</a></b> · ⭐3153 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

DeepSeek Harness Tauri 桌面版 | Only 8mb installer, zero environment setup, preset plugins, Windows / macOS / Linux.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | TypeScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **3153**   |
| Son gönderme   | 2026-10-11 |
| İlk listelenme | 2026-10-11 |

🏷 `deepseek` · `deepseek-harness` · `desktop` · `dsh` · `dsh-desktop` · `dsh-plugin` · `tauri`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dsh-tauri--deepseek-harness-desktop/f281725e73da1059.png" width="100%" alt="dsh-tauri/deepseek-harness-desktop screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/bowenliang123/dsh-context">bowenliang123/dsh-context</a></b> · ⭐1983 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

Bağlamı anlama ve yönetme için en iyi DeepSeek Harness eklentisi; bağlam istatistikleri, bileşimi, ayrıntıları, evrimini anlamak, bağlamın nasıl oluşturulduğunu ve nasıl geliştiğini görmek için bağlam panosu / tarayıcısı / kenar çubuğu ve bağlam komutunu içerir. Bağlam paneli, tarayıcısı, kenar çubuğu ve Context komutuyla; bağlamın bileşimini, evrimini, sıkıştırılmasını, budanmasını ve diğer olay ve eylemleri inceleyen tek duraklı DeepSeek Harness bağlam görselleştirme eklentisi.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | TypeScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **1983**   |
| Son gönderme   | 2026-10-11 |
| İlk listelenme | 2026-10-11 |

🏷 `cordis-plugin` · `deepseek-harness` · `deepseek-harness-plugin` · `dsh-external` · `dsh-plugin` · `dsh-plugins`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/bowenliang123--dsh-context/573c0e5849eea852.png" width="100%" alt="bowenliang123/dsh-context screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/anywhere-labs/Agents-Anywhere">anywhere-labs/Agents-Anywhere</a></b> · ⭐1561 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

跨设备的开源Agent工作台

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | TypeScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **1561**   |
| Son gönderme   | 2026-10-11 |
| İlk listelenme | 2026-10-11 |

🏷 `acp` · `agentclientprotocol` · `agents` · `claudecode` · `codex` · `codex-app` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/anywhere-labs/Agents-Anywhere/main/docs/images/readme-hero-zh.webp" width="100%" alt="anywhere-labs/Agents-Anywhere screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

<sub>Yeniden dağıtıma izin veren bir lisans belirtilmediği için varlığa upstream deposundan doğrudan bağlantı veriliyor.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/AdamPlatin123/dsh-plugin-radar">AdamPlatin123/dsh-plugin-radar</a></b> · ⭐1464 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Özet

DSH Plugin Radar — open-source ecosystem radar for DeepSeek Harness plugins: continuous discovery (21k+ candidates), k8s runtime validation (13k+ tests), 15-min snapshots; the catalog is a generated artifact — 开源 DSH 插件生态雷达：持续发现 2.1 万+ 候选、k8s 运行级实测 1.3 万+、15 分钟快照；插件目录为自动生成的产物

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | Python                                                                                          |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **1464**   |
| Son gönderme   | 2026-10-11 |
| İlk listelenme | 2026-10-11 |

🏷 `agent-plugins` · `continuous-validation` · `deepseek-harness` · `dsh` · `dsh-plugin` · `ecosystem-radar` · `plugin-registry`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/adamplatin123--dsh-plugin-radar/fb6ad7eb8891212c.jpg" width="100%" alt="AdamPlatin123/dsh-plugin-radar screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/EthanYoQ/AI-Novel-Writer">EthanYoQ/AI-Novel-Writer</a></b> · ⭐1401 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

AI roman yazma yazılımı: ilhamları, karakterleri, dünya kurgusunu, taslakları, bölüm yazımını, incelemeyi ve düzeltmeyi denetlenebilir bir iş akışında düzenler; Windows/macOS masaüstü sürümleri sunar ve yerel ile çevrim içi modelleri destekler. AI Roman Yazma Yazılımı: İlhamları, karakterleri, dünya kurgusunu, taslakları, bölüm yazımını, incelemeyi ve düzeltmeyi denetlenebilir bir iş akışında düzenler. Windows/macOS için masaüstü uygulamaları, Ollama entegrasyonu ve DeepSeek Harness (DSH) eklenti önizlemesi sunar.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | TypeScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **1401**   |
| Son gönderme   | 2026-10-11 |
| İlk listelenme | 2026-10-11 |

🏷 `ai-writing` · `creative-writing` · `deepseek-harness` · `dsh-plugin` · `electron` · `fiction-writing` · `local-first` · `long-form-fiction`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ethanyoq--ai-novel-writer/97081b4a6febc6aa.png" width="100%" alt="EthanYoQ/AI-Novel-Writer screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/vshulcz/deja-vu">vshulcz/deja-vu</a></b> · ⭐1171 · Go · 🔎 inferred · 0 天</summary>

##### 📝 Özet

Diskinizde zaten bulunan oturum geçmişinden oluşturulmuş Claude Code, Codex, Cursor ve 38 ek kodlama aracısı için bellek. Yerel arama, MCP ve kancalar; LLM yok, tek bir Go ikili dosyası.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | Go                                                                                              |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **1171**   |
| Son gönderme   | 2026-10-11 |
| İlk listelenme | 2026-10-04 |

🏷 `agent-memory` · `ai-memory` · `claude-code` · `claude-code-hooks` · `claude-code-plugins` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/8033ba54a9424c88.png" width="100%" alt="vshulcz/deja-vu screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/5fb930f1983f270b.gif" width="100%" alt="vshulcz/deja-vu animation"><br><sub>animasyonlu kayıt</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/myYangyunfan/dsh_desktop">myYangyunfan/dsh_desktop</a></b> · ⭐704 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

DeepSeek Harness (dsh) Windows masaüstü istemcisi - paketlenmiş Node.js + dsh CLI, tek tıklamayla başlatma

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | JavaScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **704**    |
| Son gönderme   | 2026-10-11 |
| İlk listelenme | 2026-10-10 |

🏷 `ai-agent` · `cordis` · `deepseek` · `deepseek-harness` · `desktop` · `desktop-app` · `dsh` · `dsh-desktop`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/myyangyunfan--dsh_desktop/822cff4e94634530.png" width="100%" alt="myYangyunfan/dsh_desktop screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xing-shuyin/pi-web-ui">xing-shuyin/pi-web-ui</a></b> · ⭐283 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

Just open your browser — get all your work done.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | TypeScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **283**    |
| Son gönderme   | 2026-10-11 |
| İlk listelenme | 2026-10-11 |

🏷 `dsh` · `dsh-desktop` · `dsh-plugin` · `pi` · `pi-web` · `pi-web-ui`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xing-shuyin--pi-web-ui/926fb8bfa4f6062a.jpg" width="100%" alt="xing-shuyin/pi-web-ui screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/acryldev/acryl">acryldev/acryl</a></b> · ⭐255 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

ACRYL - Agent Context Relay Yielding Lifecycles. Tek kalıcı çalışma alanı, tek kanonik bağlam, herhangi bir kodlama agent'ı.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | TypeScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **255**    |
| Son gönderme   | 2026-10-11 |
| İlk listelenme | 2026-10-11 |

🏷 `acryl` · `agent-context-relay` · `agentic` · `agentic-ai` · `agentic-coding` · `agentic-development-environment` · `agentic-workflow` · `agentic-workflows`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/acryldev--acryl/47cfe6b23e87eea1.png" width="100%" alt="acryldev/acryl screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/luobosibing2/dsh-jev-plugin">luobosibing2/dsh-jev-plugin</a></b> · ⭐203 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

Aracı seçimi, denetim, düzeltmeler ve onaylar için System One karar katmanı olarak luna gibi TypeSafe Jev veya Decision api entegre eden yerel DeepSeek Harness (DSH) eklentisi.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | JavaScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **203**    |
| Son gönderme   | 2026-10-11 |
| İlk listelenme | 2026-10-10 |

🏷 `agent-harness` · `ai-agents` · `cordis` · `decisions-api` · `deepseek-harness` · `dsh` · `dsh-jev` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/luobosibing2--dsh-jev-plugin/e27235473aa310aa.png" width="100%" alt="luobosibing2/dsh-jev-plugin screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/KelaoHu/dsh-lowtide">KelaoHu/dsh-lowtide</a></b> · ⭐170 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

DeepSeek Harness (dsh) için zamanı kaydırılmış görev devri: görevleri boş zamanınızda planlayın, yoğun olmayan saatlerde gözetimsiz çalışsınlar ve bir rapora geri dönün. İnsanlar tarafından değerlendirilen masaüstü + web deneyimi.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | TypeScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **170**    |
| Son gönderme   | 2026-10-11 |
| İlk listelenme | 2026-10-11 |

🏷 `ai-agent` · `automation` · `batch-processing` · `cordis` · `deepseek` · `deepseek-harness` · `dsh-plugin` · `llm`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/kelaohu--dsh-lowtide/3d2509a82d1a3f11.png" width="100%" alt="KelaoHu/dsh-lowtide screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Totoro-qaq/dsh-plugin-bridge">Totoro-qaq/dsh-plugin-bridge</a></b> · ⭐165 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

Önizlenebilir önayarlar arası oturum geçişi için DeepSeek Harness eklentisi. Sabit şemalı aktarımlar, durumu, kaynak modelin niyetini ve çözülmemiş görselleri korur; özgün oturum değişmeden kalır.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | JavaScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **165**    |
| Son gönderme   | 2026-10-11 |
| İlk listelenme | 2026-10-10 |

🏷 `context-migration` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `preset-migration` · `session-migration`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/totoro-qaq--dsh-plugin-bridge/568de849cd2e9608.png" width="100%" alt="Totoro-qaq/dsh-plugin-bridge screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/totoro-qaq--dsh-plugin-bridge/b4a12cab0ba15f06.gif" width="100%" alt="Totoro-qaq/dsh-plugin-bridge animation"><br><sub>animasyonlu kayıt</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/FeatherHunter/dsh-mattpocock-skills-deck">FeatherHunter/dsh-mattpocock-skills-deck</a></b> · ⭐134 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

Kurulumla birlikte mattpocock/skills v1.3.1'in 27 mühendislik ve verimlilik becerisi gelir; becerileri manuel olarak kurmanız gerekmez. 40 milyar token kullanılarak geliştirilen bu eklenti, temel becerilerin üzerinde 10 kat daha yüksek geliştirme verimliliği sunar ve yeni başlayanların bu beceri paketine daha hızlı alışmasına yardımcı olur. GitHub issue'ları tam olarak desteklenir; Markdown önizleme sürümündedir; GitLab şu anda desteklenmemektedir. Kullanımınız ve desteğiniz için teşekkürler 💗

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | JavaScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **134**    |
| Son gönderme   | 2026-10-11 |
| İlk listelenme | 2026-10-11 |

🏷 `agent` · `ai` · `claude` · `deepseek-harness` · `dsh` · `dsh-better-sidebar` · `dsh-plugin` · `github-issues`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/featherhunter--dsh-mattpocock-skills-deck/c4bd78003446c161.png" width="100%" alt="FeatherHunter/dsh-mattpocock-skills-deck screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/flymysql/dsh-remote">flymysql/dsh-remote</a></b> · ⭐133 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

Remote-work assistant for DeepSeek Harness (DSH): connect SSH (key or password), pick a remote workspace, operate with rw_* tools, and SFTP-mirror it into a real local DSH workspace.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | JavaScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **133**    |
| Son gönderme   | 2026-10-11 |
| İlk listelenme | 2026-10-11 |

🏷 `deepseek-harness` · `dsh` · `dsh-plugin` · `remote` · `sftp` · `ssh` · `tunnel` · `workspace`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/flymysql--dsh-remote/714d273f27c6d75b.png" width="100%" alt="flymysql/dsh-remote screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Nwflower/dsh-claude-style">Nwflower/dsh-claude-style</a></b> · ⭐131 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

DeepSeek Harness için Claude Code masaüstü teması｜ DeepSeek Harness web GUI için tasarlanmış Claude Code masaüstü teması

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | TypeScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **131**    |
| Son gönderme   | 2026-10-11 |
| İlk listelenme | 2026-10-10 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-desktop` · `cordis` · `dark-mode` · `deepseek-harness` · `desktop-theme`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Nwflower/dsh-claude-style/master/docs/screenshots/claude-home-dark.png" width="100%" alt="Nwflower/dsh-claude-style screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Nwflower/dsh-claude-style/master/docs/gifs/idle.gif" width="100%" alt="Nwflower/dsh-claude-style animation"><br><sub>animasyonlu kayıt</sub></td>
</tr></table>

<sub>Yeniden dağıtıma izin veren bir lisans belirtilmediği için varlığa upstream deposundan doğrudan bağlantı veriliyor.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/morluto/flameox">morluto/flameox</a></b> · ⭐130 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Özet

Runtime evidence that helps agents trace, profile, and burn down hotspots in application and native code, GPU kernels, and inference stacks.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | Python                                                                                          |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **130**    |
| Son gönderme   | 2026-10-11 |
| İlk listelenme | 2026-10-11 |

🏷 `benchmarking` · `coding-agents` · `cordis` · `debugging` · `developer-tools` · `dsh` · `dsh-plugin` · `gpu-profiling`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--flameox/2914b7977590380e.png" width="100%" alt="morluto/flameox screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Sutera-Diffusus/dsh-whale-musume">Sutera-Diffusus/dsh-whale-musume</a></b> · ⭐120 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

DeepSeek Harness masaüstü hayvanı eklentisi: Enerjik balina kızı maskotuyla kod yazarken size eşlik eder 🐋 DSH masaüstü 0.2.0-rc.2 ve eski Web sürümünü destekler (desktop pet / mascot, local-first)

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | JavaScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **120**    |
| Son gönderme   | 2026-10-11 |
| İlk listelenme | 2026-10-11 |

🏷 `ai-assistant` · `ai-companion` · `cordis` · `cute` · `deepseek` · `deepseek-harness` · `desktop-app` · `desktop-mascot`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/sutera-diffusus--dsh-whale-musume/cb85aa05cce65f77.png" width="100%" alt="Sutera-Diffusus/dsh-whale-musume screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/WestFox-AwA/dsh-prompt-optimizer">WestFox-AwA/dsh-prompt-optimizer</a></b> · ⭐113 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

DSH 插件 · 注入式优化器 0.8（主线）：你照常说话，它在你发送后,AI接收前把"这一轮到底要什么"理清楚，再把这份理解交给工作 AI(上下文注入) —— 原话不改写，条条带逐字依据。含控制界面（档位/权限/模型/上下文/只读工具）、拦截浮层（思维层+产出层）与真实 token 用量。可明显提升大多数模型的发挥稳定性,尤其DeepSeek-V4.1-Flash,可有明显提升

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | JavaScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **113**    |
| Son gönderme   | 2026-10-11 |
| İlk listelenme | 2026-10-11 |

🏷 `agent-workflow` · `ai-agent` · `cordis` · `deepseek` · `dsh` · `dsh-plugin` · `llm` · `prompt-engineering`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/westfox-awa--dsh-prompt-optimizer/3098cfd264cf8ca0.png" width="100%" alt="WestFox-AwA/dsh-prompt-optimizer screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/kukucaiCndy/Corum-Harness">kukucaiCndy/Corum-Harness</a></b> · ⭐65 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

Deepseek-Harness çekirdek altyapısı temel alınarak oluşturulmuş masaüstü Agent. Temel sistemin tüm yeteneklerini devralır ve IDE ile ilgili işlevleri tamamlar.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | TypeScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **65**     |
| Son gönderme   | 2026-10-11 |
| İlk listelenme | 2026-10-11 |

🏷 `agent` · `agent-os` · `ai-agent` · `cordis` · `desktop-app` · `dsh` · `electron` · `harness`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/kukucaicndy--corum-harness/b8971b2831acec9e.png" width="100%" alt="kukucaiCndy/Corum-Harness screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/whyihaveyou/dsh-suite">whyihaveyou/dsh-suite</a></b> · ⭐59 · HTML · 🔎 inferred · 0 天</summary>

##### 📝 Özet

Yaşayan DeepSeek Harness eklenti dizini — saatlik yenilenir, uyumluluk testleri günlük yapılır, uygulama içi eklenti mağazası ve scaffolder içerir. DSH eklenti canlı dizini: saatlik yenileme, günlük uyumluluk testi, yerleşik eklenti mağazası ve scaffolder.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | HTML                                                                                            |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **59**     |
| Son gönderme   | 2026-10-11 |
| İlk listelenme | 2026-10-06 |

🏷 `agent-framework` · `awesome-list` · `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/whyihaveyou--dsh-suite/e9daf3bb6313ff1b.png" width="100%" alt="whyihaveyou/dsh-suite screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/PolinniZhong/dsh-knit">PolinniZhong/dsh-knit</a></b> · ⭐53 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

AI Coding Agent'ları için göreve duyarlı çalışma alanı bağlamı alma ve yaşam döngüsü izleme: mevcut göreve en uygun belgeleri, kodu ve medyayı bulur, düzenler ve sürekli izler. Tamamen yerel, model çağrısı yok, ağ yok.  AI kodlama agent'ları için göreve duyarlı çalışma alanı bağlamı alma ve yaşam döngüsü izleme. Eldeki görevle en ilgili çalışma alanı bağlamını bulun, düzenleyin ve izleyin — yerel, deterministik, sıfır model çağrısı, sıfır ağ.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | JavaScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **53**     |
| Son gönderme   | 2026-10-11 |
| İlk listelenme | 2026-10-11 |

🏷 `agent-tools` · `ai-agent` · `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-better-sidebar`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/polinnizhong--dsh-knit/e98f690af54d1e8d.png" width="100%" alt="PolinniZhong/dsh-knit screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/polinnizhong--dsh-knit/338cb6ef3e90368c.gif" width="100%" alt="PolinniZhong/dsh-knit animation"><br><sub>animasyonlu kayıt</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/skyf0xx/hedgehog">skyf0xx/hedgehog</a></b> · ⭐44 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

HEDGEHOG codes Cleaner, Faster and with Fewer Tokens. Hedgehog's AI-driven development builds a task dependency graph from your spec-driven, BMAD-METHOD plan, so Claude Code, Cursor & Gemini CLI stay locked to it. A CLI-enforced state machine for agentic coding. Now builds DeepSeek DSH Plugins. DeepSeek Harness、DSH 插件、AI 编程、BMAD 方法. AI Copywriting

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | JavaScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **44**     |
| Son gönderme   | 2026-10-11 |
| İlk listelenme | 2026-10-11 |

🏷 `agent-skills` · `agentic-coding` · `ai-agents` · `ai-assisted-development` · `ai-coding` · `ai-copywriting` · `ai-engineering` · `ai-tools`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/skyf0xx--hedgehog/326d2d3a663269a4.jpg" width="100%" alt="skyf0xx/hedgehog screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/universe-st/dsh-game-material-master">universe-st/dsh-game-material-master</a></b> · ⭐42 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

dsh oyun varlıkları ustası eklentisi. seedream görüntü oluşturma modeli ve minimax video oluşturma modeline bağlanır; çeşitli oyun varlıkları oluşturabilir.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | JavaScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **42**     |
| Son gönderme   | 2026-10-11 |
| İlk listelenme | 2026-10-11 |

🏷 `chroma-key` · `cordis` · `deepseek-harness` · `dsh-plugin` · `ffmpeg` · `game-assets` · `image-generation` · `koishi`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/universe-st--dsh-game-material-master/9ce5badff3c3ac1c.png" width="100%" alt="universe-st/dsh-game-material-master screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/HOWILLMAKEIT/dsh-model-context-catalog">HOWILLMAKEIT/dsh-model-context-catalog</a></b> · ⭐34 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

DeepSeek Harness eklentisi: llm-pi-ai modelleri için doğru bağlam penceresini korur ve uzun oturumların yanlışlıkla bağlam taşması olarak değerlendirilmesini önler.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | JavaScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **34**     |
| Son gönderme   | 2026-10-11 |
| İlk listelenme | 2026-10-11 |

🏷 `context-window` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `javascript` · `llm` · `model-metadata`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/howillmakeit--dsh-model-context-catalog/6c743bbe3da63616.jpg" width="100%" alt="HOWILLMAKEIT/dsh-model-context-catalog screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/PensiveFei/deep-read-summarize">PensiveFei/deep-read-summarize</a></b> · ⭐31 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

Deep reading & summarization workflow for books/papers/videos/web — plugin parsers, MapReduce deep-read, JSON Schema output, Obsidian-ready (DSH)

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | JavaScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **31**     |
| Son gönderme   | 2026-10-11 |
| İlk listelenme | 2026-10-11 |

🏷 `ai-agent` · `content-summarization` · `deepseek` · `dsh-plugin` · `pipeline` · `workflow`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/pensivefei--deep-read-summarize/800b10f03f25fe11.png" width="100%" alt="PensiveFei/deep-read-summarize screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary><b>Bu kategoride daha fazlası</b> <sub>· 65</sub></summary>

- [hashgraph-online/awesome-ai-plugins](https://github.com/hashgraph-online/awesome-ai-plugins) - Claude Code, OpenAI Codex / ChatGPT, Gemini, Antigravity, Pi / Oh My Pi, Grok…
- [Dominic789654/awesome-deepseek-harness](https://github.com/Dominic789654/awesome-deepseek-harness) - A curated list of plugins, skills, MCP servers, patch/profile layers…
- [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) - DSH eklenti pazarı / DSH Plugin Marketplace: DeepSeek Harness Web GUI içinde…
- [FishBottle7/opencode2dsh](https://github.com/FishBottle7/opencode2dsh) - DSH plugin — free OpenCode Zen models for DeepSeek Harness (DSH).
- [arcships/rutis](https://github.com/arcships/rutis) - Kendi kendini yineleyen yazılımlar için bir eklenti çalışma zamanı — ajanların…
- [kejixiaoliang/awesome-dsh-plugins](https://github.com/kejixiaoliang/awesome-dsh-plugins) - DeepSeek Harness (DSH) eklentileri seçkisi — 14 kategoride 280.
- [Vncntvx/dsh-zotero](https://github.com/Vncntvx/dsh-zotero) - DeepSeek harness için Zotero araç seti;
- [KannaKuron/dsh-gitbash-shell](https://github.com/KannaKuron/dsh-gitbash-shell) - DSH eklentisi: Windows üzerindeki tüm aracı kipleri için Git Bash kabuğu.
- [ZhangFengshun/dsh-remote-ssh](https://github.com/ZhangFengshun/dsh-remote-ssh) - DSH web plugin: VSCode Remote-SSH-like remote development.
- [NekroAI/nekro-nxt](https://github.com/NekroAI/nekro-nxt) - NekroNXT: DeepSeek Harness (DSH) tabanlı çok platformlu grup sohbeti aracısı…
- [omdsh-dev/dsh-office](https://github.com/omdsh-dev/dsh-office) - Ofis üçlüsü! DeepSeek Harness (dsh) için Office belge araçları: elektronik…
- [wingsky-1/dsh-plugin-hub](https://github.com/wingsky-1/dsh-plugin-hub) - DSH (DeepSeek Harness) web GUI plugin collection — task notifications, provider…
- [dphmoblie/deepseek-harness-android](https://github.com/dphmoblie/deepseek-harness-android) - dsh Android sürümü: DeepSeek Harness, Ubuntu çalışma ortamı, eklentiler ve…
- [gjj-star/dsh-conversation-navigator](https://github.com/gjj-star/dsh-conversation-navigator) - DSH oturum gezintisi.
- [lizhiyao/oh-my-knowledge](https://github.com/lizhiyao/oh-my-knowledge) - OMK — Evidence-backed evaluation and observability for prompts, RAG, skills…
- [weishao2/tizhuang-agent-skills](https://github.com/weishao2/tizhuang-agent-skills) - 2000万+中小学K12真题题库 Skill：免费注册、免费抽题、教材/章节/知识点检索、练习测验与AI智能组卷.
- [HaoyueQin/dsh-usage-statistics-panel](https://github.com/HaoyueQin/dsh-usage-statistics-panel) - DSH web eklentisi: GitHub tarzı etkinlik ısı haritası, önbellek isabet oranı…
- [awesome-deepseekharness/awesome-deepseek-harness](https://github.com/awesome-deepseekharness/awesome-deepseek-harness) - Topluluk tarafından seçilmiş DeepSeek Harness (dsh) eklentileri, araçları…
- [hyqhyq3/dsh-mcp-manager](https://github.com/hyqhyq3/dsh-mcp-manager) - DeepSeek Harness için MCP sunucu yöneticisi eklentisi: Ayarlar → MCP sayfası…
- [Wenaixi/dsh-superpower](https://github.com/Wenaixi/dsh-superpower) - DeepSeek Harness eklentisi: 15 obra/superpowers mühendislik becerisi, iki dilli…
- [harrylabsj/kiwi](https://github.com/harrylabsj/kiwi) - A2A ticaret pazarlığı çalışma zamanı + DeepSeek Harness (dsh) eklentisi.
- [Imzl-zl/dsh-mcp-manager-ui](https://github.com/Imzl-zl/dsh-mcp-manager-ui) - DeepSeek Harness Web için MCP sunucu yönetim arayüzü — kayan panel, JSON içe…
- [liustack/pptwise](https://github.com/liustack/pptwise) - HTML değil, gerçek bir PowerPoint. Yapay zekânıza nelerin ele alınacağını…
- [mistnest/dsh-cuigengji-plugin](https://github.com/mistnest/dsh-cuigengji-plugin) - 催更姬：给大肥鱼一个小说工作台。写正文、理设定、画情节，和 AI 一起讨论、续写与改稿.
- [Y1X1n/dsh-prompt-optimizer](https://github.com/Y1X1n/dsh-prompt-optimizer) - DeepSeek Harness eklentisi · Gönderme çubuğunda istem taslağını tek tıklamayla…
- [TecFancy/dsh-auth-gate](https://github.com/TecFancy/dsh-auth-gate) - DeepSeek Harness (dsh) web arayüzü için oturum açma kapısı: parola veya…
- [AmethystLuna/embedded-workbench](https://github.com/AmethystLuna/embedded-workbench) - Gömülü C/C++ AI mühendislik eklentisi — ürün yazılımı becerileri.
- [Chael-Chael/dsh-reference-anything](https://github.com/Chael-Chael/dsh-reference-anything) - The best DeepSeek Harness plugin for referencing anything — enhanced @ menu for…
- [Sivan757/dsh-agent-plugins-market](https://github.com/Sivan757/dsh-agent-plugins-market) - DeepSeek Harness (DSH) için tek duraklı skills, subagent, MCP ve LSP yöneticisi…
- [dsh-plugin-lab/dsh-zhihu-search](https://github.com/dsh-plugin-lab/dsh-zhihu-search) - DSH 插件：基于知乎开放平台官方 API 创建的站内搜索、全网索引搜索与直答三个工具。搜索不幻觉，引用有出处。（原生嵌入“设置-插件-插件配置”）.
- [MicroMilo/upstream-radar](https://github.com/MicroMilo/upstream-radar) - DeepSeek Harness eklentileri için her zaman açık uyumluluk testi: kesin…
- [falling-ts/dsh-force-compact](https://github.com/falling-ts/dsh-force-compact) - Aggressive context compaction for local-first agents.
- [bonerush/dsh-obsidian-mem](https://github.com/bonerush/dsh-obsidian-mem) - Proje belgelerini ve uzun vadeli belleği özel bir Obsidian kasasında düz…
- [unStone/dsh-xray](https://github.com/unStone/dsh-xray) - DeepSeek Harness eklentileri için X ışını: beyan edilen yetenekler ve gerçek…
- [chnjames/dsh-plugin-market](https://github.com/chnjames/dsh-plugin-market) - DSH 插件市场 — DeepSeek Harness 设置内一键安装社区插件，并提供公开目录站（浏览 / 复制安装命令）.
- [cyanseek/dsh-landscape](https://github.com/cyanseek/dsh-landscape) - Agent-first DeepSeek Harness plugin intelligence: verify existing plugins…
- [dsh-plugin-lab/dsh-workbuddy-bridge](https://github.com/dsh-plugin-lab/dsh-workbuddy-bridge) - DSH 插件：把 WorkBuddy 桌面 App 里的模型接入 DeepSeek Harness，零配置直接用。（原生嵌入&quot;设置-插件-插件配置&quot;）.
- [lkhfrgc/scholar-llm-wiki](https://github.com/lkhfrgc/scholar-llm-wiki) - A knowledge base toolkit for research and literature review.
- [Mcd0LUO/dsh-guard-repeat-output](https://github.com/Mcd0LUO/dsh-guard-repeat-output) - Host-side degeneration guard for DSH: strips garbage code points, detects…
- [shenhuanageshei/dsh-team-link](https://github.com/shenhuanageshei/dsh-team-link) - Session deep links + full session export (markdown/JSON) + approved…
- [gulagala001/dsh-intelligent-ui](https://github.com/gulagala001/dsh-intelligent-ui) - DSH yanıtlarını kullanılabilir arayüzlere dönüştürün: hesap makineleri…
- [AmethystLuna/logicprobe](https://github.com/AmethystLuna/logicprobe) - Tasarım ve kod iddialarının doğrulanması: olgusal iddiaları kaynak kodla…
- [cherrchen/dsh-plugin-multi-root-workspace](https://github.com/cherrchen/dsh-plugin-multi-root-workspace) - Çok klasörlü çalışma alanı: DSH (DeepSeek Harness) aracısının yalnızca ana…
- [godv61/dsh-task-engine](https://github.com/godv61/dsh-task-engine) - DeepSeek Harness için mühendislik iş akışı eklentisi: görev aşamaları…
- [Kr-ATG/dsh-chat-plus](https://github.com/Kr-ATG/dsh-chat-plus) - DSH 对话体验增强套件（零源码改动，纯插件注入）。Seeker 双栏执行大盘：右栏任务 / 操作面板 / 子智能体 / 产出物四张卡 +…
- [PerryLink/dsh-plugin-doctor](https://github.com/PerryLink/dsh-plugin-doctor) - DeepSeek Harness (dsh) eklentileri için sıfır bağımlılıklı doğrulama standardı…
- [viztor/dsh-opencode-patch](https://github.com/viztor/dsh-opencode-patch) - DeepSeek Harness üzerinde OpenCode — OpenCode Zen + Go ücretsiz katman…
- [AI-Scarlett/DSH-Store](https://github.com/AI-Scarlett/DSH-Store) - DSH STORE — DeepSeek Harness için üçüncü taraf eklenti pazaryeri ve korumalı…
- [Atelyx/Atelyx](https://github.com/Atelyx/Atelyx) - Atelyx, insan odaklı ve genişletilebilir bir masaüstü çalışma alanıdır…
- [dsh-cc/dsh-cc](https://github.com/dsh-cc/dsh-cc) - DeepSeek Harness için her şey dahil bir kodlama agent.
- [dsh-plugin-lab/dsh-ds-balance](https://github.com/dsh-plugin-lab/dsh-ds-balance) - DSH plugin: shows your DeepSeek account balance at the bottom of the left…
- [fangwen9527/dsh-composer-ux](https://github.com/fangwen9527/dsh-composer-ux) - DSH Web giriş deneyimi eklentisi: gönderme/yeni satır tuşu geçişi, sağ tık…
- [Mzy123l/dsh-plugin-remote-access](https://github.com/Mzy123l/dsh-plugin-remote-access) - DeepSeek Harness masaüstü sürümü için 「sınırlı ağ segmenti + isteğe bağlı…
- [sakanamaru/dsh-minato](https://github.com/sakanamaru/dsh-minato) - dsh-minato — DeepSeek Harness (dsh) için topluluk sürümü yerel dağıtım ve…
- [tianyagk/dsh-tradewatcher](https://github.com/tianyagk/dsh-tradewatcher) - DeepSeek Harness (DSH) web eklentisi: market-dashboard kenar çubuğu sekmesi…
- [xingzhen199186/dsh-mini-remote](https://github.com/xingzhen199186/dsh-mini-remote) - DSH 极简风远程移动端，提供「单帧」、「聊天」和「完整」三种模式，将注意力支配权交还给用户.
- [argszero/cordis-plugin-empty-response-retry](https://github.com/argszero/cordis-plugin-empty-response-retry) - Bir atıf içermeyen boş model denemesini yeniden denenebilir hâle getirir;
- [eovidiu/cordis-ios](https://github.com/eovidiu/cordis-ios) - Kendi temizliklerini yapan eklentiler: iOS ve macOS için cordis eklenti…
- [Magica-Chen/dsh-preset-codex-claude](https://github.com/Magica-Chen/dsh-preset-codex-claude) - DeepSeek Harness ajan ön ayarı: Codex ve Claude Code, her biri salt okunur ve…
- [validation-engineering/cordis-verus](https://github.com/validation-engineering/cordis-verus) - Verus tarafından doğrulanmış bir lifecycle kernel ve Cordis compatibility…
- [YOU-SHOULD-KNOW-ME/antigrative-dashboard](https://github.com/YOU-SHOULD-KNOW-ME/antigrative-dashboard) - Inline Antigravity dashboard: tok/s, DSH-style cache hit rate, five-hour and…
- [Jecvay/paseo-dsh-direct](https://github.com/Jecvay/paseo-dsh-direct) - DeepSeek Harness 的 Paseo Provider Plugin (Direct Provider).
- [tellmewhattodo/dsh-serenity-plugin](https://github.com/tellmewhattodo/dsh-serenity-plugin) - dsh-serenity-plugin.
- [HaydenSmith1121/dsh-plugins](https://github.com/HaydenSmith1121/dsh-plugins) - DeepSeek Harness (dsh) 插件市场 —— 目录（一个插件一个配置文件）+ 可视化面板 + 一键安装；插件本体在…
- [SCP-008-1/dshop](https://github.com/SCP-008-1/dshop) - dsh 插件商城 - 基于 GitHub topic:dsh-plugin 自动发现与每小时定时同步.

</details>

<a id="writing"></a>

## Yazılar, tartışmalar ve videolar

Mod yeteneği hakkında yazılar, tartışmalar ve videolar.

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925102">Claude Code Mods</a></b> · ⭐6 · 👁️ observed · 9 天</summary>

##### 📝 Özet

Kaynak projede herhangi bir açıklama yayımlanmadı.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Yazılar, tartışmalar ve videolar`                                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| İlk listelenme | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50003222">What the Hell Are Claude Mods? [video]</a></b> · ⭐4 · 👁️ observed · 3 天</summary>

##### 📝 Özet

Kaynak projede herhangi bir açıklama yayımlanmadı.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Yazılar, tartışmalar ve videolar`                                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| İlk listelenme | 2026-10-09 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49999983">A Claude Code mod plays MIDI music when it works</a></b> · ⭐3 · 👁️ observed · 3 天</summary>

##### 📝 Özet

Kaynak projede herhangi bir açıklama yayımlanmadı.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Yazılar, tartışmalar ve videolar`                                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| İlk listelenme | 2026-10-08 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925800">Claude Code Mods: plugins may now modify deeper behavior</a></b> · ⭐3 · 👁️ observed · 9 天</summary>

##### 📝 Özet

Kaynak projede herhangi bir açıklama yayımlanmadı.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Yazılar, tartışmalar ve videolar`                                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| İlk listelenme | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49926243">Getting started with Claude Code mods</a></b> · ⭐3 · 👁️ observed · 9 天</summary>

##### 📝 Özet

Kaynak projede herhangi bir açıklama yayımlanmadı.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Yazılar, tartışmalar ve videolar`                                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| İlk listelenme | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49945600">Show HN: Terminal Gym – a Claude mod that makes you do pushups between prompts</a></b> · ⭐3 · 👁️ observed · 7 天</summary>

##### 📝 Özet

Merhaba HN, bunu kendim için geliştirdim ve açık kaynak hâline getirmek istedim. Sorun şuydu: Özellikle artık genellikle bu kadar çok ajanı paralel işlediğimiz için terminalde uzun saatler geçirdiğimden, istemlerin arasında hatırlatıcılar almanın bir yolunu istiyordum. İlk sürüm basit bir rep

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Yazılar, tartışmalar ve videolar`                                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| İlk listelenme | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49971594">Terminal Steps: A Claude mod for a daily step goal, synced from Apple Health</a></b> · ⭐3 · 👁️ observed · 5 天</summary>

##### 📝 Özet

Kaynak projede herhangi bir açıklama yayımlanmadı.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Yazılar, tartışmalar ve videolar`                                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| İlk listelenme | 2026-10-06 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50024345">Agent-config&amp;Claude Code mods</a></b> · ⭐2 · 👁️ observed · 1 天</summary>

##### 📝 Özet

Kaynak projede herhangi bir açıklama yayımlanmadı.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Yazılar, tartışmalar ve videolar`                                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| İlk listelenme | 2026-10-10 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49940121">Getting started with Claude Code mods</a></b> · ⭐2 · 👁️ observed · 8 天</summary>

##### 📝 Özet

Kaynak projede herhangi bir açıklama yayımlanmadı.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Yazılar, tartışmalar ve videolar`                                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| İlk listelenme | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49927599">Pi-autoresearch ported to Claude Code 1:1 using the new mods API</a></b> · ⭐2 · 👁️ observed · 9 天</summary>

##### 📝 Özet

Kaynak projede herhangi bir açıklama yayımlanmadı.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Yazılar, tartışmalar ve videolar`                                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| İlk listelenme | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49934165">Show HN: What&#x27;s Agent Doing – a Claude Code UI mod that explains each step</a></b> · ⭐2 · 👁️ observed · 8 天</summary>

##### 📝 Özet

Bunu, en yeni kodlama modelleriyle Claude belirsiz komutlarla derin çalışma moduna geçtiği ve artık ne yaptığını hiç anlayamadığım için geliştirdim. Bu, istemin üzerine tek bir satır çizen bir moddur (Claude Code'un yeni function hooks özelliğini kullanan bir eklenti): - mevcut adım,

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Yazılar, tartışmalar ve videolar`                                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| İlk listelenme | 2026-10-05 |

</details>

<a id="projects-by-implementation-language"></a>

## Uygulama diline göre projeler

Ekosistem Python ve TypeScript üzerinde yoğunlaşıyor, ancak tür denetimli istemciler başka dillerde de ortaya çıkmaya devam ediyor. Bu tablo, girdilerin kendilerinden oluşturulur.

| Dil        | Kayıtlar | Örnekler                                                                                                           |
| ---------- | -------- | ------------------------------------------------------------------------------------------------------------------ |
| TypeScript | 322      | `anthropics/claude-code`, `anthropics/claude-code-action`, `karanb192/cache-tax`                                   |
| JavaScript | 69       | `karanb192/awesome-claude-code-mods`, `karanb192/claude-code-mods`, `augiefra/claude-mods`                         |
| Python     | 32       | `anthropics/claude-agent-sdk-python`, `anthropics/claude-code-security-review`, `alexgreensh/token-optimizer`      |
| Shell      | 19       | `anthropics/claude-agent-sdk-typescript`, `andrewbakercloudscale/claude-code-cost-sidebar`, `Gharib89/claude-mods` |
| HTML       | 12       | `awss1i/assay`, `omarcevi/claudemods`, `testy-cool/awesome-claude-code-mods`                                       |
| Go         | 6        | `backstabslash/goccc`, `kylesnowschwartz/tail-claude-hud`, `livlign/ccbit`                                         |
| Rust       | 5        | `persiyanov/herdr-reviewr`, `JairoTorregrosa/claude-statusline`, `OpenClawFarm/claude-statusline`                  |
| PowerShell | 2        | `GoSlowPoke168/claude-statusline`, `rainyfei/claude-statusline-win`                                                |
| C#         | 1        | `sakanamaru/dsh-minato`                                                                                            |
| Kotlin     | 1        | `dphmoblie/deepseek-harness-android`                                                                               |
| MDX        | 1        | `jkf87/mod-guide`                                                                                                  |
| Swift      | 1        | `eovidiu/cordis-ios`                                                                                               |

<sub>Yalnızca dil belirten girdiler sayılır. Belgeler ve tartışma girdileri bu tablonun dışında tutulur.</sub>

## Katkıda bulunma

Düzeltmeler memnuniyetle karşılanır ve bu listeyi iyileştirmenin en hızlı yoludur. Bir girdi yanlış sınıflandırılmış veya yanlış derecelendirilmişse ya da bir proje ad çakışması nedeniyle yanlışlıkla dışlanmışsa bir issue veya pull request açın — otomatik filtrelerin en çok yanılma ihtimali olan kategori sonuncusudur.

---

<sub>Independent community project. Not affiliated with, endorsed by, or reviewed by Anthropic. Claude Code, Claude and Anthropic are trademarks of Anthropic. Product behaviour changes without notice; verify anything load-bearing against the official documentation. Assets remain the property of their upstream projects and are reproduced only where a licence permits.</sub>

<sub>Son güncelleme · 2026-10-11T21:12:49+08:00</sub>
