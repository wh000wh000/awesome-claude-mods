<p align="center">
  <img src="../assets/readme/hero.png" width="100%" alt="Harika Claude Modları">
</p>

<h1 align="center">Harika Claude Modları</h1>

<p align="center"><b>Claude Code modlarının ve değiştirdikleri daha derin davranışların kanıt derecelendirmeli dizini.</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-583-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="../LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
  <a href="https://wh000wh000.github.io/awesome-claude-mods/"><img src="https://img.shields.io/badge/site-searchable-1f6feb" alt="site"></a>
</p>

<p align="center"><sub><a href="../README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.pt-BR.md">Português</a> · <a href="README.ru.md">Русский</a> · <a href="README.it.md">Italiano</a> · <a href="README.ar.md">العربية</a> · <a href="README.hi.md">हिन्दी</a> · <b>Türkçe</b> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.pl.md">Polski</a> · <a href="README.nl.md">Nederlands</a> · <a href="README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **Güncel dizin** · Son senkronizasyon: `2026-10-12T08:14:15+08:00` (UTC+8)
> · Kayıtlar: **583** · Son güncellemede eklenenler: **0** · Uygulama dilleri: **13**

<sub>Aşağıdaki her kayıt otomatik olarak toplandı, filtrelendi ve yeniden kontrol edildi. Burada ücretli yerleştirme yoktur.</sub>

<a id="featured"></a>

## Anın seçkileri

