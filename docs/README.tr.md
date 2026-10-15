<p align="center">
  <img src="../assets/readme/hero.png" width="100%" alt="Harika Claude Modları">
</p>

<h1 align="center">Harika Claude Modları</h1>

<p align="center"><b>Claude Code modlarının ve değiştirdikleri daha derin davranışların kanıt derecelendirmeli dizini.</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-502-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="../LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
  <a href="https://wh000wh000.github.io/awesome-claude-mods/"><img src="https://img.shields.io/badge/site-searchable-1f6feb" alt="site"></a>
</p>

<p align="center"><sub><a href="../README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.pt-BR.md">Português</a> · <a href="README.ru.md">Русский</a> · <a href="README.it.md">Italiano</a> · <a href="README.ar.md">العربية</a> · <a href="README.hi.md">हिन्दी</a> · <b>Türkçe</b> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.pl.md">Polski</a> · <a href="README.nl.md">Nederlands</a> · <a href="README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **Güncel dizin** · Son senkronizasyon: `2026-10-16T03:45:33+08:00` (UTC+8)
> · Kayıtlar: **502** · Son güncellemede eklenenler: **0** · Uygulama dilleri: **9**

<sub>Aşağıdaki her kayıt otomatik olarak toplandı, filtrelendi ve yeniden kontrol edildi. Burada ücretli yerleştirme yoktur.</sub>

<a id="featured"></a>

## Anın seçkileri

<sub>Her kategoriden bir giriş; kanıt derecesine ve yıldızlara göre sıralanır, her güncellemede yeniden hesaplanır. Bu bir sıralamadır, onay değildir; her seçki aşağıdaki tam kartına bağlantı verir. Ekran görüntüsü veya kayıt yayınlayan projeler tercih edilir, böylece şerit görsel kalır.</sub>

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
<sub>Hayalet belirteçleri bulun. Onları düzeltin. Sıkıştırmadan sağ çıkın. Bağlam kalitesinin bozulmasından kaçının.</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo">
<b>🧵 <a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b>
<sub>⭐74991 · TypeScript · 👁️ observed</sub>
<sub>🌊 Özgün agent harness. Akıllı çok oyunculu sürüleri dağıtın, otonom iş akışlarını koordine edin ve konuşmaya dayalı AI sistemleri oluşturun. Uyarlanabilir bellek,…</sub>
</td>
<td width="50%" valign="top">
<b>📰 <a href="https://news.ycombinator.com/item?id=50099375">Claude Code Desktop Vulnerability: Preview Pane Data Exfiltration</a></b>
<sub>⭐15 · 👁️ observed</sub>
</td>
</tr>
</table>

## İçerik