<sub>Her kategoriden bir giriş; kanıt derecesine ve yıldızlara göre sıralanır, her güncellemede yeniden hesaplanır. Bu bir sıralamadır, onay değildir; her seçki aşağıdaki tam kartına bağlantı verir. Ekran görüntüsü veya kayıt yayınlayan projeler tercih edilir, böylece şerit görsel kalır.</sub>

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
<sub>⭐2537 · Python · 👁️ observed</sub>
<sub>Hayalet belirteçleri bul. Onları düzelt. Sıkıştırmadan sağ çık. Bağlam kalitesinin bozulmasını önle.</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo">
<b>🧵 <a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b>
<sub>⭐74360 · TypeScript · 👁️ observed</sub>
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
- [Resmî: Anthropic'ın kendi depoları ve sürüm notları](#resmî-anthropicın-kendi-depoları-ve-sürüm-notları) — **14**
- [Modlar: mod yeteneği kullanılarak oluşturulanlar](#modlar-mod-yeteneği-kullanılarak-oluşturulanlar) — **452**
- [DSH ve Cordis eklenti ekosistemleri](#dsh-ve-cordis-eklenti-ekosistemleri) — **106**
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
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></b> · ⭐150230 · TypeScript · ✅ official · 0 天</summary>

##### 📝 Özet

Claude Code terminalinizde çalışan, kod tabanınızı anlayan ve rutin görevleri yerine getirerek, karmaşık kodu açıklayarak ve git iş akışlarını doğal dil komutlarıyla yöneterek daha hızlı kod yazmanıza yardımcı olan aracı bir kodlama aracıdır.

<sub>🔧 Kodda kullanıldığı bulundu: `feed.xml`, `mods/diff/README.md`</sub>

##### 📌 Temel bilgiler

| Alan     | Değer                                                      |
| -------- | ---------------------------------------------------------- |
| Kategori | `Resmî: Anthropic&#x27;ın kendi depoları ve sürüm notları` |
| Kanıt    | `doğrudan Anthropic tarafından yayımlandı`                 |
| Dil      | TypeScript                                                 |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **150230** |
| Son gönderme   | 2026-10-11 |
| İlk listelenme | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b> · ⭐9479 · TypeScript · ✅ official · 2 天</summary>

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
| Yıldızlar      | **9479**   |
| Son gönderme   | 2026-10-09 |
| İlk listelenme | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-python">anthropics/claude-agent-sdk-python</a></b> · ⭐8249 · Python · ✅ official · 2 天</summary>

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
| Yıldızlar      | **8249**   |
| Son gönderme   | 2026-10-09 |
| İlk listelenme | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-security-review">anthropics/claude-code-security-review</a></b> · ⭐6346 · Python · ✅ official · 242 天</summary>

##### 📝 Özet

Güvenlik açıklarını analiz etmek için Claude kullanan yapay zekâ destekli bir güvenlik inceleme GitHub Action'ı.

##### 📌 Temel bilgiler

| Alan     | Değer                                                      |
| -------- | ---------------------------------------------------------- |
| Kategori | `Resmî: Anthropic&#x27;ın kendi depoları ve sürüm notları` |
| Kanıt    | `doğrudan Anthropic tarafından yayımlandı`                 |
| Dil      | Python                                                     |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **6346**   |
| Son gönderme   | 2026-02-11 |
| İlk listelenme | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-typescript">anthropics/claude-agent-sdk-typescript</a></b> · ⭐1798 · Shell · ✅ official · 2 天</summary>

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
| Yıldızlar      | **1798**   |
| Son gönderme   | 2026-10-09 |
| İlk listelenme | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/model-cards">anthropics/model-cards</a></b> · ⭐25 · ✅ official · 310 天</summary>

##### 📝 Özet

Claude Model Cards için yardımcı materyaller

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
<summary><b>Bu kategoride daha fazlası</b> <sub>· 2</sub></summary>

- [Claude Code 2.1.295 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Modlar için `$.ui.notify` eklendi: kendi bildirim ayarınız üzerinden yerel bir…
- [Claude Code 2.1.296 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - `UserPromptSubmit` hook&#x27;u veya modun `prompt.submit` hook&#x27;u sırasında Esc ya da…

</details>

<a id="mods"></a>

## Modlar: mod yeteneği kullanılarak oluşturulanlar

Buradaki her giriş, Claude Code'un 2.1.287 sürümünde kazandığı yeteneğin kullanıldığına dair kanıt gösterir: `ui.render` üzerinden çizim yapar, bir bölmeye, banda veya karta sahip olur, `$.ui.selection()` okur, `agent.spawn` ile ekip arkadaşları oluşturur ya da açıkça mod olduğunu belirtir.

<details>
<summary>🧩 <b><a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b> · ⭐2537 · Python · 👁️ observed · 0 天</summary>

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
| Yıldızlar      | **2537**   |
| Son gönderme   | 2026-10-11 |
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
<summary>🧩 <b><a href="https://github.com/karanb192/awesome-claude-code-mods">karanb192/awesome-claude-code-mods</a></b> · ⭐498 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Özet

GitHub üzerinden taranan, her modun ağ üzerinden okuyabileceği, yazabileceği, çalıştırabileceği veya gönderebileceği şeylerle birlikte herkese açık Claude Code modlarının (işlev hooks'ları) topluluk kataloğu. https://mods.aidojo.si/'a göz atın

<sub>🔧 Kodda kullanıldığı bulundu: `data/seeds.txt`, `README.md`, `data/repos.txt`, `finder/README.md`</sub>

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Modlar: mod yeteneği kullanılarak oluşturulanlar`                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |
| Dil      | JavaScript                                                               |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **498**    |
| Son gönderme   | 2026-10-11 |
| İlk listelenme | 2026-10-04 |

🏷 `anthropic` · `awesome` · `awesome-list` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hamzafer/claude-code-mods">hamzafer/claude-code-mods</a></b> · ⭐191 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Özet

Claude Code modları: istemin üstüne canlı satırlar, korumalar, bölmeler ve oyunlar ekleyen kancalar üzerine kurulmuş eklentiler. Bağlam çubuğu, kullanım ölçer, Codex inceleme takibi, Markdown önizlemesi, Spotify'da şu anda çalan ve daha fazlası.

<sub>🔧 Kodda kullanıldığı bulundu: `mods/next-steps/hooks/register.tsx`, `mods/agent-radar/hooks/register.tsx`, `mods/review-watch/hooks/register.tsx`</sub>

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Modlar: mod yeteneği kullanılarak oluşturulanlar`                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |
| Dil      | TypeScript                                                               |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **191**    |
| Son gönderme   | 2026-10-11 |
| İlk listelenme | 2026-10-11 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugins` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/c683a5d95e78d920.png" width="100%" alt="hamzafer/claude-code-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/0b4dc7c7692bd024.gif" width="100%" alt="hamzafer/claude-code-mods animation"><br><sub>animasyonlu kayıt</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/cache-tax">karanb192/cache-tax</a></b> · ⭐144 · TypeScript · 👁️ observed · 7 天</summary>

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
| Yıldızlar      | **144**    |
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
<summary>🧩 <b><a href="https://github.com/HeyCubit/effortless">HeyCubit/effortless</a></b> · ⭐127 · HTML · 👁️ observed · 0 天</summary>

##### 📝 Özet

Claude Code mod: picks the reasoning effort for every prompt, shows the prompt cache and context, and hands off or compacts in one click

<sub>🔧 Kodda kullanıldığı bulundu: `docs/agent-panel/PLAN.md`, `hooks/register.tsx`</sub>

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Modlar: mod yeteneği kullanılarak oluşturulanlar`                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |
| Dil      | HTML                                                                     |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **127**    |
| Son gönderme   | 2026-10-11 |
| İlk listelenme | 2026-10-12 |

🏷 `ai-tools` · `anthropic` · `claude` · `claude-code` · `claude-code-plugin` · `developer-tools` · `prompt-caching`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/heycubit--effortless/ad0a6472f7a34cd7.png" width="100%" alt="HeyCubit/effortless screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/heycubit--effortless/fcef2f9593961020.gif" width="100%" alt="HeyCubit/effortless animation"><br><sub>animasyonlu kayıt</sub></td>
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
| Son gönderme   | 2026-10-11 |
| İlk listelenme | 2026-10-10 |

🏷 `agentic-ai` · `ai-agents` · `browser-automation` · `claude-code` · `claude-code-mod` · `cli` · `code-generation` · `developer-tools`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hellosverre/claude-skins">hellosverre/claude-skins</a></b> · ⭐99 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Özet

Claude Code için kaplamalar: simgeli araç satırları, fark, tablo ve Mermaid grafik kartları, kullanım bandı ve on beş tema. /skin bunları anında değiştirir.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Modlar: mod yeteneği kullanılarak oluşturulanlar`                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |
| Dil      | TypeScript                                                               |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **99**     |
| Son gönderme   | 2026-10-11 |
| İlk listelenme | 2026-10-12 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hellosverre--claude-skins/e70c992c52ca2e70.gif" width="100%" alt="hellosverre/claude-skins animation"><br><sub>animasyonlu kayıt</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/iamumeransari/claude-show-your-work">iamumeransari/claude-show-your-work</a></b> · ⭐98 · TypeScript · 👁️ observed · 0 天</summary>

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
| Yıldızlar      | **98**     |
| Son gönderme   | 2026-10-11 |
| İlk listelenme | 2026-10-11 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/iamumeransari--claude-show-your-work/7a0af2143a7dfd15.jpg" width="100%" alt="iamumeransari/claude-show-your-work screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NahumLitvin/prismantis">NahumLitvin/prismantis</a></b> · ⭐78 · TypeScript · 👁️ observed · 0 天</summary>

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
| Yıldızlar      | **78**     |
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
<summary>🧩 <b><a href="https://github.com/Tickloop/claude-mods">Tickloop/claude-mods</a></b> · ⭐78 · TypeScript · 👁️ observed · 3 天</summary>

##### 📝 Özet

Bir claude code modları koleksiyonu

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Modlar: mod yeteneği kullanılarak oluşturulanlar`                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |
| Dil      | TypeScript                                                               |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **78**     |
| Son gönderme   | 2026-10-08 |
| İlk listelenme | 2026-10-11 |

</details>

<details>
<summary>🧩 <b><a href="https://github.com/scasella/claude-flightdeck">scasella/claude-flightdeck</a></b> · ⭐68 · TypeScript · 👁️ observed · 9 天</summary>

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
| Yıldızlar      | **68**     |
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
<summary>🧩 <b><a href="https://github.com/darrell-tw/darrelltw-mods">darrell-tw/darrelltw-mods</a></b> · ⭐65 · HTML · 👁️ observed · 6 天</summary>

##### 📝 Özet

Darrell Wang tarafından hazırlanan Claude Code modları — istemin üstünde bantlar, sıfır model token'ı. Tayvan／ABD hisse senedi panosu + devamı gelecek.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Modlar: mod yeteneği kullanılarak oluşturulanlar`                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |
| Dil      | HTML                                                                     |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **65**     |
| Son gönderme   | 2026-10-05 |
| İlk listelenme | 2026-10-11 |

</details>

<details>
<summary>🧩 <b><a href="https://github.com/zycck/claude-mods">zycck/claude-mods</a></b> · ⭐46 · TypeScript · 👁️ observed · 3 天</summary>

##### 📝 Özet

Claude Code modları: istemin üstünde canlı plan ilerleme çubukları

<sub>🔧 Kodda kullanıldığı bulundu: `README.md`</sub>

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Modlar: mod yeteneği kullanılarak oluşturulanlar`                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |
| Dil      | TypeScript                                                               |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **46**     |
| Son gönderme   | 2026-10-08 |
| İlk listelenme | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/49f09d1600b02c7a.gif" width="100%" alt="zycck/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/25f4230871cb30f6.gif" width="100%" alt="zycck/claude-mods animation"><br><sub>animasyonlu kayıt · <a href="https://raw.githubusercontent.com/zycck/claude-mods/main/media/plan-progress.mp4">Videoyu aç</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/henrik-thevibe/Claude-Fables">henrik-thevibe/Claude-Fables</a></b> · ⭐32 · TypeScript · 👁️ observed · 9 天</summary>

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
<summary>🧩 <b><a href="https://github.com/dgokcin/claude-pokemon-mod">dgokcin/claude-pokemon-mod</a></b> · ⭐25 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Özet

Claude Code'da istemin üzerinde yaşayan pikselli bir Pokémon

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Modlar: mod yeteneği kullanılarak oluşturulanlar`                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |
| Dil      | JavaScript                                                               |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **25**     |
| Son gönderme   | 2026-10-11 |
| İlk listelenme | 2026-10-11 |

🏷 `claude-code-mod` · `claude-code-mods`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/dgokcin/claude-pokemon-mod/main/gifs/pikachu-haiku.gif" width="100%" alt="dgokcin/claude-pokemon-mod screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/dgokcin/claude-pokemon-mod/main/gifs/pikachu-haiku.gif" width="100%" alt="dgokcin/claude-pokemon-mod animation"><br><sub>animasyonlu kayıt</sub></td>
</tr></table>

<sub>Yeniden dağıtıma izin veren bir lisans belirtilmediği için varlığa upstream deposundan doğrudan bağlantı veriliyor.</sub>

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
<summary>🧩 <b><a href="https://github.com/artemnovichkov/xcode-mods">artemnovichkov/xcode-mods</a></b> · ⭐20 · TypeScript · 👁️ observed · 9 天</summary>

##### 📝 Özet

Xcode'un derleme, testler, konsol ve SwiftUI önizlemeleri Claude Code içinde

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Modlar: mod yeteneği kullanılarak oluşturulanlar`                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |
| Dil      | TypeScript                                                               |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **20**     |
| Son gönderme   | 2026-10-02 |
| İlk listelenme | 2026-10-11 |

🏷 `claude-code` · `claude-code-mods` · `claude-code-plugin` · `ghostty` · `ios` · `mcp` · `swift` · `swiftui`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/artemnovichkov--xcode-mods/bc34e8dd0f730ea2.png" width="100%" alt="artemnovichkov/xcode-mods screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/lemomo-ai/lemo-mod">lemomo-ai/lemo-mod</a></b> · ⭐20 · TypeScript · 👁️ observed · 7 天</summary>

##### 📝 Özet

Claude Code modları: terminal ve masaüstü uygulaması için ihtiyacınız olduğunda etkinleştirebileceğiniz 21 stil ve eksiksiz özellik seti. · Claude için tek tıklamayla yeni bir stil uygulayın ve isteğe bağlı olarak etkinleştirilebilen eksiksiz bir özellik setine erişin.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Modlar: mod yeteneği kullanılarak oluşturulanlar`                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |
| Dil      | TypeScript                                                               |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **20**     |
| Son gönderme   | 2026-10-04 |
| İlk listelenme | 2026-10-11 |

🏷 `claude` · `claude-code` · `claude-code-mods` · `claude-code-plugins` · `developer-tools` · `mods` · `pixel-art` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/lemomo-ai--lemo-mod/d6e9ce6141976f64.png" width="100%" alt="lemomo-ai/lemo-mod screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-starter-kit">promptadvisers/claude-mods-starter-kit</a></b> · ⭐20 · JavaScript · 👁️ observed · 9 天</summary>

##### 📝 Özet

On Claude Code modu, başlangıç kılavuzları, oluşturma istemleri, güvenli demolar ve kendiniz oluşturabileceğiniz bir şablon.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Modlar: mod yeteneği kullanılarak oluşturulanlar`                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |
| Dil      | JavaScript                                                               |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **20**     |
| Son gönderme   | 2026-10-02 |
| İlk listelenme | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/promptadvisers/claude-mods-starter-kit/main/assets/cover.jpg" width="100%" alt="promptadvisers/claude-mods-starter-kit screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

<sub>Yeniden dağıtıma izin veren bir lisans belirtilmediği için varlığa upstream deposundan doğrudan bağlantı veriliyor.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/SavaSoftworks/BitFrost">SavaSoftworks/BitFrost</a></b> · ⭐16 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Özet

Codex, GLM ve diğer kodlama ajanlarını Claude Code alt ajanları olarak kullanın.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Modlar: mod yeteneği kullanılarak oluşturulanlar`                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |
| Dil      | TypeScript                                                               |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **16**     |
| Son gönderme   | 2026-10-12 |
| İlk listelenme | 2026-10-12 |

🏷 `agent-orchestration` · `ai-agents` · `claude-code` · `claude-code-mods` · `claude-code-plugin` · `codex` · `developer-tools` · `glm`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/savasoftworks--bitfrost/247eb6d28062ba3b.png" width="100%" alt="SavaSoftworks/BitFrost screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/JetsonChan/CC-Usage-Band">JetsonChan/CC-Usage-Band</a></b> · ⭐13 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Özet

Claude Code modları: usage-band, 5 saatlik/7 günlük limitlerinizi, bağlam penceresini ve önbellek isabet oranını istemin üzerinde gösterir

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Modlar: mod yeteneği kullanılarak oluşturulanlar`                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |
| Dil      | TypeScript                                                               |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **13**     |
| Son gönderme   | 2026-10-03 |
| İlk listelenme | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/jetsonchan--cc-usage-band/e9d74f1543fa7c25.png" width="100%" alt="JetsonChan/CC-Usage-Band screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/paulbkim-dev/claude-code-cache-warmer">paulbkim-dev/claude-code-cache-warmer</a></b> · ⭐13 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Özet

İstem önbelleğini sıcak tutan ve her yenilemenin maliyetini ve tasarrufunu gösteren Claude Code modu

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Modlar: mod yeteneği kullanılarak oluşturulanlar`                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |
| Dil      | TypeScript                                                               |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **13**     |
| Son gönderme   | 2026-10-11 |
| İlk listelenme | 2026-10-12 |

🏷 `claude-code` · `claude-code-plugin` · `prompt-caching`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/paulbkim-dev--claude-code-cache-warmer/5d291d279a3967a1.gif" width="100%" alt="paulbkim-dev/claude-code-cache-warmer screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/paulbkim-dev--claude-code-cache-warmer/5d291d279a3967a1.gif" width="100%" alt="paulbkim-dev/claude-code-cache-warmer animation"><br><sub>animasyonlu kayıt</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-computer-use-threads">promptadvisers/claude-mods-computer-use-threads</a></b> · ⭐12 · JavaScript · 👁️ observed · 6 天</summary>

##### 📝 Özet

İki Claude Code modu: Codex computer-use bridge ve koordineli Claude oturumları. Kaynak kodu, derleme istemleri, kurulum ve testler.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Modlar: mod yeteneği kullanılarak oluşturulanlar`                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |
| Dil      | JavaScript                                                               |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **12**     |
| Son gönderme   | 2026-10-05 |
| İlk listelenme | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/promptadvisers--claude-mods-computer-use-threads/c08dc292e500cd09.png" width="100%" alt="promptadvisers/claude-mods-computer-use-threads screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/aieo-product/claude_qamods">aieo-product/claude_qamods</a></b> · ⭐11 · TypeScript · 👁️ observed · 4 天</summary>

##### 📝 Özet

Claude Code modları, Claude sorularını okumayı ve yanıtlamayı kolaylaştırır (qa-guide).

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Modlar: mod yeteneği kullanılarak oluşturulanlar`                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |
| Dil      | TypeScript                                                               |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **11**     |
| Son gönderme   | 2026-10-07 |
| İlk listelenme | 2026-10-11 |

🏷 `askuserquestion` · `claude-code` · `claude-code-plugin` · `mod`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aieo-product--claude_qamods/e57e7bee7cb5c173.png" width="100%" alt="aieo-product/claude_qamods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aieo-product--claude_qamods/eb4a2b15bdb5ff3e.gif" width="100%" alt="aieo-product/claude_qamods animation"><br><sub>animasyonlu kayıt · <a href="https://raw.githubusercontent.com/aieo-product/claude_qamods/main/docs/media/qa-guide-pv-16x9.mp4">Videoyu aç</a></sub></td>
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
<summary>🧩 <b><a href="https://github.com/OneWave-AI/claude-code-mods">OneWave-AI/claude-code-mods</a></b> · ⭐11 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Özet

Claude Code için on açık kaynaklı mod: canlı bölmeler, bantlar, durum satırları ve araç çağrısı korumaları. Tüketim ölçeri, launch codes, session wrapped, boss fight, code pet ve daha fazlası.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Modlar: mod yeteneği kullanılarak oluşturulanlar`                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |
| Dil      | TypeScript                                                               |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **11**     |
| Son gönderme   | 2026-10-03 |
| İlk listelenme | 2026-10-11 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mods` · `claude-code-plugins`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/onewave-ai--claude-code-mods/763e0352f43b1cbc.png" width="100%" alt="OneWave-AI/claude-code-mods screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
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
<summary>🧩 <b><a href="https://github.com/Arunjay4213/claude-mods">Arunjay4213/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 26 天</summary>

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
| Yıldızlar      | **9**      |
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
<summary>🧩 <b><a href="https://github.com/deepsteve/deepsteve">deepsteve/deepsteve</a></b> · ⭐9 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Özet

Ajanlarınızın oluşturduğu Claude Code ve Codex terminalleriniz için bir kullanıcı arayüzü; böylece zihninizdeki tek model sizinki olur.

<sub>🔧 Kodda kullanıldığı bulundu: `CLAUDE.md`</sub>

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Modlar: mod yeteneği kullanılarak oluşturulanlar`                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |
| Dil      | JavaScript                                                               |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **9**      |
| Son gönderme   | 2026-10-11 |
| İlk listelenme | 2026-10-11 |

🏷 `ai-coding` · `ai-tools` · `browser-terminal` · `claude-code` · `codex` · `coding-agent` · `developer-tools` · `devtools`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/deepsteve--deepsteve/adee5ea71e2e3289.png" width="100%" alt="deepsteve/deepsteve screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/ersinkoc/claude-mods">ersinkoc/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 1 天</summary>

##### 📝 Özet

KOZMOS — Claude Code için (CLI + masaüstü) canlı, görsel modlar: istemin üstünde bantlar, kenar çubukları, durum akışı, yardımcılar, korumalar ve ses.

<sub>🔧 Kodda kullanıldığı bulundu: `mods/compass/README.md`, `mods/blackbox/README.md`, `mods/orrery/README.md`</sub>

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Modlar: mod yeteneği kullanılarak oluşturulanlar`                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |
| Dil      | TypeScript                                                               |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **9**      |
| Son gönderme   | 2026-10-10 |
| İlk listelenme | 2026-10-11 |

🏷 `anthropic` · `claude-code` · `claude-code-mods` · `claude-code-plugin` · `tui`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ersinkoc--claude-mods/ece950c6b8ad049e.png" width="100%" alt="ersinkoc/claude-mods screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/az9713/claude-mod-pack">az9713/claude-mod-pack</a></b> · ⭐8 · TypeScript · 👁️ observed · 7 天</summary>

##### 📝 Özet

Tek eklentide altı Claude Code modu (Token Weather, Cache Keeper, Wait What, Prompt Queue, Snake, Blast Radius); mod başına anahtarlar ve modlar-kancalar raporuyla birlikte.

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
| Son gönderme   | 2026-10-04 |
| İlk listelenme | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/az9713--claude-mod-pack/7889282e792ed11e.png" width="100%" alt="az9713/claude-mod-pack screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/devbrother2024/devbrothers-mods">devbrother2024/devbrothers-mods</a></b> · ⭐7 · TypeScript · 👁️ observed · 7 天</summary>

##### 📝 Özet

개발동생'in Claude Code modları koleksiyonu. Taksi paketi: taksimetre, navigasyon, hız kamerası, araç kamerası

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
| Son gönderme   | 2026-10-04 |
| İlk listelenme | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/devbrother2024--devbrothers-mods/10df726087fd2881.webp" width="100%" alt="devbrother2024/devbrothers-mods screenshot"></td>
<td align="center" valign="top"><a href="https://www.youtube.com/@%EA%B0%9C%EB%B0%9C%EB%8F%99%EC%83%9D"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/devbrother2024--devbrothers-mods/10df726087fd2881.webp" width="100%" alt="video"></a><br><sub><a href="https://www.youtube.com/@%EA%B0%9C%EB%B0%9C%EB%8F%99%EC%83%9D">Şurada izle: youtube.com</a> · oynatma barındırıcı sitede açılır; GitHub bunu satır içinde gömemez</sub></td>
</tr></table>

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
<summary><b>Bu kategoride daha fazlası</b> <sub>· 418</sub></summary>

- [0xDarkMatter/claude-mods](https://github.com/0xDarkMatter/claude-mods) - Claude Code için uzman Skills.
- [whyashthakker/awesome-claude-code-mods](https://github.com/whyashthakker/awesome-claude-code-mods) - Claude Code ile kullanabileceğiniz 100.
- [karanb192/claude-code-mods](https://github.com/karanb192/claude-code-mods) - Claude Mod.
- [ucsandman/claude-harness](https://github.com/ucsandman/claude-harness) - Her gün çalıştırdığım Claude Code harness.
- [kagamiurayama/claude-code-roof-mod](https://github.com/kagamiurayama/claude-code-roof-mod) - Claude Mods ile Claude Code.
- [nateherkai/claude-code-mods](https://github.com/nateherkai/claude-code-mods) - Dört Claude Code modu: Cache Keeper, Recording Mode, Goal Meter ve Collision…
- [Hangghost/learning-hacker-claude-mod](https://github.com/Hangghost/learning-hacker-claude-mod) - Learning Hacker.
- [kakha13/claude](https://github.com/kakha13/claude) - Claude Code modları, Claude onları okumadan önce istemlerinizi düzeltir ve…
- [nekyialabs/claude-code-toolkit](https://github.com/nekyialabs/claude-code-toolkit) - Nekyia Labs tarafından geliştirilen ve kalıcı bir evde yaşayan AIs tarafından…
- [rashedInt32/glass](https://github.com/rashedInt32/glass) - Bir mod olarak Claude Code.
- [xuanji86/claude-agentpane](https://github.com/xuanji86/claude-agentpane) - Claude Code için bir yan panel: bir oturumun çalıştırdığı alt aracılar, her…
- [AgriciDaniel/claude-mods-brain](https://github.com/AgriciDaniel/claude-mods-brain) - Claude Code modları hakkında kaynak gösteren Obsidian bilgi tabanı: nasıl…
- [letswritetw/claude-mod-open-todos](https://github.com/letswritetw/claude-mod-open-todos) - Claude Desktop (Code sekmesi) kenar çubuğu paneli: tüm Claude Code…
- [BeLazy167/claude-mods-skill](https://github.com/BeLazy167/claude-mods-skill) - Claude Code ajanlarına, başlangıç örneğiyle birlikte Claude Mods.
- [letswritetw/claude-mod-token-usage](https://github.com/letswritetw/claude-mod-token-usage) - Claude Desktop (Code sekmesi) giriş kutusunun üstündeki kullanım çubuğu: 5h /…
- [omarcevi/claudemods](https://github.com/omarcevi/claudemods) - Tek bir pazardan kurulabilen topluluk Claude modları, eklentileri ve becerileri.
- [KilimcininKorOglu/claude-code-mods](https://github.com/KilimcininKorOglu/claude-code-mods) - Claude Code için Claude Mods (işlev kancası eklentileri).
- [baselane-sh/mods-catalog](https://github.com/baselane-sh/mods-catalog) - Baselane modları galerisi: Claude Code modları, kontrol edilmiş ve sabitlenmiş.
- [eighteyes/cactus](https://github.com/eighteyes/cactus) - Konuşmalı ajanlarla çalışan insanlar için karar kuyruğu CLI/TUI.
- [ronanworks/claude-code-mods](https://github.com/ronanworks/claude-code-mods) - Claude Code modları: 像素螃蟹用量面板 usage-hud + terminalde tıklanabilen HTML…
- [xuanji86/claude-statuspane](https://github.com/xuanji86/claude-statuspane) - Claude Code için kayan durum kartı — model, bağlam, hız sınırları, maliyet, dal…
- [arasovic/claude-code-mods](https://github.com/arasovic/claude-code-mods) - Claude Code için Mods: terminal kullanıcı arayüzüne canlı bölmeler ve davranış…
- [danyuchn/claude-mods](https://github.com/danyuchn/claude-mods) - Claude Code modları: screen-guard ekran paylaşırken adları ve gizli bilgileri…
- [helenkwok/gsd-status-mod](https://github.com/helenkwok/gsd-status-mod) - Claude Code için canlı GSD panosu: yol haritası, çatalları gösteren ajan ağacı…
- [magidandrew/cx](https://github.com/magidandrew/cx) - Claude Code Extensions. Claude.
- [markneonin/paneline](https://github.com/markneonin/paneline) - Activity, Files, Agents, Context ve MCP sekmelerini içeren bir yan bölme…
- [mishgoldenberg/claude-mods](https://github.com/mishgoldenberg/claude-mods) - Claude Code için paneller, koruyucu kurallar ve kullanım kolaylığı modları…
- [ofeklevy11/claude-code-hud](https://github.com/ofeklevy11/claude-code-hud) - İstem kutusunun üstünde iki Claude Code modu: bağlam penceresi ölçer, 5 saatlik…
- [VedantAndhale/claude-pro-kit](https://github.com/VedantAndhale/claude-pro-kit) - Claude Pro planının daha uzun süre dayanmasını sağlayın: tam kullanım HUD.
- [xuanji86/claude-mdview](https://github.com/xuanji86/claude-mdview) - Claude Code.
- [hahmjuntae/claude-mods-image-preview](https://github.com/hahmjuntae/claude-mods-image-preview) - Claude Code modu: herhangi bir terminalde istemin üstünde yapıştırılan…
- [leopiney/wolfbud-claude-mod](https://github.com/leopiney/wolfbud-claude-mod) - Claude Code için sesli çalışma arkadaşı.
- [borabiricik/claude-mods](https://github.com/borabiricik/claude-mods) - Claude Code modları: typing-speed, istem başına istatistiklerle canlı yazma…
- [charimsma/dopa-mode](https://github.com/charimsma/dopa-mode) - Claude Code için havai fişekler: her tuş vuruşu, araç çağrısı, commit ve…
- [DrishtantKaushal/AwesomeClaudeCodeMods](https://github.com/DrishtantKaushal/AwesomeClaudeCodeMods) - Animasyonlu demolar, kategori listeleri ve doğrudan kaynak bağlantılarıyla…
- [galElmalah/claude-mods](https://github.com/galElmalah/claude-mods) - Claude Code modu: mermaid diyagramları transkript içinde satır içi olarak…
- [GarvitNangru/claude-code-mods](https://github.com/GarvitNangru/claude-code-mods) - Claude Code için modlar ve görünümler: Claude görevleri için canlı ilerleme…
- [ha-ptt0601/cc-mods](https://github.com/ha-ptt0601/cc-mods) - Küçük Claude Code modülleri (işlev kancası eklentileri): session-switcher ve…
- [Jhonatan-de-Souza/ClaudeMods](https://github.com/Jhonatan-de-Souza/ClaudeMods) - Claude Code modları: Claude Tools menüsü, Zen modu, terminal temaları, çaba ve…
- [LeeHigma0201/claude-code-mods](https://github.com/LeeHigma0201/claude-code-mods) - Claude Code modları: mod-scout (en çok kullanacağınız modları bulur)…
- [Nongfsq/frank-claude-cockpit](https://github.com/Nongfsq/frank-claude-cockpit) - Aynı anda birçok oturum çalıştırmak için iki Claude Code modu: istemin üstünde…
- [ayagmar/claude-modmgr](https://github.com/ayagmar/claude-modmgr) - modmgr: Claude Code modlarını keşfedin, inceleyin, açıp kapatın ve güncelleyin.
- [Boom-Vitt/boombignose-mods](https://github.com/Boom-Vitt/boombignose-mods) - Claude Code modları: bağlam çubuğu, ajanlar paneli, PDPA bulanıklaştırma.
- [claude-code-mods/best-claude-code-mods](https://github.com/claude-code-mods/best-claude-code-mods) - En iyi Claude Code modları: özenle seçilmiş, doğrulanmış, sabitlenmiş.
- [dominicrico/jev-router](https://github.com/dominicrico/jev-router) - Claude Code eklentisi: otomatik Claude model yönlendirmesi.
- [FynnXland/fynn-mods](https://github.com/FynnXland/fynn-mods) - Claude Code için altı mod: animasyonlu Clawd maskotu, kullanım limiti ve…
- [Hula-Hoop-AI/supermods](https://github.com/Hula-Hoop-AI/supermods) - Claude Code için bir mod pazaryeri: ajan döngüsü için adım hata ayıklayıcı, git…
- [ice-lfernandes/claude-code-mods](https://github.com/ice-lfernandes/claude-code-mods) - Altı Claude Code modu: plan sınırları ve istemin üstünde bağlam, izin istemleri…
- [mertkayacs/ultramod](https://github.com/mertkayacs/ultramod) - Claude Code için en iyi hepsi bir arada mod paketi: kullanım sınırları ve…
- [mthli/cc-shorts](https://github.com/mthli/cc-shorts) - Claude Code.
- [NarenDawar/narens-claude-toolkit](https://github.com/NarenDawar/narens-claude-toolkit) - Naren.
- [neteye-platform/cc-split-diff-view](https://github.com/neteye-platform/cc-split-diff-view) - Edit ve Write farklarını yan yana iki sütunda çizen Claude Code modu.
- [noash-xrc/claude-tools](https://github.com/noash-xrc/claude-tools) - Claude Code.
- [raresmun/claude-mods](https://github.com/raresmun/claude-mods) - Claude Code için modlar: Claude.
- [reporails/arcade](https://github.com/reporails/arcade) - Claude Code modları olarak klasik masaüstü oyunları;
- [testy-cool/awesome-claude-code-mods](https://github.com/testy-cool/awesome-claude-code-mods) - Eklenti pazaryeri olarak kurulabilen, derlenmiş bir Claude Code modları…
- [timoncool/givememod](https://github.com/timoncool/givememod) - İsteğe bağlı Claude Code modları — konuşmanızı okuyup size uygun modu oluşturan…
- [xsyetopz/dotclaude](https://github.com/xsyetopz/dotclaude) - Harness mühendisliğine takıntılı bir Rustacean tarafından tasarlanmış, son…
- [yash-gadodia/claude-mods](https://github.com/yash-gadodia/claude-mods) - Bir ajanın dürüst kalmasını sağlayan Claude Code modları — kapsamı koruyan…
- [alexcz-a11y/claude-mods](https://github.com/alexcz-a11y/claude-mods) - Claude Code mod koleksiyonum; her dizinde bir mod.
- [ArgonQQ/sipp](https://github.com/ArgonQQ/sipp) - 💧 Claude Code için pasif-agresif bir su içme hatırlatıcısı.
- [bostonaholic/claude-mods](https://github.com/bostonaholic/claude-mods) - Kullandığım Claude Code modları.
- [CalvoSeko/claude-factory-mod](https://github.com/CalvoSeko/claude-factory-mod) - agent-graph: ajan grafikleri tasarlamak ve çalıştırmak için bir Claude Code…
- [chenyuxiaojin/cyxj-notch](https://github.com/chenyuxiaojin/cyxj-notch) - Claude Code için macOS çentik gösterge paneli: kullanım sınırları, açık…
- [Danovich/turntype](https://github.com/Danovich/turntype) - Claude çalışırken zaman geçirmek için bir yazma testi. Bir Claude Code modu.
- [DarioFontanel/claude-code-mods](https://github.com/DarioFontanel/claude-code-mods) - Claude Code başına mod: prompt cache çubuğu, sonraki adımlar, hızlı düğmeler ve…
- [dougcunha/claude-mods](https://github.com/dougcunha/claude-mods) - Claude Code için modlar: function-hooks API eklentisiyle oluşturulmuş paneller…
- [DragosMocrii/proc-stats](https://github.com/DragosMocrii/proc-stats) - Claude Code modu: oturumun belleğini, CPU.
- [drkokorev/context-diet](https://github.com/drkokorev/context-diet) - Büyük araç çıktılarını Claude Code.
- [EgonLeitner/dashband](https://github.com/EgonLeitner/dashband) - Claude Code için istem alt bilgisinde ve istemin üzerinde istem önbelleğini…
- [Elesiann/usagemeter](https://github.com/Elesiann/usagemeter) - Kodlama ajanlarınızın (Claude Code, Codex, OpenCode, Antigravity) maliyeti…
- [estruyf/claude-stats-mod](https://github.com/estruyf/claude-stats-mod) - Kullanım limitlerinizi ve harcamalarınızı istemin üzerindeki bantta gösteren…
- [herman925/925-cc-plugins](https://github.com/herman925/925-cc-plugins) - Herman.
- [homieyangg/claude-code-mods](https://github.com/homieyangg/claude-code-mods) - Claude Code modları: planlar için ilerleme çubukları, Claude.
- [lorenzh/rabe](https://github.com/lorenzh/rabe) - Claude Code.
- [macleodlabs-ai/claudeflow](https://github.com/macleodlabs-ai/claudeflow) - MacLeod Labs imzalı Claude Code modları: streams, bir oturumun iç içe geçmiş…
- [MankhongGarden/claude-code-mods-field-notes](https://github.com/MankhongGarden/claude-code-mods-field-notes) - Windows üzerindeki Claude Code modları hakkında birinci gün saha notları…
- [NMenzel/claude-devtools-mod](https://github.com/NMenzel/claude-devtools-mod) - Claude DevTools: Claude Code araç çağrıları için hata ayıklayıcı.
- [oMaN-Rod/claude-code-widgets](https://github.com/oMaN-Rod/claude-code-widgets) - Small cards that sit under the Claude Code prompt, or docked beside the…
- [patitow/claude-mod-cost-visibility](https://github.com/patitow/claude-mod-cost-visibility) - Claude Code modu: istemin üzerinde canlı maliyet, bağlam ve plan kota…
- [rbartoli/agent-usage-guard](https://github.com/rbartoli/agent-usage-guard) - Alt ajanların çoğalmasını, yoğun bağlamlı istemleri ve yeniden deneme…
- [revenantworks/claude-skills](https://github.com/revenantworks/claude-skills) - Beş pakette Claude için 28 Agent Skills.
- [schreibse/claude-code-mods](https://github.com/schreibse/claude-code-mods) - claude için code-mods.
- [shimo4228/harness-scope](https://github.com/shimo4228/harness-scope) - Genel becerilerinizi, aracıları, kuralları ve araçlarınızı adlandırılmış…
- [simplecore-inc/claude-mods](https://github.com/simplecore-inc/claude-mods) - Claude Code eklentileri (modlar): birkaç Claude hesabı arasında geçiş yapın…
- [Singh-AP/awesome-claude-mods](https://github.com/Singh-AP/awesome-claude-mods) - 🧩 Test edilmiş, tek komutla kurulabilen Claude Code modları: YOLO modu için…
- [Sma1lboy/claude-mods](https://github.com/Sma1lboy/claude-mods) - Claude Code için modlar: function hook.
- [smukh/roll-credits](https://github.com/smukh/roll-credits) - Kodlama oturumunuz için film tarzı jenerik.
- [Szotasz/claude-mods](https://github.com/Szotasz/claude-mods) - Kendi Claude Code modlarım için eklenti marketplace.
- [theonly1me/claude-code-mods](https://github.com/theonly1me/claude-code-mods) - Tarafımdan oluşturulmuş bir dizi claude code modu.
- [y-hirakaw/claude-code-mods](https://github.com/y-hirakaw/claude-code-mods) - Claude Code modları. touch-map: Claude tarafından listelenen, okunan…
- [yodakeisuke/claudelingo](https://github.com/yodakeisuke/claudelingo) - Claude Code ile çalışırken yabancı bir dil öğrenin.
- [20alexl/windvane](https://github.com/20alexl/windvane) - Uzun bir Claude Code oturumunu sizin yerinize takip eder: bağlamın dolmasını…
- [alaturqua/tower-mods](https://github.com/alaturqua/tower-mods) - Tek bir kontrol kulesinden birden fazla depoda çok sayıda oturum çalıştırmak…
- [andrewbakercloudscale/claude-code-cost-sidebar](https://github.com/andrewbakercloudscale/claude-code-cost-sidebar) - Claude Code için canlı maliyet, token ve bağlam kullanımı kenar çubuğu: oturum…
- [atharv6f/headway](https://github.com/atharv6f/headway) - Claude Code isteminizin üzerinde hedef, görevler ve agent.
- [BjoernSchotte/ccmod-amp](https://github.com/BjoernSchotte/ccmod-amp) - Claude Code içinde internet radyosu: cliamp kenar çubuğu, mini oynatıcı…
- [chrisluo5311/squad-chat](https://github.com/chrisluo5311/squad-chat) - Claude pişiriyor. Ekibinizle sohbet edin.
- [comertial/comertial-mods](https://github.com/comertial/comertial-mods) - Gerçek Mühendisler için Claude Code modları.
- [CrazyCoder/claude-desktop-recap](https://github.com/CrazyCoder/claude-desktop-recap) - Claude Code.
- [DarkVelours/claude-code-galactic-battle](https://github.com/DarkVelours/claude-code-galactic-battle) - Claude Code.
- [Davron2004/slash-coverage](https://github.com/Davron2004/slash-coverage) - Her Claude Code ajanının bağlamında hangi dosyaların olduğunu ve her birinden…
- [enhki/claude-mods](https://github.com/enhki/claude-mods) - Terminal ve masaüstü uygulaması için küçük Claude Code modları.
- [erte-del/claude-mods](https://github.com/erte-del/claude-mods) - Claude Code modları (eklenti mağazası): bağlam, maliyet ve kullanım…
- [Exdenta/ambient-spanish](https://github.com/Exdenta/ambient-spanish) - Ajan yanıtlarına İspanyolca kelimeler ekleyen Claude CLI becerisi + modu.
- [FrBmt-BIGetNouf/alarum-claude-mod](https://github.com/FrBmt-BIGetNouf/alarum-claude-mod) - Claude Code prompt.
- [FrBmt-BIGetNouf/floatee-claude-mod](https://github.com/FrBmt-BIGetNouf/floatee-claude-mod) - Floatee bekleme listeniz Claude Code isteminin üzerinde: yapılacaklarınızı tek…
- [gonzalonicolasr/claude-code-nerv](https://github.com/gonzalonicolasr/claude-code-nerv) - Claude Code için Evangelion tarzı kenar çubuğu: bağlam, kota, etkinlik, PR.
- [gregdotca/ccmod-the-machine](https://github.com/gregdotca/ccmod-the-machine) - Onu Person of Interest dizisindeki The Machine olarak yeniden biçimlendiren bir…
- [herlonventura/claude-model-squad](https://github.com/herlonventura/claude-model-squad) - Claude Code modu: pikselli bir ekip her görev için doğru modeli.
- [ibrahimkobeissy/claude-mods](https://github.com/ibrahimkobeissy/claude-mods) - Claude Code için açık kaynaklı modlar: bölmeler, durum satırları, bildirimler…
- [jduerrmann/agent-crew](https://github.com/jduerrmann/agent-crew) - Her alt ajan, dokunduğu dosyalar ve oturumunuzun kullanımı ile maliyeti için…
- [jonyfs/astrolabe](https://github.com/jonyfs/astrolabe) - 🧭 Claude Code mod: oturum durumu, canlı Spec Kit ilerlemesi ve kullanım…
- [kongyo2/context-view](https://github.com/kongyo2/context-view) - Bağlam penceresi, istemin üzerinde tek satır olarak;
- [kyledarling-io/claude-code-desktop-hud](https://github.com/kyledarling-io/claude-code-desktop-hud) - Claude Code Desktop için canlı görev HUD.
- [LupusMalusDeviant/mod-box](https://github.com/LupusMalusDeviant/mod-box) - Tek bir eklentide on dört Claude Code modu;
- [m4cd4r4/clear-resume](https://github.com/m4cd4r4/clear-resume) - Claude Code için ücretsiz, açık kaynaklı bir eklenti.
- [maxsoldev/pstash](https://github.com/maxsoldev/pstash) - Prompt.
- [Mechazawa/claude-inline-images](https://github.com/Mechazawa/claude-inline-images) - Ghostty ve kitty.
- [meganemura/pull-request-pane](https://github.com/meganemura/pull-request-pane) - Oturumun GitHub pull request.
- [muctebadikmen/claude-code-araclari](https://github.com/muctebadikmen/claude-code-araclari) - Claude Code modları: otomatik devir ve ilerleme çubuğu.
- [NotRedFox/NotRedFoxs-Claude-skills](https://github.com/NotRedFox/NotRedFoxs-Claude-skills) - Claude Code becerileri: belge doğrulayıcı, kod denetçisi, hata anıları günlüğü…
- [ondrhn/sharpprompt](https://github.com/ondrhn/sharpprompt) - Göndermeden önce kaba istemleri anlaşılır hâle getiren Claude Code modu.
- [pepperonas/loc-today](https://github.com/pepperonas/loc-today) - Claude Code modu: tüm oturumlarda Claude tarafından bugün yazılan kod satırları…
- [pepperonas/path-links](https://github.com/pepperonas/path-links) - Claude Code modu: yanıtlardaki tıklanabilir yollar — klasörü açmak için…
- [rezzminator/buddy](https://github.com/rezzminator/buddy) - Claude Code arkadaş eklentisi: isteminizin üzerinde kurallarınızı hatırlayan ve…
- [rezzminator/tool-visibility-controller](https://github.com/rezzminator/tool-visibility-controller) - Claude Code plugin for per-agent tool visibility — hide and refuse subagents…
- [roma-vibe/jev-governor](https://github.com/roma-vibe/jev-governor) - Claude Code modu: daha ucuz uzun oturumlar için Jev yönlendirmeli model/çaba…
- [samfrmr/barmkin-mod](https://github.com/samfrmr/barmkin-mod) - Claude Code modları: Claude Code için güvenlik katmanı — gizli bilgilerin…
- [seanrobertwright/claude-mods](https://github.com/seanrobertwright/claude-mods) - Bir Claude Code modları koleksiyonu.
- [Sennjen/claude-sdlc](https://github.com/Sennjen/claude-sdlc) - Claude Code plugin&#x27;i ve mod&#x27;u: hook ile zorunlu kılınan insan onayı kapıları ve…
- [SeongGwangJu/k-mods](https://github.com/SeongGwangJu/k-mods) - Harika Claude Code modları koleksiyonu | 클로드 코드 모드 모음집.
- [shahsanket2107/clarvis](https://github.com/shahsanket2107/clarvis) - Clarvis: Claude Code için resmî olmayan bir Avengers hayran modu.
- [Spardutti/claude-mods](https://github.com/Spardutti/claude-mods) - Claude Code modları: günlük çalışmalar için canlı paneller ve hook.
- [tanujarun/it-speaks](https://github.com/tanujarun/it-speaks) - Konuşuyor: Claude.
- [timoncool/slapbox](https://github.com/timoncool/slapbox) - 🍑 Hata yaptığında Claude.
- [TroyJLorents-GH/mod-squad](https://github.com/TroyJLorents-GH/mod-squad) - Claude Code modları: canlı bölmeler, maliyet farkındalıklı model yönlendirme ve…
- [VaitaR/claude-code-limits](https://github.com/VaitaR/claude-code-limits) - Claude Code modu: istemin üstünde tek satırda 5h/7d kotası, bağlam penceresi…
- [valeryia-piatrova/token-hamster](https://github.com/valeryia-piatrova/token-hamster) - 🐹 Claude Code modu ve eklentisi: kullanım monitörü, token izleyici ve durum…
- [VictorGambarini/jev-mod](https://github.com/VictorGambarini/jev-mod) - Küçük kararları ucuz bir karar modeline devreden bir Claude Code modu…
- [yuntaengtaeng/snitch](https://github.com/yuntaengtaeng/snitch) - Claude Code modu, Claude.
- [afterever/claude-mods](https://github.com/afterever/claude-mods) - afterever imzalı Claude Code modları (eklenti mağazası).
- [ajkatom/claude-mods](https://github.com/ajkatom/claude-mods)
- [Akurganow/model-router](https://github.com/Akurganow/model-router) - Claude Code modu: her alt agent.
- [alan-oliv/claude-mods](https://github.com/alan-oliv/claude-mods) - Claude Code modları: istemin üzerinde oturum istatistik kartları.
- [Aler1x/claude-cat](https://github.com/Aler1x/claude-cat) - Claude Code isteminin üzerinde animasyonlu bir braille kedisi.
- [alinaqi/mixture-of-models-claude-mod](https://github.com/alinaqi/mixture-of-models-claude-mod) - Claude Code modu: ucuz işleri bir alt Claude Code aracılığıyla GLM/Kimi.
- [aloki-alok/omni-cat](https://github.com/aloki-alok/omni-cat) - Claude Code isteminizin üzerinde, bir OmniDimension ses ajanı test çağrısı…
- [ambervdberg/smartcompact](https://github.com/ambervdberg/smartcompact) - Bağlam penceresini küçük tutmak için sıkıştırma işlemini uygun bir anda seçen…
- [an80sPWNstar/claude-mods](https://github.com/an80sPWNstar/claude-mods) - Claude Code için Claude modları: token-meter.
- [anderson-spider/claude-mods](https://github.com/anderson-spider/claude-mods) - anderson-spider tarafından geliştirilen Claude Code eklenti pazaryeri.
- [andrej-kolic/claude-mods](https://github.com/andrej-kolic/claude-mods) - Claude Code için genel amaçlı modlar: bantlar, paneller, bildirimler ve…
- [Ashley-Pettit/villager-hp](https://github.com/Ashley-Pettit/villager-hp) - Haftalık tempo uyarısıyla birlikte Claude kullanım sınırlarınızı animasyonlu…
- [AskTinNguyen/ather-mods](https://github.com/AskTinNguyen/ather-mods) - S2 ekibi için Claude Code modları (the ather marketplace).
- [astrosteveo/plain-english](https://github.com/astrosteveo/plain-english) - Claude.
- [Atanur/deskfit](https://github.com/Atanur/deskfit) - Claude çalışırken kısa antrenmanlar: günlük hedef, seriler, rozetler ve isteğe…
- [aycandv/claude-usage-meter](https://github.com/aycandv/claude-usage-meter) - Claude Code için kullanım panosu: modele göre harcama.
- [benjaminr/nowplaying](https://github.com/benjaminr/nowplaying) - Claude Code için Now Playing modu: istemin üzerinde kapak görseli, kontroller…
- [Berkay2002/berkays-mods](https://github.com/Berkay2002/berkays-mods) - Claude Code mods for orchestrator and worker sessions.
- [broening/claude-mods](https://github.com/broening/claude-mods) - Claude Code için modlar: önbellek saati, patlama yarıçapı, öneriler, iş…
- [Carismarkus/clowl](https://github.com/Carismarkus/clowl) - Claude Code.
- [cGradying/claude-code-cockpit](https://github.com/cGradying/claude-code-cockpit) - Tek bir eklenti olarak yüklenen ve varsayılan olarak sessiz çalışan tek…
- [ChaseWNorton/claude-doom](https://github.com/ChaseWNorton/claude-doom) - İçinde Freedoom bulunan orijinal Doom motoru, Claude Code içinde oynanabilir.
- [cldotdev/claude-todo-list](https://github.com/cldotdev/claude-todo-list) - Bir konuşmadaki açık maddelerin güncel listesini tutan ve bunu istemin üzerinde…
- [comertial/claude-pending-changes](https://github.com/comertial/claude-pending-changes) - Terminalden çıkmadan, bir çekme isteği gibi, Claude.
- [CTeitzel/cache-band](https://github.com/CTeitzel/cache-band) - Claude Code modu: istemin üzerinde istem önbelleği geri sayımını, önbellek…
- [dalemorgan04/claude-mods](https://github.com/dalemorgan04/claude-mods) - Claude Modları.
- [danielmertens/Claude-mods](https://github.com/danielmertens/Claude-mods) - Kişisel Claude modlarından oluşan koleksiyon.
- [darshk07/claude-mods](https://github.com/darshk07/claude-mods)
- [davidurco/cc-tamagotchi](https://github.com/davidurco/cc-tamagotchi) - Claude Code içinde yaşayan bir Tamagotchi: yumurtadan çıkar, Claude.
- [DazzleML/claude-bookmarks](https://github.com/DazzleML/claude-bookmarks) - Claude Code terminal konuşmalarında yer imleri ve vim tarzı işaretler: bir…
- [delexw/codyssey](https://github.com/delexw/codyssey) - Her Claude Code oturumunu küçük bir maceraya dönüştürün: ajanın ruh hâlini…
- [densi97/claude-code-command-log](https://github.com/densi97/claude-code-command-log) - Agent tarafından çalıştırılan komutları açıklayan Claude Code modu.
- [diamondT/claude-mods](https://github.com/diamondT/claude-mods)
- [dieg666/claude-herald](https://github.com/dieg666/claude-herald) - Bir Claude Code modu: istemin üzerinde, Claude haberlerini ve…
- [dot-agi/arrester](https://github.com/dot-agi/arrester) - Claude Code modu: bir guard araç çağrısını engelledikten sonra aynı hedefe…
- [dot-agi/downrange](https://github.com/dot-agi/downrange) - Claude Code modu: gerçek çıktından okunan ilerleme ve tahmini varış süreleriyle…
- [dot-agi/high-command](https://github.com/dot-agi/high-command) - Claude Code modu: ekip arkadaşlarından, adlandırılmış alt ajanlardan ve diğer…
- [dot-agi/sandbox-tuner](https://github.com/dot-agi/sandbox-tuner) - Claude Code modu: sandbox engellemelerini açıklar ve tekrarlanan engellemeleri…
- [dricosnyman/claude-favourites](https://github.com/dricosnyman/claude-favourites) - Claude Code için favoriler: komutlarınız ve becerileriniz için tek tıklamalı…
- [Egrn/claude-code-mutedit](https://github.com/Egrn/claude-code-mutedit) - Hey, susturdum! Farkı bırak, ritmi kes; artık düzenleme yok, daha az kredi.
- [Eiyuo/Claude-Mods](https://github.com/Eiyuo/Claude-Mods)
- [ekinertac/claude-code-mods](https://github.com/ekinertac/claude-code-mods) - Claude Code modları: rewrite-prompt.
- [elijah-rou/agent-kit](https://github.com/elijah-rou/agent-kit) - Pi, Codex ve Claude Code için talimatlar, beceriler, Pi uzantıları ve Claude…
- [eric1hua/claudemods-desktop-statusline](https://github.com/eric1hua/claudemods-desktop-statusline) - Masaüstü uygulamasında ve terminalde istemin üzerinde bir bant olarak abonelik…
- [fatihkartal35/claude-mods](https://github.com/fatihkartal35/claude-mods) - Claude Code modları: auto-model-detector, her istemi doğru model ve çaba…
- [floheissler/cc-worktree-radar](https://github.com/floheissler/cc-worktree-radar) - İstemin üzerinde paralel dallarınızın ve çalışma ağaçlarınızın canlı radarı…
- [Gat0rRex/claude-mods](https://github.com/Gat0rRex/claude-mods) - Claude Code modları (function-hook eklentileri): bağlam bandı, yarım kalan…
- [Gharib89/claude-mods](https://github.com/Gharib89/claude-mods) - Tek bir marketplace üzerinden yüklenen Claude Code modları.
- [grota/beppe-claude-mods](https://github.com/grota/beppe-claude-mods) - Modlarımı içeren Claude Code eklenti pazarı.
- [hb03/claude-mods](https://github.com/hb03/claude-mods) - Claude Code için Almanca modlar: bağlam/önbellek ipuçları, yönlendirmeli açık…
- [HectorBailey/claude-mods](https://github.com/HectorBailey/claude-mods) - Hector Bailey.
- [hernandezsanti/claude-code-mods](https://github.com/hernandezsanti/claude-code-mods) - Claude Code mods that enforce ticket-based commits, protect paid CI minutes and…
- [humvnpvrvdox777/NextSteps](https://github.com/humvnpvrvdox777/NextSteps) - Claude Code modu: her yanıttan sonra herhangi bir dilde üç sonraki adım;
- [Huuuuung/think-meter](https://github.com/Huuuuung/think-meter) - Claude Code modu: her yanıtın ne kadar sürdüğü, Claude.
- [huynl-96/claude-mods](https://github.com/huynl-96/claude-mods) - Claude Code modları: streamer-mode, ekranınızı paylaşırken özel panelleri…
- [hyperbola-bear/claude-mods](https://github.com/hyperbola-bear/claude-mods) - claude modlarım için.
- [iceberggymnast/claude-code-mods](https://github.com/iceberggymnast/claude-code-mods) - Claude Code function-hook eklentileri (modlar).
- [icedevil2001/auto-continue](https://github.com/icedevil2001/auto-continue) - Claude Code modu: 5 saatlik kullanım sınırının dolmasını bekler ve sizin için…
- [imsungbin/quackpit-mod](https://github.com/imsungbin/quackpit-mod) - Claude Code isteminizin üzerinde bir kokpit. Ördek göstergeleri okur.
- [ipartington/claude-mods](https://github.com/ipartington/claude-mods) - Claude Code modları (function-hook eklentileri): PR birleştirme takibi, /clear…
- [iyiob96/Context-Mod-Companion](https://github.com/iyiob96/Context-Mod-Companion) - Claude Code modu: RTK tasarrufları ve pikselli Yemenli yoldaş içeren bağlam…
- [jakerains/claudemods](https://github.com/jakerains/claudemods) - Küçük Claude Code modları: bağlam ve plan kullanımı göstergeleri, istem…
- [jamesnguyen1309/claude-usage](https://github.com/jamesnguyen1309/claude-usage) - Claude Code modu: istem başına canlı token kullanımı, modeller ve alt agent.
- [jessetsai1024/claude-ctx-panel](https://github.com/jessetsai1024/claude-ctx-panel) - Kenar çubuğunda bağlam kullanım paneli: toplam, kategoriler, tur başına büyüme…
- [jessetsai1024/claude-files](https://github.com/jessetsai1024/claude-files) - Kenar çubuğunda dosya listesi: bu konuşmada hangi dosyalar oluşturuldu…
- [jessetsai1024/claude-maomao](https://github.com/jessetsai1024/claude-maomao) - Girdi kutusunun üzerinde koşup zıplayan 8-bit tarzı 毛毛.
- [jessetsai1024/claude-prompts](https://github.com/jessetsai1024/claude-prompts) - Kenar çubuğunda “sorduğum sorular”: kullanıcının bu konuşmada yazdığı her…
- [jessetsai1024/claude-timeline](https://github.com/jessetsai1024/claude-timeline) - Kenar çubuğunda zaman çizelgesi: bu turda zaman nereye harcandı.
- [jessetsai1024/claude-tokens](https://github.com/jessetsai1024/claude-tokens) - Kenar çubuğunda token alışverişi: ana konuşma her seferinde Anthropic.
- [jessetsai1024/claude-whisper](https://github.com/jessetsai1024/claude-whisper) - claude code.
- [jkf87/mod-guide](https://github.com/jkf87/mod-guide) - Unofficial community guide to Claude Code mods (function hooks) in 6 languages…
- [juro-mont/claude-ev-charging](https://github.com/juro-mont/claude-ev-charging) - Claude Code yardımcı ajanları için bir elektrikli araç şarj ilerleme çubuğu ve…
- [KaiC5504/clawd-bar](https://github.com/KaiC5504/clawd-bar) - Clawd, Claude Code prompt.
- [kajidog/cc-mods-tts](https://github.com/kajidog/cc-mods-tts) - Claude Code.
- [kbrdn1/claude-crosstalk](https://github.com/kbrdn1/claude-crosstalk) - Claude Code oturumlarınız arasındaki konuşmaları okumak ve bu konuşmalara…
- [ke11/claude-mods](https://github.com/ke11/claude-mods) - Claude Code modları. PixBar: isteminizin üzerinde yer alan ve turunuz…
- [kkatsuyoshi/claude-mods](https://github.com/kkatsuyoshi/claude-mods) - claude modları.
- [KKK12142/claude-mods](https://github.com/KKK12142/claude-mods) - Claude Code modları (usage-meter, ...).
- [krishna-goutham-tls/cc-mods](https://github.com/krishna-goutham-tls/cc-mods) - İki Claude Code modu: sohbetin yanında bir dosya bölmesi olan folio ve durum…
- [kuehn-lars/cc-graph](https://github.com/kuehn-lars/cc-graph) - cc-graph: Claude Code.
- [leonidb/claude-code-mods](https://github.com/leonidb/claude-code-mods) - Claude Code.
- [linsanmufilm-svg/claude-mods](https://github.com/linsanmufilm-svg/claude-mods) - Sanmu&#x27;nun Claude Code modları — bir eklenti marketplace&#x27;i.
- [LordMordelon/claude-mods](https://github.com/LordMordelon/claude-mods) - Angel.
- [Lucas-CX/awesome-claude-mods](https://github.com/Lucas-CX/awesome-claude-mods) - Topluluk tarafından derlenmiş bir Claude Code Modları rehberi: kullanım…
- [LupusMalusDeviant/claude-mods](https://github.com/LupusMalusDeviant/claude-mods) - Mod Box.
- [luwux/keepwarm](https://github.com/luwux/keepwarm) - Claude Code mod: guards the 1-hour prompt cache of idle sessions — countdown…
- [M-i-k-e-l/agent-state](https://github.com/M-i-k-e-l/agent-state) - Claude.
- [makingaipractical/brain-drain-for-claude-code](https://github.com/makingaipractical/brain-drain-for-claude-code) - How full Claude.
- [Malkiz/claude-reply-comments](https://github.com/Malkiz/claude-reply-comments) - Claude Code modu: Claude noktasını doğrudan metin üzerinde madde madde…
- [MarcusJellinghaus/claude-mode-gate](https://github.com/MarcusJellinghaus/claude-mode-gate) - Değiştirilebilir izin profillerine sahip bir Claude Code modu: güvenli bir…
- [MarkMerk/markmerk-mods](https://github.com/MarkMerk/markmerk-mods) - Claude Code için küçük modlar: runner-avatar, isteminizin üzerinde koşan küçük…
- [Marnel8/claude-mods-](https://github.com/Marnel8/claude-mods-)
- [martin-macak/claude-code-mod-tracking](https://github.com/martin-macak/claude-code-mod-tracking) - İlgili yapıları ve referansları izlemek için Claude Code modu.
- [mattbv/intent-ledger](https://github.com/mattbv/intent-ledger) - Claude Code modu: Yapay zekâ kodlama ajanınızın neyi amaçladığını…
- [MDmubarak786/claude-mods](https://github.com/MDmubarak786/claude-mods) - Claude Code için topluluk modları: Claude Code içinde çalışan korumalar…
- [michaelblaess/turbo-mod](https://github.com/michaelblaess/turbo-mod) - Side pane for Claude Code: files Claude wrote, terminal splits, git repo status…
- [MkGut/claude-tutor](https://github.com/MkGut/claude-tutor) - Claude Code mod: a sidebar tutor that explains what Claude is doing as it works.
- [mmedum/glimt](https://github.com/mmedum/glimt) - Claude Code için sessiz bir yan bölme: bu oturumun ne yaptığı, planı, ajanları…
- [mmedum/nuet](https://github.com/mmedum/nuet) - Claude Code dökümündeki her istemin ve her yanıtın üzerinde, kendi saat…
- [mmedum/spor](https://github.com/mmedum/spor) - Claude Code&#x27;un katlayarak gizlediği şeyleri geri getirir: Claude&#x27;in okuduğu…
- [muellerei/enable-todo-tools](https://github.com/muellerei/enable-todo-tools) - Oturum başlangıcında CLAUDE_CODE_ENABLE_TODO_TOOLS ayarlayarak, bunları devre…
- [muellerei/sweet-spot](https://github.com/muellerei/sweet-spot) - Güvenli bir duraklama bekleyen, ardından oturumunuzu devralan veya oturumu…
- [muellerei/task-line](https://github.com/muellerei/task-line) - Claude Code modu: istemin üzerinde görev listesi başına bir satır;
- [nachtgold/claude-code-connect-four](https://github.com/nachtgold/claude-code-connect-four) - Claude Code içinde bir AI.
- [naoanao/agent-cross-check](https://github.com/naoanao/agent-cross-check) - Claude Code modu: başka bir kodlama ajanı deponuza commit yaptığında Claude…
- [naoanao/shared-repo-guard](https://github.com/naoanao/shared-repo-guard) - Birden çok AI ajanının paylaştığı depolar için Claude Code modu: gizli…
- [Nelahia/claude-mods](https://github.com/Nelahia/claude-mods) - Claude Code modlarımı tek komutla kurar ve yapılandırır (macOS, Linux, Windows).
- [NeonOrchard/tab-alert](https://github.com/NeonOrchard/tab-alert) - Claude Code modu: Claude sizi beklerken terminal sekmesini yanıp söndürür.
- [nerevar48/nerevar-mods](https://github.com/nerevar48/nerevar-mods) - Claude Code modları pazaryeri.
- [NicBritz/claude-code-mods](https://github.com/NicBritz/claude-code-mods) - Hiç token harcamayan Claude Code için eğlenceli, ücretsiz modlar.
- [nu0ma/query-guard](https://github.com/nu0ma/query-guard) - Claude Code.
- [OG-Matcha/tessera](https://github.com/OG-Matcha/tessera) - Claude Code, Windows ve CJK öncelikli tek bir mod: herhangi bir terminalde…
- [ohade/claude-mods](https://github.com/ohade/claude-mods) - Claude Code modları: görsel küçük resimleri ve durum satırı.
- [Orbitmap/claude-mods](https://github.com/Orbitmap/claude-mods) - OrbitMap ekibi tarafından hazırlanan Claude Code modları.
- [osaki42/awesome-claude-mods](https://github.com/osaki42/awesome-claude-mods) - Sizin için yaptıklarına göre sıralanmış en iyi Claude Code Modları.
- [Para-FR/claude-code-mods-fr](https://github.com/Para-FR/claude-code-mods-fr) - Claude Code için iki Claude Modu: garde-du-corps.
- [petershk/explain-permission](https://github.com/petershk/explain-permission) - Claude Code mod: explains each permission request in plain English.
- [philarete173/claude_mods](https://github.com/philarete173/claude_mods) - Claude masaüstü uygulamasının Code sekmesi için gerçek zamanlı oturum…
- [pkkid/claude-mods](https://github.com/pkkid/claude-mods) - Claude Desktop kurulumum için çeşitli modlar ve beceriler.
- [pradyb/claude-mods](https://github.com/pradyb/claude-mods) - Claude Code için modifikasyonlar: safety-guard yıkıcı komutları ve gizli…
- [pvjbuilds/crab-buddy](https://github.com/pvjbuilds/crab-buddy) - An animated pixel-art Claude crab for Claude Code: it acts out what Claude is…
- [rajib2k5/claude-market-watch](https://github.com/rajib2k5/claude-market-watch) - Claude Code modu: canlı hisse senedi şeridi, /quote bölmesi, fiyat uyarıları…
- [ramtinJ95/claude-mods](https://github.com/ramtinJ95/claude-mods) - Tek bir eklenti marketplace olarak yayımlanan Claude Code modları.
- [ray-amjad/cache-clock](https://github.com/ray-amjad/cache-clock) - Claude Code modu: prompt&#x27;un üzerinde kullanılan bağlamı ve prompt cache&#x27;in…
- [ray-amjad/diagram-pane](https://github.com/ray-amjad/diagram-pane) - Claude Code modu: Claude.
- [ray-amjad/dream-pass](https://github.com/ray-amjad/dream-pass) - Claude Code modu: Claude.
- [ray-amjad/prompt-bouncer](https://github.com/ray-amjad/prompt-bouncer) - Claude Code modu: Claude görmeden önce belirsiz prompt.
- [ray-amjad/secret-box](https://github.com/ray-amjad/secret-box) - Claude Code modu: Claude, sırlarınızı görmeden onları kullanır.
- [ray-amjad/transcript-redactor](https://github.com/ray-amjad/transcript-redactor) - Sırları oturum dökümünden uzak tutan bir Claude Code modu: her anahtar, Claude…
- [RedRoosterKey/claude-code-ssh-usage-band](https://github.com/RedRoosterKey/claude-code-ssh-usage-band) - Claude Code modu: istemin üzerindeki bir satırda SSH ana bilgisayarı, RAM ve…
- [Risdon8/push-ups](https://github.com/Risdon8/push-ups) - Claude Code modu: Claude çalışırken yapılacak şınavlar. Jeton yok.
- [rogadev/paceline-mod](https://github.com/rogadev/paceline-mod) - Bir Claude Code modu olarak paceline: kullanım limitlerinizi istemin üzerindeki…
- [Rohitp/claude-mods](https://github.com/Rohitp/claude-mods) - claude code için modlar.
- [saadk408/stepline](https://github.com/saadk408/stepline) - Claude Code modu: plan modunda onayladığınız planı prompt.
- [saksham10arora-dotcom/awesome-claude-mods](https://github.com/saksham10arora-dotcom/awesome-claude-mods) - Özenle seçilmiş Claude Code modları listesi.
- [saksham10arora-dotcom/claude-frugal](https://github.com/saksham10arora-dotcom/claude-frugal) - Maliyetsiz mod: yardımcı ajanlar Haiku üzerinde çalışır;
- [saksham10arora-dotcom/claude-lofi](https://github.com/saksham10arora-dotcom/claude-lofi) - Oturumu takip eden bir lofi müzikleri: sakinlik, odaklanma, akış ve testlerin…
- [saksham10arora-dotcom/claude-teach-me](https://github.com/saksham10arora-dotcom/claude-teach-me) - Claude kod yazarken öğrenin: kodu değiştiren bir turdan sonra, tam o…
- [saksham10arora-dotcom/claude-vhs](https://github.com/saksham10arora-dotcom/claude-vhs) - Claude.
- [shengyy/ccoverhead](https://github.com/shengyy/ccoverhead) - İstemin üzerinde bağlamı, büyümeyi, kotayı, önbelleği, yerel maliyeti ve ajan…
- [shissncg/claude-mods](https://github.com/shissncg/claude-mods)
- [sidhantunnithan/jindan-cc-marketplace](https://github.com/sidhantunnithan/jindan-cc-marketplace) - Kişisel Claude Code modları.
- [Spendry/claude-code-mods](https://github.com/Spendry/claude-code-mods) - Eklenti marketplace olarak kurulabilen Claude Code modları: deviation-kernel…
- [speti4/doom-pane](https://github.com/speti4/doom-pane) - Kurulum gerektirmeyen, Claude Code bölmesinde çalışan orijinal DOOM: motor…
- [StalicJi/my-mods](https://github.com/StalicJi/my-mods) - Kişisel Claude Code mod marketplace.
- [stelmach-systems/claude-mods](https://github.com/stelmach-systems/claude-mods) - Claude Code modları (işlev kancaları): ajan paneli, bütçe çubuğu, oturum filosu.
- [SteveAnthonyFM/subagent-guard](https://github.com/SteveAnthonyFM/subagent-guard) - Claude.
- [steven-ngle/blade-of-commits](https://github.com/steven-ngle/blade-of-commits) - Dans eden pixel-art Malenia ile Claude Code için tek tıkla commit mesajları.
- [Sunkanxx/Mods](https://github.com/Sunkanxx/Mods) - Claude Code modları — marketplace sunkanxx-mods.
- [Tanish-Dev/claude-usage-band](https://github.com/Tanish-Dev/claude-usage-band) - Clawd Meter — Claude Code modu; Claude plan kullanımınızı.
- [tartinerlabs/claude-code-mods](https://github.com/tartinerlabs/claude-code-mods)
- [thangdo19/claude-code-mods](https://github.com/thangdo19/claude-code-mods) - Claude Code.
- [TheBabaYaga/claude-session-flow](https://github.com/TheBabaYaga/claude-session-flow) - Her istemi, Claude.
- [theishandubey/claude-mods](https://github.com/theishandubey/claude-mods) - Modlardan oluşan bir Claude Code eklenti pazaryeri: Claude Code içinde bantlar…
- [tomfluff/claude-read-along](https://github.com/tomfluff/claude-read-along) - Okunan cümle vurgulanırken Claude Code yanıtlarını dinleyin.
- [tunglt1810/claude-gadgets](https://github.com/tunglt1810/claude-gadgets) - Bazı Claude modları.
- [twentynineteen/scrooge-context-vault](https://github.com/twentynineteen/scrooge-context-vault) - Claude Code modu: bağlam pencereniz Scrooge McDuck.
- [tyree88/tempered_plugins](https://github.com/tyree88/tempered_plugins) - Tempered Works.
- [UsamaSadiq/claude-mods](https://github.com/UsamaSadiq/claude-mods) - Small, fun and useful mods for Claude Code.
- [VAlux/claude-session-progress](https://github.com/VAlux/claude-session-progress) - Claude Code modu: uzun süren görevler için animasyonlu ilerleme bandı ve…
- [Vansitha/clawd-watch](https://github.com/Vansitha/clawd-watch) - Üç küçük Claude Code modu: alt ajanlarınızın ne zaman tamamlanacağını görün…
- [varunmoka7/image-shrinker](https://github.com/varunmoka7/image-shrinker) - Claude onları okumadan önce büyük ekran görüntülerini küçültür;
- [varunmoka7/layman](https://github.com/varunmoka7/layman) - &quot;Kayboldum&quot; deyin, Claude son yanıtını günlük ifadelerle yeniden açıklasın.
- [varunmoka7/next-steps-autopilot](https://github.com/varunmoka7/next-steps-autopilot) - İstem kutusunun üzerinde önerilen sonraki istemleri gösterir.
- [varunmoka7/side-chat](https://github.com/varunmoka7/side-chat) - Çalışmanızın yanındaki bir bölmede Claude.
- [vihrea1337/pager](https://github.com/vihrea1337/pager) - Claude, bir görev tamamlandığında veya izin beklediğinde Telegram üzerinden…
- [WeaponizedLego/claude-code-mods](https://github.com/WeaponizedLego/claude-code-mods) - Claude Code modlarım.
- [wellavelino/mystique](https://github.com/wellavelino/mystique) - Bir Claude Code modu: yanıtlar için fosforlu kalem, tablo olarak sorgu…
- [wimcraft/godville-pane](https://github.com/wimcraft/godville-pane) - Bir Claude Code modu: Godville kahramanınız ve günlüğünüz bir kenar çubuğunda.
- [wnsogabriel/claude-mods](https://github.com/wnsogabriel/claude-mods) - Claude Code için modlar: kullanım sınırları çubuğu (5 saat/haftalık) ve…
- [Wowbagger1994/claude-mods](https://github.com/Wowbagger1994/claude-mods) - Mod per Claude Code: segreti oscurati, cose da fare, verifiche e CI, diario…
- [wukonigcom/quanta-costa](https://github.com/wukonigcom/quanta-costa) - 🧾 Claude Code eklentisi: Claude Pro/Max kullanım limitleriniz, hız tahmini…
- [xinhuagu/oh-my-claude-mods](https://github.com/xinhuagu/oh-my-claude-mods) - Claude Code için modlar. agent-crew: alt aracılarınızı rol, model, mevcut araç…
- [yeonwooook/claude-study-latex](https://github.com/yeonwooook/claude-study-latex) - Claude.
- [YohanGarcia/agent-taskboard](https://github.com/YohanGarcia/agent-taskboard) - Claude Code için canlı görev panosu: oluşturmadan önce planlayın, her görevi…
- [zaripovfarrukh/claude-code-mods](https://github.com/zaripovfarrukh/claude-code-mods)
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - Durdurulamaz Anthropic PBC ekibinden (bağlantısı yoktur), kodlama…
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) - Neler olduğunu gösteren bir Claude Code eklentisi - bağlam kullanımı, etkin…
- [sirmalloc/ccstatusline](https://github.com/sirmalloc/ccstatusline) - 🚀 Claude Code CLI için powerline desteği, temalar ve daha fazlasını içeren…
- [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) - Claude Code.
- [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) - Claude Code.
- [op7418/guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill) - 🪧 Claude Code / Codex skill — Xiaohongshu karuselleri ve WeChat 21:9+1:1 kapak…
- [Owloops/claude-powerline](https://github.com/Owloops/claude-powerline) - Claude Code için güzel, vim tarzı powerline.
- [persiyanov/herdr-reviewr](https://github.com/persiyanov/herdr-reviewr) - Kodlama aracınızın diff.
- [devswha/herdr-web-ui](https://github.com/devswha/herdr-web-ui) - herdr için tarayıcı ve telefon istemcisi: her ajan bölmesi için sohbet ve canlı…
- [uppinote20/claude-dashboard](https://github.com/uppinote20/claude-dashboard) - Bağlam kullanımı, API hız sınırları ve maliyet takibiyle Claude Code için…
- [starbaser/ccproxy](https://github.com/starbaser/ccproxy) - Claude Code için modlar oluşturun: Her isteğe kanca ekleyin, her yanıtı…
- [NYCU-Chung/cc-statusline](https://github.com/NYCU-Chung/cc-statusline) - Claude Code için kapsamlı durum satırı panosu — oturum bilgileri, kota…
- [gwittebolle/claude-carbon](https://github.com/gwittebolle/claude-carbon) - claude-carbon: Claude Code oturumlarınızın karbon ayak izini takip edin.
- [AwesomeZun/CC-statusline](https://github.com/AwesomeZun/CC-statusline) - awesomejun tarafından Claude Code için hazırlanmış estetik durum satırı.
- [a86582751/dsh-nexttavern](https://github.com/a86582751/dsh-nexttavern) - DeepSeek Harness 长篇角色扮演agent（DSH酒馆插件）：SillyTavern…
- [JohnnyVizz/claude-kit](https://github.com/JohnnyVizz/claude-kit) - Herkese açık Claude Code Skills.
- [escapeboy/claude-code-kit](https://github.com/escapeboy/claude-code-kit) - Claude Code için Skills.
- [mvalentsev/awesome-free-ai-coding](https://github.com/mvalentsev/awesome-free-ai-coding) - 📡 Yasal ücretsiz LLM APIs ve kodlama aracıları — kendini günceller, haftada iki…
- [chen731215-dev/dsh-tavern-v2](https://github.com/chen731215-dev/dsh-tavern-v2) - DeepSeek Harness Tavern Eklentisi - karakter kartı rol yapma, dünya kitabı…
- [backstabslash/goccc](https://github.com/backstabslash/goccc) - Claude Code için hızlı, bağımlılık gerektirmeyen maliyet hesaplayıcı ve…
- [kylesnowschwartz/tail-claude-hud](https://github.com/kylesnowschwartz/tail-claude-hud) - Claude Code oturumları için terminal statusline.
- [arturogarrido/claudinho](https://github.com/arturogarrido/claudinho) - ⚽ Takip ettiğiniz müsabaka için canlı futbol skorları, fikstürler ve puan…
- [WormAlien/hub-cc](https://github.com/WormAlien/hub-cc) - Claude Code için Windows ve macOS üzerinde yerel kontrol düzlemi: sabit bir uç…
- [johncattrall/keymap-ai](https://github.com/johncattrall/keymap-ai) - Kodlama aracınızı klavye ürün yazılımı uzmanına dönüştüren Agent Skill.
- [ashafizullah/claude-code-muslim-mods](https://github.com/ashafizullah/claude-code-muslim-mods) - Claude Code içinde namaz vakitleri, Hicri tarih, zikirler, günlük ayet, sünnet…
- [philoserf/claude-code-config](https://github.com/philoserf/claude-code-config) - ~/.claude içinde sürümlendirilen kişisel Claude Code yapılandırması…
- [GoSlowPoke168/claude-statusline](https://github.com/GoSlowPoke168/claude-statusline) - Claude Code için iki satırlı truecolor durum satırı.
- [proDreams/dsh-tidewatch](https://github.com/proDreams/dsh-tidewatch) - DeepSeek Harness için yüzen yoğun/yoğun olmayan dönem gelgit kartı: i18n…
- [hoobnn/hoobnn-agent-mods](https://github.com/hoobnn/hoobnn-agent-mods) - Claude Code, pi ve DeepSeek Harness için eklenti koleksiyonu: durum çubuğu…
- [pierrebelin/claude-code-toolkit](https://github.com/pierrebelin/claude-code-toolkit) - .NET DDD/Clean Architecture için taşınabilir Claude Code araç seti: katı TDD…
- [jcdendrite/claude-config](https://github.com/jcdendrite/claude-config) - Taşınabilir Claude Code genel yapılandırması: özel beceriler, PreToolUse…
- [mutlumehmet/claude-plugins](https://github.com/mutlumehmet/claude-plugins) - Her gün kullandığım Claude Code eklentileri: herkesin makinesinde çalışacak…
- [manson341349-beep/claude-desktop-mods](https://github.com/manson341349-beep/claude-desktop-mods) - Claude Desktop.
- [cmfok/dsh-feishucard](https://github.com/cmfok/dsh-feishucard) - DSH &lt;-&gt; Feishu (Lark) köprüsü, kendi geliştirmemizdir (fork değildir): akışlı…
- [darthmolen/hytale-claude-code-marketplace](https://github.com/darthmolen/hytale-claude-code-marketplace) - Hytale oyununda modları kolaylaştırmak için Claude Code Eklentileri ve…
- [frsorrentino/fable-director](https://github.com/frsorrentino/fable-director) - Claude Code için token yönetimi: en üst model yönlendirir, yürütme en ucuz…
- [jeancarlo-javier/claude-status-bar](https://github.com/jeancarlo-javier/claude-status-bar) - Claude Code için canlı iş akışı aşaması durum satırı.
- [romnycristopher/claude-am-mods](https://github.com/romnycristopher/claude-am-mods) - Claude Code Awesome Media modları için depo.
- [tedserbinski/claude-code-statusline](https://github.com/tedserbinski/claude-code-statusline) - Claude Code için basit ve kullanışlı durum satırı kurulumu.
- [cesarschutz/claude-code-kit](https://github.com/cesarschutz/claude-code-kit) - Claude Code için eklenti mağazası: modlar, beceriler, agent&#x27;lar, hook&#x27;lar…
- [crosscountryridinggirlwonder916/claude-statusline](https://github.com/crosscountryridinggirlwonder916/claude-statusline) - Daha iyi çalışma alanı farkındalığı için Claude Code durum satırını hız…
- [fbincon/claude-code-statusline](https://github.com/fbincon/claude-code-statusline) - Linux, WSL, Windows ve macOS için yapılandırılabilir Claude Code durum satırı;
- [JairoTorregrosa/claude-statusline](https://github.com/JairoTorregrosa/claude-statusline) - Claude Code için hızlı Rust durum satırı — önce yük, önbelleğe alınmış git…
- [jsh135790/claude-code-capsule-panel](https://github.com/jsh135790/claude-code-capsule-panel) - Claude Code için canlı kullanım panosu — Catppuccin kapsül tarzı bir yan…
- [jv-k/claude-gauge](https://github.com/jv-k/claude-gauge) - Claude Code için bir durum satırı ve token satırı: bağlam, tempo…
- [kyllian330/claude-statusline](https://github.com/kyllian330/claude-statusline) - Model, bağlam, sınırlar, git bilgileri ve oturum süresi dahil olmak üzere…
- [Obednal97/claude-statusline-kit](https://github.com/Obednal97/claude-statusline-kit) - Çok satırlı Claude Code durum satırı: harcama, bağlam yüzdesi, git ve etkin…
- [tc3oliver/claude-team-kit](https://github.com/tc3oliver/claude-team-kit) - Yerel aracı ekipleri. Kontrol altında.
- [yedidya-buildfy/claude-addons](https://github.com/yedidya-buildfy/claude-addons) - Claude Code eklentileri: sekme durumunda renkli nokta izleyicisi + yerleşik GSD…
- [zach-source/claude-factory](https://github.com/zach-source/claude-factory) - herdr üzerinde Claude Code için tanımlanabilir yazılım fabrikaları: xstate…
- [akhilnalliboina/claude-usage-statusline](https://github.com/akhilnalliboina/claude-usage-statusline) - macOS ve Linux için Claude Code kullanım durum satırı, herdr yükleyici…
- [alfredwesterveld/claude-cache-status](https://github.com/alfredwesterveld/claude-cache-status) - Claude Code masaüstü modu: istem önbelleği TTL geri sayımı, isabet oranı ve…
- [andkirby/claude-statusline](https://github.com/andkirby/claude-statusline) - Claude Code için özel durum satırı — kullanım yüzdesi, bağlam boyutu, maliyet…
- [AsyrafHussin/claude-code-statusline](https://github.com/AsyrafHussin/claude-code-statusline) - Claude Code için sade ve bilgilendirici bir durum satırı — projeyi, git…
- [bunderlog/claude-plugins](https://github.com/bunderlog/claude-plugins) - baloo içeren Claude Code eklenti pazaryeri: beceriler, değişiklikleri projenin…
- [crafts69guy/claude-statusline.nvim](https://github.com/crafts69guy/claude-statusline.nvim) - Lua içinde Claude Code durum satırı ve canlı bir Neovim oyun alanı.
- [ctfbio/claude-code-statusline](https://github.com/ctfbio/claude-code-statusline) - Profesyonel düzeyde Claude Code durum satırı: oturum süresi, ECB döviz…
- [cvrt-gmbh/claude-statusline](https://github.com/cvrt-gmbh/claude-statusline) - Claude Code için abonelik farkındalıklı durum satırı.
- [diegorv/koko.claude-statusline](https://github.com/diegorv/koko.claude-statusline) - Claude Code için zengin bir terminal durum satırı — Bun + TypeScript, çalışma…
- [emmanuelbarturen/claude-code-statusline](https://github.com/emmanuelbarturen/claude-code-statusline) - Statusline para Claude Code en español: tarea, skills, contexto con semáforo…
- [FukKwang/claude-statusline](https://github.com/FukKwang/claude-statusline) - Colorful Claude Code status line: plan limits, context, cost and tokens.
- [Gabriel-Dalton/claude-statusline-tokens](https://github.com/Gabriel-Dalton/claude-statusline-tokens) - Claude Code status line for Windows: token totals, API-rate cost, and…
- [giribboy77-arch/claude-statusline](https://github.com/giribboy77-arch/claude-statusline) - Claude Code özel durum satırı (model, efor, bağlam, önbellek, kullanım sınırı).
- [gvart/claude-config](https://github.com/gvart/claude-config) - My Claude Code setup: agent-monitor mod, skills, agents and a one-command…
- [hieuvo/claude-imgview](https://github.com/hieuvo/claude-imgview) - Görüntüleri Claude Code içinde önizleyin: resmi açmak için bir yanıtın…
- [irfanfaraaz/claude-kit](https://github.com/irfanfaraaz/claude-kit) - Claude Code kurulumum: modlar, beceriler ve eklentiler.
- [izahamyatim/claude-plugin-fizzy](https://github.com/izahamyatim/claude-plugin-fizzy) - 🚀 Gerçek zamanlı ekip görünürlüğü için Claude.
- [kernastra/claudecode](https://github.com/kernastra/claudecode) - Oluşturduğum ve paylaşmak istediğim bir Claude Code becerileri, modları ve…
- [kevinbadi/creatoros-claude-plugin](https://github.com/kevinbadi/creatoros-claude-plugin) - Creator OS for Claude Code: the connector, skills and a mod.
- [Leechlike-intangibleasset343/claude-code-statusline](https://github.com/Leechlike-intangibleasset343/claude-code-statusline) - Bağlamı, maliyeti, süreyi, git dalını, hız sınırlarını ve canlı kullanımı…
- [lucasmm96/claude-statusline](https://github.com/lucasmm96/claude-statusline) - Claude Code statusline hook — tracks token usage and context across sessions…
- [msinclair-sudo/claude-code-setup](https://github.com/msinclair-sudo/claude-code-setup) - Claude Code ortam yükleyicisi: skills, statusline, hooks, permissions ve isteğe…
- [OpenClawFarm/claude-statusline](https://github.com/OpenClawFarm/claude-statusline) - Claude Code için HUD tarzı durum satırı — ağ durumu, TPS, bağlam, kotalar ve…
- [parisgroup-ai/claude-statusline](https://github.com/parisgroup-ai/claude-statusline) - @parisgroup-ai/claude-statusline — macOS + Linux için Claude Code durum satırı.
- [primelogiclabio/claude-tools](https://github.com/primelogiclabio/claude-tools) - Claude Code ve Cowork için beceriler ve modlar — project-tracker, reference-doc…
- [robinalexandre/claude-code-kit](https://github.com/robinalexandre/claude-code-kit) - Claude Code için beceriler, modlar, kancalar ve durum satırı;
- [rotemx-10x/claude-code-statusline](https://github.com/rotemx-10x/claude-code-statusline) - Claude Code için iki satırlı bir durum satırı.
- [satoramoto/awesome-claude](https://github.com/satoramoto/awesome-claude) - Paylaşılan bir bileşen kiti, bir oyun alanı ve Storybook içeren Claude Code…
- [Shawn200212/humanizer_formal_claude](https://github.com/Shawn200212/humanizer_formal_claude) - Bilingual (中/英) interpretable model for repairing AI-drafted academic prose.
- [Sofia-D4L/claude-conf](https://github.com/Sofia-D4L/claude-conf) - Claude Code için taşınabilir yapılandırma (statusline + yükleyici).
- [SohamShirsat/claude-cockpit](https://github.com/SohamShirsat/claude-cockpit) - Claude Code için küçük bir gösterge tablosu: bağlam yüzdesi, önbellek geri…
- [speti4/claude-statusline](https://github.com/speti4/claude-statusline) - Claude Code için özel terminal durum çubuğu: model, dizin, git durumu, bağlam…
- [thaiquangquy/claude.me](https://github.com/thaiquangquy/claude.me) - Taşınabilir Claude Code yapılandırması: CLAUDE.md, ayarlar, durum satırı…
- [vibe-coding-labs/claude-code-status-skills](https://github.com/vibe-coding-labs/claude-code-status-skills) - Claude Code durum satırı: mevcut model kimliği, ana bilgisayar adı…
- [vladimir-ks/ai-agile-claude-code-statusline](https://github.com/vladimir-ks/ai-agile-claude-code-statusline) - Claude Code için gerçek zamanlı maliyet takibi ve oturum izleme durum satırı.
- [warodan/vscode-claude-code-patch](https://github.com/warodan/vscode-claude-code-patch) - Claude Code becerisi (VS Code, Windows): sohbette dosya yollarının altında…
- [ymoud/claude-code-statusline](https://github.com/ymoud/claude-code-statusline) - Klasörü, git dalını, modeli, bağlam penceresi kullanımını ve plan kullanım…
- [YoniYon00/claude-feedback-rings](https://github.com/YoniYon00/claude-feedback-rings) - Context Rot Detector 2026 - Claude Code Ajanları için Proaktif AI Bellek ve Hız…
- [zhuyansen/awesome-claude-code-hooks](https://github.com/zhuyansen/awesome-claude-code-hooks) - Claude Code kancaları, alt ajanları ve durum satırları: türe göre düzenlenmiş…
- [tronschell/statusline.sh](https://github.com/tronschell/statusline.sh) - Claude Code durum satırları için görsel oluşturucu.
- [Magnus-Gille/tokenatlas](https://github.com/Magnus-Gille/tokenatlas) - Gerçek zamanlı belirteç kullanımını ve tahmini enerji tüketimini gösteren…
- [babarot/c-c-statusline](https://github.com/babarot/c-c-statusline) - A Deno-powered status line for Claude Code CLI.
- [ishuagrawal/clawdhouse](https://github.com/ishuagrawal/clawdhouse) - Claude Code için modlar: işlev kancaları üzerine kurulu bölmeler, bantlar ve…
- [timvdhoorn/cc-my-pi](https://github.com/timvdhoorn/cc-my-pi) - Pi kodlama ajanı için Claude Code tarzı arayüz paketi — araç oluşturma…
- [ashishsk93/baton-mods](https://github.com/ashishsk93/baton-mods) - Görevleri Claude Code oturumlarınız arasında aktarın.
- [lahoramaker/mods-mcp](https://github.com/lahoramaker/mods-mcp) - Fablab.
- [Rimcat-JA/translate-ck3-mods](https://github.com/Rimcat-JA/translate-ck3-mods) - Yerel bir LLM ile CK3 modlarını çevirmek için Codex ve Claude Code becerisi.
- [sTomerG/agent-kit](https://github.com/sTomerG/agent-kit) - Claude Code için açık kaynaklı modlar ve diğer uzantılar.
- [Apparux/cc-fusion](https://github.com/Apparux/cc-fusion) - Claude Code durum satırı: CCometixLine görünümü + Claude HUD işlevselliği.
- [charlie947/mod-maker](https://github.com/charlie947/mod-maker) - Mod Maker: Claude Code.
- [Niedvin/ClauDiscobombulating](https://github.com/Niedvin/ClauDiscobombulating) - Claude Code için prompt-bar modu: kullanım sınırları, önbellek zamanlayıcısı +…

</details>

<a id="dsh-cordis"></a>

## DSH ve Cordis eklenti ekosistemleri

DeepSeek Harness ve Cordis aynı yere farklı bir yönden ulaşır: onlar için eklenti, mod mekanizmasıdır; dolayısıyla oradaki bir eklenti, buradaki bir moda denktir.

<details>
<summary>🧵 <b><a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b> · ⭐74360 · TypeScript · 👁️ observed · 0 天</summary>

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
| Yıldızlar      | **74360**  |
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
<summary>🧵 <b><a href="https://github.com/morluto/rea">morluto/rea</a></b> · ⭐103536 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Yıldızlar      | **103536** |
| Son gönderme   | 2026-10-12 |
| İlk listelenme | 2026-10-05 |

🏷 `agent-skills` · `ai-agents` · `binary-analysis` · `claude-code` · `cli` · `codex` · `cordis` · `ctf`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--rea/f46ca8b1518ae39f.png" width="100%" alt="morluto/rea screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/nexu-io/open-design">nexu-io/open-design</a></b> · ⭐100566 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Yıldızlar      | **100566** |
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
<summary>🧵 <b><a href="https://github.com/tt-a1i/archify">tt-a1i/archify</a></b> · ⭐82046 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Yıldızlar      | **82046**  |
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
<summary>🧵 <b><a href="https://github.com/esengine/DeepSeek-Reasonix">esengine/DeepSeek-Reasonix</a></b> · ⭐35768 · Go · 🔎 inferred · 0 天</summary>

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
| Yıldızlar      | **35768**  |
| Son gönderme   | 2026-10-11 |
| İlk listelenme | 2026-10-06 |

🏷 `agent` · `agent-framework` · `ai-agent` · `ai-coding` · `cli` · `coding-agent` · `deepseek` · `developer-tools`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/titanwings/distilly">titanwings/distilly</a></b> · ⭐25500 · Python · 🔎 inferred · 19 天</summary>

##### 📝 Özet

Distilly — Herhangi bir Agent veya Bot için nasıl düşündüklerini yeniden kullanılabilir Skills'lere dönüştürün. Önceden Colleague Skill（原同事 Skill）.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | Python                                                                                          |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **25500**  |
| Son gönderme   | 2026-09-22 |
| İlk listelenme | 2026-10-11 |

🏷 `agent-skills` · `agentic-ai` · `ai-agent` · `ai-agents` · `ai-assistants` · `ai-persona` · `claude-code` · `claude-skills`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/titanwings--distilly/bf54e387044cab88.png" width="100%" alt="titanwings/distilly screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Q00/ouroboros">Q00/ouroboros</a></b> · ⭐6203 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Özet

Agent OS: the agent gets smarter on its own. We just hold the line: Interview-gated, staged evaluation, budgeted evolution loop. MCP server, 14 runtimes: Claude Code, Codex CLI, Gemini CLI, OpenCode, Copilot, Kiro and more.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | Python                                                                                          |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **6203**   |
| Son gönderme   | 2026-10-11 |
| İlk listelenme | 2026-10-12 |

🏷 `agent-os` · `agentic-ai` · `ai-agent` · `ai-coding-agent` · `claude-code` · `cli` · `codex` · `coding-agent`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/q00--ouroboros/5b0b313f6f066fb8.png" width="100%" alt="Q00/ouroboros screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/q00--ouroboros/099492564830e817.gif" width="100%" alt="Q00/ouroboros animation"><br><sub>animasyonlu kayıt</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/MeteorNOX/DeepSeek-Balance-Whale-Widget">MeteorNOX/DeepSeek-Balance-Whale-Widget</a></b> · ⭐4495 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Yıldızlar      | **4495**   |
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
<summary>🧵 <b><a href="https://github.com/strukto-ai/mirage">strukto-ai/mirage</a></b> · ⭐3682 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

Dünyanın İlk AI Ajanları için Sanal Terminali

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | TypeScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **3682**   |
| Son gönderme   | 2026-10-11 |
| İlk listelenme | 2026-10-12 |

🏷 `agent-sandbox` · `agent-tools` · `ai-agents` · `bash` · `claude-code` · `dsh` · `dsh-plugin` · `fuse`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-tauri/deepseek-harness-desktop">dsh-tauri/deepseek-harness-desktop</a></b> · ⭐3088 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

DeepSeek Harness Tauri masaüstü sürümü | Yalnızca 8 MB yükleyici, sıfır ortam kurulumu, önceden ayarlanmış eklentiler, Windows / macOS / Linux.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | TypeScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **3088**   |
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
<summary>🧵 <b><a href="https://github.com/xmanrui/dsh-im">xmanrui/dsh-im</a></b> · ⭐1849 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

QR kodu veya bot kimlik bilgileriyle IM botlarını DeepSeek Harness'e bağlayın (Feishu, WeChat, DingTalk, WeCom, QQ, Slack, Telegram, Discord ve WhatsApp desteklenir). IM botlarını QR kodu veya kimlik bilgileri aracılığıyla DeepSeek Harness'e bağlayın (9 kanal).

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | JavaScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **1849**   |
| Son gönderme   | 2026-10-11 |
| İlk listelenme | 2026-10-12 |

🏷 `ai-agents` · `chatbot` · `cordis` · `deepseek` · `deepseek-harness` · `dingtalk-bot` · `discord-bot` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xmanrui--dsh-im/cba81787088f67af.jpg" width="100%" alt="xmanrui/dsh-im screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/kenryu42/cc-safety-net">kenryu42/cc-safety-net</a></b> · ⭐1591 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

AI kodlama aracıları için yürütme öncesi koruma. Bir araç çağrısı çalıştırılmadan önce yıkıcı Git ve dosya sistemi komutlarını ve hassas dosyalara erişmeye yönelik yaygın girişimleri engeller. Amp Code, Antigravity CLI, Claude Code, Codex, Cursor, DeepSeek Harness, Devin CLI, GitHub Copilot CLI, Grok Build, Hermes Agent, Kimi Code, OpenClaw, OpenCode ve Pi'yi destekler.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | TypeScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **1591**   |
| Son gönderme   | 2026-10-11 |
| İlk listelenme | 2026-10-11 |

🏷 `ai-agents` · `ai-safety` · `antigravity` · `claude` · `claude-code` · `claude-code-plugin` · `cli` · `codex`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/anywhere-labs/Agents-Anywhere">anywhere-labs/Agents-Anywhere</a></b> · ⭐1579 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

Cihazlar arası açık kaynaklı Agent çalışma alanı

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | TypeScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **1579**   |
| Son gönderme   | 2026-10-11 |
| İlk listelenme | 2026-10-12 |

🏷 `acp` · `agentclientprotocol` · `agents` · `claudecode` · `codex` · `codex-app` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/anywhere-labs/Agents-Anywhere/main/docs/images/readme-hero-zh.webp" width="100%" alt="anywhere-labs/Agents-Anywhere screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

<sub>Yeniden dağıtıma izin veren bir lisans belirtilmediği için varlığa upstream deposundan doğrudan bağlantı veriliyor.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/AdamPlatin123/dsh-plugin-radar">AdamPlatin123/dsh-plugin-radar</a></b> · ⭐1465 · Python · 🔎 inferred · 0 天</summary>

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
| Yıldızlar      | **1465**   |
| Son gönderme   | 2026-10-11 |
| İlk listelenme | 2026-10-12 |

🏷 `agent-plugins` · `continuous-validation` · `deepseek-harness` · `dsh` · `dsh-plugin` · `ecosystem-radar` · `plugin-registry`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/adamplatin123--dsh-plugin-radar/fb6ad7eb8891212c.jpg" width="100%" alt="AdamPlatin123/dsh-plugin-radar screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/EthanYoQ/AI-Novel-Writer">EthanYoQ/AI-Novel-Writer</a></b> · ⭐1410 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Yıldızlar      | **1410**   |
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
<summary>🧵 <b><a href="https://github.com/vshulcz/deja-vu">vshulcz/deja-vu</a></b> · ⭐1174 · Go · 🔎 inferred · 0 天</summary>

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
| Yıldızlar      | **1174**   |
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
<summary>🧵 <b><a href="https://github.com/myYangyunfan/dsh_desktop">myYangyunfan/dsh_desktop</a></b> · ⭐705 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Yıldızlar      | **705**    |
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
<summary>🧵 <b><a href="https://github.com/vibeinging/dsh-desktop">vibeinging/dsh-desktop</a></b> · ⭐592 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

DeepSeek Harness Masaüstü Uygulaması: DSH Oturumları, projeler, dosyalar, web araştırması, eklentiler ve Office ürünleri için yerel AI masaüstü çalışma alanı.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | JavaScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **592**    |
| Son gönderme   | 2026-10-11 |
| İlk listelenme | 2026-10-12 |

🏷 `agentic-workflows` · `ai-agent` · `ai-workbench` · `data-analysis` · `deepseek-harness` · `desktop-app` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vibeinging--dsh-desktop/ccbf15d3a2c42437.png" width="100%" alt="vibeinging/dsh-desktop screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Ikalus1988/MisakaNet">Ikalus1988/MisakaNet</a></b> · ⭐526 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Özet

📚 Yapay Zekâ Ajanlarının doğrulanmış hata ayıklama deneyimlerini eşzamansız olarak paylaşması ve araması için sıfır bağımlılıklı, git destekli mikro ders kütüphanesi. | https://misakanet.org

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | Python                                                                                          |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **526**    |
| Son gönderme   | 2026-10-11 |
| İlk listelenme | 2026-10-12 |

🏷 `action` · `agents` · `cloudflare-workers` · `codex` · `cordis-plugin` · `d1` · `deepseek-harness` · `deepseek-harness-plugin`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ikalus1988--misakanet/f6853900d49aba17.jpg" width="100%" alt="Ikalus1988/MisakaNet screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/DDDMUC/dsh-free-search">DDDMUC/dsh-free-search</a></b> · ⭐369 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

DeepSeek Harness için ücretsiz web arama sağlayıcısı - DuckDuckGo arka ucu, API anahtarı gerekmez

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | JavaScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **369**    |
| Son gönderme   | 2026-10-11 |
| İlk listelenme | 2026-10-12 |

🏷 `bing` · `deepseek-harness` · `dsh` · `dsh-plugin` · `duckduckgo` · `web-search`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dddmuc--dsh-free-search/ec034e713544ead5.png" width="100%" alt="DDDMUC/dsh-free-search screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xing-shuyin/pi-web-ui">xing-shuyin/pi-web-ui</a></b> · ⭐285 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Yıldızlar      | **285**    |
| Son gönderme   | 2026-10-11 |
| İlk listelenme | 2026-10-12 |

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
<summary>🧵 <b><a href="https://github.com/luobosibing2/dsh-jev-plugin">luobosibing2/dsh-jev-plugin</a></b> · ⭐204 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Yıldızlar      | **204**    |
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
<summary>🧵 <b><a href="https://github.com/xiajiajun516/dsh-config-manager">xiajiajun516/dsh-config-manager</a></b> · ⭐176 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

DeepSeek Harness (DSH) yedekleme ve geri yükleme eklentisi — DSH yapılandırmanızın, eklentilerinizin, MCP sunucularınızın, becerilerinizin ve çalışma alanınızın tamamını dışa aktarın, içe aktarın, taşıyın ve eşitleyin. Başka bir makineye tek tıklamayla geçiş.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | TypeScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **176**    |
| Son gönderme   | 2026-10-11 |
| İlk listelenme | 2026-10-12 |

🏷 `backup` · `cli` · `config-manager` · `configuration` · `cordis` · `deepseek` · `deepseek-harness` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xiajiajun516--dsh-config-manager/52a2f3587f8e40b4.png" width="100%" alt="xiajiajun516/dsh-config-manager screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/KelaoHu/dsh-lowtide">KelaoHu/dsh-lowtide</a></b> · ⭐172 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Yıldızlar      | **172**    |
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
<summary>🧵 <b><a href="https://github.com/morluto/flameox">morluto/flameox</a></b> · ⭐145 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Özet

Agent'ların uygulama ve yerel koddaki, GPU çekirdeklerindeki ve çıkarım yığınlarındaki darboğazları izlemesine, profillemesine ve ortadan kaldırmasına yardımcı olan çalışma zamanı kanıtları.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | Python                                                                                          |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **145**    |
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
<summary>🧵 <b><a href="https://github.com/2BingLing/dsh-market">2BingLing/dsh-market</a></b> · ⭐139 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

DeepSeek Harness 插件市场 · 持续收录 6000+ DSH 插件：中文搜索 + 实用五维评分 + 一键安装。Web 版与 DSH 侧边栏插件双形态。Plugin marketplace for DeepSeek Harness: 6000+ plugins, Chinese search, 5-dim scoring, one-click install.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | TypeScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **139**    |
| Son gönderme   | 2026-10-11 |
| İlk listelenme | 2026-10-12 |

🏷 `deepseek-harness` · `deepseek-harness-plugin` · `deepseek-harness-plugins` · `dsh` · `dsh-bundle` · `dsh-market` · `dsh-plugin` · `dsh-plugins`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/2BingLing/dsh-market/master/assets/readme/banner.webp" width="100%" alt="2BingLing/dsh-market screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

<sub>Yeniden dağıtıma izin veren bir lisans belirtilmediği için varlığa upstream deposundan doğrudan bağlantı veriliyor.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/FeatherHunter/dsh-mattpocock-skills-deck">FeatherHunter/dsh-mattpocock-skills-deck</a></b> · ⭐135 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

Kurulumla birlikte mattpocock/skills v1.3.1'in 27 mühendislik ve verimlilik becerisi gelir; becerileri manuel olarak yüklemeniz gerekmez. 40 milyar token ile oluşturulan bu eklenti, özgün becerilerin üzerinde 10 kat geliştirme verimliliği sunar ve yeni başlayanların bu beceri paketini daha hızlı öğrenmesine yardımcı olur. GitHub issue'ları tam olarak desteklenir; Markdown önizleme sürümündedir; GitLab şu anda desteklenmemektedir. Kullanımınız ve desteğiniz için teşekkürler 💗

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | JavaScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **135**    |
| Son gönderme   | 2026-10-11 |
| İlk listelenme | 2026-10-12 |

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

DeepSeek Harness (DSH) için uzaktan çalışma yardımcısı: SSH'ye (anahtar veya parola ile) bağlanın, uzak bir çalışma alanı seçin, rw_* araçlarıyla çalışın ve bunu gerçek bir yerel DSH çalışma alanına SFTP ile yansıtın.

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
| İlk listelenme | 2026-10-12 |

🏷 `deepseek-harness` · `dsh` · `dsh-plugin` · `remote` · `sftp` · `ssh` · `tunnel` · `workspace`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/flymysql--dsh-remote/714d273f27c6d75b.png" width="100%" alt="flymysql/dsh-remote screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Nwflower/dsh-claude-style">Nwflower/dsh-claude-style</a></b> · ⭐133 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Yıldızlar      | **133**    |
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
<summary>🧵 <b><a href="https://github.com/WestFox-AwA/dsh-prompt-optimizer">WestFox-AwA/dsh-prompt-optimizer</a></b> · ⭐113 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

DSH eklentisi · Enjeksiyon tabanlı optimizer 0.8 (ana sürüm): Siz her zamanki gibi konuşun; o, mesajınızı gönderdikten ve AI almadan önce “bu turda gerçekte ne isteniyor” sorusunu netleştirir, ardından bu anlayışı çalışan AI'ya (bağlam enjeksiyonu) aktarır — orijinal ifadeyi yeniden yazmaz, her maddeyi kelimesi kelimesine dayanakla sunar. Kontrol arayüzü (seviye/izin/model/bağlam/salt okunur araçlar), engelleme katmanı (düşünce katmanı + çıktı katmanı) ve gerçek token kullanımı içerir. Çoğu modelin, özellikle DeepSeek-V4.1-Flash'ın performans kararlılığını belirgin biçimde artırabilir.

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
<summary>🧵 <b><a href="https://github.com/Noob-stupid/dsh-plugin-gating-hub">Noob-stupid/dsh-plugin-gating-hub</a></b> · ⭐100 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

DSH eklentisi - çerçeve yükseltme güvenliği ve eklenti geçitleme: sözleşme ön denetimi, geri alma noktası, başarısızlıkta otomatik geri alma, kanıta dayalı otomatik devre dışı bırakma; ayrıca çok kaynaklı eklenti pazarı. Resmî değildir. | DSH eklentisi: çerçeve yükseltme güvenliği + eklenti geçitleme — yükseltme öncesi sözleşme ön denetimi, geri alma noktası, başarısızlıkta otomatik geri alma, yalnızca doğrulanmış kanıt varsa otomatik devre dışı bırakma; ayrıca çok kaynaklı eklenti pazarı. Resmî olmayan topluluk projesi.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | JavaScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **100**    |
| Son gönderme   | 2026-10-11 |
| İlk listelenme | 2026-10-12 |

🏷 `ai-empower` · `cli` · `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-plugins` · `framework-upgrade` · `marketplace`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/noob-stupid--dsh-plugin-gating-hub/0b18270cf916dc1c.png" width="100%" alt="Noob-stupid/dsh-plugin-gating-hub screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ZASENJC/dsh-plugins-store">ZASENJC/dsh-plugins-store</a></b> · ⭐69 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

DeepSeek-Harness topluluk eklentilerini otomatik olarak sınıflandıran, derleyen ve doğrulayan pazar. DeepSeek-Harness topluluk eklentileri pazarı için otomatik sınıflandırma, derleme ve doğrulama.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | TypeScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **69**     |
| Son gönderme   | 2026-10-11 |
| İlk listelenme | 2026-10-12 |

🏷 `agent-tools` · `awesome-list` · `community-project` · `deepseek-harness` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zasenjc--dsh-plugins-store/e83b24d43eca5912.png" width="100%" alt="ZASENJC/dsh-plugins-store screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary><b>Bu kategoride daha fazlası</b> <sub>· 72</sub></summary>

- [hashgraph-online/awesome-ai-plugins](https://github.com/hashgraph-online/awesome-ai-plugins) - Claude Code, OpenAI Codex / ChatGPT, Gemini, Antigravity, Pi / Oh My Pi, Grok…
- [FishBottle7/opencode2dsh](https://github.com/FishBottle7/opencode2dsh) - DSH eklentisi — DeepSeek Harness (DSH) için ücretsiz OpenCode Zen modelleri.
- [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) - DSH eklenti pazarı / DSH Plugin Marketplace: DeepSeek Harness Web GUI içinde…
- [arcships/rutis](https://github.com/arcships/rutis) - Kendi kendini yineleyen yazılımlar için bir eklenti çalışma zamanı — ajanların…
- [like-study1/Oh-My-DSH](https://github.com/like-study1/Oh-My-DSH) - 🐳 DeepSeek Harness eklenti topluluğu — dsh-plugin ekosistemini otomatik…
- [adamkhalile/luau-docs-oracle](https://github.com/adamkhalile/luau-docs-oracle) - En İyi Roblox Luau Hata Denetleyicisi ve API Doğrulayıcı 2026 DevForum MCP Aracı.
- [kukucaiCndy/Corum-Harness](https://github.com/kukucaiCndy/Corum-Harness) - Deepseek-Harness çekirdek altyapısı temel alınarak oluşturulmuş masaüstü Agent.
- [whyihaveyou/dsh-suite](https://github.com/whyihaveyou/dsh-suite) - Yaşayan DeepSeek Harness eklenti dizini — saatlik yenilenir, uyumluluk testleri…
- [1475505/miliastra-beyond-simulator](https://github.com/1475505/miliastra-beyond-simulator) - Bin Yıldız Sandbox simülatörü: Lua tarafından desteklenen 2D harici tuhaf diyar…
- [PolinniZhong/dsh-knit](https://github.com/PolinniZhong/dsh-knit) - AI Coding Agent.
- [kejixiaoliang/awesome-dsh-plugins](https://github.com/kejixiaoliang/awesome-dsh-plugins) - DeepSeek Harness (DSH) eklentileri seçkisi — 14 kategoride 280.
- [GZX2211/dsh-Visual-Workflow](https://github.com/GZX2211/dsh-Visual-Workflow) - Görsel Agent orkestrasyon platformu｜DeepSeek Harness temelinde;
- [universe-st/dsh-game-material-master](https://github.com/universe-st/dsh-game-material-master) - dsh oyun varlıkları ustası eklentisi. seedream görüntü oluşturma modeli ve…
- [Links2008/DeepSeek-Harness-Desktop](https://github.com/Links2008/DeepSeek-Harness-Desktop) - Windows 桌面版 DeepSeek Harness 发行版，支持原生通知、流畅的窗口控制、捆绑运行时和自动更新。追踪官方主分支.
- [HOWILLMAKEIT/dsh-model-context-catalog](https://github.com/HOWILLMAKEIT/dsh-model-context-catalog) - DeepSeek Harness eklentisi: model bağlam pencerelerini tek tıklamayla…
- [NekroAI/nekro-nxt](https://github.com/NekroAI/nekro-nxt) - NekroNXT: DeepSeek Harness (DSH) tabanlı çok platformlu grup sohbeti aracısı…
- [Lixiaoyiao/deepseek-harness-action](https://github.com/Lixiaoyiao/deepseek-harness-action) - Community GitHub Action for DeepSeek Harness — AI Code Review · CI Diagnosis ·…
- [wingsky-1/dsh-plugin-hub](https://github.com/wingsky-1/dsh-plugin-hub) - DSH (DeepSeek Harness) web GUI eklenti koleksiyonu — görev bildirimleri…
- [BotHarness/DeepSeekBot](https://github.com/BotHarness/DeepSeekBot) - DeepSeek Harness üzerine kurulmuş açık kaynaklı GrokBot alternatifi.
- [zp-home/dsh-recommend](https://github.com/zp-home/dsh-recommend) - DSH eklenti ekosistemi için şeffaf sıralama ve öneriler: dsh-plugin konusunu…
- [awesome-deepseekharness/awesome-deepseek-harness](https://github.com/awesome-deepseekharness/awesome-deepseek-harness) - Topluluk tarafından seçilmiş DeepSeek Harness (dsh) eklentileri, araçları…
- [hyqhyq3/dsh-mcp-manager](https://github.com/hyqhyq3/dsh-mcp-manager) - DeepSeek Harness için MCP sunucu yöneticisi eklentisi: Ayarlar → MCP sayfası…
- [harrylabsj/kiwi](https://github.com/harrylabsj/kiwi) - A2A ticaret pazarlığı çalışma zamanı + DeepSeek Harness (dsh) eklentisi.
- [Imzl-zl/dsh-toolbox-ui](https://github.com/Imzl-zl/dsh-toolbox-ui) - DeepSeek Harness Web için araç kutusu paneli: MCP yöneticisi.
- [Y1X1n/dsh-prompt-optimizer](https://github.com/Y1X1n/dsh-prompt-optimizer) - DeepSeek Harness eklentisi · Gönderme çubuğunda istem taslağını tek tıklamayla…
- [YELEBAI/dsh-plugin-marketplace](https://github.com/YELEBAI/dsh-plugin-marketplace) - DeepSeek Harness için doğrulanmış eklenti pazarı ve otonom kayıt defteri.
- [liustack/pptwise](https://github.com/liustack/pptwise) - HTML değil, gerçek bir PowerPoint. Yapay zekânıza nelerin ele alınacağını…
- [Roarpeng/GraphFlow](https://github.com/Roarpeng/GraphFlow) - Kodlama aracıları için yerel öncelikli kod bilgi grafiği ve bağlam harness.
- [dshworks/awesome-dsh-plugins](https://github.com/dshworks/awesome-dsh-plugins) - DeepSeek Harness (dsh) eklentileri, paketleri ve becerileri için spam filtreli…
- [billLiao/awesome-dsh-plugin](https://github.com/billLiao/awesome-dsh-plugin) - A curated list of plugins for DeepSeek Harness (dsh) — 精选 DeepSeek Harness 插件列表.
- [AmethystLuna/embedded-workbench](https://github.com/AmethystLuna/embedded-workbench) - Gömülü C/C++ AI mühendislik eklentisi — ürün yazılımı becerileri.
- [Ianzhyh/workbuddy-to-dsh](https://github.com/Ianzhyh/workbuddy-to-dsh) - Yerel WorkBuddy masaüstü uygulamasında oturum açmış modelleri.
- [muyuanjin/dsh-ptc-plus](https://github.com/muyuanjin/dsh-ptc-plus) - A session-bound agent-native REPL for DeepSeek Harness PTC mode.
- [MichaelShii/dsh-plugin-teamflow](https://github.com/MichaelShii/dsh-plugin-teamflow) - dsh plugin teamflow.
- [MicroMilo/upstream-radar](https://github.com/MicroMilo/upstream-radar) - DeepSeek Harness eklentileri için her zaman açık uyumluluk testi: kesin…
- [falling-ts/dsh-force-compact](https://github.com/falling-ts/dsh-force-compact) - Yerel öncelikli agent.
- [GooDAnDReaDY/dsh-subscriptions](https://github.com/GooDAnDReaDY/dsh-subscriptions) - DeepSeek Harness için OAuth aboneliği LLM sağlayıcıları: ChatGPT Codex, Claude…
- [yoza10635/dsh-argp](https://github.com/yoza10635/dsh-argp) - DeepSeek Harness (dsh) için korumalı bağlam sıkıştırma: LLM önerir…
- [vecnode/vncode](https://github.com/vecnode/vncode) - vncode 🤖 Agent-Human IDE ⌨️ Web ve Masaüstü sürümleri;
- [bonerush/dsh-obsidian-mem](https://github.com/bonerush/dsh-obsidian-mem) - Proje belgelerini ve uzun süreli belleği özel bir Obsidian kasasında düz…
- [cccakeee/awesome-dsh-plugins](https://github.com/cccakeee/awesome-dsh-plugins) - DeepSeek Harness (DSH) eklentileri için seçilmiş, kanıta dayalı dizin…
- [dsh-pub/dsh-pub](https://github.com/dsh-pub/dsh-pub) - The bilingual, source-backed registry and installer for the DeepSeek Harness…
- [Icather/dsh-clean-desktop-shell](https://github.com/Icather/dsh-clean-desktop-shell) - DSH için saf masaüstü kabuğu: sıradan bir uygulama gibi çift tıklamayla tek…
- [unStone/dsh-xray](https://github.com/unStone/dsh-xray) - DeepSeek Harness eklentileri için X ışını: beyan edilen yetenekler ve gerçek…
- [YangShen-SWE/dsh-plugin-simple-pet](https://github.com/YangShen-SWE/dsh-plugin-simple-pet) - DeepSeek faturalandırmalı Windows masaüstü evcil hayvanı, Codex abonelik…
- [chnjames/dsh-plugin-market](https://github.com/chnjames/dsh-plugin-market) - DSH eklenti pazarı — DeepSeek Harness ayarlarından topluluk eklentilerini tek…
- [cyanseek/dsh-landscape](https://github.com/cyanseek/dsh-landscape) - Agent-first DeepSeek Harness plugin intelligence: verify existing plugins…
- [KannaKuron/dsh-ide-git](https://github.com/KannaKuron/dsh-ide-git) - DSH eklentisi: yerel bir dsh-better-sidebar sekmesi olarak IDE düzeyinde Git…
- [ywsldxk/dsh-plugin-stars](https://github.com/ywsldxk/dsh-plugin-stars) - DeepSeek Harness (DSH) eklenti liderlik tablosu ve dizini｜DeepSeek Harness…
- [cherrchen/dsh-plugin-multi-root-workspace](https://github.com/cherrchen/dsh-plugin-multi-root-workspace) - Çok klasörlü çalışma alanı: DSH (DeepSeek Harness) aracısının yalnızca ana…
- [majiayu000/dsh-plugin-registry](https://github.com/majiayu000/dsh-plugin-registry) - Seçilmiş listelere ve bildirim dosyasıyla doğrulanmış GitHub keşfine sahip…
- [PerryLink/dsh-plugin-doctor](https://github.com/PerryLink/dsh-plugin-doctor) - DeepSeek Harness (dsh) eklentileri için sıfır bağımlılıklı doğrulama standardı…
- [TheYoungChen/dsh-plugin-market](https://github.com/TheYoungChen/dsh-plugin-market) - DeepSeek Harness eklenti pazarı - dsh-plugin konusu eklentilerine göz atın…
- [viztor/dsh-opencode-patch](https://github.com/viztor/dsh-opencode-patch) - DeepSeek Harness üzerinde OpenCode — OpenCode Zen + Go ücretsiz katman…
- [AI-Scarlett/DSH-Store](https://github.com/AI-Scarlett/DSH-Store) - DSH STORE — DeepSeek Harness için üçüncü taraf eklenti pazaryeri ve korumalı…
- [Atelyx/Atelyx](https://github.com/Atelyx/Atelyx) - Atelyx, insan odaklı ve genişletilebilir bir masaüstü çalışma alanıdır…
- [dsh-cc/dsh-cc](https://github.com/dsh-cc/dsh-cc) - DeepSeek Harness için her şey dahil bir kodlama agent.
- [GooDAnDReaDY/dsh-live-canvas](https://github.com/GooDAnDReaDY/dsh-live-canvas) - Etkileşimli Görsel Ön Yüz Stüdyosu, Retool Tarzı CRUD Motoru, Zaman Yolculuklu…
- [ItQianChen/dsh-github-flow](https://github.com/ItQianChen/dsh-github-flow) - DeepSeek Harness Agent.
- [lmzhen/dsh-evolution](https://github.com/lmzhen/dsh-evolution) - Hermes-inspired agent self-evolution plugin family, purpose-built for DeepSeek…
- [sakanamaru/dsh-minato](https://github.com/sakanamaru/dsh-minato) - dsh-minato — DeepSeek Harness (dsh) için topluluk sürümü yerel dağıtım ve…
- [Seelerc/dsh-plugin-delete-archived](https://github.com/Seelerc/dsh-plugin-delete-archived) - Arşivlenmiş DeepSeek Harness oturumlarını, disk üzerindeki geçmişleri ve günlük…
- [tianyagk/dsh-tradewatcher](https://github.com/tianyagk/dsh-tradewatcher) - DeepSeek Harness (DSH) web eklentisi: market-dashboard kenar çubuğu sekmesi…
- [argszero/cordis-plugin-empty-response-retry](https://github.com/argszero/cordis-plugin-empty-response-retry) - Bir atıf içermeyen boş model denemesini yeniden denenebilir hâle getirir;
- [argszero/cordis-plugin-goal-progress-guard](https://github.com/argszero/cordis-plugin-goal-progress-guard) - dsh otonom hedef turları için ilerleme değerlendirmesi: arka plan işleri…
- [argszero/cordis-plugin-length-stop-overflow](https://github.com/argszero/cordis-plugin-length-stop-overflow) - dsh plugin: turn a truncated length stop into the CONTEXT_WINDOW_EXCEEDED…
- [eovidiu/cordis-ios](https://github.com/eovidiu/cordis-ios) - Kendi temizliklerini yapan eklentiler: iOS ve macOS için cordis eklenti…
- [Magica-Chen/dsh-preset-codex-claude](https://github.com/Magica-Chen/dsh-preset-codex-claude) - DeepSeek Harness ajan ön ayarı: Codex ve Claude Code, her biri salt okunur ve…
- [validation-engineering/cordis-verus](https://github.com/validation-engineering/cordis-verus) - Verus tarafından doğrulanmış bir lifecycle kernel ve Cordis compatibility…
- [helloHupc/dsh-plugin-hub](https://github.com/helloHupc/dsh-plugin-hub) - DSH eklenti toplama sitesi: DeepSeek Harness eklentilerini web genelinde toplu…
- [HaydenSmith1121/dsh-plugins](https://github.com/HaydenSmith1121/dsh-plugins) - DeepSeek Harness (dsh) eklenti pazarı — katalog.
- [SCP-008-1/dshop](https://github.com/SCP-008-1/dshop) - dsh eklenti mağazası - GitHub tabanlı topic:dsh-plugin ile otomatik keşif ve…

</details>

<a id="writing"></a>

## Yazılar, tartışmalar ve videolar

Mod yeteneği hakkında yazılar, tartışmalar ve videolar.

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925102">Claude Code Mods</a></b> · ⭐6 · 👁️ observed · 10 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49999983">A Claude Code mod plays MIDI music when it works</a></b> · ⭐3 · 👁️ observed · 4 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925800">Claude Code Mods: plugins may now modify deeper behavior</a></b> · ⭐3 · 👁️ observed · 10 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49926243">Getting started with Claude Code mods</a></b> · ⭐3 · 👁️ observed · 10 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49945600">Show HN: Terminal Gym – a Claude mod that makes you do pushups between prompts</a></b> · ⭐3 · 👁️ observed · 8 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49971594">Terminal Steps: A Claude mod for a daily step goal, synced from Apple Health</a></b> · ⭐3 · 👁️ observed · 6 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50024345">Agent-config&amp;Claude Code mods</a></b> · ⭐2 · 👁️ observed · 2 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49940121">Getting started with Claude Code mods</a></b> · ⭐2 · 👁️ observed · 9 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49927599">Pi-autoresearch ported to Claude Code 1:1 using the new mods API</a></b> · ⭐2 · 👁️ observed · 10 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49934165">Show HN: What&#x27;s Agent Doing – a Claude Code UI mod that explains each step</a></b> · ⭐2 · 👁️ observed · 9 天</summary>

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
| TypeScript | 370      | `anthropics/claude-code`, `anthropics/claude-code-action`, `hamzafer/claude-code-mods`                             |
| JavaScript | 86       | `karanb192/awesome-claude-code-mods`, `karanb192/claude-code-mods`, `ucsandman/claude-harness`                     |
| Python     | 39       | `anthropics/claude-agent-sdk-python`, `anthropics/claude-code-security-review`, `alexgreensh/token-optimizer`      |
| Shell      | 25       | `anthropics/claude-agent-sdk-typescript`, `0xDarkMatter/claude-mods`, `BeLazy167/claude-mods-skill`                |
| HTML       | 16       | `HeyCubit/effortless`, `awss1i/assay`, `darrell-tw/darrelltw-mods`                                                 |
| Rust       | 6        | `persiyanov/herdr-reviewr`, `JairoTorregrosa/claude-statusline`, `OpenClawFarm/claude-statusline`                  |
| Go         | 5        | `backstabslash/goccc`, `kylesnowschwartz/tail-claude-hud`, `bunderlog/claude-plugins`                              |
| PowerShell | 3        | `GoSlowPoke168/claude-statusline`, `Gabriel-Dalton/claude-statusline-tokens`, `YangShen-SWE/dsh-plugin-simple-pet` |
| C          | 1        | `reporails/arcade`                                                                                                 |
| C#         | 1        | `sakanamaru/dsh-minato`                                                                                            |
| Lua        | 1        | `crafts69guy/claude-statusline.nvim`                                                                               |
| MDX        | 1        | `jkf87/mod-guide`                                                                                                  |
| Swift      | 1        | `eovidiu/cordis-ios`                                                                                               |

<sub>Yalnızca dil belirten girdiler sayılır. Belgeler ve tartışma girdileri bu tablonun dışında tutulur.</sub>

## Katkıda bulunma

Düzeltmeler memnuniyetle karşılanır ve bu listeyi iyileştirmenin en hızlı yoludur. Bir girdi yanlış sınıflandırılmış veya yanlış derecelendirilmişse ya da bir proje ad çakışması nedeniyle yanlışlıkla dışlanmışsa bir issue veya pull request açın — otomatik filtrelerin en çok yanılma ihtimali olan kategori sonuncusudur.

---

<sub>Independent community project. Not affiliated with, endorsed by, or reviewed by Anthropic. Claude Code, Claude and Anthropic are trademarks of Anthropic. Product behaviour changes without notice; verify anything load-bearing against the official documentation. Assets remain the property of their upstream projects and are reproduced only where a licence permits.</sub>

<sub>Son güncelleme · 2026-10-12T08:14:15+08:00</sub>