- [Claude Code modu nedir](#claude-code-modu-nedir)
- [Kayıtlar nasıl derecelendiriliyor](#kayıtlar-nasıl-derecelendiriliyor)
- [Resmî: Anthropic'ın kendi depoları ve sürüm notları](#resmî-anthropicın-kendi-depoları-ve-sürüm-notları) — **17**
- [Modlar: mod yeteneği kullanılarak oluşturulanlar](#modlar-mod-yeteneği-kullanılarak-oluşturulanlar) — **382**
- [DSH ve Cordis eklenti ekosistemleri](#dsh-ve-cordis-eklenti-ekosistemleri) — **95**
- [Yazılar, tartışmalar ve videolar](#yazılar-tartışmalar-ve-videolar) — **8**
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
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></b> · ⭐151049 · TypeScript · ✅ official · 0 天</summary>

##### 📝 Özet

Claude Code terminalinizde çalışan, kod tabanınızı anlayan ve rutin görevleri yerine getirerek, karmaşık kodu açıklayarak ve git iş akışlarını doğal dil komutlarıyla yöneterek daha hızlı kod yazmanıza yardımcı olan aracı bir kodlama aracıdır.

<sub>🔧 Kodda kullanıldığı bulundu: `feed.xml`, `mods/diff/README.md`, `mods/diff/hooks/host/host.ts`</sub>

##### 📌 Temel bilgiler

| Alan     | Değer                                                      |
| -------- | ---------------------------------------------------------- |
| Kategori | `Resmî: Anthropic&#x27;ın kendi depoları ve sürüm notları` |
| Kanıt    | `doğrudan Anthropic tarafından yayımlandı`                 |
| Dil      | TypeScript                                                 |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **151049** |
| Son gönderme   | 2026-10-15 |
| İlk listelenme | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b> · ⭐9524 · TypeScript · ✅ official · 0 天</summary>

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
| Yıldızlar      | **9524**   |
| Son gönderme   | 2026-10-15 |
| İlk listelenme | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-python">anthropics/claude-agent-sdk-python</a></b> · ⭐8286 · Python · ✅ official · 0 天</summary>

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
| Yıldızlar      | **8286**   |
| Son gönderme   | 2026-10-15 |
| İlk listelenme | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-security-review">anthropics/claude-code-security-review</a></b> · ⭐6390 · Python · ✅ official · 246 天</summary>

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
| Yıldızlar      | **6390**   |
| Son gönderme   | 2026-02-11 |
| İlk listelenme | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-typescript">anthropics/claude-agent-sdk-typescript</a></b> · ⭐1813 · Shell · ✅ official · 0 天</summary>

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
| Yıldızlar      | **1813**   |
| Son gönderme   | 2026-10-15 |
| İlk listelenme | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/model-cards">anthropics/model-cards</a></b> · ⭐25 · ✅ official · 314 天</summary>

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
<summary><b>Bu kategoride daha fazlası</b> <sub>· 5</sub></summary>

- [Claude Code 2.1.295 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Modlar için `$.ui.notify` eklendi: kendi bildirim ayarınız üzerinden yerel bir…
- [Claude Code 2.1.296 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - `UserPromptSubmit` hook&#x27;u veya modun `prompt.submit` hook&#x27;u sırasında Esc ya da…
- [Claude Code 2.1.299 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Added `$.prompt.media` so a `prompt.submit` hook of a mod installed by managed…
- [Claude Code 2.1.300 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Added `virtualText` to a mod.
- [Claude Code 2.1.301 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Added `rows` to a mod.

</details>

<a id="mods"></a>

## Modlar: mod yeteneği kullanılarak oluşturulanlar

Buradaki her giriş, Claude Code'un 2.1.287 sürümünde kazandığı yeteneğin kullanıldığına dair kanıt gösterir: `ui.render` üzerinden çizim yapar, bir bölmeye, banda veya karta sahip olur, `$.ui.selection()` okur, `agent.spawn` ile ekip arkadaşları oluşturur ya da açıkça mod olduğunu belirtir.

<details>
<summary>🧩 <b><a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b> · ⭐2568 · Python · 👁️ observed · 0 天</summary>

##### 📝 Özet

Hayalet belirteçleri bulun. Onları düzeltin. Sıkıştırmadan sağ çıkın. Bağlam kalitesinin bozulmasından kaçının.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Modlar: mod yeteneği kullanılarak oluşturulanlar`                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |
| Dil      | Python                                                                   |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **2568**   |
| Son gönderme   | 2026-10-15 |
| İlk listelenme | 2026-10-13 |

🏷 `agentskills` · `claude-code` · `claude-code-mod` · `claude-code-skill` · `claude-plugin` · `codex` · `context-engineering` · `context-window`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer animation"><br><sub>animasyonlu kayıt</sub></td>
</tr></table>

<sub>Yeniden dağıtıma izin veren bir lisans belirtilmediği için varlığa upstream deposundan doğrudan bağlantı veriliyor.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/YeonwooSung/my-claude-code-mods">YeonwooSung/my-claude-code-mods</a></b> · ⭐826 · TypeScript · 👁️ observed · 1 天</summary>

##### 📝 Özet

Custom Claude Code Mods that I need

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Modlar: mod yeteneği kullanılarak oluşturulanlar`                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |
| Dil      | TypeScript                                                               |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **826**    |
| Son gönderme   | 2026-10-14 |
| İlk listelenme | 2026-10-15 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/awesome-claude-code-mods">karanb192/awesome-claude-code-mods</a></b> · ⭐594 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Özet

GitHub üzerinden taranan, her modun ağ üzerinden okuyabileceği, yazabileceği, çalıştırabileceği veya gönderebileceği şeylerle birlikte herkese açık Claude Code modlarının (işlev hooks'ları) topluluk kataloğu. https://mods.aidojo.si/'a göz atın

<sub>🔧 Kodda kullanıldığı bulundu: `data/seeds.txt`, `data/duplicates.txt`, `tools/kind.mjs`, `README.md`</sub>

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Modlar: mod yeteneği kullanılarak oluşturulanlar`                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |
| Dil      | JavaScript                                                               |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **594**    |
| Son gönderme   | 2026-10-15 |
| İlk listelenme | 2026-10-04 |

🏷 `anthropic` · `awesome` · `awesome-list` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hamzafer/claude-code-mods">hamzafer/claude-code-mods</a></b> · ⭐254 · TypeScript · 👁️ observed · 0 天</summary>

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
| Yıldızlar      | **254**    |
| Son gönderme   | 2026-10-15 |
| İlk listelenme | 2026-10-11 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugins` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/c683a5d95e78d920.png" width="100%" alt="hamzafer/claude-code-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/0b4dc7c7692bd024.gif" width="100%" alt="hamzafer/claude-code-mods animation"><br><sub>animasyonlu kayıt</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/iamumeransari/claude-show-your-work">iamumeransari/claude-show-your-work</a></b> · ⭐212 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Özet

Claude Code plugin to see, review and iterate on your agent's work without leaving the terminal: show images, play videos, and run visual QA with Playwright recordings and before/after comparisons inside the Claude Code terminal. Works in any terminal that supports the kitty graphics protocol, fully cross-platform on macOS, Linux and Windows.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Modlar: mod yeteneği kullanılarak oluşturulanlar`                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |
| Dil      | TypeScript                                                               |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **212**    |
| Son gönderme   | 2026-10-15 |
| İlk listelenme | 2026-10-13 |

🏷 `agentic-coding` · `ai-agents` · `ai-tools` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/iamumeransari--claude-show-your-work/7a0af2143a7dfd15.jpg" width="100%" alt="iamumeransari/claude-show-your-work screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/cache-tax">karanb192/cache-tax</a></b> · ⭐193 · TypeScript · 👁️ observed · 11 天</summary>

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
| Yıldızlar      | **193**    |
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
<summary>🧩 <b><a href="https://github.com/hellosverre/claude-skins">hellosverre/claude-skins</a></b> · ⭐151 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Özet

Claude Code için kaplamalar: simgeli araç satırları, diff, tablo ve Mermaid grafik kartları, kullanım bandı ve on beş tema. /skin bunları canlı olarak değiştirir.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Modlar: mod yeteneği kullanılarak oluşturulanlar`                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |
| Dil      | TypeScript                                                               |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **151**    |
| Son gönderme   | 2026-10-15 |
| İlk listelenme | 2026-10-16 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hellosverre--claude-skins/e70c992c52ca2e70.gif" width="100%" alt="hellosverre/claude-skins animation"><br><sub>animasyonlu kayıt</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NahumLitvin/prismantis">NahumLitvin/prismantis</a></b> · ⭐115 · TypeScript · 👁️ observed · 0 天</summary>

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
| Yıldızlar      | **115**    |
| Son gönderme   | 2026-10-15 |
| İlk listelenme | 2026-10-11 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `markdown` · `mermaid` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/f6e44059e77434b4.png" width="100%" alt="NahumLitvin/prismantis screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/00e2cffa219a3511.gif" width="100%" alt="NahumLitvin/prismantis animation"><br><sub>animasyonlu kayıt</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/cablate/ctx-handoff-mod">cablate/ctx-handoff-mod</a></b> · ⭐99 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Özet

Claude Code mod: hands off to a fresh conversation when context fills up, keeps the cache warm while you're away, and turns what you teach Claude into project notes

<sub>🔧 Kodda kullanıldığı bulundu: `docs/guide.md`, `docs/guide.zh-TW.md`</sub>

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
| Son gönderme   | 2026-10-15 |
| İlk listelenme | 2026-10-15 |

🏷 `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-plugin` · `context-management` · `prompt-caching`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/scasella/claude-flightdeck">scasella/claude-flightdeck</a></b> · ⭐92 · TypeScript · 👁️ observed · 3 天</summary>

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
| Yıldızlar      | **92**     |
| Son gönderme   | 2026-10-12 |
| İlk listelenme | 2026-10-10 |

🏷 `agent-observability` · `agent-visualization` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/scasella--claude-flightdeck/8c83ca6b4347b2f9.gif" width="100%" alt="scasella/claude-flightdeck screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/scasella--claude-flightdeck/8c83ca6b4347b2f9.gif" width="100%" alt="scasella/claude-flightdeck animation"><br><sub>animasyonlu kayıt</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Tickloop/claude-mods">Tickloop/claude-mods</a></b> · ⭐80 · TypeScript · 👁️ observed · 7 天</summary>

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
| Yıldızlar      | **80**     |
| Son gönderme   | 2026-10-08 |
| İlk listelenme | 2026-10-11 |

</details>

<details>
<summary>🧩 <b><a href="https://github.com/whyashthakker/awesome-claude-code-mods">whyashthakker/awesome-claude-code-mods</a></b> · ⭐68 · TypeScript · 👁️ observed · 12 天</summary>

##### 📝 Özet

Claude Code ile kullanabileceğiniz 100'den fazla mod koleksiyonu.

<sub>🔧 Kodda kullanıldığı bulundu: `README.md`, `docs/COMMUNITY_MODS.md`, `mods/agent-board/hooks/register.js`, `mods/desktop-agent-desk/hooks/register.js`</sub>

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
| Son gönderme   | 2026-10-03 |
| İlk listelenme | 2026-10-11 |

🏷 `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/zycck/claude-mods">zycck/claude-mods</a></b> · ⭐54 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Özet

Claude Code modları: istemin üstünde canlı plan ilerleme çubukları

<sub>🔧 Kodda kullanıldığı bulundu: `README.md`, `README.zh-CN.md`, `README.es.md`, `README.de.md`</sub>

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Modlar: mod yeteneği kullanılarak oluşturulanlar`                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |
| Dil      | JavaScript                                                               |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **54**     |
| Son gönderme   | 2026-10-14 |
| İlk listelenme | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/49f09d1600b02c7a.gif" width="100%" alt="zycck/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/25f4230871cb30f6.gif" width="100%" alt="zycck/claude-mods animation"><br><sub>animasyonlu kayıt · <a href="https://raw.githubusercontent.com/zycck/claude-mods/main/media/plan-progress.mp4">Videoyu aç</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/oikon48/prompt-rail">oikon48/prompt-rail</a></b> · ⭐33 · TypeScript · 👁️ observed · 0 天</summary>

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
| Yıldızlar      | **33**     |
| Son gönderme   | 2026-10-15 |
| İlk listelenme | 2026-10-04 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `function-hooks`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/oikon48--prompt-rail/d6ee96dd984886df.png" width="100%" alt="oikon48/prompt-rail screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/oikon48--prompt-rail/87309761ea9d1f19.gif" width="100%" alt="oikon48/prompt-rail animation"><br><sub>animasyonlu kayıt</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/tzafrir/human-in-the-loop">tzafrir/human-in-the-loop</a></b> · ⭐29 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Özet

A Claude Code mod: Claude assigns you the tasks only you can do. They wait in a pane until you answer, and your answer goes back to Claude.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Modlar: mod yeteneği kullanılarak oluşturulanlar`                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |
| Dil      | TypeScript                                                               |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **29**     |
| Son gönderme   | 2026-10-15 |
| İlk listelenme | 2026-10-15 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tzafrir--human-in-the-loop/80234f85f660a0df.gif" width="100%" alt="tzafrir/human-in-the-loop screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tzafrir--human-in-the-loop/ba055747f756e694.gif" width="100%" alt="tzafrir/human-in-the-loop animation"><br><sub>animasyonlu kayıt</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Jhonatan-de-Souza/ClaudeMods">Jhonatan-de-Souza/ClaudeMods</a></b> · ⭐24 · TypeScript · 👁️ observed · 1 天</summary>

##### 📝 Özet

Claude Code modları: Claude Tools menüsü, Zen modu, terminal temaları, çaba ve mod kontrolleri

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
| Son gönderme   | 2026-10-14 |
| İlk listelenme | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Jhonatan-de-Souza/ClaudeMods/main/docs/screenshots/zen.png" width="100%" alt="Jhonatan-de-Souza/ClaudeMods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Jhonatan-de-Souza/ClaudeMods/main/docs/screenshots/zen-demo.gif" width="100%" alt="Jhonatan-de-Souza/ClaudeMods animation"><br><sub>animasyonlu kayıt</sub></td>
</tr></table>

<sub>Yeniden dağıtıma izin veren bir lisans belirtilmediği için varlığa upstream deposundan doğrudan bağlantı veriliyor.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/lemomo-ai/lemo-mod">lemomo-ai/lemo-mod</a></b> · ⭐22 · TypeScript · 👁️ observed · 11 天</summary>

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
| Yıldızlar      | **22**     |
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
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-starter-kit">promptadvisers/claude-mods-starter-kit</a></b> · ⭐20 · JavaScript · 👁️ observed · 13 天</summary>

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
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-computer-use-threads">promptadvisers/claude-mods-computer-use-threads</a></b> · ⭐16 · JavaScript · 👁️ observed · 10 天</summary>

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
| Yıldızlar      | **16**     |
| Son gönderme   | 2026-10-05 |
| İlk listelenme | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/promptadvisers--claude-mods-computer-use-threads/c08dc292e500cd09.png" width="100%" alt="promptadvisers/claude-mods-computer-use-threads screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Unayung/cc-mods-enil">Unayung/cc-mods-enil</a></b> · ⭐15 · TypeScript · 👁️ observed · 2 天</summary>

##### 📝 Özet

Claude Code içinde LINE: Claude Code modu olarak enil TUI

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Modlar: mod yeteneği kullanılarak oluşturulanlar`                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |
| Dil      | TypeScript                                                               |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **15**     |
| Son gönderme   | 2026-10-13 |
| İlk listelenme | 2026-10-13 |

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/unayung--cc-mods-enil/c1156c6f17379207.png" width="100%" alt="Unayung/cc-mods-enil screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/JetsonChan/CC-Usage-Band">JetsonChan/CC-Usage-Band</a></b> · ⭐14 · TypeScript · 👁️ observed · 12 天</summary>

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
| Yıldızlar      | **14**     |
| Son gönderme   | 2026-10-03 |
| İlk listelenme | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/jetsonchan--cc-usage-band/e9d74f1543fa7c25.png" width="100%" alt="JetsonChan/CC-Usage-Band screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/OneWave-AI/claude-code-mods">OneWave-AI/claude-code-mods</a></b> · ⭐14 · TypeScript · 👁️ observed · 12 天</summary>

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
| Yıldızlar      | **14**     |
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
<summary>🧩 <b><a href="https://github.com/aieo-product/claude_qamods">aieo-product/claude_qamods</a></b> · ⭐12 · TypeScript · 👁️ observed · 8 天</summary>

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
| Yıldızlar      | **12**     |
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
<summary>🧩 <b><a href="https://github.com/augiefra/claude-mods">augiefra/claude-mods</a></b> · ⭐12 · JavaScript · 👁️ observed · 2 天</summary>

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
| Yıldızlar      | **12**     |
| Son gönderme   | 2026-10-13 |
| İlk listelenme | 2026-10-04 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `claude-code-plugins` · `claude-code-statusline`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/augiefra--claude-mods/5e1358adde3e377d.png" width="100%" alt="augiefra/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/augiefra--claude-mods/27f137c61fc42d0c.gif" width="100%" alt="augiefra/claude-mods animation"><br><sub>animasyonlu kayıt</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/ersinkoc/claude-mods">ersinkoc/claude-mods</a></b> · ⭐11 · TypeScript · 👁️ observed · 5 天</summary>

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
| Yıldızlar      | **11**     |
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
<summary>🧩 <b><a href="https://github.com/furqan-khan07/pixelband">furqan-khan07/pixelband</a></b> · ⭐10 · TypeScript · 👁️ observed · 11 天</summary>

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
<summary>🧩 <b><a href="https://github.com/VedantAndhale/claude-pro-kit">VedantAndhale/claude-pro-kit</a></b> · ⭐10 · TypeScript · 👁️ observed · 6 天</summary>

##### 📝 Özet

Claude Pro planının daha uzun süre dayanmasını sağlayın: tam kullanım HUD'sı, daha kısa kabuk çıktısı ve tekrarlanan dosya okumalarını önlemek için Claude Code modları. Modlar sıfır token harcar.

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
| Son gönderme   | 2026-10-09 |
| İlk listelenme | 2026-10-11 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mods` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vedantandhale--claude-pro-kit/176355f2fdfc7ab9.png" width="100%" alt="VedantAndhale/claude-pro-kit screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vedantandhale--claude-pro-kit/0e3c2fea33c7be45.gif" width="100%" alt="VedantAndhale/claude-pro-kit animation"><br><sub>animasyonlu kayıt</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Arunjay4213/claude-mods">Arunjay4213/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 30 天</summary>

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
<summary>🧩 <b><a href="https://github.com/deepsteve/deepsteve">deepsteve/deepsteve</a></b> · ⭐9 · JavaScript · 👁️ observed · 1 天</summary>

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
| Son gönderme   | 2026-10-14 |
| İlk listelenme | 2026-10-11 |

🏷 `ai-coding` · `ai-tools` · `browser-terminal` · `claude-code` · `codex` · `coding-agent` · `developer-tools` · `devtools`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/deepsteve--deepsteve/adee5ea71e2e3289.png" width="100%" alt="deepsteve/deepsteve screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/az9713/claude-mod-pack">az9713/claude-mod-pack</a></b> · ⭐8 · TypeScript · 👁️ observed · 11 天</summary>

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
<summary>🧩 <b><a href="https://github.com/devbrother2024/devbrothers-mods">devbrother2024/devbrothers-mods</a></b> · ⭐8 · TypeScript · 👁️ observed · 11 天</summary>

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
| Yıldızlar      | **8**      |
| Son gönderme   | 2026-10-04 |
| İlk listelenme | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/devbrother2024--devbrothers-mods/10df726087fd2881.webp" width="100%" alt="devbrother2024/devbrothers-mods screenshot"></td>
<td align="center" valign="top"><a href="https://www.youtube.com/@%EA%B0%9C%EB%B0%9C%EB%8F%99%EC%83%9D"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/devbrother2024--devbrothers-mods/10df726087fd2881.webp" width="100%" alt="video"></a><br><sub><a href="https://www.youtube.com/@%EA%B0%9C%EB%B0%9C%EB%8F%99%EC%83%9D">Şurada izle: youtube.com</a> · oynatma barındırıcı sitede açılır; GitHub bunu satır içinde gömemez</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/mishgoldenberg/claude-mods">mishgoldenberg/claude-mods</a></b> · ⭐8 · TypeScript · 👁️ observed · 9 天</summary>

##### 📝 Özet

Claude Code için paneller, koruyucu kurallar ve kullanım kolaylığı modları: bağlam, kullanım, canlı etkinlik, bildirimler, güvenlik kuralları, istem koçu, komut merkezi.

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
| Son gönderme   | 2026-10-06 |
| İlk listelenme | 2026-10-11 |

🏷 `ai-agents` · `ai-safety` · `anthropic` · `claude` · `claude-code` · `claude-code-plugins` · `developer-tools` · `llm`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/mishgoldenberg--claude-mods/9458e91720f67521.gif" width="100%" alt="mishgoldenberg/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/mishgoldenberg--claude-mods/9458e91720f67521.gif" width="100%" alt="mishgoldenberg/claude-mods animation"><br><sub>animasyonlu kayıt</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/timoncool/givememod">timoncool/givememod</a></b> · ⭐8 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Özet

İsteğe bağlı Claude Code modları — konuşmanızı okuyup size uygun modu oluşturan bir beceri: plan ilerleme çubuğu, dosyalar bölmesi, bağlam göstergesi, riskli komut koruması, test izleyicisi. Test edilmiş 11 şablon, 29 yapı taşı, 3.057 herkese açık modun haritası. Terminal ve masaüstü.

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
| Son gönderme   | 2026-10-15 |
| İlk listelenme | 2026-10-11 |

🏷 `agent-skills` · `ai-tools` · `anthropic` · `claude` · `claude-code` · `claude-code-mods` · `claude-code-plugin` · `claude-code-skill`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/timoncool--givememod/6fb8ba0c74031f7f.png" width="100%" alt="timoncool/givememod screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/timoncool--givememod/5f58df5c7bdd37f9.gif" width="100%" alt="timoncool/givememod animation"><br><sub>animasyonlu kayıt</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Danovich/turntype">Danovich/turntype</a></b> · ⭐7 · TypeScript · 👁️ observed · 4 天</summary>

##### 📝 Özet

Claude çalışırken zaman geçirmek için bir yazma testi. Bir Claude Code modu.

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
| Son gönderme   | 2026-10-11 |
| İlk listelenme | 2026-10-12 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `claude-mods` · `typing` · `typing-game` · `typing-practice` · `typing-test`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/danovich--turntype/24d5c7d94e15fcfb.gif" width="100%" alt="Danovich/turntype screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/danovich--turntype/24d5c7d94e15fcfb.gif" width="100%" alt="Danovich/turntype animation"><br><sub>animasyonlu kayıt</sub></td>
</tr></table>

</details>

<details>
<summary><b>Bu kategoride daha fazlası</b> <sub>· 348</sub></summary>

- [darrell-tw/darrelltw-mods](https://github.com/darrell-tw/darrelltw-mods) - Darrell Wang tarafından hazırlanan Claude Code modları — istemin üstünde…
- [ray-amjad/claude-code-mods](https://github.com/ray-amjad/claude-code-mods) - Ray Amjad.
- [0xDarkMatter/claude-mods](https://github.com/0xDarkMatter/claude-mods) - Claude Code için uzman Skills.
- [karanb192/claude-code-mods](https://github.com/karanb192/claude-code-mods) - Claude Mod.
- [nateherkai/claude-code-mods](https://github.com/nateherkai/claude-code-mods) - Dört Claude Code modu: Cache Keeper, Recording Mode, Goal Meter ve Collision…
- [ucsandman/claude-harness](https://github.com/ucsandman/claude-harness) - Her gün çalıştırdığım Claude Code harness.
- [kagamiurayama/claude-code-roof-mod](https://github.com/kagamiurayama/claude-code-roof-mod) - Claude Mods ile Claude Code.
- [RiskAverseTech/toolgate](https://github.com/RiskAverseTech/toolgate) - A measured tool-call firewall for AI agents: allow, ask or deny before the…
- [artemnovichkov/xcode-mods](https://github.com/artemnovichkov/xcode-mods) - Xcode.
- [BrianHuang813/clawd-actor](https://github.com/BrianHuang813/clawd-actor) - Claude Code modu: Clawd, istemin üstünde Claude tarafından yapılanları…
- [nvr0x5/claude-deck](https://github.com/nvr0x5/claude-deck) - A cockpit for Claude Code: live plan bars, subagent strips, usage limits with…
- [centminmod/claude-plugins](https://github.com/centminmod/claude-plugins) - Personal Claude Code plugin marketplace — session-metrics, more to come.
- [AgriciDaniel/claude-mods-brain](https://github.com/AgriciDaniel/claude-mods-brain) - Claude Code modları hakkında kaynak gösteren Obsidian bilgi tabanı: nasıl…
- [Hangghost/learning-hacker-claude-mod](https://github.com/Hangghost/learning-hacker-claude-mod) - Learning Hacker.
- [kakha13/claude](https://github.com/kakha13/claude) - Claude Code modları, Claude onları okumadan önce istemlerinizi düzeltir ve…
- [nekyialabs/claude-code-toolkit](https://github.com/nekyialabs/claude-code-toolkit) - Nekyia Labs tarafından geliştirilen ve kalıcı bir evde yaşayan AIs tarafından…
- [xuanji86/claude-agentpane](https://github.com/xuanji86/claude-agentpane) - Claude Code için bir yan panel: bir oturumun çalıştırdığı alt aracılar, her…
- [letswritetw/claude-mod-open-todos](https://github.com/letswritetw/claude-mod-open-todos) - Claude Desktop (Code sekmesi) kenar çubuğu paneli: tüm Claude Code…
- [letswritetw/claude-mod-token-usage](https://github.com/letswritetw/claude-mod-token-usage) - Claude Desktop (Code sekmesi) giriş kutusunun üstündeki kullanım çubuğu: 5h /…
- [KilimcininKorOglu/claude-code-mods](https://github.com/KilimcininKorOglu/claude-code-mods) - Claude Code için Claude Mods (işlev kancası eklentileri).
- [xuanji86/claude-statuspane](https://github.com/xuanji86/claude-statuspane) - Claude Code için kayan durum kartı — model, bağlam, hız sınırları, maliyet, dal…
- [BeLazy167/claude-mods-skill](https://github.com/BeLazy167/claude-mods-skill) - Claude Code ajanlarına, başlangıç örneğiyle birlikte Claude Mods.
- [bruw/workflow-conductor](https://github.com/bruw/workflow-conductor) - Visual workflow planner in Claude Code.
- [eighteyes/cactus](https://github.com/eighteyes/cactus) - Konuşmalı ajanlarla çalışan insanlar için karar kuyruğu CLI/TUI.
- [omarcevi/claudemods](https://github.com/omarcevi/claudemods) - Tek bir pazardan kurulabilen topluluk Claude modları, eklentileri ve becerileri.
- [davekiss/mods](https://github.com/davekiss/mods) - Dave Kiss tarafından geliştirilen Claude Code modları.
- [baselane-sh/mods-catalog](https://github.com/baselane-sh/mods-catalog) - Baselane modları galerisi: Claude Code modları, kontrol edilmiş ve sabitlenmiş.
- [hellosverre/mod-store](https://github.com/hellosverre/mod-store) - Claude Code içinde Claude Code modları için uygulama mağazası: 2.700 modu…
- [ice-lfernandes/claude-code-mods](https://github.com/ice-lfernandes/claude-code-mods) - Altı Claude Code modu: plan sınırları ve istemin üstünde bağlam, izin istemleri…
- [markneonin/paneline](https://github.com/markneonin/paneline) - Activity, Files, Agents, Context ve MCP sekmelerini içeren bir yan bölme…
- [natsukium/claude-code-figures-plugin](https://github.com/natsukium/claude-code-figures-plugin) - Draw diagrams, LaTeX math, and tool-result images inline in kitty-graphics…
- [neteye-platform/cc-split-diff-view](https://github.com/neteye-platform/cc-split-diff-view) - Edit ve Write farklarını yan yana iki sütunda çizen Claude Code modu.
- [ronanworks/claude-code-mods](https://github.com/ronanworks/claude-code-mods) - Claude Code modları: 像素螃蟹用量面板 usage-hud + terminalde tıklanabilen HTML…
- [arasovic/claude-code-mods](https://github.com/arasovic/claude-code-mods) - Claude Code için Mods: terminal kullanıcı arayüzüne canlı bölmeler ve davranış…
- [danyuchn/claude-mods](https://github.com/danyuchn/claude-mods) - Claude Code modları: screen-guard ekran paylaşırken adları ve gizli bilgileri…
- [GarvitNangru/claude-code-mods](https://github.com/GarvitNangru/claude-code-mods) - Claude Code için modlar ve görünümler: Claude görevleri için canlı ilerleme…
- [helenkwok/gsd-status-mod](https://github.com/helenkwok/gsd-status-mod) - Live GSD dashboard for Claude Code: roadmap, agent tree with forks, context and…
- [magidandrew/cx](https://github.com/magidandrew/cx) - Claude Code Extensions. Claude.
- [ofeklevy11/claude-code-hud](https://github.com/ofeklevy11/claude-code-hud) - İstem kutusunun üstünde iki Claude Code modu: bağlam penceresi ölçer, 5 saatlik…
- [Szotasz/claude-mods](https://github.com/Szotasz/claude-mods) - Kendi Claude Code modlarım için eklenti marketplace.
- [xuanji86/claude-mdview](https://github.com/xuanji86/claude-mdview) - Claude Code.
- [Antreas-Strb/glanceflow](https://github.com/Antreas-Strb/glanceflow) - Claude Code için GlanceFlow: istemin üzerinde planı, ilerlemeyi ve Claude.
- [Boom-Vitt/boombignose-mods](https://github.com/Boom-Vitt/boombignose-mods) - Claude Code modları: bağlam çubuğu, ajanlar paneli, PDPA bulanıklaştırma.
- [hahmjuntae/claude-mods-image-preview](https://github.com/hahmjuntae/claude-mods-image-preview) - Claude Code modu: herhangi bir terminalde istemin üstünde yapıştırılan…
- [leopiney/wolfbud-claude-mod](https://github.com/leopiney/wolfbud-claude-mod) - Claude Code için sesli çalışma arkadaşı.
- [Nongfsq/frank-claude-cockpit](https://github.com/Nongfsq/frank-claude-cockpit) - Aynı anda birçok oturum çalıştırmak için iki Claude Code modu: istemin üstünde…
- [borabiricik/claude-mods](https://github.com/borabiricik/claude-mods) - Claude Code modları: typing-speed, istem başına istatistiklerle canlı yazma…
- [dougcunha/claude-mods](https://github.com/dougcunha/claude-mods) - Claude Code için modlar: function-hooks API eklentisiyle oluşturulmuş paneller…
- [DrishtantKaushal/AwesomeClaudeCodeMods](https://github.com/DrishtantKaushal/AwesomeClaudeCodeMods) - Animasyonlu demolar, kategori listeleri ve doğrudan kaynak bağlantılarıyla…
- [galElmalah/claude-mods](https://github.com/galElmalah/claude-mods) - Claude Code modu: mermaid diyagramları transkript içinde satır içi olarak…
- [ha-ptt0601/cc-mods](https://github.com/ha-ptt0601/cc-mods) - Küçük Claude Code modülleri (işlev kancası eklentileri): session-switcher ve…
- [LeeHigma0201/claude-code-mods](https://github.com/LeeHigma0201/claude-code-mods) - Claude Code modları: mod-scout (en çok kullanacağınız modları bulur)…
- [mertkayacs/ultramod](https://github.com/mertkayacs/ultramod) - the best all-in-one mod pack for Claude Code.
- [NarenDawar/narens-claude-toolkit](https://github.com/NarenDawar/narens-claude-toolkit) - Naren.
- [nuromirzak/nibbl](https://github.com/nuromirzak/nibbl) - A tiny pixel pet that nibbles your bugs. Lives above your Claude Code prompt.
- [theonly1me/claude-code-mods](https://github.com/theonly1me/claude-code-mods) - Tarafımdan oluşturulmuş bir dizi claude code modu.
- [ayagmar/claude-modmgr](https://github.com/ayagmar/claude-modmgr) - modmgr: Claude Code modlarını keşfedin, inceleyin, açıp kapatın ve güncelleyin.
- [claude-code-mods/best-claude-code-mods](https://github.com/claude-code-mods/best-claude-code-mods) - En iyi Claude Code modları: özenle seçilmiş, doğrulanmış, sabitlenmiş.
- [comertial/comertial-mods](https://github.com/comertial/comertial-mods) - Gerçek Mühendisler için Claude Code modları.
- [dominicrico/jev-router](https://github.com/dominicrico/jev-router) - Claude Code eklentisi: otomatik Claude model yönlendirmesi.
- [FynnXland/fynn-mods](https://github.com/FynnXland/fynn-mods) - Claude Code için altı mod: animasyonlu Clawd maskotu, kullanım limiti ve…
- [ibrahimkobeissy/claude-mods](https://github.com/ibrahimkobeissy/claude-mods) - Claude Code için açık kaynaklı modlar: bölmeler, durum satırları, bildirimler…
- [Malkiz/claude-reply-comments](https://github.com/Malkiz/claude-reply-comments) - Claude Code modu: Claude.
- [nextscape/ns-mods](https://github.com/nextscape/ns-mods) - Nextscape が公開する Claude Code mod（関数フックのプラグイン）集。使う mod を選んで導入できるマーケットプレイス.
- [oMaN-Rod/claude-code-widgets](https://github.com/oMaN-Rod/claude-code-widgets) - Small cards that sit under the Claude Code prompt, or docked beside the…
- [omeerdvrn/o-mods](https://github.com/omeerdvrn/o-mods)
- [peeratop02/attention-sounds](https://github.com/peeratop02/attention-sounds) - Claude Code mod: plays a sound when Claude is done, needs permission, or asks a…
- [raresmun/claude-mods](https://github.com/raresmun/claude-mods) - Claude Code için modlar: Claude.
- [reporails/arcade](https://github.com/reporails/arcade) - Claude Code modları olarak klasik masaüstü oyunları;
- [schreibse/claude-code-mods](https://github.com/schreibse/claude-code-mods) - claude için code-mods.
- [shimo4228/harness-scope](https://github.com/shimo4228/harness-scope) - Genel becerilerinizi, aracıları, kuralları ve araçlarınızı adlandırılmış…
- [Singh-AP/awesome-claude-mods](https://github.com/Singh-AP/awesome-claude-mods) - 🧩 Test edilmiş, tek komutla kurulabilen Claude Code modları: YOLO modu için…
- [soulrocha/Claude-code-hero-journey](https://github.com/soulrocha/Claude-code-hero-journey) - 🦀 A cozy RPG HUD mod for Claude Code.
- [testy-cool/awesome-claude-code-mods](https://github.com/testy-cool/awesome-claude-code-mods) - Eklenti pazaryeri olarak kurulabilen, derlenmiş bir Claude Code modları…
- [wdsewdser-bit/claude-code-mods](https://github.com/wdsewdser-bit/claude-code-mods) - İki Claude Code modu: cache-keeper ve ctx-mod.
- [yash-gadodia/claude-mods](https://github.com/yash-gadodia/claude-mods) - Bir ajanın dürüst kalmasını sağlayan Claude Code modları — kapsamı koruyan…
- [agentic-workbench/agent-quick-menu](https://github.com/agentic-workbench/agent-quick-menu) - Quick menu for Claude Code: every plugin.
- [AlexeyHRDesign/colorwheel](https://github.com/AlexeyHRDesign/colorwheel) - Themed replies, full-width diagrams, and your context and limits at a glance…
- [bradtraversy/claude-mods](https://github.com/bradtraversy/claude-mods) - Personal Claude Code mods for interface customization, safety, and verification.
- [gaius-codius/ostrakon](https://github.com/gaius-codius/ostrakon) - Çalışma sırasında akla gelen düşünceleri yakalayan, bunları projeler ve…
- [helenlin0621/tea-egg](https://github.com/helenlin0621/tea-egg) - Kod yazarken yavaşça marine olan bir çay yumurtası yetiştir · Kod yazarken…
- [herman925/925-cc-plugins](https://github.com/herman925/925-cc-plugins) - Herman.
- [Krs7N/context-meter](https://github.com/Krs7N/context-meter) - Live context-window meter above the Claude Code prompt: animated fill bar…
- [KyongSik-Yoon/cc-desktop-mod](https://github.com/KyongSik-Yoon/cc-desktop-mod) - Claude Code eklentisi (modu), Claude Code terminal kullanıcı arayüzünü Claude…
- [lorenzh/rabe](https://github.com/lorenzh/rabe) - Claude Code.
- [MankhongGarden/claude-code-mods-field-notes](https://github.com/MankhongGarden/claude-code-mods-field-notes) - Windows üzerindeki Claude Code modları hakkında birinci gün saha notları…
- [midudev/better-claude](https://github.com/midudev/better-claude) - Small plugins and mods that make your life (and Claude Code) better.
- [patitow/claude-mod-cost-visibility](https://github.com/patitow/claude-mod-cost-visibility) - Claude Code modu: istemin üzerinde canlı maliyet, bağlam ve plan kota…
- [ruslanshchuchkin/claude-techno-mod](https://github.com/ruslanshchuchkin/claude-techno-mod) - 😈 We are making some TECHNO babyyyy 😈.
- [Ryan-LT/claude-mods](https://github.com/Ryan-LT/claude-mods) - Claude Code mods: always-on usage-limits band.
- [Sennjen/claude-sdlc](https://github.com/Sennjen/claude-sdlc) - Claude Code plugin&#x27;i ve mod&#x27;u: hook ile zorunlu kılınan insan onayı kapıları ve…
- [timoncool/slapbox](https://github.com/timoncool/slapbox) - 🍑 Hata yaptığında Claude.
- [vulcanshen/ccdrawu](https://github.com/vulcanshen/ccdrawu) - A sidebar for Claude Code: usage limits, context, model, cost, git and session…
- [yodakeisuke/claudelingo](https://github.com/yodakeisuke/claudelingo) - Claude Code ile çalışırken yabancı bir dil öğrenin.
- [andrewbakercloudscale/claude-code-cost-sidebar](https://github.com/andrewbakercloudscale/claude-code-cost-sidebar) - Claude Code için canlı maliyet, token ve bağlam kullanımı kenar çubuğu: oturum…
- [Azertyuiop442/deepshrink](https://github.com/Azertyuiop442/deepshrink) - Proven-freshness context store for coding agents - mtime-verified reuse, TF-IDF…
- [cldotdev/claude-todo-list](https://github.com/cldotdev/claude-todo-list) - Bir konuşmadaki açık öğelerin güncel listesini tutan ve bunu istemin üzerindeki…
- [connectwithub/loopkeeper](https://github.com/connectwithub/loopkeeper) - Claude Code.
- [Davron2004/slash-coverage](https://github.com/Davron2004/slash-coverage) - Her Claude Code ajanının bağlamında hangi dosyaların olduğunu ve her birinden…
- [enhki/claude-mods](https://github.com/enhki/claude-mods) - Terminal ve masaüstü uygulaması için küçük Claude Code modları.
- [Exdenta/ambient-spanish](https://github.com/Exdenta/ambient-spanish) - Ajan yanıtlarına İspanyolca kelimeler ekleyen Claude CLI becerisi + modu.
- [FrBmt-BIGetNouf/floatee-claude-mod](https://github.com/FrBmt-BIGetNouf/floatee-claude-mod) - Floatee bekleme listeniz Claude Code isteminin üzerinde: yapılacaklarınızı tek…
- [HyunjunJeon/claude-workflow-mods](https://github.com/HyunjunJeon/claude-workflow-mods) - dag-workflow: canlı DAG paneliyle alt aracıların zorunlu ve doğrulanmış DAG iş…
- [joaquinsalinas06/crabbus](https://github.com/joaquinsalinas06/crabbus) - See what every Claude Code subagent is really doing — two-way messaging, tokens…
- [JSungMin/crew-graph](https://github.com/JSungMin/crew-graph) - Claude Code mod: live pane with your agent crew as a tree, plan/doc…
- [kongyo2/context-view](https://github.com/kongyo2/context-view) - Bağlam penceresi, istemin üzerinde tek satır olarak;
- [Kruhlikau/subagent-tuner](https://github.com/Kruhlikau/subagent-tuner) - Claude Code modu: her alt ajanın modelini ve akıl yürütme eforunu seçer.
- [leonidb/claude-code-mods](https://github.com/leonidb/claude-code-mods) - Claude Code.
- [m4cd4r4/clear-resume](https://github.com/m4cd4r4/clear-resume) - Claude Code için ücretsiz, açık kaynaklı bir eklenti.
- [meganemura/pull-request-pane](https://github.com/meganemura/pull-request-pane) - A Claude Mod that shows the session.
- [michalstrnadel/claude-docket](https://github.com/michalstrnadel/claude-docket) - ◆ A minimal task board inside Claude Code — see what Claude is working on…
- [MitchMedeiros/veneer](https://github.com/MitchMedeiros/veneer) - Take your Claude Code terminal sessions to the next level! Enhanced visuals…
- [modmyclaude/claude-code-mods](https://github.com/modmyclaude/claude-code-mods) - Claude Code mods: curated and tested.
- [muctebadikmen/claude-code-araclari](https://github.com/muctebadikmen/claude-code-araclari) - Claude Code modları: otomatik devir ve ilerleme çubuğu.
- [nninkovic95/clawd-band](https://github.com/nninkovic95/clawd-band) - Animated Clawd + weekly/5-hour usage bars and reset countdowns above the Claude…
- [nonputtipong/claude-code-prompt-enhancer](https://github.com/nonputtipong/claude-code-prompt-enhancer) - ✻ A Claude Code mod that rewrites your rough draft into a clear, project-aware…
- [NotRedFox/NotRedFoxs-Claude-skills](https://github.com/NotRedFox/NotRedFoxs-Claude-skills) - Claude Code becerileri: belge doğrulayıcı, kod denetçisi, hata anıları günlüğü…
- [oobg/claude-code-mods](https://github.com/oobg/claude-code-mods) - Claude Code 입력창과 도구 결과에 기능을 더하는 모드 모음.
- [Plagemes/claude-mods](https://github.com/Plagemes/claude-mods) - 200+ open-source mods for Claude Code: guardrails, status lines, panes and…
- [rezzminator/buddy](https://github.com/rezzminator/buddy) - Claude Code arkadaş eklentisi: isteminizin üzerinde kurallarınızı hatırlayan ve…
- [rezzminator/tool-visibility-controller](https://github.com/rezzminator/tool-visibility-controller) - Claude Code plugin for per-agent tool visibility — hide and refuse subagents…
- [roma-vibe/jev-governor](https://github.com/roma-vibe/jev-governor) - Claude Code mod: Jev-guided model/effort routing, verbatim context compaction…
- [Ron-Nefyodov/prompt-library-mod](https://github.com/Ron-Nefyodov/prompt-library-mod) - Save, search and reuse your best Claude Code prompts. Community mod.
- [Ron-Nefyodov/wrapped-mod](https://github.com/Ron-Nefyodov/wrapped-mod) - Your Claude Code year in one shareable card. Community mod.
- [RyanWeera/crab-progress](https://github.com/RyanWeera/crab-progress) - A Claude Code mod: progress bar with a pixel mascot, costumes for every task…
- [simota/claude-mods](https://github.com/simota/claude-mods) - Personal Claude Code mods (function-hook plugins) as one marketplace…
- [Spardutti/claude-mods](https://github.com/Spardutti/claude-mods) - Claude Code mods: live panels and hooks for daily work.
- [tanujarun/it-speaks](https://github.com/tanujarun/it-speaks) - Konuşuyor: Claude.
- [tripolskiydigital/claude-links](https://github.com/tripolskiydigital/claude-links) - A links bar for Claude Desktop.
- [TroyJLorents-GH/mod-squad](https://github.com/TroyJLorents-GH/mod-squad) - Claude Code modları: canlı bölmeler, maliyet farkındalıklı model yönlendirme ve…
- [valeryia-piatrova/token-hamster](https://github.com/valeryia-piatrova/token-hamster) - 🐹 Claude Code modu ve eklentisi: kullanım monitörü, token izleyici ve durum…
- [varunmoka7/next-steps-autopilot](https://github.com/varunmoka7/next-steps-autopilot) - Shows suggested next prompts above the prompt box.
- [verdantran/code-city](https://github.com/verdantran/code-city) - An idle pixel-art city for Claude Code.
- [Xabilimon1/emcc-claude-code-mods](https://github.com/Xabilimon1/emcc-claude-code-mods) - Claude Code modları: EMCC (Every Mod Claude Code), Claude Code için seçilmiş ve…
- [0hte/glitchdeck](https://github.com/0hte/glitchdeck) - A Claude Code mod that docks a live pane beside your conversation: what Claude…
- [aecheman27-gif/claude-mods](https://github.com/aecheman27-gif/claude-mods) - Claude Code mods marketplace (my-claude-mods): status band, panes, guards and…
- [aiob3/claude-grounds](https://github.com/aiob3/claude-grounds) - Claude Code mods that make &quot;done&quot; checkable: the task goal stays on screen and…
- [aiob3/claude-grounds-demo](https://github.com/aiob3/claude-grounds-demo) - Demo for claude-grounds (Claude Code mods): a median() bug with text sort and a…
- [Akurganow/model-router](https://github.com/Akurganow/model-router) - Claude Code mod: route each subagent to the cheapest Claude model, judged by…
- [Aler1x/claude-cat](https://github.com/Aler1x/claude-cat) - Claude Code isteminin üzerinde animasyonlu bir braille kedisi.
- [aloki-alok/omni-cat](https://github.com/aloki-alok/omni-cat) - Claude Code isteminizin üzerinde, bir OmniDimension ses ajanı test çağrısı…
- [alvaro-hi/progress-ring](https://github.com/alvaro-hi/progress-ring) - Progress Ring for Claude Code: know where Claude is in a long plan.
- [ambervdberg/smartcompact](https://github.com/ambervdberg/smartcompact) - Bağlam penceresini küçük tutmak için sıkıştırma işlemini uygun bir anda seçen…
- [an80sPWNstar/claude-mods](https://github.com/an80sPWNstar/claude-mods) - Claude Code için Claude modları: token-meter.
- [anderson-spider/claude-mods](https://github.com/anderson-spider/claude-mods) - Claude Code plugin marketplace by anderson-spider.
- [andrej-kolic/claude-mods](https://github.com/andrej-kolic/claude-mods) - Claude Code için genel amaçlı modlar: bantlar, paneller, bildirimler ve…
- [aquarius-wing/copy-session-id](https://github.com/aquarius-wing/copy-session-id) - A Claude Code mod that adds a Copy Session ID button above the prompt.
- [Ashley-Pettit/villager-hp](https://github.com/Ashley-Pettit/villager-hp) - Haftalık tempo uyarısıyla birlikte Claude kullanım sınırlarınızı animasyonlu…
- [Atanur/deskfit](https://github.com/Atanur/deskfit) - Claude çalışırken kısa antrenmanlar: günlük hedef, seriler, rozetler ve isteğe…
- [AweGuider/Claude-Context-Control](https://github.com/AweGuider/Claude-Context-Control) - Context Control: a Claude Code mod showing context window fill, what fills it…
- [benjaminr/nowplaying](https://github.com/benjaminr/nowplaying) - Claude Code için Now Playing modu: istemin üzerinde kapak görseli, kontroller…
- [berkakkaya/subagents-panel](https://github.com/berkakkaya/subagents-panel) - See what your Claude Code subagents are doing, live, in a side panel.
- [Br4inergy/claude-hands-off](https://github.com/Br4inergy/claude-hands-off) - Your AI agent can&#x27;t push to a repo, deploy a project or drop a table that isn&#x27;t…
- [Br4inergy/claude-huddle](https://github.com/Br4inergy/claude-huddle) - See when your Claude Code sessions are about to collide in the same repo, and…
- [Br4inergy/claude-loadout](https://github.com/Br4inergy/claude-loadout) - Loadout, the mod manager for Claude Code: audits every mod and every update…
- [broening/claude-mods](https://github.com/broening/claude-mods) - Claude Code için modlar: önbellek saati, patlama yarıçapı, öneriler, iş…
- [candygoogy/notary](https://github.com/candygoogy/notary) - See what Claude changed, turn by turn. Keep it or send it back.
- [Carismarkus/clowl](https://github.com/Carismarkus/clowl) - Claude Code.
- [CiroVilmer/jev-agent-router](https://github.com/CiroVilmer/jev-agent-router) - Claude Code mod that picks the model and effort of every subagent from its task…
- [CoderDayton/vii-mods](https://github.com/CoderDayton/vii-mods) - Claude Code mods for memory, safety and workflow.
- [danieldeusing/capi-cc-mod](https://github.com/danieldeusing/capi-cc-mod) - Capi: a Claude Code mod that teaches you a language above the prompt, one…
- [DarthSonic/cache-weather-and-pause-resume](https://github.com/DarthSonic/cache-weather-and-pause-resume) - Claude Code mod: a band above the prompt with the prompt-cache countdown…
- [DarthSonic/claude-plugins](https://github.com/DarthSonic/claude-plugins) - Claude Code marketplace darthsonic: a catalog of plugins and mods, each in a…
- [DazzleML/claude-bookmarks](https://github.com/DazzleML/claude-bookmarks) - Bookmarks and vim-style marks inside Claude Code terminal conversations…
- [dot-agi/downrange](https://github.com/dot-agi/downrange) - Claude Code mod: background jobs in one view, with progress and ETAs read from…
- [edtrackai/claude-code-guardrails-lite](https://github.com/edtrackai/claude-code-guardrails-lite) - Free Claude Code plugin: denies .env reads, git force push and rm -rf on / or…
- [feizaodemon/claude-mods](https://github.com/feizaodemon/claude-mods) - Claude Code modları (işlev kancası eklentileri): session-meter ve daha fazlası.
- [flaviorg/claude-mods](https://github.com/flaviorg/claude-mods) - Hub marketplace for my original Claude Code mods: tripwire, canopy, crew…
- [flaviorg/crew](https://github.com/flaviorg/crew) - Claude Code mod: a live panel of the subagents Claude delegates to — model…
- [funkadelic/claude-secret-scrub](https://github.com/funkadelic/claude-secret-scrub)
- [hearsawho25/roberts-mods](https://github.com/hearsawho25/roberts-mods) - Claude Code mods (hooks-module plugins) shared as a plugin marketplace. MIT.
- [Hekzory/spend-meter](https://github.com/Hekzory/spend-meter) - Claude Code için canlı harcama ölçer: sağ tarafa sabitlenmiş, alt agent.
- [helenkwok/rustgis-tui](https://github.com/helenkwok/rustgis-tui) - A terminal UI for RustGIS, and a Claude Code pane you and Claude drive…
- [HuliLulu46/cc-commit-command](https://github.com/HuliLulu46/cc-commit-command)
- [HuliLulu46/cc-effort-switch](https://github.com/HuliLulu46/cc-effort-switch)
- [HuliLulu46/cc-prompt-polish](https://github.com/HuliLulu46/cc-prompt-polish)
- [HuliLulu46/pending-decisions](https://github.com/HuliLulu46/pending-decisions)
- [humvnpvrvdox777/NextSteps](https://github.com/humvnpvrvdox777/NextSteps) - Claude Code mod: three next steps after each answer, in any language, with an…
- [Huuuuung/think-meter](https://github.com/Huuuuung/think-meter) - Claude Code modu: her yanıtın ne kadar sürdüğü, Claude.
- [huynl-96/claude-mods](https://github.com/huynl-96/claude-mods) - Claude Code mods: streamer-mode hides private panes, bands and the status line…
- [isandrel/redact-restore](https://github.com/isandrel/redact-restore) - Reversible redaction for Claude Code: the model sees placeholders, you and your…
- [iyiob96/Context-Mod-Companion](https://github.com/iyiob96/Context-Mod-Companion) - Claude Code mod: context window band with RTK savings and a pixel Yemeni…
- [jessetsai1024/claude-ctx-panel](https://github.com/jessetsai1024/claude-ctx-panel) - Kenar çubuğunda bağlam kullanım paneli: toplam, kategoriler, tur başına büyüme…
- [jessetsai1024/claude-files](https://github.com/jessetsai1024/claude-files) - Kenar çubuğunda dosya listesi: bu konuşmada hangi dosyalar oluşturuldu…
- [jessetsai1024/claude-maomao](https://github.com/jessetsai1024/claude-maomao) - Girdi kutusunun üzerinde koşup zıplayan 8-bit tarzı 毛毛.
- [jessetsai1024/claude-prompts](https://github.com/jessetsai1024/claude-prompts) - Kenar çubuğunda “sorduğum sorular”: kullanıcının bu konuşmada yazdığı her…
- [jessetsai1024/claude-timeline](https://github.com/jessetsai1024/claude-timeline) - Kenar çubuğunda zaman çizelgesi: bu turda zaman nereye harcandı.
- [jessetsai1024/claude-tokens](https://github.com/jessetsai1024/claude-tokens) - Kenar çubuğunda token alışverişi: ana konuşma her seferinde Anthropic.
- [jessetsai1024/claude-whisper](https://github.com/jessetsai1024/claude-whisper) - claude code.
- [jsc2304/great-question](https://github.com/jsc2304/great-question) - Know the question before it is asked, and what you can safely say.
- [Jsolee/claude-mods](https://github.com/Jsolee/claude-mods) - Mods de Claude Code de Joan Solé: comunitat, el panell dels subagents amb el…
- [KaiC5504/clawd-bar](https://github.com/KaiC5504/clawd-bar) - Clawd, Claude Code prompt.
- [kajidog/cc-mods-tts](https://github.com/kajidog/cc-mods-tts) - Claude Code yanıtlarını ve bildirimlerini VOICEVOX / Irodori-TTS gibi araçlarla…
- [katipally/modz](https://github.com/katipally/modz) - Claude Code mods: install with /plugin install &lt;mod&gt; --marketplace…
- [kiankhooban/open-paths](https://github.com/kiankhooban/open-paths) - Click a file path in Claude Code and the file opens in its app: Word, Preview…
- [Kiyliy/claude-code-tps](https://github.com/Kiyliy/claude-code-tps) - Claude Code mod: status line showing output speed (tps), TTFT, total time and…
- [Koder-SpA/claude-mods](https://github.com/Koder-SpA/claude-mods) - Claude Code plugins by Koder SpA — real-time token cost, context and rate-limit…
- [krishna-goutham-tls/cc-mods](https://github.com/krishna-goutham-tls/cc-mods) - Two Claude Code mods: folio, a file pane beside the chat, and tint, a restyle…
- [kuzmany/cc-model-effort-switcher](https://github.com/kuzmany/cc-model-effort-switcher) - Switch Claude Code model and reasoning effort in one command: /m opus high.
- [lijingwu2026/claude-code-plan-tracker](https://github.com/lijingwu2026/claude-code-plan-tracker) - A live board of your approved plan: which steps are done, running, blocked or…
- [Lucas-CX/awesome-claude-mods](https://github.com/Lucas-CX/awesome-claude-mods) - Topluluk tarafından derlenmiş bir Claude Code Modları rehberi: kullanım…
- [M-i-k-e-l/agent-state](https://github.com/M-i-k-e-l/agent-state) - Claude.
- [MDmubarak786/claude-mods](https://github.com/MDmubarak786/claude-mods) - Claude Code için topluluk modları: Claude Code içinde çalışan korumalar…
- [miiraheart/marginalia](https://github.com/miiraheart/marginalia) - Claude Code mod: select text in the conversation, then quote it into your…
- [minhtran3124/cc-ste-mod](https://github.com/minhtran3124/cc-ste-mod) - Claude Code mod that rewrites your prompt in ASD-STE100 Simplified Technical…
- [Mistakey/anvil](https://github.com/Mistakey/anvil) - Claude Code mod: keeps the prompt cache warm while you.
- [muellerei/enable-todo-tools](https://github.com/muellerei/enable-todo-tools) - Oturum başlangıcında CLAUDE_CODE_ENABLE_TODO_TOOLS ayarlayarak, bunları devre…
- [muellerei/sweet-spot](https://github.com/muellerei/sweet-spot) - Güvenli bir duraklama bekleyen, ardından oturumunuzu devralan veya oturumu…
- [muellerei/task-line](https://github.com/muellerei/task-line) - Claude Code modu: istemin üzerinde görev listesi başına bir satır;
- [nachtgold/claude-code-connect-four](https://github.com/nachtgold/claude-code-connect-four) - Claude Code içinde bir AI.
- [Nagato-Yuzuru/crabarium](https://github.com/Nagato-Yuzuru/crabarium) - A Claude Code mod: a pane that shows the main session and its subagents, with…
- [naoanao/agent-cross-check](https://github.com/naoanao/agent-cross-check) - Claude Code modu: başka bir kodlama ajanı deponuza commit yaptığında Claude…
- [naoanao/shared-repo-guard](https://github.com/naoanao/shared-repo-guard) - Birden çok AI ajanının paylaştığı depolar için Claude Code modu: gizli…
- [natansalvadorligabo/claude-usage-meter](https://github.com/natansalvadorligabo/claude-usage-meter) - A Claude Code mod that shows context, 5-hour session and weekly usage on the…
- [patrick-lai/claude-fish-stack-mod](https://github.com/patrick-lai/claude-fish-stack-mod) - fishStack: bir Claude Code modu. Salt okunur başlangıçlı kalıcı worktree.
- [PeterTing/claude-mod](https://github.com/PeterTing/claude-mod) - Hand-made and curated Claude Code mods: panes, status lines, slash commands…
- [philarete173/claude_mods](https://github.com/philarete173/claude_mods) - Claude masaüstü uygulamasının Code sekmesi için canlı oturum istatistikleri yan…
- [PickleBoxer/pickle](https://github.com/PickleBoxer/pickle) - pickle for Claude Code: language-agnostic engineering playbooks and principles…
- [pradyb/claude-mods](https://github.com/pradyb/claude-mods) - Mods for Claude Code: safety-guard blocks destructive commands and secret-file…
- [qr1x55/Detaly-Claude-Mod](https://github.com/qr1x55/Detaly-Claude-Mod) - Live progress bars above the prompt for long jobs in Claude Code.
- [rakavanagh/savvy-status](https://github.com/rakavanagh/savvy-status) - Claude Code mod: watch your subagents work as a crew of crabs, with live file…
- [ramonfabrega/mods](https://github.com/ramonfabrega/mods) - Claude Code mods: hooks modules that change the interface.
- [Risdon8/push-ups](https://github.com/Risdon8/push-ups) - Claude Code modu: Claude çalışırken yapılacak şınavlar. Jeton yok.
- [RobGruhl/claude-mod-learnings](https://github.com/RobGruhl/claude-mod-learnings) - Hook Chain: ELI5.
- [rolottr/claude-mod-meatproxy](https://github.com/rolottr/claude-mod-meatproxy) - Claude Code mod that shows drafts in a side pane, where you copy them as rich…
- [RomuloDrumond/claude-last-turn-diff](https://github.com/RomuloDrumond/claude-last-turn-diff) - A Claude Code mod: GitHub-style diffs of the files Claude edited in the last…
- [Ron-Nefyodov/pet-mod](https://github.com/Ron-Nefyodov/pet-mod) - A tiny terminal pet that lives on your Claude Code sessions. Community mod.
- [saadk408/stepline](https://github.com/saadk408/stepline) - Claude Code modu: plan modunda onayladığınız planı prompt.
- [saksham10arora-dotcom/awesome-claude-mods](https://github.com/saksham10arora-dotcom/awesome-claude-mods) - Özenle seçilmiş Claude Code modları listesi.
- [saksham10arora-dotcom/claude-frugal](https://github.com/saksham10arora-dotcom/claude-frugal) - Maliyetsiz mod: yardımcı ajanlar Haiku üzerinde çalışır;
- [saksham10arora-dotcom/claude-lofi](https://github.com/saksham10arora-dotcom/claude-lofi) - Oturumu takip eden bir lofi müzikleri: sakinlik, odaklanma, akış ve testlerin…
- [saksham10arora-dotcom/claude-teach-me](https://github.com/saksham10arora-dotcom/claude-teach-me) - Claude kod yazarken öğrenin: kodu değiştiren bir turdan sonra, tam o…
- [saksham10arora-dotcom/claude-vhs](https://github.com/saksham10arora-dotcom/claude-vhs) - Claude.
- [samykantari/secret-redact](https://github.com/samykantari/secret-redact) - Claude Code mod that masks secrets in tool outputs before Claude reads them.
- [sergeiwallace/beads-ui](https://github.com/sergeiwallace/beads-ui) - Beads task manager UI: a Claude Code mod for the TUI, an MCP UI app for Claude…
- [sergeiwallace/doc-editor](https://github.com/sergeiwallace/doc-editor) - A doc viewer and editor inside the Claude Code TUI, built as a Claude Code mod…
- [sgript-labs/claude-mods](https://github.com/sgript-labs/claude-mods) - Claude Code mods from Sgript: Sprout, a pixel creature above the prompt, plus…
- [StanislavKozachenko/claude-mods](https://github.com/StanislavKozachenko/claude-mods) - A collection of Claude Code mods: TypeScript function hooks, shipped as a…
- [steven-ngle/blade-of-commits](https://github.com/steven-ngle/blade-of-commits) - Dans eden pixel-art Malenia ile Claude Code için tek tıkla commit mesajları.
- [Tanish-Dev/claude-usage-band](https://github.com/Tanish-Dev/claude-usage-band) - Clawd Meter — Claude Code modu; Claude plan kullanımınızı.
- [TheBabaYaga/claude-session-flow](https://github.com/TheBabaYaga/claude-session-flow) - Her istemi, Claude.
- [theishandubey/claude-mods](https://github.com/theishandubey/claude-mods) - Modlardan oluşan bir Claude Code eklenti pazaryeri: Claude Code içinde bantlar…
- [VAlux/claude-session-progress](https://github.com/VAlux/claude-session-progress) - Claude Code modu: uzun süren görevler için animasyonlu ilerleme bandı ve…
- [Vansitha/clawd-watch](https://github.com/Vansitha/clawd-watch) - Üç küçük Claude Code modu: alt ajanlarınızın ne zaman tamamlanacağını görün…
- [varunmoka7/layman](https://github.com/varunmoka7/layman) - &quot;Kayboldum&quot; deyin, Claude son yanıtını günlük ifadelerle yeniden açıklasın.
- [varunmoka7/side-chat](https://github.com/varunmoka7/side-chat) - Çalışmanızın yanındaki bir bölmede Claude.
- [vinicius-sandes/crabhud](https://github.com/vinicius-sandes/crabhud) - A Claude Code mod: a crab that shows what Claude is doing, a progress bar for…
- [williamchong/cc-mod-caffeinate](https://github.com/williamchong/cc-mod-caffeinate) - A Claude Code mod that keeps your Mac.
- [wjsekrud/motive-mem](https://github.com/wjsekrud/motive-mem) - Claude Code mod: after every turn, a separate model reviews the change against…
- [wukonigcom/quanta-costa](https://github.com/wukonigcom/quanta-costa) - 🧾 Claude Code eklentisi: Claude Pro/Max kullanım limitleriniz, hız tahmini…
- [xinhuagu/oh-my-claude-mods](https://github.com/xinhuagu/oh-my-claude-mods) - Claude Code için modlar. agent-crew: alt aracılarınızı rol, model, mevcut araç…
- [yyh-001/dsh-supermarket](https://github.com/yyh-001/dsh-supermarket) - 超级市场：面向 AI 的 DSH 多市场插件，统一发现、管理与使用 Skills、MCP、Claude Mods、整合包和 Agent 预设.
- [zexion7873/usage-band](https://github.com/zexion7873/usage-band) - Always-on band above the Claude Code prompt: context fill and rate-limit…
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - Durdurulamaz Anthropic PBC ekibinden (bağlantısı yoktur), kodlama…
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) - Neler olduğunu gösteren bir Claude Code eklentisi - bağlam kullanımı, etkin…
- [sirmalloc/ccstatusline](https://github.com/sirmalloc/ccstatusline) - 🚀 Claude Code CLI için powerline desteği, temalar ve daha fazlasını içeren…
- [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) - Claude Code.
- [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) - Claude Code ve Codex için AI video becerisi — Remotion ile sinematik ürün…
- [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) - Claude Code.
- [op7418/guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill) - 🪧 Claude Code / Codex skill — Xiaohongshu karuselleri ve WeChat 21:9+1:1 kapak…
- [persiyanov/herdr-reviewr](https://github.com/persiyanov/herdr-reviewr) - Kodlama aracınızın diff.
- [uppinote20/claude-dashboard](https://github.com/uppinote20/claude-dashboard) - Bağlam kullanımı, API hız sınırları ve maliyet takibiyle Claude Code için…
- [starbaser/ccproxy](https://github.com/starbaser/ccproxy) - Claude Code için modlar oluşturun: Her isteğe kanca ekleyin, her yanıtı…
- [NYCU-Chung/cc-statusline](https://github.com/NYCU-Chung/cc-statusline) - Claude Code için kapsamlı statusline dashboard.
- [gwittebolle/claude-carbon](https://github.com/gwittebolle/claude-carbon) - claude-carbon: Claude Code oturumlarınızın karbon ayak izini takip edin.
- [JohnnyVizz/claude-kit](https://github.com/JohnnyVizz/claude-kit) - Herkese açık Claude Code Skills.
- [awesomezun/claude-statusline](https://github.com/awesomezun/claude-statusline) - An aesthetic statusline for Claude Code by awesomezun.
- [escapeboy/claude-code-kit](https://github.com/escapeboy/claude-code-kit) - Claude Code için Skills.
- [mvalentsev/awesome-free-ai-coding](https://github.com/mvalentsev/awesome-free-ai-coding) - 📡 Yasal ücretsiz LLM APIs ve coding agent.
- [arturogarrido/claudinho](https://github.com/arturogarrido/claudinho) - ⚽ Takip ettiğiniz müsabaka için canlı futbol skorları, fikstürler ve puan…
- [johncattrall/keymap-ai](https://github.com/johncattrall/keymap-ai) - Kodlama aracınızı klavye ürün yazılımı uzmanına dönüştüren Agent Skill.
- [benabraham/claude-code-status-line](https://github.com/benabraham/claude-code-status-line) - Statusline script for Claude Code CLI – shows context and quota usage, model…
- [ashafizullah/claude-code-muslim-mods](https://github.com/ashafizullah/claude-code-muslim-mods) - Claude Code içinde namaz vakitleri, Hicri tarih, zikirler, günlük ayet, sünnet…
- [rlaope/deepseek-bot](https://github.com/rlaope/deepseek-bot) - DeepSeek Harness gonna be your personal agent, a self-hosted AI teammate that…
- [hoobnn/hoobnn-agent-mods](https://github.com/hoobnn/hoobnn-agent-mods) - Claude Code, pi ve DeepSeek Harness için eklenti koleksiyonu: durum çubuğu…
- [pierrebelin/claude-code-toolkit](https://github.com/pierrebelin/claude-code-toolkit) - .NET DDD/Clean Architecture için taşınabilir Claude Code araç seti: katı TDD…
- [FlorinI/Florians-Claude-Code-Kit](https://github.com/FlorinI/Florians-Claude-Code-Kit) - Cross-platform Node status line for Claude Code, plus /handover…
- [jcdendrite/claude-config](https://github.com/jcdendrite/claude-config) - Taşınabilir Claude Code global yapılandırması: özel beceriler, PreToolUse…
- [manson341349-beep/claude-desktop-mods](https://github.com/manson341349-beep/claude-desktop-mods) - Claude Desktop.
- [mutlumehmet/claude-plugins](https://github.com/mutlumehmet/claude-plugins) - Her gün kullandığım Claude Code eklentileri: herkesin makinesinde çalışacak…
- [alpadalar/ccinfobar](https://github.com/alpadalar/ccinfobar) - Sürükle ve bırak düzenleyicisine sahip, özelleştirilebilir bir Claude Code…
- [ogxo-io/plugins](https://github.com/ogxo-io/plugins) - Claude Code plugin marketplace from ogxo: cost-aware agent routing with a live…
- [rapita/claude-grammar](https://github.com/rapita/claude-grammar) - Background English grammar coach for Claude Code.
- [will-pagane/claude-superdev-harness](https://github.com/will-pagane/claude-superdev-harness) - Minha config pessoal do Claude Code — CLAUDE.md global, statusline custom…
- [abdullahkavakli/let-them-talk](https://github.com/abdullahkavakli/let-them-talk) - Claude Code ajanlarınız için görsel pano: oturumları, alt ajanları ve arka plan…
- [cativo23/lumira](https://github.com/cativo23/lumira) - Real-time statusline HUD for Claude Code and Qwen Code.
- [cmfok/dsh-feishucard](https://github.com/cmfok/dsh-feishucard) - DSH &lt;-&gt; Feishu (Lark) bridge, self-developed (not a fork): streaming reply card…
- [darthmolen/hytale-claude-code-marketplace](https://github.com/darthmolen/hytale-claude-code-marketplace) - Hytale oyununda modları kolaylaştırmak için Claude Code Eklentileri ve…
- [hopp1395/cc-outline](https://github.com/hopp1395/cc-outline) - Windows Terminal ve tmux içinde Claude Code için bölünmüş panel görüntüleyici…
- [romnycristopher/claude-am-mods](https://github.com/romnycristopher/claude-am-mods) - Claude Code Awesome Media modları için depo.
- [fbincon/claude-code-statusline](https://github.com/fbincon/claude-code-statusline) - Configurable Claude Code status line for Linux, WSL, Windows and macOS, with…
- [kgdemir/claude-agentic-os](https://github.com/kgdemir/claude-agentic-os) - Claude Agentic OS: portable Claude Code setup — global rules, plugin set…
- [michalschroeder/claude-statusline](https://github.com/michalschroeder/claude-statusline) - My Claude Code statusline + supporting hooks.
- [RaggioS/claude-code-statusline](https://github.com/RaggioS/claude-code-statusline) - Single-file POSIX statusline for Claude Code: dir, git branch, model, context…
- [aquahitt/claude-code-limit-alerts](https://github.com/aquahitt/claude-code-limit-alerts) - Usage-limit alerts for Claude Code: macOS notifications, in-app warnings and…
- [carterptull/ampline-claude](https://github.com/carterptull/ampline-claude) - Claude Code için güçlendirilmiş renk derecelendirmeli, bağımlılıksız bir durum…
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
- [ctfbio/claude-code-statusline](https://github.com/ctfbio/claude-code-statusline) - Profesyonel düzeyde Claude Code durum satırı: oturum süresi, ECB döviz…
- [drewkhouryorg/claude-statusline](https://github.com/drewkhouryorg/claude-statusline) - Claude Code için bir durum satırı: bağlam, sınırlar ve haftanın temposu…
- [fabifont/claude-statusline](https://github.com/fabifont/claude-statusline) - Minimal offline Claude Code status line written in Rust.
- [Fibonach0/claude-code-gadgets-linux](https://github.com/Fibonach0/claude-code-gadgets-linux) - Accesorios para Claude Code en Linux (Debian/Ubuntu): % de uso en la bandeja…
- [hieuvo/claude-imgview](https://github.com/hieuvo/claude-imgview) - Görüntüleri Claude Code içinde önizleyin: resmi açmak için bir yanıtın…
- [IchiSieben/claude-kit](https://github.com/IchiSieben/claude-kit) - An operating kit for Claude Code: routing by lane, subagents, a review gate…
- [jamesyoung-dev/claude-cache-countdown](https://github.com/jamesyoung-dev/claude-cache-countdown) - Keeps claude_statusline_plus.
- [jaszerr/Claude-Statusline](https://github.com/jaszerr/Claude-Statusline) - Minimal, extensible status line for Claude Code.
- [jdmalter/claude-code-statusline](https://github.com/jdmalter/claude-code-statusline) - A muted three-line status line for Claude Code, in bash for Git Bash on Windows.
- [JesseWebDotCom/claude-overview](https://github.com/JesseWebDotCom/claude-overview) - A live Claude Code side pane: Claude and Codex usage limits, context breakdown…
- [jinhuang712/claude-super-statusline](https://github.com/jinhuang712/claude-super-statusline) - A SUPER customizable &amp; pretty statusline for Claude — in Claude Code and the…
- [lucasmm96/claude-statusline](https://github.com/lucasmm96/claude-statusline) - Claude Code durum satırı kancası — oturumlar arasında token kullanımını ve…
- [milan44i/claude-setup](https://github.com/milan44i/claude-setup) - An installable Claude Code setup: self-healing TypeScript hook…
- [mileschintw/claude-cache-timer](https://github.com/mileschintw/claude-cache-timer) - Prompt cache countdown and auto-compact for Claude Code.
- [mr-pmillz/claude-code-pmillz-statusline](https://github.com/mr-pmillz/claude-code-pmillz-statusline) - a status line variant for claude code that shows useful info.
- [msinclair-sudo/claude-code-setup](https://github.com/msinclair-sudo/claude-code-setup) - Claude Code environment installer: skills, statusline, hooks, permissions, and…
- [ni-c/claude-usage-statusline](https://github.com/ni-c/claude-usage-statusline) - Claude Code status line with rate-limit usage and reset countdowns, git branch…
- [ppezzull/glm-claude-hud](https://github.com/ppezzull/glm-claude-hud) - Show GLM Coding Plan (Z.ai/Zhipu) token usage in the claude-hud statusline for…
- [rperez93/claude-progress](https://github.com/rperez93/claude-progress) - Progress bars with an honest ETA in the Claude Code status line: count…
- [Rubio-Enterprises/claude-statusline](https://github.com/Rubio-Enterprises/claude-statusline) - Özel Claude Code durum satırı (üst kaynak: kamranahmedse/claude-statusline).
- [SACRVM/claude-code-statusline](https://github.com/SACRVM/claude-code-statusline) - A Claude Code status line with real Anthropic usage % (5h + 7d), context bar…
- [spyrad/claude-code-statusline](https://github.com/spyrad/claude-code-statusline) - A status line for Claude Code on Windows: model, repo and branch, rate-limit…
- [stelsoft/claude-code-statusline](https://github.com/stelsoft/claude-code-statusline) - Zero-dependency bash statusline for Claude Code: context usage bar + 5h/7d…
- [TheGnarCo/claude-statusline](https://github.com/TheGnarCo/claude-statusline) - The Gnar Company.
- [tsalkin/claude-code-statusline](https://github.com/tsalkin/claude-code-statusline) - Two-line status line for Claude Code: context, cache health, effort drift…
- [tumuyijiao114514/claude-pulse](https://github.com/tumuyijiao114514/claude-pulse) - ⚡ Claude Code için Evrensel Çok Protokollü StatusLine, Kendi Kendine Öğrenen…
- [u007/claude-plugins](https://github.com/u007/claude-plugins) - Personal Claude Code plugin marketplace: context-status statusline and…
- [Winn-Gaoti-Studio/claude-code-statusline](https://github.com/Winn-Gaoti-Studio/claude-code-statusline) - A Claude Code statusline with gradient progress bars, color-graded session…
- [yacb2/claude-statusline](https://github.com/yacb2/claude-statusline) - Three-line Claude Code status line: context depth, cross-session rate limits…
- [YoniYon00/claude-feedback-rings](https://github.com/YoniYon00/claude-feedback-rings) - Context Rot Detector 2026 - Claude Code Ajanları için Proaktif AI Bellek ve Hız…
- [ZeyuSi-2099/claude-code-statusline](https://github.com/ZeyuSi-2099/claude-code-statusline) - Claude Code custom statusline (macOS): cwd/git/model/effort/ctx/5h/wk in one…
- [zhuyansen/awesome-claude-code-hooks](https://github.com/zhuyansen/awesome-claude-code-hooks) - Claude Code kancaları, alt ajanları ve durum satırları: türe göre düzenlenmiş…
- [ratelworks/token-horse](https://github.com/ratelworks/token-horse) - Token usage reactive horse pet for Claude Code statuslines and Codex CLI…
- [ishuagrawal/clawdhouse](https://github.com/ishuagrawal/clawdhouse) - Claude Code için modlar: işlev kancaları üzerine kurulu bölmeler, bantlar ve…
- [ashishsk93/baton-mods](https://github.com/ashishsk93/baton-mods) - Görevleri Claude Code oturumlarınız arasında aktarın.
- [charlie947/mod-maker](https://github.com/charlie947/mod-maker) - Mod Maker: Claude Code.
- [devnix/burnbar](https://github.com/devnix/burnbar) - Rich statusline plugin for Claude Code — context window progress bar, token…
- [lahoramaker/mods-mcp](https://github.com/lahoramaker/mods-mcp) - Fablab.
- [Rimcat-JA/translate-ck3-mods](https://github.com/Rimcat-JA/translate-ck3-mods) - Yerel bir LLM ile CK3 modlarını çevirmek için Codex ve Claude Code becerisi.
- [sTomerG/agent-kit](https://github.com/sTomerG/agent-kit) - Claude Code için açık kaynaklı modlar ve diğer uzantılar.
- [Isllanrx/status_cli](https://github.com/Isllanrx/status_cli) - Status line in Rust for Claude Code, Codex CLI and Antigravity CLI: usage…

</details>

<a id="dsh-cordis"></a>

## DSH ve Cordis eklenti ekosistemleri

DeepSeek Harness ve Cordis aynı yere farklı bir yönden ulaşır: onlar için eklenti, mod mekanizmasıdır; dolayısıyla oradaki bir eklenti, buradaki bir moda denktir.

<details>
<summary>🧵 <b><a href="https://github.com/deepseek-ai/deepseek-harness">deepseek-ai/deepseek-harness</a></b> · ⭐250372 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Özet

DeepSeek Harness: Everything is a Plugin.

<sub>🔧 Kodda kullanıldığı bulundu: `packages/experimental/claude-code-mods/src/elements.ts`, `packages/experimental/claude-code-mods/src/matcher.ts`, `packages/experimental/claude-code-mods/src/index.ts`, `docs/config-catalog.zh.md`</sub>

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                    |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |
| Dil      | TypeScript                                                               |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **250372** |
| Son gönderme   | 2026-10-15 |
| İlk listelenme | 2026-10-15 |

🏷 `ai-agents` · `cordis` · `dsh` · `dsh-plugin`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b> · ⭐74991 · TypeScript · 👁️ observed · 0 天</summary>

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
| Yıldızlar      | **74991**  |
| Son gönderme   | 2026-10-15 |
| İlk listelenme | 2026-10-04 |

🏷 `agentic-ai` · `agentic-framework` · `agentic-workflow` · `agents` · `ai-agents` · `ai-assistant` · `ai-skills` · `autonomous-agents`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/2ca82c9c9a7fca31.gif" width="100%" alt="ruvnet/ruflo animation"><br><sub>animasyonlu kayıt</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ccch1mneyyy/dsh-TUI">ccch1mneyyy/dsh-TUI</a></b> · ⭐4635 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Özet

DSH'nin resmî olarak en çok önerilen TUI eklentisi — yüksek performans, düşük ek yük, sevimli piksel balinası, akıcı fare etkileşimi. npm üzerinden tek komutla kurulum. / DSH 官方首推的 TUI 插件，高性能低占用，可爱像素鲸鱼，流畅鼠标交互，npm 一键安装

<sub>🔧 Kodda kullanıldığı bulundu: `scripts/verify-kernel-commands.tsx`</sub>

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                    |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |
| Dil      | TypeScript                                                               |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **4635**   |
| Son gönderme   | 2026-10-15 |
| İlk listelenme | 2026-10-12 |

🏷 `claude-code` · `coding-agent` · `deepseek` · `deepseek-harness` · `dsh-plugin` · `ink` · `react` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ccch1mneyyy--dsh-tui/18fd45f8f1eaca04.png" width="100%" alt="ccch1mneyyy/dsh-TUI screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/hashgraph-online/awesome-ai-plugins">hashgraph-online/awesome-ai-plugins</a></b> · ⭐702 · Python · 👁️ observed · 0 天</summary>

##### 📝 Özet

Claude Code, OpenAI Codex / ChatGPT, Gemini, Antigravity, Pi / Oh My Pi, Grok, OpenCodek DSH, Kimi ve daha fazlası dâhil yapay zekâ asistanları için en iyi harika yapay zekâ eklentilerinin özenle seçilmiş listesi. https://hol.org/plugins

<sub>🔧 Kodda kullanıldığı bulundu: `README.md`</sub>

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                    |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |
| Dil      | Python                                                                   |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **702**    |
| Son gönderme   | 2026-10-15 |
| İlk listelenme | 2026-10-04 |

🏷 `ai-assistant` · `ai-plugin` · `awesome` · `awesome-list` · `best-ai-plugins` · `best-antigravity-plugins` · `best-claude-plugins` · `best-codex-plugins`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/morluto/rea">morluto/rea</a></b> · ⭐266429 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Yıldızlar      | **266429** |
| Son gönderme   | 2026-10-15 |
| İlk listelenme | 2026-10-05 |

🏷 `agent-skills` · `ai-agents` · `binary-analysis` · `claude-code` · `cli` · `codex` · `cordis` · `decompiler`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--rea/f46ca8b1518ae39f.png" width="100%" alt="morluto/rea screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/nexu-io/open-design">nexu-io/open-design</a></b> · ⭐101333 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

The 1st Collaborative AI Design Agent Workspace. Local-first and open source. Create prototypes, websites, apps, dashboards, presentations, images, and videos with your team and AI agents. Share work, exchange feedback, and iterate together in one workspace.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | TypeScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **101333** |
| Son gönderme   | 2026-10-15 |
| İlk listelenme | 2026-10-04 |

🏷 `agent-skills` · `ai-design` · `byok` · `claude-code-for-design` · `claude-design` · `codex-design` · `coding-agents` · `cursor-design`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nexu-io--open-design/a1049df34322d3ce.png" width="100%" alt="nexu-io/open-design screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/tt-a1i/archify">tt-a1i/archify</a></b> · ⭐84002 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Yıldızlar      | **84002**  |
| Son gönderme   | 2026-10-15 |
| İlk listelenme | 2026-10-04 |

🏷 `agent-skills` · `ai-agents` · `architecture-diagram` · `claude-code` · `claude-skills` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tt-a1i--archify/71b7d4b2427db202.png" width="100%" alt="tt-a1i/archify screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/esengine/DeepSeek-Reasonix">esengine/DeepSeek-Reasonix</a></b> · ⭐35805 · Go · 🔎 inferred · 0 天</summary>

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
| Yıldızlar      | **35805**  |
| Son gönderme   | 2026-10-15 |
| İlk listelenme | 2026-10-06 |

🏷 `agent` · `agent-framework` · `ai-agent` · `ai-coding` · `cli` · `coding-agent` · `deepseek` · `developer-tools`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/anywhere-labs/dsh-desktop">anywhere-labs/dsh-desktop</a></b> · ⭐30954 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

DeepSeek Harness (DSH) eklenti ekosistemi için geliştirilmiş modern masaüstü çözümü. Her şey bir «eklenti»dir; masaüstünün kendisi de bir «eklenti»dir.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | TypeScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **30954**  |
| Son gönderme   | 2026-10-15 |
| İlk listelenme | 2026-10-13 |

🏷 `cordis` · `cordis-plugin` · `deepseek` · `deepseek-harness` · `desktop` · `dsh` · `dsh-plugin` · `dsh-plugin-desktop`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anywhere-labs--dsh-desktop/b72e79b4c3cadb81.png" width="100%" alt="anywhere-labs/dsh-desktop screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/titanwings/distilly">titanwings/distilly</a></b> · ⭐25659 · Python · 🔎 inferred · 2 天</summary>

##### 📝 Özet

Distilly — herhangi bir Agent veya Bot için nasıl düşündüklerini yeniden kullanılabilir Skills'e damıtın. Eski adı Colleague Skill（原同事 Skill）.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | Python                                                                                          |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **25659**  |
| Son gönderme   | 2026-10-13 |
| İlk listelenme | 2026-10-13 |

🏷 `agent-skills` · `agentic-ai` · `ai-agent` · `ai-agents` · `ai-assistants` · `ai-persona` · `claude-code` · `claude-skills`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/titanwings--distilly/1e118bb52fdcbd1c.png" width="100%" alt="titanwings/distilly screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/awesome-dsh-plugin/awesome-dsh-plugin">awesome-dsh-plugin/awesome-dsh-plugin</a></b> · ⭐18885 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

A curated list of plugins for DeepSeek Harness (dsh) · DeepSeek Harness 插件精选列表

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | JavaScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **18885**  |
| Son gönderme   | 2026-10-15 |
| İlk listelenme | 2026-10-15 |

🏷 `awesome` · `awesome-list` · `deepseek-harness` · `dsh` · `dsh-plugin`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/cordiverse/cordis">cordiverse/cordis</a></b> · ⭐9205 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

Uzamsal-zamansal birleştirilebilirlik meta-çerçevesi

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | TypeScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **9205**   |
| Son gönderme   | 2026-10-15 |
| İlk listelenme | 2026-10-13 |

🏷 `effect` · `framework` · `nodejs` · `plugin`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/zhu1090093659/dsh-web">zhu1090093659/dsh-web</a></b> · ⭐8795 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

DeepSeek Harness (DSH) Web 插件聚合生态 · Her şey bir eklentidir, Creative Workshop üzerinden dağıtılır｜｜DeepSeek Harness (DSH) Web Eklenti Toplama Ekosistemi · Her şey bir eklentidir, Creative Workshop üzerinden dağıtılır

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | TypeScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **8795**   |
| Son gönderme   | 2026-10-15 |
| İlk listelenme | 2026-10-13 |

🏷 `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-web` · `dsh-web-ui`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zhu1090093659--dsh-web/5153c3c61827ebb8.jpg" width="100%" alt="zhu1090093659/dsh-web screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/liustack/modlens">liustack/modlens</a></b> · ⭐4270 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

The first vision plugin for DeepSeek Harness, and the vision bridge for every text-only coding agent. Paste an image, get structured JSON evidence (OCR, layout, semantics). | 全网最强 DeepSeek Harness 外挂视觉插件，为 DeepSeek、GLM 等纯文本模型外挂视觉能力，粘贴图片即得结构化 JSON 证据（OCR、版面、语义）。

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | TypeScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **4270**   |
| Son gönderme   | 2026-10-15 |
| İlk listelenme | 2026-10-16 |

🏷 `agent-skills` · `claude-code` · `claude-skills` · `codex` · `cordis` · `deepseek` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/liustack--modlens/8fbbbd4e56d098c7.jpg" width="100%" alt="liustack/modlens screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-tauri/deepseek-harness-desktop">dsh-tauri/deepseek-harness-desktop</a></b> · ⭐3019 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Yıldızlar      | **3019**   |
| Son gönderme   | 2026-10-15 |
| İlk listelenme | 2026-10-15 |

🏷 `deepseek` · `deepseek-harness` · `desktop` · `dsh` · `dsh-desktop` · `dsh-plugin` · `tauri`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dsh-tauri--deepseek-harness-desktop/f281725e73da1059.png" width="100%" alt="dsh-tauri/deepseek-harness-desktop screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/AdamPlatin123/dsh-plugin-radar">AdamPlatin123/dsh-plugin-radar</a></b> · ⭐1473 · Python · 🔎 inferred · 0 天</summary>

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
| Yıldızlar      | **1473**   |
| Son gönderme   | 2026-10-15 |
| İlk listelenme | 2026-10-15 |

🏷 `agent-plugins` · `continuous-validation` · `deepseek-harness` · `dsh` · `dsh-plugin` · `ecosystem-radar` · `plugin-registry`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/adamplatin123--dsh-plugin-radar/fb6ad7eb8891212c.jpg" width="100%" alt="AdamPlatin123/dsh-plugin-radar screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/vshulcz/deja-vu">vshulcz/deja-vu</a></b> · ⭐1204 · Go · 🔎 inferred · 0 天</summary>

##### 📝 Özet

Coding agent memory for Claude Code, Codex, Cursor and 39 more, built from the session history already on your disk. Local search, MCP and hooks, no LLM, one Go binary.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | Go                                                                                              |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **1204**   |
| Son gönderme   | 2026-10-15 |
| İlk listelenme | 2026-10-04 |

🏷 `agent-memory` · `ai-memory` · `claude-code` · `claude-code-hooks` · `claude-code-plugins` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/8033ba54a9424c88.png" width="100%" alt="vshulcz/deja-vu screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/5fb930f1983f270b.gif" width="100%" alt="vshulcz/deja-vu animation"><br><sub>animasyonlu kayıt</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/liustack/modsearch">liustack/modsearch</a></b> · ⭐703 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

🥇 The strongest free web search plugin for DeepSeek Harness, and the search bridge for every model without native web access. Free, no signup, no API key. Ask the web or X, get structured JSON evidence. | 🥇 全网最强的 DeepSeek Harness 免费联网搜索插件，免费免注册免 API key。为不能联网的模型补上搜索，问网页或 X，拿回结构化 JSON 证据（搜索、抓取、引用）。

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | TypeScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **703**    |
| Son gönderme   | 2026-10-15 |
| İlk listelenme | 2026-10-16 |

🏷 `agent-skills` · `agentic-workflow` · `claude-code` · `claude-skills` · `codex` · `cordis` · `deepseek` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/liustack--modsearch/3f14f3226c889c46.jpg" width="100%" alt="liustack/modsearch screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Ikalus1988/MisakaNet">Ikalus1988/MisakaNet</a></b> · ⭐526 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Özet

📚 AI Agents'ın doğrulanmış hata ayıklama deneyimlerini eşzamansız olarak paylaşması ve araması için sıfır bağımlılıklı, git destekli bir mikro ders kütüphanesi. | https://misakanet.org

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
| Son gönderme   | 2026-10-15 |
| İlk listelenme | 2026-10-13 |

🏷 `action` · `agents` · `cloudflare-workers` · `codex` · `cordis-plugin` · `d1` · `deepseek-harness` · `deepseek-harness-plugin`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ikalus1988--misakanet/f6853900d49aba17.jpg" width="100%" alt="Ikalus1988/MisakaNet screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/vibeinging/dsh-desktop">vibeinging/dsh-desktop</a></b> · ⭐483 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

DeepSeek Harness Desktop App: a local AI desktop workspace for DSH Sessions, projects, files, web research, plugins, and Office artifacts.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | JavaScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **483**    |
| Son gönderme   | 2026-10-15 |
| İlk listelenme | 2026-10-16 |

🏷 `agentic-workflows` · `ai-agent` · `ai-workbench` · `data-analysis` · `deepseek-harness` · `desktop-app` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vibeinging--dsh-desktop/ccbf15d3a2c42437.png" width="100%" alt="vibeinging/dsh-desktop screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/cv-superding/dsh-deepseek-web-login">cv-superding/dsh-deepseek-web-login</a></b> · ⭐274 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

Unofficial DSH (DeepSeek Harness) plugin: use chat.deepseek.com web models as an LLM provider - browser-login capture, PoW solving, SSE streaming, prompting-based tool calls.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | JavaScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **274**    |
| Son gönderme   | 2026-10-15 |
| İlk listelenme | 2026-10-15 |

🏷 `browser-automation` · `cordis` · `cordis-plugin` · `deepseek` · `deepseek-harness` · `dsh` · `llm-provider`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/cv-superding--dsh-deepseek-web-login/b95392c45786ce03.png" width="100%" alt="cv-superding/dsh-deepseek-web-login screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/acryldev/acryl">acryldev/acryl</a></b> · ⭐256 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

ACRYL - Agent Context Relay Yielding Lifecycles. One persistent workspace, one canonical context, any coding agent.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | TypeScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **256**    |
| Son gönderme   | 2026-10-15 |
| İlk listelenme | 2026-10-16 |

🏷 `acryl` · `agent-context-relay` · `agentic` · `agentic-ai` · `agentic-coding` · `agentic-development-environment` · `agentic-workflow` · `agentic-workflows`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/acryldev--acryl/47cfe6b23e87eea1.png" width="100%" alt="acryldev/acryl screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Nwflower/dsh-claude-style">Nwflower/dsh-claude-style</a></b> · ⭐164 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

Claude Code Desktop theme for DeepSeek Harness｜ 为 DeepSeek Harness 网页 GUI 打造的 Claude Code 桌面主题

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | TypeScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **164**    |
| Son gönderme   | 2026-10-15 |
| İlk listelenme | 2026-10-15 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-desktop` · `cordis` · `dark-mode` · `deepseek-harness` · `desktop-theme`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Nwflower/dsh-claude-style/master/docs/screenshots/claude-home-dark.png" width="100%" alt="Nwflower/dsh-claude-style screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Nwflower/dsh-claude-style/master/docs/gifs/idle.gif" width="100%" alt="Nwflower/dsh-claude-style animation"><br><sub>animasyonlu kayıt</sub></td>
</tr></table>

<sub>Yeniden dağıtıma izin veren bir lisans belirtilmediği için varlığa upstream deposundan doğrudan bağlantı veriliyor.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Totoro-qaq/dsh-plugin-bridge">Totoro-qaq/dsh-plugin-bridge</a></b> · ⭐163 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

DeepSeek Harness plugin for previewable cross-preset session migration. Fixed-schema handoffs preserve state, source-model intent, and unresolved images; the original session stays untouched.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | JavaScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **163**    |
| Son gönderme   | 2026-10-15 |
| İlk listelenme | 2026-10-15 |

🏷 `context-migration` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `preset-migration` · `session-migration`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/totoro-qaq--dsh-plugin-bridge/568de849cd2e9608.png" width="100%" alt="Totoro-qaq/dsh-plugin-bridge screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/totoro-qaq--dsh-plugin-bridge/b4a12cab0ba15f06.gif" width="100%" alt="Totoro-qaq/dsh-plugin-bridge animation"><br><sub>animasyonlu kayıt</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/FeatherHunter/dsh-mattpocock-skills-deck">FeatherHunter/dsh-mattpocock-skills-deck</a></b> · ⭐151 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

Kurulumla birlikte mattpocock/skills v1.3.1 içindeki 27 mühendislik ve verimlilik becerisi hazır gelir; becerileri manuel olarak kurmanız gerekmez. 40 milyar token ile oluşturulan bu eklenti, özgün becerilerin üzerinde 10 kat geliştirme verimliliği sunar ve yeni başlayanların bu beceri paketine daha hızlı alışmasına yardımcı olur. GitHub issue'ları tam olarak desteklenir; Markdown önizleme sürümündedir; GitLab şu anda desteklenmemektedir. Kullanımınız ve desteğiniz için teşekkürler 💗

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | JavaScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **151**    |
| Son gönderme   | 2026-10-15 |
| İlk listelenme | 2026-10-13 |

🏷 `agent` · `ai` · `claude` · `deepseek-harness` · `dsh` · `dsh-better-sidebar` · `dsh-plugin` · `github-issues`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/featherhunter--dsh-mattpocock-skills-deck/c4bd78003446c161.png" width="100%" alt="FeatherHunter/dsh-mattpocock-skills-deck screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Duskriver/dsh-opencode-go">Duskriver/dsh-opencode-go</a></b> · ⭐133 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

用于deepseek-harness的opencode-go套餐增强插件。多账号管理、额度UI面板、自动更新模型。An opencode-go subscription enhancement plugin for deepseek-harness — featuring multi-account management, a quota UI panel, and automatic model updates.

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
| Son gönderme   | 2026-10-15 |
| İlk listelenme | 2026-10-16 |

🏷 `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/duskriver--dsh-opencode-go/a745e1f7913eaf45.png" width="100%" alt="Duskriver/dsh-opencode-go screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/duskriver--dsh-opencode-go/d75a597695831f54.gif" width="100%" alt="Duskriver/dsh-opencode-go animation"><br><sub>animasyonlu kayıt</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Sutera-Diffusus/dsh-whale-musume">Sutera-Diffusus/dsh-whale-musume</a></b> · ⭐128 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

DeepSeek Harness masaüstü evcil hayvan eklentisi: enerjik balina kız maskot kod yazarken sana eşlik eder 🐋 DSH masaüstü 0.2.0-rc.2 ve eski Web sürümünü destekler (desktop pet / mascot, local-first)

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | JavaScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **128**    |
| Son gönderme   | 2026-10-15 |
| İlk listelenme | 2026-10-13 |

🏷 `ai-assistant` · `ai-companion` · `cordis` · `cute` · `deepseek` · `deepseek-harness` · `desktop-app` · `desktop-mascot`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/sutera-diffusus--dsh-whale-musume/cb85aa05cce65f77.png" width="100%" alt="Sutera-Diffusus/dsh-whale-musume screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Microqian2th/dsh-codex-effort-slider">Microqian2th/dsh-codex-effort-slider</a></b> · ⭐124 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

Codex 风格的推理等级滑条（DeepSeek Harness 插件）：可拖动连续滑条 + 高档位渐变星尘特效

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | JavaScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **124**    |
| Son gönderme   | 2026-10-15 |
| İlk listelenme | 2026-10-15 |

🏷 `ai` · `ai-agents` · `codex` · `deepseek` · `deepseek-ai` · `deepseek-harness` · `deepseek-plugin` · `deepseek-v4`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/microqian2th--dsh-codex-effort-slider/eb0c0410e75227ba.png" width="100%" alt="Microqian2th/dsh-codex-effort-slider screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/WestFox-AwA/dsh-prompt-optimizer">WestFox-AwA/dsh-prompt-optimizer</a></b> · ⭐119 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Yıldızlar      | **119**    |
| Son gönderme   | 2026-10-15 |
| İlk listelenme | 2026-10-15 |

🏷 `agent-workflow` · `ai-agent` · `cordis` · `deepseek` · `dsh` · `dsh-plugin` · `llm` · `prompt-engineering`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/westfox-awa--dsh-prompt-optimizer/3098cfd264cf8ca0.png" width="100%" alt="WestFox-AwA/dsh-prompt-optimizer screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/EricWang1358/dsh-web-studyhub">EricWang1358/dsh-web-studyhub</a></b> · ⭐107 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

StudyHub: a DeepSeek Harness (DSH) plugin that turns your own material into questions and spaced review · 把自己的资料变成题目与间隔复习的 DSH 学习插件

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | JavaScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **107**    |
| Son gönderme   | 2026-10-15 |
| İlk listelenme | 2026-10-16 |

🏷 `dsh` · `dsh-plugin` · `education` · `flashcards` · `spaced-repetition` · `study`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ericwang1358--dsh-web-studyhub/1e4a97948bc59f9d.jpg" width="100%" alt="EricWang1358/dsh-web-studyhub screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/BotHarness/DeepSeekBot">BotHarness/DeepSeekBot</a></b> · ⭐98 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

Open-source GrokBot alternative built on DeepSeek Harness. Build your personal bot team: multiple personal agents with persistent memory, identities and permissions, extensible through DSH plugins.｜基于 DeepSeek Harness 的开源 GrokBot 平替：有长期记忆的个人 AI Bot 团队，支持多 Bot 协作、身份权限与插件生态扩展。MIT.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | TypeScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **98**     |
| Son gönderme   | 2026-10-15 |
| İlk listelenme | 2026-10-15 |

🏷 `agent-memory` · `ai-agent` · `bot-marketplace` · `deepseek` · `deepseek-bot` · `deepseek-harness` · `deepseekbot` · `discord-bot`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/botharness--deepseekbot/1e570820fa589149.jpg" width="100%" alt="BotHarness/DeepSeekBot screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/botharness--deepseekbot/bcaac533fb86df37.gif" width="100%" alt="BotHarness/DeepSeekBot animation"><br><sub>animasyonlu kayıt</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Fishsb/dsh-prompt-enhancer">Fishsb/dsh-prompt-enhancer</a></b> · ⭐92 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

DeepSeek Harness (DSH) 插件：✨ 提示词一键增强 + 💬 语音识别（说完自动停·云端/本地双引擎）· 附 🔁 服务异常一键重启

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | JavaScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **92**     |
| Son gönderme   | 2026-10-15 |
| İlk listelenme | 2026-10-16 |

🏷 `deepseek` · `deepseek-harness` · `dsh-plugin` · `plugin` · `prompt-engineering`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Fishsb/dsh-prompt-enhancer/main/docs/screenshots/voice-main.png" width="100%" alt="Fishsb/dsh-prompt-enhancer screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

<sub>Yeniden dağıtıma izin veren bir lisans belirtilmediği için varlığa upstream deposundan doğrudan bağlantı veriliyor.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/kukucaiCndy/Corum-Harness">kukucaiCndy/Corum-Harness</a></b> · ⭐77 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Yıldızlar      | **77**     |
| Son gönderme   | 2026-10-15 |
| İlk listelenme | 2026-10-11 |

🏷 `agent` · `agent-os` · `ai-agent` · `cordis` · `desktop-app` · `dsh` · `electron` · `harness`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/kukucaicndy--corum-harness/b8971b2831acec9e.png" width="100%" alt="kukucaiCndy/Corum-Harness screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ZASENJC/dsh-plugins-store">ZASENJC/dsh-plugins-store</a></b> · ⭐70 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

自动分类、收录和验证 DeepSeek-Harness 社区插件的市场。 Automatically categorize, curate, and validate the DeepSeek-Harness community plugin marketplace.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | TypeScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **70**     |
| Son gönderme   | 2026-10-15 |
| İlk listelenme | 2026-10-16 |

🏷 `agent-tools` · `awesome-list` · `community-project` · `deepseek-harness` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zasenjc--dsh-plugins-store/e83b24d43eca5912.png" width="100%" alt="ZASENJC/dsh-plugins-store screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary><b>Bu kategoride daha fazlası</b> <sub>· 61</sub></summary>

- [strukto-ai/mirage](https://github.com/strukto-ai/mirage) - Dünyanın İlk AI Ajanları için Sanal Terminali.
- [kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net) - AI coding agent.
- [bruc3van/awesome-dsh-plugin](https://github.com/bruc3van/awesome-dsh-plugin) - 30 秒找到真正适合你的 DeepSeek Harness插件。每天自动抓取 GitHub 上的 `dsh-plugin`…
- [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) - DSH eklenti pazarı / DSH Plugin Marketplace: DeepSeek Harness Web GUI içinde…
- [arcships/rutis](https://github.com/arcships/rutis) - Kendi kendini yineleyen yazılımlar için bir eklenti çalışma zamanı — ajanların…
- [adamkhalile/luau-docs-oracle](https://github.com/adamkhalile/luau-docs-oracle) - Best Roblox Luau Bug Checker and API Verifier 2026 DevForum MCP Tool.
- [whyihaveyou/dsh-suite](https://github.com/whyihaveyou/dsh-suite) - Yaşayan DeepSeek Harness eklenti dizini — saatlik yenilenir, uyumluluk testleri…
- [kejixiaoliang/awesome-dsh-plugins](https://github.com/kejixiaoliang/awesome-dsh-plugins) - DeepSeek Harness (DSH) eklentileri seçkisi — 14 kategoride 280.
- [hkkz9522/dsh-session-manager](https://github.com/hkkz9522/dsh-session-manager) - DeepSeek Harness session and workspace manager —— Workspaces: archive and…
- [limbo947/dsh-recall-plugin](https://github.com/limbo947/dsh-recall-plugin) - 消息撤回插件：回到发送该消息时的状态 DSH Message Recall Plugin: Return to the state when the…
- [Lxiayu/DshCockpit](https://github.com/Lxiayu/DshCockpit) - Desktop cockpit for DeepSeek Harness (dsh): token usage &amp; cost tracking, budget…
- [Fengze233/dsh-vscode](https://github.com/Fengze233/dsh-vscode) - 在 VS Code 侧边栏内嵌使用 DeepSeek Harness（DSH）网页界面的插件.
- [GooDAnDReaDY/dsh-russian-lang](https://github.com/GooDAnDReaDY/dsh-russian-lang) - 100% русская локализация и Smart UX для DeepSeek Harness (DSH v0.1.7+): 7574…
- [KannaKuron/dsh-gitbash-shell](https://github.com/KannaKuron/dsh-gitbash-shell) - DSH eklentisi: Windows üzerindeki tüm ajan modları için Git Bash kabuğu.
- [zaofan-make/dsh-qqbot](https://github.com/zaofan-make/dsh-qqbot) - AI 统管 QQ 群组：审核放行、群发文件、沟通其他 web 会话的 AI！ ；气氛组担当：表情包自动入库、AI 自己决定开口、多预设多人格轮班陪聊!
- [UncleK/dsh-think-translate](https://github.com/UncleK/dsh-think-translate) - Thinking-chain UI translation for DeepSeek Harness: 8 target languages, local…
- [siweina/dsh-novel-writer](https://github.com/siweina/dsh-novel-writer) - 给中文网文作者的本地写作工作台.
- [Roarpeng/GraphFlow](https://github.com/Roarpeng/GraphFlow) - Local-first code knowledge graph and context harness for coding agents.
- [zp-home/dsh-recommend](https://github.com/zp-home/dsh-recommend) - DSH 插件生态透明排行与推荐：每日自动抓取 dsh-plugin 话题 + 公开评分模型 + 排行/推荐插件与静态站.
- [pearjelly/deep-blend](https://github.com/pearjelly/deep-blend) - Create and refine Blender product scenes in DSH: editable recipes, model…
- [YELEBAI/dsh-plugin-marketplace](https://github.com/YELEBAI/dsh-plugin-marketplace) - Verified plugin marketplace and autonomous registry for DeepSeek Harness.
- [KCNyu/clawock](https://github.com/KCNyu/clawock) - Stock investment and portfolio decision workflows for AI agents: Claude Code…
- [dshworks/awesome-dsh-plugins](https://github.com/dshworks/awesome-dsh-plugins) - DeepSeek Harness (dsh) eklentileri, paketleri ve becerileri için spam filtreli…
- [tancheng33/dsh-ontology](https://github.com/tancheng33/dsh-ontology) - A typed, inference-capable ontology (TBox + ABox) plugin for DeepSeek Harness…
- [Ianzhyh/workbuddy-to-dsh](https://github.com/Ianzhyh/workbuddy-to-dsh) - 把本机 WorkBuddy 桌面端已登录的模型（DeepSeek / GLM / Kimi / MiniMax 等）变成本地的 OpenAI 与…
- [ouli-1242/dsh-plugin-tool-management](https://github.com/ouli-1242/dsh-plugin-tool-management) - 一个设置面板，统一管理 MCP、技能、记忆、子智能体、提示词和归档会话；可自定义搭配场景，一个场景即可切换整个环境；Agent也能帮你操作这个插件.
- [earthwalker17/MiniDSH](https://github.com/earthwalker17/MiniDSH) - Minimal surface, complete architecture: a small, local-first coding-agent…
- [xbzbing/dsh-git-panel](https://github.com/xbzbing/dsh-git-panel) - DSH eklentisi: Web GUI içinde IDE tarzı Git paneli——dal/commit geçmişi genel…
- [lhh010/dsh-paste-input](https://github.com/lhh010/dsh-paste-input) - DSH WebUI 文件输入增强：Ctrl+V 粘贴 + 拖拽 + 选择文件.
- [GooDAnDReaDY/dsh-key-rotation](https://github.com/GooDAnDReaDY/dsh-key-rotation) - Per-provider API key rotation for DeepSeek Harness: key pools, automatic 429…
- [cccakeee/awesome-dsh-plugins](https://github.com/cccakeee/awesome-dsh-plugins) - A curated, evidence-led directory of DeepSeek Harness (DSH) plugins: verified…
- [chnjames/dsh-plugin-market](https://github.com/chnjames/dsh-plugin-market) - DSH 插件市场 — DeepSeek Harness 设置内一键安装社区插件，并提供公开目录站（浏览 / 复制安装命令）.
- [unStone/dsh-xray](https://github.com/unStone/dsh-xray) - DeepSeek Harness eklentileri için X-ray: beyan edilen yetenekler ve gerçek…
- [cyanseek/dsh-landscape](https://github.com/cyanseek/dsh-landscape) - Agent-first DeepSeek Harness plugin intelligence: verify existing plugins…
- [shenhuanageshei/dsh-team-link](https://github.com/shenhuanageshei/dsh-team-link) - Session deep links + full session export (markdown/JSON) + approved…
- [AKI2253/Sidor_UI](https://github.com/AKI2253/Sidor_UI) - SIDOR starfield skin for DeepSeek Harness Web GUI: intro animation, starfield…
- [AnonyJcy/dsh-j-space](https://github.com/AnonyJcy/dsh-j-space) - J-Space Cognition Suite SV1 原生 DeepSeek Harness 智能体预设与独立 Cordis…
- [ywsldxk/dsh-plugin-stars](https://github.com/ywsldxk/dsh-plugin-stars) - DeepSeek Harness (DSH) plugin leaderboard &amp; directory｜DeepSeek…
- [z7ping/agent-lens](https://github.com/z7ping/agent-lens) - AI kodlama ajanlarının gözlemlenebilir her eylemini görün.
- [GooDAnDReaDY/dsh-dsml-artifact-guard](https://github.com/GooDAnDReaDY/dsh-dsml-artifact-guard) - Sanitizes leaked DeepSeek DSML closing tags from model text streams.
- [kolawong/fast-compaction-dsh](https://github.com/kolawong/fast-compaction-dsh) - Verdict-based context compaction for DeepSeek Harness — replaces lossy LLM…
- [PerryLink/dsh-plugin-doctor](https://github.com/PerryLink/dsh-plugin-doctor) - DeepSeek Harness (dsh) eklentileri için sıfır bağımlılıklı doğrulama standardı…
- [PerryLink/perrylink](https://github.com/PerryLink/perrylink) - DeepSeek Harness eklenti ekosistemi: 101 depoluk bir ailede 86 açık kaynaklı…
- [tianyagk/dsh-tradewatcher](https://github.com/tianyagk/dsh-tradewatcher) - DeepSeek Harness (DSH) web eklentisi: market-dashboard kenar çubuğu sekmesi…
- [viztor/dsh-opencode-patch](https://github.com/viztor/dsh-opencode-patch) - DeepSeek Harness üzerinde OpenCode — OpenCode Zen + Go ücretsiz katman…
- [AI-Scarlett/DSH-Store](https://github.com/AI-Scarlett/DSH-Store) - DSH STORE — DeepSeek Harness için üçüncü taraf eklenti pazaryeri ve korumalı…
- [Atelyx/Atelyx](https://github.com/Atelyx/Atelyx) - Atelyx, insan odaklı ve genişletilebilir bir masaüstü çalışma alanıdır…
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
- [argszero/cordis-plugin-sandbox-grant-advisor](https://github.com/argszero/cordis-plugin-sandbox-grant-advisor) - DeepSeek Harness eklentisi: Windows sandbox ACL sağlama hatasını…
- [zhang-guo-wen/dsh-claude-compat](https://github.com/zhang-guo-wen/dsh-claude-compat) - deepseek harness 插件，兼容claude的skill、rules加载规则，mcp配置.
- [q253595422/dsh-imagegen-video](https://github.com/q253595422/dsh-imagegen-video) - DeepSeek Harness plugin: image + video generation studio with an infinite…
- [SCP-008-1/dshop](https://github.com/SCP-008-1/dshop) - dsh 插件商城 - 基于 GitHub topic:dsh-plugin 自动发现与每小时定时同步.

</details>

<a id="writing"></a>

## Yazılar, tartışmalar ve videolar

Mod yeteneği hakkında yazılar, tartışmalar ve videolar.

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50099375">Claude Code Desktop Vulnerability: Preview Pane Data Exfiltration</a></b> · ⭐15 · 👁️ observed · 0 天</summary>

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
| İlk listelenme | 2026-10-15 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49945600">Show HN: Terminal Gym – a Claude mod that makes you do pushups between prompts</a></b> · ⭐4 · 👁️ observed · 12 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50003222">What the Hell Are Claude Mods? [video]</a></b> · ⭐4 · 👁️ observed · 7 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49999983">A Claude Code mod plays MIDI music when it works</a></b> · ⭐3 · 👁️ observed · 7 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925800">Claude Code Mods: plugins may now modify deeper behavior</a></b> · ⭐3 · 👁️ observed · 14 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50024345">Agent-config&amp;Claude Code mods</a></b> · ⭐2 · 👁️ observed · 6 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49940121">Getting started with Claude Code mods</a></b> · ⭐2 · 👁️ observed · 12 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49934165">Show HN: What&#x27;s Agent Doing – a Claude Code UI mod that explains each step</a></b> · ⭐2 · 👁️ observed · 13 天</summary>

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

| Dil        | Kayıtlar | Örnekler                                                                                                      |
| ---------- | -------- | ------------------------------------------------------------------------------------------------------------- |
| TypeScript | 298      | `anthropics/claude-code`, `anthropics/claude-code-action`, `YeonwooSung/my-claude-code-mods`                  |
| JavaScript | 85       | `karanb192/awesome-claude-code-mods`, `zycck/claude-mods`, `karanb192/claude-code-mods`                       |
| Python     | 35       | `anthropics/claude-agent-sdk-python`, `anthropics/claude-code-security-review`, `alexgreensh/token-optimizer` |
| Shell      | 33       | `anthropics/claude-agent-sdk-typescript`, `0xDarkMatter/claude-mods`, `BeLazy167/claude-mods-skill`           |
| HTML       | 11       | `darrell-tw/darrelltw-mods`, `omarcevi/claudemods`, `testy-cool/awesome-claude-code-mods`                     |
| Rust       | 7        | `helenkwok/rustgis-tui`, `persiyanov/herdr-reviewr`, `ta17eee/claude-code-statusline`                         |
| Go         | 3        | `vulcanshen/ccdrawu`, `esengine/DeepSeek-Reasonix`, `vshulcz/deja-vu`                                         |
| PowerShell | 2        | `spyrad/claude-code-statusline`, `ZeyuSi-2099/claude-code-statusline`                                         |
| C          | 1        | `reporails/arcade`                                                                                            |

<sub>Yalnızca dil belirten girdiler sayılır. Belgeler ve tartışma girdileri bu tablonun dışında tutulur.</sub>

## Katkıda bulunma

Düzeltmeler memnuniyetle karşılanır ve bu listeyi iyileştirmenin en hızlı yoludur. Bir girdi yanlış sınıflandırılmış veya yanlış derecelendirilmişse ya da bir proje ad çakışması nedeniyle yanlışlıkla dışlanmışsa bir issue veya pull request açın — otomatik filtrelerin en çok yanılma ihtimali olan kategori sonuncusudur.

---

<sub>Independent community project. Not affiliated with, endorsed by, or reviewed by Anthropic. Claude Code, Claude and Anthropic are trademarks of Anthropic. Product behaviour changes without notice; verify anything load-bearing against the official documentation. Assets remain the property of their upstream projects and are reproduced only where a licence permits.</sub>

<sub>Son güncelleme · 2026-10-16T03:45:33+08:00</sub>
