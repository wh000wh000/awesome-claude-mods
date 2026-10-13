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
> **Güncel dizin** · Son senkronizasyon: `2026-10-13T08:29:52+08:00` (UTC+8)
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
<sub>⭐9488 · TypeScript · ✅ official</sub>
</td>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer">
<b>🧩 <a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b>
<sub>⭐2543 · Python · 👁️ observed</sub>
<sub>Hayalet belirteçleri bulun. Onları düzeltin. Sıkıştırmadan sağ çıkın. Bağlam kalitesinin bozulmasından kaçının.</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo">
<b>🧵 <a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b>
<sub>⭐74447 · TypeScript · 👁️ observed</sub>
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
- [Resmî: Anthropic'ın kendi depoları ve sürüm notları](#resmî-anthropicın-kendi-depoları-ve-sürüm-notları) — **16**
- [Modlar: mod yeteneği kullanılarak oluşturulanlar](#modlar-mod-yeteneği-kullanılarak-oluşturulanlar) — **448**
- [DSH ve Cordis eklenti ekosistemleri](#dsh-ve-cordis-eklenti-ekosistemleri) — **108**
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
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></b> · ⭐150436 · TypeScript · ✅ official · 0 天</summary>

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
| Yıldızlar      | **150436** |
| Son gönderme   | 2026-10-13 |
| İlk listelenme | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b> · ⭐9488 · TypeScript · ✅ official · 3 天</summary>

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
| Yıldızlar      | **9488**   |
| Son gönderme   | 2026-10-09 |
| İlk listelenme | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-python">anthropics/claude-agent-sdk-python</a></b> · ⭐8255 · Python · ✅ official · 3 天</summary>

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
| Yıldızlar      | **8255**   |
| Son gönderme   | 2026-10-09 |
| İlk listelenme | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-security-review">anthropics/claude-code-security-review</a></b> · ⭐6355 · Python · ✅ official · 243 天</summary>

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
| Yıldızlar      | **6355**   |
| Son gönderme   | 2026-02-11 |
| İlk listelenme | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-typescript">anthropics/claude-agent-sdk-typescript</a></b> · ⭐1800 · Shell · ✅ official · 3 天</summary>

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
| Yıldızlar      | **1800**   |
| Son gönderme   | 2026-10-09 |
| İlk listelenme | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/model-cards">anthropics/model-cards</a></b> · ⭐25 · ✅ official · 311 天</summary>

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
<summary>🏛️ <b><a href="https://github.com/PerryLink/dsh-mcp-panel">PerryLink/dsh-mcp-panel</a></b> · ⭐74 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

Resmî DeepSeek Harness MCP istemcisi için MCP yönetim konsolu: sağlık tanılamaları ve işlem hattı deneme çağrıları içeren /mcp komutu, sunucu CRUD işlemlerine sahip bir Ayarlar MCP sekmesi (onay kontrollü yazmalar, otomatik yedeklemeler) ve resmî araç işlem hattı (Apache-2.0, dsh-plugin) üzerinden bir araç deneme konsolu.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `Resmî: Anthropic&#x27;ın kendi depoları ve sürüm notları`                                      |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | TypeScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **74**     |
| Son gönderme   | 2026-10-12 |
| İlk listelenme | 2026-10-13 |

🏷 `ai-agent` · `ai-agents` · `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-mcp-panel/f435adadbab44c9f.png" width="100%" alt="PerryLink/dsh-mcp-panel screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-mcp-panel/79405ad96d2dc69e.gif" width="100%" alt="PerryLink/dsh-mcp-panel animation"><br><sub>animasyonlu kayıt</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/PerryLink/dsh-ticktick">PerryLink/dsh-ticktick</a></b> · ⭐4 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

DeepSeek Harness için TickTick (Dida365) görev köprüsü: oturum başlığı görev paneli (liste filtresi, yapılmamış/tamamlanmış görünümler, arama, sürükleyerek yeniden sıralama), özenle seçilmiş 11 ajan aracı, ayarlar kartı; resmi TickTick MCP uç noktası üzerinden.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `Resmî: Anthropic&#x27;ın kendi depoları ve sürüm notları`                                      |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | TypeScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **4**      |
| Son gönderme   | 2026-10-12 |
| İlk listelenme | 2026-10-13 |

🏷 `ai-agent` · `ai-agents` · `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dida365` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-ticktick/aa581021cb97f4dd.png" width="100%" alt="PerryLink/dsh-ticktick screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-ticktick/44088595da097cb2.gif" width="100%" alt="PerryLink/dsh-ticktick animation"><br><sub>animasyonlu kayıt</sub></td>
</tr></table>

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
<summary>🧩 <b><a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b> · ⭐2543 · Python · 👁️ observed · 0 天</summary>

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
| Yıldızlar      | **2543**   |
| Son gönderme   | 2026-10-12 |
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
<summary>🧩 <b><a href="https://github.com/karanb192/awesome-claude-code-mods">karanb192/awesome-claude-code-mods</a></b> · ⭐535 · JavaScript · 👁️ observed · 0 天</summary>

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
| Yıldızlar      | **535**    |
| Son gönderme   | 2026-10-12 |
| İlk listelenme | 2026-10-04 |

🏷 `anthropic` · `awesome` · `awesome-list` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hamzafer/claude-code-mods">hamzafer/claude-code-mods</a></b> · ⭐211 · TypeScript · 👁️ observed · 0 天</summary>

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
| Yıldızlar      | **211**    |
| Son gönderme   | 2026-10-12 |
| İlk listelenme | 2026-10-11 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugins` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/c683a5d95e78d920.png" width="100%" alt="hamzafer/claude-code-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/0b4dc7c7692bd024.gif" width="100%" alt="hamzafer/claude-code-mods animation"><br><sub>animasyonlu kayıt</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/cache-tax">karanb192/cache-tax</a></b> · ⭐163 · TypeScript · 👁️ observed · 8 天</summary>

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
| Yıldızlar      | **163**    |
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
<summary>🧩 <b><a href="https://github.com/hellosverre/claude-skins">hellosverre/claude-skins</a></b> · ⭐119 · TypeScript · 👁️ observed · 0 天</summary>

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
| Yıldızlar      | **119**    |
| Son gönderme   | 2026-10-12 |
| İlk listelenme | 2026-10-13 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hellosverre--claude-skins/e70c992c52ca2e70.gif" width="100%" alt="hellosverre/claude-skins animation"><br><sub>animasyonlu kayıt</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NahumLitvin/prismantis">NahumLitvin/prismantis</a></b> · ⭐89 · TypeScript · 👁️ observed · 0 天</summary>

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
| Yıldızlar      | **89**     |
| Son gönderme   | 2026-10-12 |
| İlk listelenme | 2026-10-11 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `markdown` · `mermaid` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/f6e44059e77434b4.png" width="100%" alt="NahumLitvin/prismantis screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/00e2cffa219a3511.gif" width="100%" alt="NahumLitvin/prismantis animation"><br><sub>animasyonlu kayıt</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Tickloop/claude-mods">Tickloop/claude-mods</a></b> · ⭐79 · TypeScript · 👁️ observed · 4 天</summary>

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
| Yıldızlar      | **79**     |
| Son gönderme   | 2026-10-08 |
| İlk listelenme | 2026-10-11 |

</details>

<details>
<summary>🧩 <b><a href="https://github.com/scasella/claude-flightdeck">scasella/claude-flightdeck</a></b> · ⭐75 · TypeScript · 👁️ observed · 0 天</summary>

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
| Yıldızlar      | **75**     |
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
<summary>🧩 <b><a href="https://github.com/darrell-tw/darrelltw-mods">darrell-tw/darrelltw-mods</a></b> · ⭐65 · HTML · 👁️ observed · 7 天</summary>

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
<summary>🧩 <b><a href="https://github.com/0xDarkMatter/claude-mods">0xDarkMatter/claude-mods</a></b> · ⭐62 · Shell · 👁️ observed · 5 天</summary>

##### 📝 Özet

Claude Code için uzman Skills'ler, aracılar, komutlar, kurallar, kancalar ve çıktı stilleri — oturum sürekliliği + gerçek dünya geliştirme iş akışları için modern CLI araçları

<sub>🔧 Kodda kullanıldığı bulundu: `justfile`, `skills/auto-skill/SKILL.md`, `skills/task-runner/SKILL.md`</sub>

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Modlar: mod yeteneği kullanılarak oluşturulanlar`                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |
| Dil      | Shell                                                                    |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **62**     |
| Son gönderme   | 2026-10-07 |
| İlk listelenme | 2026-10-11 |

🏷 `agent-skills` · `ai-agents` · `ai-tools` · `anthropic` · `claude` · `claude-code` · `claude-skills` · `developer-tools`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/whyashthakker/awesome-claude-code-mods">whyashthakker/awesome-claude-code-mods</a></b> · ⭐55 · TypeScript · 👁️ observed · 9 天</summary>

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
| Yıldızlar      | **55**     |
| Son gönderme   | 2026-10-03 |
| İlk listelenme | 2026-10-11 |

🏷 `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/zycck/claude-mods">zycck/claude-mods</a></b> · ⭐47 · TypeScript · 👁️ observed · 4 天</summary>

##### 📝 Özet

Claude Code modları: istemin üstünde canlı plan ilerleme çubukları

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Modlar: mod yeteneği kullanılarak oluşturulanlar`                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |
| Dil      | TypeScript                                                               |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **47**     |
| Son gönderme   | 2026-10-08 |
| İlk listelenme | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/49f09d1600b02c7a.gif" width="100%" alt="zycck/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/25f4230871cb30f6.gif" width="100%" alt="zycck/claude-mods animation"><br><sub>animasyonlu kayıt · <a href="https://raw.githubusercontent.com/zycck/claude-mods/main/media/plan-progress.mp4">Videoyu aç</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/henrik-thevibe/Claude-Fables">henrik-thevibe/Claude-Fables</a></b> · ⭐32 · TypeScript · 👁️ observed · 10 天</summary>

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
<summary>🧩 <b><a href="https://github.com/oikon48/prompt-rail">oikon48/prompt-rail</a></b> · ⭐28 · TypeScript · 👁️ observed · 9 天</summary>

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
| Yıldızlar      | **28**     |
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
<summary>🧩 <b><a href="https://github.com/NovusEdge/glowup">NovusEdge/glowup</a></b> · ⭐26 · TypeScript · 👁️ observed · 0 天</summary>

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
| Yıldızlar      | **26**     |
| Son gönderme   | 2026-10-13 |
| İlk listelenme | 2026-10-11 |

🏷 `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `developer-tools` · `eye-candy` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/52396333a085f3d5.gif" width="100%" alt="NovusEdge/glowup screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/4905ed24c2c755ad.gif" width="100%" alt="NovusEdge/glowup animation"><br><sub>animasyonlu kayıt</sub></td>
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
| Son gönderme   | 2026-10-12 |
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
<summary>🧩 <b><a href="https://github.com/artemnovichkov/xcode-mods">artemnovichkov/xcode-mods</a></b> · ⭐20 · TypeScript · 👁️ observed · 10 天</summary>

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
<summary>🧩 <b><a href="https://github.com/lemomo-ai/lemo-mod">lemomo-ai/lemo-mod</a></b> · ⭐20 · TypeScript · 👁️ observed · 8 天</summary>

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
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-starter-kit">promptadvisers/claude-mods-starter-kit</a></b> · ⭐20 · JavaScript · 👁️ observed · 10 天</summary>

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
<summary>🧩 <b><a href="https://github.com/Amorfx/claude-paste-view">Amorfx/claude-paste-view</a></b> · ⭐19 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Özet

Claude Code modu: yapıştırılan görüntüleri ve uzun yapıştırılmış metni istemin üzerinde önizler

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Modlar: mod yeteneği kullanılarak oluşturulanlar`                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |
| Dil      | TypeScript                                                               |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **19**     |
| Son gönderme   | 2026-10-12 |
| İlk listelenme | 2026-10-12 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `clipboard` · `ghostty` · `image-preview` · `kitty` · `paste`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/amorfx--claude-paste-view/972d572d11675bb5.png" width="100%" alt="Amorfx/claude-paste-view screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/BrianHuang813/clawd-actor">BrianHuang813/clawd-actor</a></b> · ⭐17 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Özet

Claude Code modu: Clawd, istemin üstünde Claude tarafından yapılanları canlandırır

##### 📌 Temel bilgiler

| Alan     | Değer                                                                    |
| -------- | ------------------------------------------------------------------------ |
| Kategori | `Modlar: mod yeteneği kullanılarak oluşturulanlar`                       |
| Kanıt    | `kendi metni bir moddan (API) söz ediyor veya mod yeteneğini bildiriyor` |
| Dil      | TypeScript                                                               |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **17**     |
| Son gönderme   | 2026-10-12 |
| İlk listelenme | 2026-10-12 |

🏷 `animation` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-plugin` · `clawd` · `hooks` · `spinner`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/brianhuang813--clawd-actor/d6174db0110613e4.gif" width="100%" alt="BrianHuang813/clawd-actor screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/brianhuang813--clawd-actor/d6174db0110613e4.gif" width="100%" alt="BrianHuang813/clawd-actor animation"><br><sub>animasyonlu kayıt</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-computer-use-threads">promptadvisers/claude-mods-computer-use-threads</a></b> · ⭐16 · JavaScript · 👁️ observed · 7 天</summary>

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
<summary>🧩 <b><a href="https://github.com/JetsonChan/CC-Usage-Band">JetsonChan/CC-Usage-Band</a></b> · ⭐13 · TypeScript · 👁️ observed · 9 天</summary>

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
<summary>🧩 <b><a href="https://github.com/OneWave-AI/claude-code-mods">OneWave-AI/claude-code-mods</a></b> · ⭐13 · TypeScript · 👁️ observed · 9 天</summary>

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
| Yıldızlar      | **13**     |
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
<summary>🧩 <b><a href="https://github.com/aieo-product/claude_qamods">aieo-product/claude_qamods</a></b> · ⭐12 · TypeScript · 👁️ observed · 5 天</summary>

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
<summary>🧩 <b><a href="https://github.com/augiefra/claude-mods">augiefra/claude-mods</a></b> · ⭐12 · JavaScript · 👁️ observed · 1 天</summary>

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
<summary>🧩 <b><a href="https://github.com/furqan-khan07/pixelband">furqan-khan07/pixelband</a></b> · ⭐10 · TypeScript · 👁️ observed · 8 天</summary>

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
<summary>🧩 <b><a href="https://github.com/Arunjay4213/claude-mods">Arunjay4213/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 27 天</summary>

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
| Son gönderme   | 2026-10-12 |
| İlk listelenme | 2026-10-11 |

🏷 `ai-coding` · `ai-tools` · `browser-terminal` · `claude-code` · `codex` · `coding-agent` · `developer-tools` · `devtools`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/deepsteve--deepsteve/adee5ea71e2e3289.png" width="100%" alt="deepsteve/deepsteve screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/ersinkoc/claude-mods">ersinkoc/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 2 天</summary>

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
<summary>🧩 <b><a href="https://github.com/VedantAndhale/claude-pro-kit">VedantAndhale/claude-pro-kit</a></b> · ⭐9 · TypeScript · 👁️ observed · 3 天</summary>

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
| Yıldızlar      | **9**      |
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
<summary>🧩 <b><a href="https://github.com/az9713/claude-mod-pack">az9713/claude-mod-pack</a></b> · ⭐8 · TypeScript · 👁️ observed · 8 天</summary>

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
<summary>🧩 <b><a href="https://github.com/devbrother2024/devbrothers-mods">devbrother2024/devbrothers-mods</a></b> · ⭐8 · TypeScript · 👁️ observed · 8 天</summary>

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
<summary>🧩 <b><a href="https://github.com/Shuffzord/RoadRaven">Shuffzord/RoadRaven</a></b> · ⭐8 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Özet

Kendi kendini izleyen planınız. Claude Code ve herhangi bir MCP ana bilgisayarının canlı olarak güncel tuttuğu yerel masaüstü yol haritası ağacı. Sade JSON, bulut yok.

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
| Son gönderme   | 2026-10-12 |
| İlk listelenme | 2026-10-13 |

🏷 `ai-agents` · `bun` · `claude-code` · `claude-code-mod` · `claude-code-plugin` · `desktop-app` · `electrobun` · `local-first`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Shuffzord/RoadRaven/master/screenshots/events.png" width="100%" alt="Shuffzord/RoadRaven screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

<sub>Yeniden dağıtıma izin veren bir lisans belirtilmediği için varlığa upstream deposundan doğrudan bağlantı veriliyor.</sub>

</details>

<details>
<summary><b>Bu kategoride daha fazlası</b> <sub>· 414</sub></summary>

- [karanb192/claude-code-mods](https://github.com/karanb192/claude-code-mods) - Claude Mod.
- [ray-amjad/claude-code-mods](https://github.com/ray-amjad/claude-code-mods) - Ray Amjad.
- [ucsandman/claude-harness](https://github.com/ucsandman/claude-harness) - Her gün çalıştırdığım Claude Code harness.
- [kagamiurayama/claude-code-roof-mod](https://github.com/kagamiurayama/claude-code-roof-mod) - Claude Mods ile Claude Code.
- [nateherkai/claude-code-mods](https://github.com/nateherkai/claude-code-mods) - Dört Claude Code modu: Cache Keeper, Recording Mode, Goal Meter ve Collision…
- [Hangghost/learning-hacker-claude-mod](https://github.com/Hangghost/learning-hacker-claude-mod) - Learning Hacker.
- [kakha13/claude](https://github.com/kakha13/claude) - Claude Code modları, Claude onları okumadan önce istemlerinizi düzeltir ve…
- [AgriciDaniel/claude-mods-brain](https://github.com/AgriciDaniel/claude-mods-brain) - Claude Code modları hakkında kaynak gösteren Obsidian bilgi tabanı: nasıl…
- [nekyialabs/claude-code-toolkit](https://github.com/nekyialabs/claude-code-toolkit) - Nekyia Labs tarafından geliştirilen ve kalıcı bir evde yaşayan AIs tarafından…
- [nvr0x5/claude-deck](https://github.com/nvr0x5/claude-deck) - Claude Code için kokpit: isteminizin hemen üzerinde canlı plan çubukları, alt…
- [rashedInt32/glass](https://github.com/rashedInt32/glass) - Bir mod olarak Claude Code.
- [xuanji86/claude-agentpane](https://github.com/xuanji86/claude-agentpane) - Claude Code için bir yan panel: bir oturumun çalıştırdığı alt aracılar, her…
- [Jhonatan-de-Souza/ClaudeMods](https://github.com/Jhonatan-de-Souza/ClaudeMods) - Claude Code modları: Claude Tools menüsü, Zen modu, terminal temaları, çaba ve…
- [letswritetw/claude-mod-open-todos](https://github.com/letswritetw/claude-mod-open-todos) - Claude Desktop (Code sekmesi) kenar çubuğu paneli: tüm Claude Code…
- [letswritetw/claude-mod-token-usage](https://github.com/letswritetw/claude-mod-token-usage) - Claude Desktop (Code sekmesi) giriş kutusunun üstündeki kullanım çubuğu: 5h /…
- [BeLazy167/claude-mods-skill](https://github.com/BeLazy167/claude-mods-skill) - Claude Code ajanlarına, başlangıç örneğiyle birlikte Claude Mods.
- [omarcevi/claudemods](https://github.com/omarcevi/claudemods) - Tek bir pazardan kurulabilen topluluk Claude modları, eklentileri ve becerileri.
- [KilimcininKorOglu/claude-code-mods](https://github.com/KilimcininKorOglu/claude-code-mods) - Claude Code için Claude Mods (işlev kancası eklentileri).
- [baselane-sh/mods-catalog](https://github.com/baselane-sh/mods-catalog) - Baselane modları galerisi: Claude Code modları, kontrol edilmiş ve sabitlenmiş.
- [eighteyes/cactus](https://github.com/eighteyes/cactus) - Konuşmalı ajanlarla çalışan insanlar için karar kuyruğu CLI/TUI.
- [neteye-platform/cc-split-diff-view](https://github.com/neteye-platform/cc-split-diff-view) - Edit ve Write farklarını yan yana iki sütunda çizen Claude Code modu.
- [nogu66/md-prompt](https://github.com/nogu66/md-prompt) - Siz yazarken Markdown, Claude Code.
- [ronanworks/claude-code-mods](https://github.com/ronanworks/claude-code-mods) - Claude Code modları: 像素螃蟹用量面板 usage-hud + terminalde tıklanabilen HTML…
- [xuanji86/claude-statuspane](https://github.com/xuanji86/claude-statuspane) - Claude Code için kayan durum kartı — model, bağlam, hız sınırları, maliyet, dal…
- [arasovic/claude-code-mods](https://github.com/arasovic/claude-code-mods) - Claude Code için Mods: terminal kullanıcı arayüzüne canlı bölmeler ve davranış…
- [danyuchn/claude-mods](https://github.com/danyuchn/claude-mods) - Claude Code modları: screen-guard ekran paylaşırken adları ve gizli bilgileri…
- [GarvitNangru/claude-code-mods](https://github.com/GarvitNangru/claude-code-mods) - Claude Code için modlar ve görünümler: Claude görevleri için canlı ilerleme…
- [magidandrew/cx](https://github.com/magidandrew/cx) - Claude Code Extensions. Claude.
- [markneonin/paneline](https://github.com/markneonin/paneline) - Activity, Files, Agents, Context ve MCP sekmelerini içeren bir yan bölme…
- [mishgoldenberg/claude-mods](https://github.com/mishgoldenberg/claude-mods) - Claude Code için paneller, koruyucu kurallar ve kullanım kolaylığı modları…
- [ofeklevy11/claude-code-hud](https://github.com/ofeklevy11/claude-code-hud) - İstem kutusunun üstünde iki Claude Code modu: bağlam penceresi ölçer, 5 saatlik…
- [xuanji86/claude-mdview](https://github.com/xuanji86/claude-mdview) - Claude Code.
- [chrisluo5311/squad-chat](https://github.com/chrisluo5311/squad-chat) - Claude pişiriyor. Ekibinizle sohbet edin.
- [Danovich/turntype](https://github.com/Danovich/turntype) - Claude çalışırken zaman geçirmek için bir yazma testi. Bir Claude Code modu.
- [hahmjuntae/claude-mods-image-preview](https://github.com/hahmjuntae/claude-mods-image-preview) - Claude Code modu: herhangi bir terminalde istemin üstünde yapıştırılan…
- [leopiney/wolfbud-claude-mod](https://github.com/leopiney/wolfbud-claude-mod) - Claude Code için sesli çalışma arkadaşı.
- [Antreas-Strb/glanceflow](https://github.com/Antreas-Strb/glanceflow) - Claude Code için GlanceFlow: istemin üzerinde planı, ilerlemeyi ve Claude.
- [BatuhanCakmakk/wavy-usage](https://github.com/BatuhanCakmakk/wavy-usage) - Liquid-filled usage rings above the Claude Code prompt: 5h/7d limits, context…
- [Boom-Vitt/boombignose-mods](https://github.com/Boom-Vitt/boombignose-mods) - Claude Code modları: bağlam çubuğu, ajanlar paneli, PDPA bulanıklaştırma.
- [borabiricik/claude-mods](https://github.com/borabiricik/claude-mods) - Claude Code modları: typing-speed, istem başına istatistiklerle canlı yazma…
- [charimsma/dopa-mode](https://github.com/charimsma/dopa-mode) - Claude Code için havai fişekler: her tuş vuruşu, araç çağrısı, commit ve…
- [davekiss/mods](https://github.com/davekiss/mods) - Dave Kiss tarafından geliştirilen Claude Code modları.
- [dougcunha/claude-mods](https://github.com/dougcunha/claude-mods) - Claude Code için modlar: function-hooks API eklentisiyle oluşturulmuş paneller…
- [DrishtantKaushal/AwesomeClaudeCodeMods](https://github.com/DrishtantKaushal/AwesomeClaudeCodeMods) - Animasyonlu demolar, kategori listeleri ve doğrudan kaynak bağlantılarıyla…
- [galElmalah/claude-mods](https://github.com/galElmalah/claude-mods) - Claude Code modu: mermaid diyagramları transkript içinde satır içi olarak…
- [ha-ptt0601/cc-mods](https://github.com/ha-ptt0601/cc-mods) - Küçük Claude Code modülleri (işlev kancası eklentileri): session-switcher ve…
- [hellosverre/mod-store](https://github.com/hellosverre/mod-store) - Claude Code içinde Claude Code modları için uygulama mağazası: 2.700 modu…
- [ice-lfernandes/claude-code-mods](https://github.com/ice-lfernandes/claude-code-mods) - Altı Claude Code modu: plan sınırları ve istemin üstünde bağlam, izin istemleri…
- [LeeHigma0201/claude-code-mods](https://github.com/LeeHigma0201/claude-code-mods) - Claude Code modları: mod-scout (en çok kullanacağınız modları bulur)…
- [Nongfsq/frank-claude-cockpit](https://github.com/Nongfsq/frank-claude-cockpit) - Aynı anda birçok oturum çalıştırmak için iki Claude Code modu: istemin üstünde…
- [timoncool/givememod](https://github.com/timoncool/givememod) - İsteğe bağlı Claude Code modları — konuşmanızı okuyup size uygun modu oluşturan…
- [ayagmar/claude-modmgr](https://github.com/ayagmar/claude-modmgr) - modmgr: Claude Code modlarını keşfedin, inceleyin, açıp kapatın ve güncelleyin.
- [claude-code-mods/best-claude-code-mods](https://github.com/claude-code-mods/best-claude-code-mods) - En iyi Claude Code modları: özenle seçilmiş, doğrulanmış, sabitlenmiş.
- [dominicrico/jev-router](https://github.com/dominicrico/jev-router) - Claude Code eklentisi: otomatik Claude model yönlendirmesi.
- [ElirazKed/claude-code-pr-watch](https://github.com/ElirazKed/claude-code-pr-watch) - Claude Code modu: bir oturumun açtığı veya gönderdiği GitHub PR.
- [FynnXland/fynn-mods](https://github.com/FynnXland/fynn-mods) - Claude Code için altı mod: animasyonlu Clawd maskotu, kullanım limiti ve…
- [Hula-Hoop-AI/supermods](https://github.com/Hula-Hoop-AI/supermods) - Claude Code için bir mod pazaryeri: ajan döngüsü için adım hata ayıklayıcı, git…
- [ibrahimkobeissy/claude-mods](https://github.com/ibrahimkobeissy/claude-mods) - Claude Code için açık kaynaklı modlar: bölmeler, durum satırları, bildirimler…
- [mertkayacs/ultramod](https://github.com/mertkayacs/ultramod) - Claude Code için en iyi hepsi bir arada mod paketi: kullanım sınırları ve…
- [mthli/cc-shorts](https://github.com/mthli/cc-shorts) - Claude Code.
- [NarenDawar/narens-claude-toolkit](https://github.com/NarenDawar/narens-claude-toolkit) - Naren.
- [raresmun/claude-mods](https://github.com/raresmun/claude-mods) - Claude Code için modlar: Claude.
- [reporails/arcade](https://github.com/reporails/arcade) - Claude Code modları olarak klasik masaüstü oyunları;
- [schreibse/claude-code-mods](https://github.com/schreibse/claude-code-mods) - claude için code-mods.
- [Szotasz/claude-mods](https://github.com/Szotasz/claude-mods) - Kendi Claude Code modlarım için eklenti marketplace.
- [testy-cool/awesome-claude-code-mods](https://github.com/testy-cool/awesome-claude-code-mods) - Eklenti pazaryeri olarak kurulabilen, derlenmiş bir Claude Code modları…
- [wdsewdser-bit/claude-code-mods](https://github.com/wdsewdser-bit/claude-code-mods) - İki Claude Code modu: cache-keeper ve ctx-mod.
- [xsyetopz/dotclaude](https://github.com/xsyetopz/dotclaude) - Harness mühendisliğine takıntılı bir Rustacean tarafından tasarlanmış, son…
- [yash-gadodia/claude-mods](https://github.com/yash-gadodia/claude-mods) - Bir ajanın dürüst kalmasını sağlayan Claude Code modları — kapsamı koruyan…
- [CodyAMaughan/meme-factory](https://github.com/CodyAMaughan/meme-factory) - Fabrikadan yeni çıktı. Bir Claude Code modu: bir meme isteyin, çalışmaya devam…
- [DarioFontanel/claude-code-mods](https://github.com/DarioFontanel/claude-code-mods) - Claude Code başına mod: prompt cache çubuğu, sonraki adımlar, hızlı düğmeler ve…
- [estruyf/claude-stats-mod](https://github.com/estruyf/claude-stats-mod) - Kullanım limitlerinizi ve harcamalarınızı istemin üzerindeki bantta gösteren…
- [gaius-codius/ostrakon](https://github.com/gaius-codius/ostrakon) - Çalışma sırasında akla gelen düşünceleri yakalayan, bunları projeler ve…
- [gerricchaplin/pr-pulse](https://github.com/gerricchaplin/pr-pulse) - Claude Code içinde canlı GitHub PR durumu, birleştirmeye hazır olma durumu…
- [herman925/925-cc-plugins](https://github.com/herman925/925-cc-plugins) - Herman.
- [homieyangg/claude-code-mods](https://github.com/homieyangg/claude-code-mods) - Claude Code modları: planlar için ilerleme çubukları, Claude.
- [Malkiz/claude-reply-comments](https://github.com/Malkiz/claude-reply-comments) - Claude Code modu: Claude.
- [MankhongGarden/claude-code-mods-field-notes](https://github.com/MankhongGarden/claude-code-mods-field-notes) - Windows üzerindeki Claude Code modları hakkında birinci gün saha notları…
- [NMenzel/claude-devtools-mod](https://github.com/NMenzel/claude-devtools-mod) - Claude DevTools: Claude Code araç çağrıları için hata ayıklayıcı.
- [oborchers/claude-gh-status](https://github.com/oborchers/claude-gh-status) - Claude Code modu: doğrulanmış birleştirme işlemleriyle, bir bantta ve panelde…
- [oMaN-Rod/claude-code-widgets](https://github.com/oMaN-Rod/claude-code-widgets) - Claude Code isteminin altında duran veya tam ekranda dökümün yanına sabitlenen…
- [patitow/claude-mod-cost-visibility](https://github.com/patitow/claude-mod-cost-visibility) - Claude Code modu: istemin üzerinde canlı maliyet, bağlam ve plan kota…
- [ruslanshchuchkin/claude-techno-mod](https://github.com/ruslanshchuchkin/claude-techno-mod) - 😈 Biraz TECHNO yapıyoruz bebeğim 😈.
- [Sennjen/claude-sdlc](https://github.com/Sennjen/claude-sdlc) - Claude Code plugin&#x27;i ve mod&#x27;u: hook ile zorunlu kılınan insan onayı kapıları ve…
- [shimo4228/harness-scope](https://github.com/shimo4228/harness-scope) - Genel becerilerinizi, aracıları, kuralları ve araçlarınızı adlandırılmış…
- [Singh-AP/awesome-claude-mods](https://github.com/Singh-AP/awesome-claude-mods) - 🧩 Test edilmiş, tek komutla kurulabilen Claude Code modları: YOLO modu için…
- [soulrocha/Claude-code-hero-journey](https://github.com/soulrocha/Claude-code-hero-journey) - 🦀 Claude Code için rahat bir RPG HUD modu.
- [theonly1me/claude-code-mods](https://github.com/theonly1me/claude-code-mods) - Tarafımdan oluşturulmuş bir dizi claude code modu.
- [y-hirakaw/claude-code-mods](https://github.com/y-hirakaw/claude-code-mods) - Claude Code modları. touch-map: Claude tarafından listelenen, okunan…
- [yodakeisuke/claudelingo](https://github.com/yodakeisuke/claudelingo) - Claude Code ile çalışırken yabancı bir dil öğrenin.
- [yuntaengtaeng/snitch](https://github.com/yuntaengtaeng/snitch) - Claude Code modu; Claude.
- [0xctx/sysop](https://github.com/0xctx/sysop) - Claude.
- [20alexl/windvane](https://github.com/20alexl/windvane) - Uzun bir Claude Code oturumunu sizin yerinize takip eder: bağlamın dolmasını…
- [404Mayank/cachebeat](https://github.com/404Mayank/cachebeat) - Siz uzaktayken istem önbelleğinizi sıcak tutan bir Claude Code modu.
- [andrewbakercloudscale/claude-code-cost-sidebar](https://github.com/andrewbakercloudscale/claude-code-cost-sidebar) - Claude Code için canlı maliyet, token ve bağlam kullanımı kenar çubuğu: oturum…
- [ayagmar/claude-mods](https://github.com/ayagmar/claude-mods) - ayagmar.
- [bully911210/claude-code-mods](https://github.com/bully911210/claude-code-mods) - Claude Code için işlev kancası modları: sınır telemetrisi satırı, çoklu seçim…
- [comertial/comertial-mods](https://github.com/comertial/comertial-mods) - Gerçek Mühendisler için Claude Code modları.
- [CrazyCoder/claude-desktop-recap](https://github.com/CrazyCoder/claude-desktop-recap) - Claude Code.
- [danielpg95/modster-hunter](https://github.com/danielpg95/modster-hunter) - Bir Claude Code modu: Claude çalışırken boşta duran bir oyunda piksel sanatı…
- [Davron2004/slash-coverage](https://github.com/Davron2004/slash-coverage) - Her Claude Code ajanının bağlamında hangi dosyaların olduğunu ve her birinden…
- [enhki/claude-mods](https://github.com/enhki/claude-mods) - Terminal ve masaüstü uygulaması için küçük Claude Code modları.
- [Exdenta/ambient-spanish](https://github.com/Exdenta/ambient-spanish) - Ajan yanıtlarına İspanyolca kelimeler ekleyen Claude CLI becerisi + modu.
- [florian101010/cache-meter](https://github.com/florian101010/cache-meter) - Claude Code Mod – stop wasting tokens: /keepwarm.
- [FrBmt-BIGetNouf/alarum-claude-mod](https://github.com/FrBmt-BIGetNouf/alarum-claude-mod) - Claude Code prompt.
- [FrBmt-BIGetNouf/floatee-claude-mod](https://github.com/FrBmt-BIGetNouf/floatee-claude-mod) - Floatee bekleme listeniz Claude Code isteminin üzerinde: yapılacaklarınızı tek…
- [gregdotca/ccmod-the-machine](https://github.com/gregdotca/ccmod-the-machine) - Onu Person of Interest dizisindeki The Machine olarak yeniden biçimlendiren bir…
- [JimmySadek/claude-code-tint-mod](https://github.com/JimmySadek/claude-code-tint-mod) - Claude Code modu (CC tint modu): her pencereyi deposuna göre renklendirir…
- [jonyfs/astrolabe](https://github.com/jonyfs/astrolabe) - 🧭 Claude Code mod: oturum durumu, canlı Spec Kit ilerlemesi ve kullanım…
- [kevinmedeiros/claude-mods](https://github.com/kevinmedeiros/claude-mods) - Live mods for Claude Code: plan limits that tell you how long they.
- [kongyo2/context-view](https://github.com/kongyo2/context-view) - Bağlam penceresi, istemin üzerinde tek satır olarak;
- [kuehn-lars/cc-graph](https://github.com/kuehn-lars/cc-graph) - cc-graph: Claude Code.
- [kyledarling-io/claude-code-desktop-hud](https://github.com/kyledarling-io/claude-code-desktop-hud) - Claude Code Desktop için canlı görev HUD.
- [KyongSik-Yoon/cc-desktop-mod](https://github.com/KyongSik-Yoon/cc-desktop-mod) - Claude Code eklentisi (modu), Claude Code terminal kullanıcı arayüzünü Claude…
- [leonidb/claude-code-mods](https://github.com/leonidb/claude-code-mods) - Claude Code.
- [LupusMalusDeviant/mod-box](https://github.com/LupusMalusDeviant/mod-box) - Tek bir eklentide, her biri açılıp kapatılabilen on dört Claude Code modu;
- [m4cd4r4/clear-resume](https://github.com/m4cd4r4/clear-resume) - Claude Code için ücretsiz, açık kaynaklı bir eklenti.
- [midudev/better-claude](https://github.com/midudev/better-claude) - Claude Code için mod olarak bir prompt kuyruğu: /after &lt;task&gt;, yönlendirme…
- [modmyclaude/claude-code-mods](https://github.com/modmyclaude/claude-code-mods) - Claude Code modları: özenle seçilmiş, test edilmiş ve her mod, onu oluşturan…
- [NotRedFox/NotRedFoxs-Claude-skills](https://github.com/NotRedFox/NotRedFoxs-Claude-skills) - Claude Code becerileri: belge doğrulayıcı, kod denetçisi, hata anıları günlüğü…
- [Orfila-antoine/claude-mods](https://github.com/Orfila-antoine/claude-mods)
- [pablodiazjorge/rea-casebook](https://github.com/pablodiazjorge/rea-casebook) - Agent.
- [rezzminator/buddy](https://github.com/rezzminator/buddy) - Claude Code arkadaş eklentisi: isteminizin üzerinde kurallarınızı hatırlayan ve…
- [rezzminator/tool-visibility-controller](https://github.com/rezzminator/tool-visibility-controller) - Ajan başına araç görünürlüğü için Claude Code eklentisi — her döngüde alt…
- [samfrmr/barmkin-mod](https://github.com/samfrmr/barmkin-mod) - Claude Code modları: Claude Code için güvenlik katmanı - gizli bilgileri…
- [SeongGwangJu/k-mods](https://github.com/SeongGwangJu/k-mods) - Harika Claude Code modları koleksiyonu | 클로드 코드 모드 모음집.
- [shahsanket2107/clarvis](https://github.com/shahsanket2107/clarvis) - Clarvis: Claude Code için resmî olmayan bir Avengers hayran modu.
- [tanujarun/it-speaks](https://github.com/tanujarun/it-speaks) - Konuşuyor: Claude.
- [timoncool/slapbox](https://github.com/timoncool/slapbox) - 🍑 Hata yaptığında Claude.
- [TroyJLorents-GH/mod-squad](https://github.com/TroyJLorents-GH/mod-squad) - Claude Code modları: canlı bölmeler, maliyet farkındalıklı model yönlendirme ve…
- [UtsavBalar1231/oh-my-claudeagent](https://github.com/UtsavBalar1231/oh-my-claudeagent) - Claude Code, kanıtlarıyla. Çalışmayı planlayan, devreden ve tamamlandığını…
- [VaitaR/claude-code-limits](https://github.com/VaitaR/claude-code-limits) - Claude Code modu: istemin üzerindeki tek satırda 5s/7g kotası, bağlam…
- [valeryia-piatrova/token-hamster](https://github.com/valeryia-piatrova/token-hamster) - 🐹 Claude Code modu ve eklentisi: kullanım monitörü, token izleyici ve durum…
- [Xabilimon1/EMCC](https://github.com/Xabilimon1/EMCC) - EMCC (Every Mod Claude Code): seçilmiş ve test edilmiş Claude Code modları…
- [yyosifov/prompt-mods](https://github.com/yyosifov/prompt-mods) - Prompt kutusu için küçük, tamamlanmış Claude Code modları.
- [0xgigilau/claude-usage-meters](https://github.com/0xgigilau/claude-usage-meters) - Claude Code modu: bağlam, oturum/hafta/ay kullanımı ve model başına token payı…
- [aecheman27-gif/claude-mods](https://github.com/aecheman27-gif/claude-mods) - Claude Code modları pazaryeri (my-claude-mods): durum bandı, paneller…
- [alan-oliv/claude-mods](https://github.com/alan-oliv/claude-mods) - Claude Code modları: istemin üzerinde oturum istatistik kartları.
- [Aler1x/claude-cat](https://github.com/Aler1x/claude-cat) - Claude Code isteminin üzerinde animasyonlu bir braille kedisi.
- [aloki-alok/omni-cat](https://github.com/aloki-alok/omni-cat) - Claude Code isteminizin üzerinde, bir OmniDimension ses ajanı test çağrısı…
- [ambervdberg/smartcompact](https://github.com/ambervdberg/smartcompact) - Bağlam penceresini küçük tutmak için sıkıştırma işlemini uygun bir anda seçen…
- [an80sPWNstar/claude-mods](https://github.com/an80sPWNstar/claude-mods) - Claude Code için Claude modları: token-meter.
- [andrej-kolic/claude-mods](https://github.com/andrej-kolic/claude-mods) - Claude Code için genel amaçlı modlar: bantlar, paneller, bildirimler ve…
- [andytw366/claude-mods](https://github.com/andytw366/claude-mods)
- [aott33/model-router](https://github.com/aott33/model-router) - Her alt aracı başlamadan önce modelini seçen ve her birinin maliyetini gösteren…
- [arthurglaizal/quiet-token-bar](https://github.com/arthurglaizal/quiet-token-bar) - A Claude Code mod: your context window in one quiet line, grey until it matters.
- [arthurseredaa/herdr-pane-peek](https://github.com/arthurseredaa/herdr-pane-peek) - herdr için Claude Code modu: tüm çalışma alanlarında bölmeleri arayın ve…
- [Ashley-Pettit/lgtm-flash](https://github.com/Ashley-Pettit/lgtm-flash) - The LGTM Lines ship sails past after every code change — a Claude Code mod.
- [Ashley-Pettit/villager-hp](https://github.com/Ashley-Pettit/villager-hp) - Haftalık tempo uyarısıyla birlikte Claude kullanım sınırlarınızı animasyonlu…
- [AskTinNguyen/ather-mods](https://github.com/AskTinNguyen/ather-mods) - S2 ekibi için Claude Code modları (ather pazaryeri).
- [astrosteveo/plain-english](https://github.com/astrosteveo/plain-english) - A Claude Code mod that makes Claude write plain English and flags its usual…
- [Atanur/deskfit](https://github.com/Atanur/deskfit) - Claude çalışırken kısa antrenmanlar: günlük hedef, seriler, rozetler ve isteğe…
- [avishalom/session-note](https://github.com/avishalom/session-note) - Claude Code mod: pin a context comment and a color to a session.
- [aycandv/claude-usage-meter](https://github.com/aycandv/claude-usage-meter) - Claude Code için kullanım panosu: modele göre harcama.
- [barmoshe/bar-mods](https://github.com/barmoshe/bar-mods) - Claude Code modları: Claude Code içinde çalışan canlı bölmeler, bantlar ve…
- [Barncore/agent-watch](https://github.com/Barncore/agent-watch) - Alt aracılarınızın ne yaptığını gösteren bir Claude Code modu: istemin üzerinde…
- [Barncore/turn-timer](https://github.com/Barncore/turn-timer) - Her turun ne kadar sürdüğünü Claude.
- [benelog/claude-mods](https://github.com/benelog/claude-mods) - Claude Code için modlar: durum satırı HUD.
- [benjaminr/nowplaying](https://github.com/benjaminr/nowplaying) - Claude Code için Now Playing modu: istemin üzerinde kapak görseli, kontroller…
- [bracyw/claude-mods](https://github.com/bracyw/claude-mods) - Bakımı yapılan, denetlenmiş Claude Code mod kopyaları (filetree, cache-tax).
- [brahim1o1/claude-turn-profiler](https://github.com/brahim1o1/claude-turn-profiler) - Claude Code için Performance sekmesi şunları gösterir: her model isteği ve araç…
- [broening/claude-mods](https://github.com/broening/claude-mods) - Claude Code için modlar: önbellek saati, patlama yarıçapı, öneriler, iş…
- [Carismarkus/clowl](https://github.com/Carismarkus/clowl) - Claude Code.
- [cch-agent/claude-mods](https://github.com/cch-agent/claude-mods) - Kişisel Claude Code modları.
- [cdeust/claude-mods](https://github.com/cdeust/claude-mods) - Claude Code mods for the ai-architect.tools harness: one concern per mod, state…
- [ChaseWNorton/claude-doom](https://github.com/ChaseWNorton/claude-doom) - İçinde Freedoom bulunan orijinal Doom motoru, Claude Code içinde oynanabilir.
- [chshin84/claude-mods](https://github.com/chshin84/claude-mods) - Claude Code 단어 사전 패널과 상태 표시줄 플러그인.
- [cldotdev/claude-todo-list](https://github.com/cldotdev/claude-todo-list) - A Claude Code mod that keeps a running list of the open items in a conversation…
- [connectwithub/loopkeeper](https://github.com/connectwithub/loopkeeper) - Claude Code.
- [cprentice9/ccmods](https://github.com/cprentice9/ccmods) - Claude Code modları.
- [CTeitzel/claude-code-cache-band](https://github.com/CTeitzel/claude-code-cache-band) - Claude Code modu: prompt.
- [DannyW618/What-skills-am-i-using](https://github.com/DannyW618/What-skills-am-i-using) - Claude Code modu: konuşmanızın hangi becerileri, eklentileri, alt ajanları ve…
- [davidcoulson/crab-workshop](https://github.com/davidcoulson/crab-workshop) - Çok sayıda paralel oturum içeren homelab iş akışı için on bir Claude Code modu…
- [davidurco/cc-tamagotchi](https://github.com/davidurco/cc-tamagotchi) - Claude Code içinde yaşayan bir Tamagotchi: yumurtadan çıkar, Claude.
- [deepr1tester-cloud/claude-pr-tracker](https://github.com/deepr1tester-cloud/claude-pr-tracker) - Claude Code modu: prompt.
- [dim-owl/roll-call](https://github.com/dim-owl/roll-call) - Bir Claude Code modu: prompt.
- [dookers-code/dooks-mods](https://github.com/dookers-code/dooks-mods) - claude modlarından oluşan koleksiyonum.
- [dot-agi/arrester](https://github.com/dot-agi/arrester) - Claude Code modu: bir guard araç çağrısını engelledikten sonra aynı hedefe…
- [dot-agi/downrange](https://github.com/dot-agi/downrange) - Claude Code modu: gerçek çıktından okunan ilerleme ve tahmini varış süreleriyle…
- [dot-agi/high-command](https://github.com/dot-agi/high-command) - Claude Code modu: ekip arkadaşlarından, adlandırılmış alt ajanlardan ve diğer…
- [dot-agi/sandbox-tuner](https://github.com/dot-agi/sandbox-tuner) - Claude Code modu: sandbox engellemelerini açıklar ve tekrarlanan engellemeleri…
- [dricosnyman/claude-favourites](https://github.com/dricosnyman/claude-favourites) - Claude Code için favoriler: komutlarınız ve becerileriniz için tek tıklamalı…
- [drolosoft/taskrail](https://github.com/drolosoft/taskrail) - Claude Code isteminin üstünde oturum planınızın canlı dalga panosu.
- [Eiyuo/Claude-Mods](https://github.com/Eiyuo/Claude-Mods)
- [elijah-rou/agent-kit](https://github.com/elijah-rou/agent-kit) - Pi, Codex ve Claude Code için talimatlar, beceriler, Pi uzantıları ve Claude…
- [feizaodemon/claude-mods](https://github.com/feizaodemon/claude-mods) - Claude Code modları (işlev kancası eklentileri): session-meter ve daha fazlası.
- [finalpantasy/claude-mod-hider](https://github.com/finalpantasy/claude-mod-hider) - Claude Mod Hider: isteminizin üzerindeki tüm Claude Code modlarını gizleyen ve…
- [finalpantasy/claude-mod-pack](https://github.com/finalpantasy/claude-mod-pack) - Claude Mod Pack: small Claude Code mods.
- [fllag/claude-mods](https://github.com/fllag/claude-mods) - Hospedin ekibinin Claude Code için test aşamasındaki modları.
- [fran343/claude-mods](https://github.com/fran343/claude-mods)
- [francktrouillez/claude-freeze](https://github.com/francktrouillez/claude-freeze) - Claude Code modu: bir oturumu dondurun ve hiçbir şey olmamış gibi daha sonra…
- [g761007/hudcade](https://github.com/g761007/hudcade) - Claude Code için bağlamı, maliyeti, önbelleği, aracıları ve hız sınırlarını bir…
- [GeckoKing9/claude-code-copy-button](https://github.com/GeckoKing9/claude-code-copy-button) - Claude Code yanıtlarındaki her kod bloğuna Ctrl+tıklamayla bağlantı kopyalama…
- [gggg5151/claude-desktop-links-to-vscode-mod](https://github.com/gggg5151/claude-desktop-links-to-vscode-mod) - Masaüstü uygulaması için bir Claude Code modu: yanıttaki bir dosya başvurusuna…
- [h3h/blocks-only](https://github.com/h3h/blocks-only) - Claude Code modu: kodlama turları, yazılan blokların doğrulanmış raporuyla sona…
- [haruki-cl/claude-code-mods](https://github.com/haruki-cl/claude-code-mods) - Claude Code modları: token-weather (bağlam kullanımı ve bellek paneli), run-cat…
- [hb03/claude-mods](https://github.com/hb03/claude-mods) - Claude Code için Almanca modlar: bağlam/önbellek ipuçları, rehberli açık…
- [Hekzory/spend-meter](https://github.com/Hekzory/spend-meter) - Claude Code için canlı harcama ölçer: sağ tarafa sabitlenmiş, alt agent.
- [Huuuuung/think-meter](https://github.com/Huuuuung/think-meter) - Claude Code modu: her yanıtın ne kadar sürdüğü, Claude.
- [hymleong/claude-mods](https://github.com/hymleong/claude-mods) - claude modları pazaryeri.
- [imsungbin/quackpit-mod](https://github.com/imsungbin/quackpit-mod) - Claude Code isteminizin üzerinde bir kokpit. Ördek göstergeleri okur.
- [Isaacg1000/isaac-mods](https://github.com/Isaacg1000/isaac-mods) - Eight Claude Code mods: progress panel, tool skins, file tree, cache and delete…
- [jasonXiao422/drawing2sw](https://github.com/jasonXiao422/drawing2sw) - Mühendislik çizimlerinizi otomatik olarak okur ve ardından SolidWorks.
- [jeffyfung/claude-mods](https://github.com/jeffyfung/claude-mods) - A place to house my claude mods.
- [JeremyHo1123/claude-code-agent-board](https://github.com/JeremyHo1123/claude-code-agent-board) - VS Code içinde Claude Code alt ajanlarının canlı panosu: her konuşmanın alt…
- [jessetsai1024/claude-ctx-panel](https://github.com/jessetsai1024/claude-ctx-panel) - Kenar çubuğunda bağlam kullanım paneli: toplam, kategoriler, tur başına büyüme…
- [jessetsai1024/claude-files](https://github.com/jessetsai1024/claude-files) - Kenar çubuğunda dosya listesi: bu konuşmada hangi dosyalar oluşturuldu…
- [jessetsai1024/claude-maomao](https://github.com/jessetsai1024/claude-maomao) - Girdi kutusunun üzerinde koşup zıplayan 8-bit tarzı 毛毛.
- [jessetsai1024/claude-prompts](https://github.com/jessetsai1024/claude-prompts) - Kenar çubuğunda “sorduğum sorular”: kullanıcının bu konuşmada yazdığı her…
- [jessetsai1024/claude-timeline](https://github.com/jessetsai1024/claude-timeline) - Kenar çubuğunda zaman çizelgesi: bu turda zaman nereye harcandı.
- [jessetsai1024/claude-tokens](https://github.com/jessetsai1024/claude-tokens) - Kenar çubuğunda token alışverişi: ana konuşma her seferinde Anthropic.
- [jessetsai1024/claude-whisper](https://github.com/jessetsai1024/claude-whisper) - claude code.
- [jkf87/mod-guide](https://github.com/jkf87/mod-guide) - Unofficial community guide to Claude Code mods (function hooks) in 6 languages…
- [jorgehsy/claude-mods](https://github.com/jorgehsy/claude-mods) - Claude Code mod kataloğu.
- [Joseph-Ayoub/claude-mods](https://github.com/Joseph-Ayoub/claude-mods) - Joseph Ayoub.
- [jrojasdeveloper/naruto-buddy](https://github.com/jrojasdeveloper/naruto-buddy) - Claude Code modu: prompt.
- [jrpferreira2002-jpg/clawd-vibe](https://github.com/jrpferreira2002-jpg/clawd-vibe) - Claude Code modu: istemin üzerinde Clawd, clawd.
- [KaiC5504/clawd-bar](https://github.com/KaiC5504/clawd-bar) - Clawd, Claude Code prompt.
- [kajidog/cc-mods-tts](https://github.com/kajidog/cc-mods-tts) - Claude Code yanıtlarını ve bildirimlerini VOICEVOX / Irodori-TTS gibi araçlarla…
- [ke11/claude-mods](https://github.com/ke11/claude-mods) - Claude Code modları. PixBar: isteminizin üzerinde yer alan ve turunuz…
- [KiranPothana/session-board](https://github.com/KiranPothana/session-board) - Claude Code modu: her Claude Code oturumunu canlı olarak ne yaptıklarını ve…
- [KrasimirKralev/krasi-mods](https://github.com/KrasimirKralev/krasi-mods) - Tek bir eklenti pazaryerinde küçük Claude Code modları.
- [Kruhlikau/subagent-tuner](https://github.com/Kruhlikau/subagent-tuner) - Claude Code modu: her alt ajanın modelini ve akıl yürütme eforunu seçer.
- [krysmalskipl/claude-code-mods](https://github.com/krysmalskipl/claude-code-mods) - Claude Code mods by krysmalskipl: install only the ones you want.
- [kyuskoj/claude-mods](https://github.com/kyuskoj/claude-mods)
- [lakmadev/claude-mods](https://github.com/lakmadev/claude-mods) - On Claude Code modu: animasyonlu piksel evcil hayvanı, Code Wrapped, lo-fi…
- [Loup0007A/claude-mods](https://github.com/Loup0007A/claude-mods)
- [Lucas-CX/awesome-claude-mods](https://github.com/Lucas-CX/awesome-claude-mods) - Topluluk tarafından derlenmiş bir Claude Code Modları rehberi: kullanım…
- [lucianokatze/mk-usage](https://github.com/lucianokatze/mk-usage) - Claude Code modu: planınızın limitleri (5 saatlik oturum, hafta) ve yenilenme…
- [LupusMalusDeviant/claude-mods](https://github.com/LupusMalusDeviant/claude-mods) - Mod Box.
- [Lutifya/claude-code-mods](https://github.com/Lutifya/claude-code-mods) - Claude Code mods: next-steps (suggested prompts + usage bars) and scratch.
- [M-i-k-e-l/agent-state](https://github.com/M-i-k-e-l/agent-state) - Claude.
- [malinfossum/mango-buddy](https://github.com/malinfossum/mango-buddy) - Claude Code isteminizin üzerinde tüylü siyah bir kedi.
- [malitov/effort-per-model](https://github.com/malitov/effort-per-model) - Claude Code modu: model başına efor düzeyini hatırlar ve geçiş yaptığınızda…
- [marcelmatula/claude-mods](https://github.com/marcelmatula/claude-mods) - Marcel.
- [MarkMerk/markmerk-mods](https://github.com/MarkMerk/markmerk-mods) - Claude Code için küçük modlar: runner-avatar, isteminizin üzerinde koşan küçük…
- [MathysRaw/claude-mods](https://github.com/MathysRaw/claude-mods) - Claude modları: token sayacı (token-meter).
- [mattbv/intent-ledger](https://github.com/mattbv/intent-ledger) - Claude Code modu: Yapay zekâ kodlama ajanınızın neyi amaçladığını…
- [max-gom/claude-session-remover](https://github.com/max-gom/claude-session-remover) - Claude Code modu: oturumları disk üzerindeki verileriyle birlikte.
- [melandres8/claude-mods](https://github.com/melandres8/claude-mods) - Claude Code modları: relevo (iki oturum arasındaki planner/builder aktarımı) ve…
- [michaelblaess/turbo-mod](https://github.com/michaelblaess/turbo-mod) - Claude Code için yan bölme: Claude.
- [mkiselyow/diff-lens](https://github.com/mkiselyow/diff-lens) - Claude Code mod: ask Claude to guide you through a PR, click any file link in…
- [moabualruz/rice-multi-models](https://github.com/moabualruz/rice-multi-models) - Claude Code modu: oturum ve alt ajan modelleri olarak Codex (ChatGPT aboneliği)…
- [monkfrodo/claude-mods](https://github.com/monkfrodo/claude-mods)
- [MoriHiroshiDesu/hiroshi-claude-mods](https://github.com/MoriHiroshiDesu/hiroshi-claude-mods) - Claude Code için kişisel modlar (arayüz ve davranış).
- [mtami/terminal-tab-title](https://github.com/mtami/terminal-tab-title) - Claude Code modu: terminal sekmesine Claude.
- [muellerei/enable-todo-tools](https://github.com/muellerei/enable-todo-tools) - Oturum başlangıcında CLAUDE_CODE_ENABLE_TODO_TOOLS ayarlayarak, bunları devre…
- [muellerei/sweet-spot](https://github.com/muellerei/sweet-spot) - Güvenli bir duraklama bekleyen, ardından oturumunuzu devralan veya oturumu…
- [muellerei/task-line](https://github.com/muellerei/task-line) - Claude Code modu: istemin üzerinde görev listesi başına bir satır;
- [mugenracerman/clean-view](https://github.com/mugenracerman/clean-view) - Claude Code mod: hides technical output and shows a plain-English progress box…
- [nachtgold/claude-code-connect-four](https://github.com/nachtgold/claude-code-connect-four) - Claude Code içinde bir AI.
- [naoanao/agent-cross-check](https://github.com/naoanao/agent-cross-check) - Claude Code modu: başka bir kodlama ajanı deponuza commit yaptığında Claude…
- [naoanao/shared-repo-guard](https://github.com/naoanao/shared-repo-guard) - Birden çok AI ajanının paylaştığı depolar için Claude Code modu: gizli…
- [Nasrallah-Adel/claude-delegate-launcher](https://github.com/Nasrallah-Adel/claude-delegate-launcher) - İstemin üzerinde her delegate-skills uygulayıcısı (codex, agy, copilot, ...)…
- [NicoSKOOL/seo-mods](https://github.com/NicoSKOOL/seo-mods) - SEO için Claude Code modları: istemin üzerinde canlı DataWise sıralamaları ve…
- [nnemirovsky/cc-monitor-rearm](https://github.com/nnemirovsky/cc-monitor-rearm) - Süreleri dolduğunda Claude Code&#x27;un uzun Monitor izlemelerini, Claude&#x27;i…
- [nozomichi00/claude-code-mods](https://github.com/nozomichi00/claude-code-mods)
- [nu0ma/query-guard](https://github.com/nu0ma/query-guard) - Claude Code.
- [nwilsson/claudepad](https://github.com/nwilsson/claudepad) - Claude Code için bir mod olarak not defteri bölmesi.
- [OG-Matcha/tessera](https://github.com/OG-Matcha/tessera) - Claude Code, Windows ve CJK öncelikli tek bir mod: herhangi bir terminalde…
- [ohade/claude-mods](https://github.com/ohade/claude-mods) - Claude Code modları: görsel küçük resimleri ve durum satırı.
- [olioskar/megamaid-claude-plugin](https://github.com/olioskar/megamaid-claude-plugin) - megamaid: Claude Code modları tarafından zorunlu kılınan kapsamlı inceleme →…
- [omarnaman/claude-mods](https://github.com/omarnaman/claude-mods)
- [osaki42/awesome-claude-mods](https://github.com/osaki42/awesome-claude-mods) - Sizin için yaptıklarına göre sıralanmış en iyi Claude Code Modları.
- [Para-FR/claude-code-mods-fr](https://github.com/Para-FR/claude-code-mods-fr) - Claude Code için iki Claude Modu: garde-du-corps.
- [patrick-lai/claude-fish-stack-mod](https://github.com/patrick-lai/claude-fish-stack-mod) - fishStack: bir Claude Code modu. Salt okunur başlangıçlı kalıcı worktree.
- [philarete173/claude_mods](https://github.com/philarete173/claude_mods) - Claude masaüstü uygulamasının Code sekmesi için canlı oturum istatistikleri yan…
- [PhilRoli/claude-mods](https://github.com/PhilRoli/claude-mods) - Claude Code modu: TrainTracker treniniz gelmeden önce oturumları duraklatır.
- [pradyb/claude-mods](https://github.com/pradyb/claude-mods) - Claude Code için modifikasyonlar: safety-guard yıkıcı komutları ve gizli…
- [pvjbuilds/crab-buddy](https://github.com/pvjbuilds/crab-buddy) - Claude Code için animasyonlu piksel sanatlı bir Claude yengeci: Claude.
- [r1305/claude-mods](https://github.com/r1305/claude-mods) - Mods para Claude Code: enrutado de modelos con dashboard de consumo y…
- [rafagomes/claude-code-mods](https://github.com/rafagomes/claude-code-mods) - Claude Code için modlar: oturum içinde çalışan işlev kancası eklentileri…
- [Risdon8/push-ups](https://github.com/Risdon8/push-ups) - Claude Code modu: Claude çalışırken yapılacak şınavlar. Jeton yok.
- [risen372/claude-mods](https://github.com/risen372/claude-mods)
- [RobGruhl/claude-mod-learnings](https://github.com/RobGruhl/claude-mod-learnings) - Hook Chain: ELI5.
- [Rohitp/claude-mods](https://github.com/Rohitp/claude-mods) - claude code için modlar.
- [Ross-cripto/modshelf](https://github.com/Ross-cripto/modshelf) - Katkılar için depo becerileri ve tutarlı çizimlerle Claude Code modları için…
- [saadk408/stepline](https://github.com/saadk408/stepline) - Claude Code modu: plan modunda onayladığınız planı prompt.
- [saksham10arora-dotcom/awesome-claude-mods](https://github.com/saksham10arora-dotcom/awesome-claude-mods) - Özenle seçilmiş Claude Code modları listesi.
- [saksham10arora-dotcom/claude-frugal](https://github.com/saksham10arora-dotcom/claude-frugal) - Maliyetsiz mod: yardımcı ajanlar Haiku üzerinde çalışır;
- [saksham10arora-dotcom/claude-lofi](https://github.com/saksham10arora-dotcom/claude-lofi) - Oturumu takip eden bir lofi müzikleri: sakinlik, odaklanma, akış ve testlerin…
- [saksham10arora-dotcom/claude-teach-me](https://github.com/saksham10arora-dotcom/claude-teach-me) - Claude kod yazarken öğrenin: kodu değiştiren bir turdan sonra, tam o…
- [saksham10arora-dotcom/claude-vhs](https://github.com/saksham10arora-dotcom/claude-vhs) - Claude.
- [sam-ruff/account-switcher-claude-code-mod](https://github.com/sam-ruff/account-switcher-claude-code-mod) - claude code için hesaplar arasında geçiş yapmanızı sağlayan bir mod.
- [servaes/cockpit](https://github.com/servaes/cockpit) - André Servaes tarafından hazırlanan Cockpit Board ve diğer Claude Code modları.
- [Showrin/claude-mods](https://github.com/Showrin/claude-mods) - Daha üretken bir günlük çalışma için Showrin.
- [sillss1/brain-dash](https://github.com/sillss1/brain-dash) - Claude Code modu: kodun yanındaki bir bölmede bağlam ve plan limitlerini yanma…
- [someonewithpc/claude-mod-keep-going](https://github.com/someonewithpc/claude-mod-keep-going) - Katılımsız oturumların kullanım limitleri, API hataları ve tam bağlamlar…
- [sp1e/context-meter](https://github.com/sp1e/context-meter) - Claude Code modu: oturum başına bağlam penceresi ölçer;
- [StanislavKozachenko/claude-mods](https://github.com/StanislavKozachenko/claude-mods) - TypeScript işlev kancası içeren ve eklenti pazaryeri olarak sunulan Claude Code…
- [steven-ngle/blade-of-commits](https://github.com/steven-ngle/blade-of-commits) - Dans eden pixel-art Malenia ile Claude Code için tek tıkla commit mesajları.
- [T-AI-Labs/claude-code-mods](https://github.com/T-AI-Labs/claude-code-mods) - Claude Code için modlar. cache-meter: istem önbelleği isabet oranı, bağlam…
- [Tanish-Dev/claude-usage-band](https://github.com/Tanish-Dev/claude-usage-band) - Clawd Meter — Claude Code modu; Claude plan kullanımınızı.
- [tanmen/claude-tanmen-plugins](https://github.com/tanmen/claude-tanmen-plugins) - tanmen tarafından hazırlanan resmi olmayan Claude Code modları.
- [tanwar-harsh/luff-crew-monitor](https://github.com/tanwar-harsh/luff-crew-monitor) - Claude Code modu: her alt ajan için canlı ekip paneli.
- [thangnguyen-69/claude-mods](https://github.com/thangnguyen-69/claude-mods) - Claude Code eklenti pazar yeri: tailnet üzerindeki Plannotator incelemeleri ve…
- [TheBabaYaga/claude-session-flow](https://github.com/TheBabaYaga/claude-session-flow) - Her istemi, Claude.
- [theishandubey/claude-mods](https://github.com/theishandubey/claude-mods) - Modlardan oluşan bir Claude Code eklenti pazaryeri: Claude Code içinde bantlar…
- [thomasreichmann/image-peek](https://github.com/thomasreichmann/image-peek) - Claude Code mod: inline previews of the images Claude reads, drawn in the…
- [tomfluff/claude-read-along](https://github.com/tomfluff/claude-read-along) - Okunan cümle vurgulanırken Claude Code.
- [TomySpagnoletti/cc-mods-copy-latest-replies](https://github.com/TomySpagnoletti/cc-mods-copy-latest-replies) - Claude Code modu: Claude.
- [Toptaab/token-garden](https://github.com/Toptaab/token-garden) - Toptaab tarafından hazırlanan Claude Code modları.
- [tornikegomareli/claude-whoami](https://github.com/tornikegomareli/claude-whoami) - İstem altbilgisinde hangi Claude hesabı, kuruluşu ve planında oturum açtığınızı…
- [VAlux/claude-session-progress](https://github.com/VAlux/claude-session-progress) - Claude Code modu: uzun süren görevler için animasyonlu ilerleme bandı ve…
- [Vansitha/clawd-watch](https://github.com/Vansitha/clawd-watch) - Üç küçük Claude Code modu: alt ajanlarınızın ne zaman tamamlanacağını görün…
- [varunmoka7/layman](https://github.com/varunmoka7/layman) - &quot;Kayboldum&quot; deyin, Claude son yanıtını günlük ifadelerle yeniden açıklasın.
- [varunmoka7/side-chat](https://github.com/varunmoka7/side-chat) - Çalışmanızın yanındaki bir bölmede Claude.
- [vmurin/cache-weather](https://github.com/vmurin/cache-weather) - İstem altındaki izin modu satırında (durum satırında değil) istem önbelleği…
- [webfront/claude-mods](https://github.com/webfront/claude-mods) - claude code ve claude app.
- [wesleystagg/model-router](https://github.com/wesleystagg/model-router) - Claude Code modu: oturumun kendi modeli, her alt aracının modelini ve eforunu…
- [wisbech/molt](https://github.com/wisbech/molt) - molt — bağlam kabuğuna sığmadığında onu klasöre bırak ve devam et.
- [wonr-spec/claude-mods](https://github.com/wonr-spec/claude-mods) - Claude Code mod 모음 (wonr-mods 마켓플레이스).
- [Wowbagger1994/claude-mods](https://github.com/Wowbagger1994/claude-mods) - Claude Code için mod: maskelenmiş sırlar, yapılacaklar, kontroller ve CI…
- [wukonigcom/quanta-costa](https://github.com/wukonigcom/quanta-costa) - 🧾 Claude Code eklentisi: Claude Pro/Max kullanım limitleriniz, hız tahmini…
- [xinhuagu/oh-my-claude-mods](https://github.com/xinhuagu/oh-my-claude-mods) - Claude Code için modlar. agent-crew: alt aracılarınızı rol, model, mevcut araç…
- [zhitongLIU/claude-code-mods](https://github.com/zhitongLIU/claude-code-mods)
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - Durdurulamaz Anthropic PBC ekibinden (bağlantısı yoktur), kodlama…
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) - Neler olduğunu gösteren bir Claude Code eklentisi - bağlam kullanımı, etkin…
- [sirmalloc/ccstatusline](https://github.com/sirmalloc/ccstatusline) - 🚀 Claude Code CLI için powerline desteği, temalar ve daha fazlasını içeren…
- [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) - Claude Code.
- [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) - Claude Code ve Codex için AI video becerisi — Remotion ile sinematik ürün…
- [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) - Claude Code.
- [persiyanov/herdr-reviewr](https://github.com/persiyanov/herdr-reviewr) - Kodlama aracınızın diff.
- [uppinote20/claude-dashboard](https://github.com/uppinote20/claude-dashboard) - Bağlam kullanımı, API hız sınırları ve maliyet takibiyle Claude Code için…
- [starbaser/ccproxy](https://github.com/starbaser/ccproxy) - Claude Code için modlar oluşturun: Her isteğe kanca ekleyin, her yanıtı…
- [gwittebolle/claude-carbon](https://github.com/gwittebolle/claude-carbon) - claude-carbon: Claude Code oturumlarınızın karbon ayak izini takip edin.
- [AwesomeZun/CC-statusline](https://github.com/AwesomeZun/CC-statusline) - awesomejun tarafından Claude Code için hazırlanmış estetik durum satırı.
- [a86582751/dsh-nexttavern](https://github.com/a86582751/dsh-nexttavern) - DeepSeek Harness uzun biçimli rol yapma ajanı (DSH酒馆 eklentisi): SillyTavern…
- [JohnnyVizz/claude-kit](https://github.com/JohnnyVizz/claude-kit) - Herkese açık Claude Code Skills.
- [escapeboy/claude-code-kit](https://github.com/escapeboy/claude-code-kit) - Claude Code için Skills.
- [arturogarrido/claudinho](https://github.com/arturogarrido/claudinho) - ⚽ Takip ettiğiniz müsabaka için canlı futbol skorları, fikstürler ve puan…
- [johncattrall/keymap-ai](https://github.com/johncattrall/keymap-ai) - Kodlama aracınızı klavye ürün yazılımı uzmanına dönüştüren Agent Skill.
- [PerryLink/dsh-talk](https://github.com/PerryLink/dsh-talk) - DeepSeek Harness için ses öncelikli oturum döngüsü: tarayıcı/yerel konuşmadan…
- [ashafizullah/claude-code-muslim-mods](https://github.com/ashafizullah/claude-code-muslim-mods) - Claude Code içinde namaz vakitleri, Hicri tarih, zikirler, günlük ayet, sünnet…
- [philoserf/claude-code-config](https://github.com/philoserf/claude-code-config) - ~/.claude içinde sürümlendirilen kişisel Claude Code yapılandırması…
- [benz-ai-x/dsh-research-graph](https://github.com/benz-ai-x/dsh-research-graph) - DSH Research Graph · 研图 — araştırma konuları, izlenebilir bilgi kartları ve…
- [1225Sakura/oh-my-deepseekharness](https://github.com/1225Sakura/oh-my-deepseekharness) - DeepSeek Harness için çoklu ajan orkestrasyon katmanı (omd)…
- [hoobnn/hoobnn-agent-mods](https://github.com/hoobnn/hoobnn-agent-mods) - Claude Code, pi ve DeepSeek Harness için eklenti koleksiyonu: durum çubuğu…
- [pierrebelin/claude-code-toolkit](https://github.com/pierrebelin/claude-code-toolkit) - .NET DDD/Clean Architecture için taşınabilir Claude Code araç seti: katı TDD…
- [TurboKach/claude-code-statusline](https://github.com/TurboKach/claude-code-statusline) - Hafif Claude Code durum satırı — tek bir ~170 satırlık Bash betiği, sıfır…
- [jcdendrite/claude-config](https://github.com/jcdendrite/claude-config) - Taşınabilir Claude Code global yapılandırması: özel beceriler, PreToolUse…
- [manson341349-beep/claude-desktop-mods](https://github.com/manson341349-beep/claude-desktop-mods) - Claude Desktop.
- [mutlumehmet/claude-plugins](https://github.com/mutlumehmet/claude-plugins) - Her gün kullandığım Claude Code eklentileri: herkesin makinesinde çalışacak…
- [cc-friend/ccost](https://github.com/cc-friend/ccost) - Yerel konuşma günlüklerinden ve durum satırı verilerinden Claude Code token…
- [ericbust/namedrop](https://github.com/ericbust/namedrop) - @mentions for Codex, Claude Code, and your terminal.
- [mkalkere/claude-statusline](https://github.com/mkalkere/claude-statusline) - Claude Code için güzel ve bilgilendirici durum satırı.
- [abdullahkavakli/let-them-talk](https://github.com/abdullahkavakli/let-them-talk) - Claude Code ajanlarınız için görsel pano: oturumları, alt ajanları ve arka plan…
- [alpadalar/ccinfobar](https://github.com/alpadalar/ccinfobar) - Sürükle ve bırak düzenleyicisine sahip, özelleştirilebilir bir Claude Code…
- [darthmolen/hytale-claude-code-marketplace](https://github.com/darthmolen/hytale-claude-code-marketplace) - Hytale oyununda modları kolaylaştırmak için Claude Code Eklentileri ve…
- [devrim-1283/claude-code-statusline](https://github.com/devrim-1283/claude-code-statusline) - Claude Code için tek satırlı, renk kodlu durum satırı — klasör, model, bağlam…
- [frsorrentino/fable-director](https://github.com/frsorrentino/fable-director) - Claude Code için token yönetimi: en üst model yönlendirir, yürütme en ucuz…
- [jeancarlo-javier/claude-status-bar](https://github.com/jeancarlo-javier/claude-status-bar) - Claude Code için canlı iş akışı aşaması durum satırı.
- [risukisu/claude-code-statusline](https://github.com/risukisu/claude-code-statusline) - Claude Code terminali için 3 satırlı mikro pano — model, bağlam tüketimi, hız…
- [romnycristopher/claude-am-mods](https://github.com/romnycristopher/claude-am-mods) - Claude Code Awesome Media modları için depo.
- [rootstudioyaml/sprag](https://github.com/rootstudioyaml/sprag) - Claude Code ve Codex token harcamasını azaltın: aramaları ve test…
- [mitre/claude-statusline](https://github.com/mitre/claude-statusline) - Claude Code için hızlı, yapılandırılabilir durum satırı — tek statik Go ikilisi.
- [carterptull/ampline-claude](https://github.com/carterptull/ampline-claude) - An amplified color-graded, zero-dependency statusline for Claude Code.
- [crosscountryridinggirlwonder916/claude-statusline](https://github.com/crosscountryridinggirlwonder916/claude-statusline) - Daha iyi çalışma alanı farkındalığı için Claude Code durum satırını hız…
- [L3DigitalNet/ClaudeCodeStatusLine](https://github.com/L3DigitalNet/ClaudeCodeStatusLine) - Claude Code için kompakt ve aktif olarak sürdürülen durum satırı — model, çaba…
- [Ma1achy/claude-statusline](https://github.com/Ma1achy/claude-statusline) - Claude Code için her şeyle oynanabilen dost canlısı durum satırı — truecolor…
- [zach-source/claude-factory](https://github.com/zach-source/claude-factory) - herdr üzerinde Claude Code için tanımlanabilir yazılım fabrikaları: xstate…
- [0xSerachu/claude-shortcuts](https://github.com/0xSerachu/claude-shortcuts) - Explore and quiz yourself on all Claude Code shortcuts with categorized…
- [Alpinoo/claude-code-usage-statusline](https://github.com/Alpinoo/claude-code-usage-statusline) - Claude Code için Windows PowerShell durum satırı: sıfırlama geri sayımlarıyla 5…
- [ctfbio/claude-code-statusline](https://github.com/ctfbio/claude-code-statusline) - Professional-grade Claude Code statusline: session duration, multi-currency…
- [divramod/divramod-claude-code-plugins](https://github.com/divramod/divramod-claude-code-plugins) - divramod&#x27;un Claude Code eklentileri, tek bir marketplace&#x27;te: Claude Code için…
- [erDevKumar/claude-code-companion](https://github.com/erDevKumar/claude-code-companion) - VS Code uzantısı: yerel bir IPC soketi üzerinden statusLine aracılığıyla Claude…
- [fbandres/ccmods](https://github.com/fbandres/ccmods) - Claude Code için modlar: eklenti olarak kurulabilen canlı bölmeler, göstergeler…
- [FukKwang/claude-statusline](https://github.com/FukKwang/claude-statusline) - Renkli Claude Code durum satırı: plan limitleri, bağlam, maliyet ve token.
- [Gabriel-Dalton/claude-statusline-tokens](https://github.com/Gabriel-Dalton/claude-statusline-tokens) - Windows için Claude Code durum satırı: token toplamları, API-rate maliyeti ve 5…
- [gvart/claude-config](https://github.com/gvart/claude-config) - Claude Code kurulumum: agent-monitor modu, beceriler, aracılar ve tek komutlu…
- [hieuvo/claude-imgview](https://github.com/hieuvo/claude-imgview) - Görüntüleri Claude Code içinde önizleyin: resmi açmak için bir yanıtın…
- [IceThunder/claude-statusline](https://github.com/IceThunder/claude-statusline) - Claude Code durum satırı: model, 5s/7g kota çubukları, aylık harcama çubuğu, cwd.
- [IdoSagiv/claude-config](https://github.com/IdoSagiv/claude-config) - Kişisel Claude Code yapılandırması: izinler, durum satırı, MCP sunucuları.
- [ihororlovskyi/claude-statusline](https://github.com/ihororlovskyi/claude-statusline) - Ajan paneli satırlarına sahip Claude Code durum satırı.
- [kgdemir/claude-agentic-os](https://github.com/kgdemir/claude-agentic-os) - Claude Agentic OS: taşınabilir Claude Code kurulumu — genel kurallar, eklenti…
- [Kimmihappy793/claude-status-line](https://github.com/Kimmihappy793/claude-status-line) - Bağlamı, git durumunu, maliyetleri ve hız sınırlarını gösteren ayrıntılı…
- [Leechlike-intangibleasset343/claude-code-statusline](https://github.com/Leechlike-intangibleasset343/claude-code-statusline) - Bağlamı, maliyeti, süreyi, git dalını, hız sınırlarını ve canlı kullanımı…
- [LounisBou/claude-statusbar](https://github.com/LounisBou/claude-statusbar) - Bir terminal kodlama ajanı için iki satırlı durum çubuğu: dizin, git, PR…
- [lucasmm96/claude-statusline](https://github.com/lucasmm96/claude-statusline) - Claude Code durum satırı kancası — oturumlar arasında token kullanımını ve…
- [markallisongit/claude-statusline](https://github.com/markallisongit/claude-statusline) - Claude Code durum satırı; Linux ve Windows üzerindeki Git Bash için…
- [mgstegmaier/claude-plugins](https://github.com/mgstegmaier/claude-plugins) - ev yapımı, kafessiz claude eklentileri, becerileri, modları ve daha fazlası.
- [munkgorn/usage-statusline-claude](https://github.com/munkgorn/usage-statusline-claude) - Claude Code için zengin çok satırlı durum satırı — canlı kullanım sınırları.
- [mvrozanti/claude-progressbar](https://github.com/mvrozanti/claude-progressbar) - Progress bars for the Bash commands Claude Code runs, drawn in its statusline…
- [naughty00shortie/claude-statusline](https://github.com/naughty00shortie/claude-statusline) - Çok satırlı Claude Code durum satırı: bağlam çubuğu, git dalı, hesap başına…
- [parisgroup-ai/claude-statusline](https://github.com/parisgroup-ai/claude-statusline) - @parisgroup-ai/claude-statusline — macOS + Linux için Claude Code durum satırı.
- [peaceinitiativemenhadenoil263/claude-status-bar](https://github.com/peaceinitiativemenhadenoil263/claude-status-bar) - Etkin görevler, bekleyen izinler ve geçen süre için gerçek zamanlı…
- [pkkid/claude-aitools](https://github.com/pkkid/claude-aitools) - Various mods and skills for my Claude Desktop setup.
- [primelogiclabio/claude-tools](https://github.com/primelogiclabio/claude-tools) - Claude Code ve Cowork için beceriler ve modlar — project-tracker, reference-doc…
- [rainyfei/claude-statusline-win](https://github.com/rainyfei/claude-statusline-win) - Windows (PowerShell) için Claude Code durum satırı: kullanım çubukları, hız…
- [Rubio-Enterprises/claude-statusline](https://github.com/Rubio-Enterprises/claude-statusline) - Özel Claude Code durum satırı (üst kaynak: kamranahmedse/claude-statusline).
- [satoramoto/awesome-claude](https://github.com/satoramoto/awesome-claude) - Paylaşılan bir bileşen kiti, playground ve Storybook ile Claude Code…
- [scaso01/claude-risk-guardrails](https://github.com/scaso01/claude-risk-guardrails) - Claude Code için model risk yönetimi korumaları: altı mod paketinde 25 kontrol;
- [Screddyice/claude-code-harness](https://github.com/Screddyice/claude-code-harness) - Claude Code için başlangıç altyapısı: kancalar, durum satırı, yerel modeller…
- [Sofia-D4L/claude-conf](https://github.com/Sofia-D4L/claude-conf) - Claude Code için taşınabilir yapılandırma (statusline + yükleyici).
- [t4t5u0/claude-statusline](https://github.com/t4t5u0/claude-statusline) - Claude Code için 4 satırlık durum satırı.
- [thaiquangquy/claude.me](https://github.com/thaiquangquy/claude.me) - Taşınabilir Claude Code yapılandırması: CLAUDE.md, settings, statusline, skills.
- [tumuyijiao114514/claude-pulse](https://github.com/tumuyijiao114514/claude-pulse) - ⚡ Claude Code için Evrensel Çok Protokollü StatusLine, Kendi Kendine Öğrenen…
- [tylergraydev/cc-mods](https://github.com/tylergraydev/cc-mods) - Claude Code için modlar: işlev kancası eklentileri olarak yan bölmeler, durum…
- [Undone-drawknife974/claude-code-statusline](https://github.com/Undone-drawknife974/claude-code-statusline) - Terminaliniz için hafif ve bağımlılık gerektirmeyen bir durum satırı panosuyla…
- [vladdu/claude-kit](https://github.com/vladdu/claude-kit) - Benim Claude Code becerilerim, eklentilerim ve modlarım (pazar yeri: vladdu).
- [whr819987540/claude-sync-settings](https://github.com/whr819987540/claude-sync-settings) - Claude Code kullanıcı düzeyi yapılandırmasını çoklu makineler arasında…
- [Winn-Gaoti-Studio/claude-code-statusline](https://github.com/Winn-Gaoti-Studio/claude-code-statusline) - Degrade ilerleme çubuklarına, renk derecelendirmeli oturum çabasına ve worktree…
- [ymoud/claude-code-statusline](https://github.com/ymoud/claude-code-statusline) - Klasörü, git dalını, modeli, bağlam penceresi kullanımını ve plan kullanım…
- [YoniYon00/claude-feedback-rings](https://github.com/YoniYon00/claude-feedback-rings) - Context Rot Detector 2026 - Claude Code Ajanları için Proaktif AI Bellek ve Hız…
- [zhuyansen/awesome-claude-code-hooks](https://github.com/zhuyansen/awesome-claude-code-hooks) - Claude Code kancaları, alt ajanları ve durum satırları: türe göre düzenlenmiş…
- [tronschell/statusline.sh](https://github.com/tronschell/statusline.sh) - Claude Code durum satırları için görsel bir oluşturucu.
- [Magnus-Gille/tokenatlas](https://github.com/Magnus-Gille/tokenatlas) - Gerçek zamanlı belirteç kullanımını ve tahmini enerji tüketimini gösteren…
- [previsioncystolith584/ai-video-downloader](https://github.com/previsioncystolith584/ai-video-downloader) - Download videos from major platforms and automatically add translated…
- [ishuagrawal/clawdhouse](https://github.com/ishuagrawal/clawdhouse) - Claude Code için modlar: işlev kancaları üzerine kurulu bölmeler, bantlar ve…
- [ashishsk93/baton-mods](https://github.com/ashishsk93/baton-mods) - Görevleri Claude Code oturumlarınız arasında aktarın.
- [lahoramaker/mods-mcp](https://github.com/lahoramaker/mods-mcp) - Fablab.
- [charlie947/mod-maker](https://github.com/charlie947/mod-maker) - Mod Maker: Claude Code.
- [Rimcat-JA/translate-ck3-mods](https://github.com/Rimcat-JA/translate-ck3-mods) - Yerel bir LLM ile CK3 modlarını çevirmek için Codex ve Claude Code becerisi.
- [sTomerG/agent-kit](https://github.com/sTomerG/agent-kit) - Claude Code için açık kaynaklı modlar ve diğer uzantılar.

</details>

<a id="dsh-cordis"></a>

## DSH ve Cordis eklenti ekosistemleri

DeepSeek Harness ve Cordis aynı yere farklı bir yönden ulaşır: onlar için eklenti, mod mekanizmasıdır; dolayısıyla oradaki bir eklenti, buradaki bir moda denktir.

<details>
<summary>🧵 <b><a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b> · ⭐74447 · TypeScript · 👁️ observed · 0 天</summary>

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
| Yıldızlar      | **74447**  |
| Son gönderme   | 2026-10-12 |
| İlk listelenme | 2026-10-04 |

🏷 `agentic-ai` · `agentic-framework` · `agentic-workflow` · `agents` · `ai-agents` · `ai-assistant` · `ai-skills` · `autonomous-agents`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/2ca82c9c9a7fca31.gif" width="100%" alt="ruvnet/ruflo animation"><br><sub>animasyonlu kayıt</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/morluto/rea">morluto/rea</a></b> · ⭐156274 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Yıldızlar      | **156274** |
| Son gönderme   | 2026-10-13 |
| İlk listelenme | 2026-10-05 |

🏷 `agent-skills` · `ai-agents` · `binary-analysis` · `claude-code` · `cli` · `codex` · `cordis` · `ctf`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--rea/f46ca8b1518ae39f.png" width="100%" alt="morluto/rea screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/nexu-io/open-design">nexu-io/open-design</a></b> · ⭐100754 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Yıldızlar      | **100754** |
| Son gönderme   | 2026-10-12 |
| İlk listelenme | 2026-10-04 |

🏷 `agent-skills` · `ai-design` · `byok` · `claude-code-for-design` · `claude-design` · `codex-design` · `coding-agents` · `cursor-design`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nexu-io--open-design/a1049df34322d3ce.png" width="100%" alt="nexu-io/open-design screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/tt-a1i/archify">tt-a1i/archify</a></b> · ⭐82542 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Yıldızlar      | **82542**  |
| Son gönderme   | 2026-10-12 |
| İlk listelenme | 2026-10-04 |

🏷 `agent-skills` · `ai-agents` · `architecture-diagram` · `claude-code` · `claude-skills` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tt-a1i--archify/71b7d4b2427db202.png" width="100%" alt="tt-a1i/archify screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/esengine/DeepSeek-Reasonix">esengine/DeepSeek-Reasonix</a></b> · ⭐35769 · Go · 🔎 inferred · 0 天</summary>

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
| Yıldızlar      | **35769**  |
| Son gönderme   | 2026-10-13 |
| İlk listelenme | 2026-10-06 |

🏷 `agent` · `agent-framework` · `ai-agent` · `ai-coding` · `cli` · `coding-agent` · `deepseek` · `developer-tools`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/awesome-dsh-plugin/awesome-dsh-plugin">awesome-dsh-plugin/awesome-dsh-plugin</a></b> · ⭐18519 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

DeepSeek Harness (dsh) için derlenmiş eklenti listesi · DeepSeek Harness eklentilerinden seçki

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | JavaScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **18519**  |
| Son gönderme   | 2026-10-12 |
| İlk listelenme | 2026-10-13 |

🏷 `awesome` · `awesome-list` · `deepseek-harness` · `dsh` · `dsh-plugin`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/zhu1090093659/dsh-web">zhu1090093659/dsh-web</a></b> · ⭐8667 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

DeepSeek Harness (DSH) Web 插件聚合生态 · 万物皆插件，通过创意工坊分发｜｜DeepSeek Harness (DSH) Web Eklenti Toplama Ekosistemi · Her şey bir eklentidir, Creative Workshop üzerinden dağıtılır

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | TypeScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **8667**   |
| Son gönderme   | 2026-10-12 |
| İlk listelenme | 2026-10-12 |

🏷 `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-web` · `dsh-web-ui`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zhu1090093659--dsh-web/5153c3c61827ebb8.jpg" width="100%" alt="zhu1090093659/dsh-web screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-market/dsh-market">dsh-market/dsh-market</a></b> · ⭐6277 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

DeepSeek Harness içindeki eklenti pazarı — göz atın, arayın, tek tıklamayla yükleyin · DSH görsel eklenti pazarı

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | TypeScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **6277**   |
| Son gönderme   | 2026-10-12 |
| İlk listelenme | 2026-10-13 |

🏷 `deepseek-harness` · `dsh-plugin` · `marketplace`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dsh-market--dsh-market/06b60aace017dab8.png" width="100%" alt="dsh-market/dsh-market screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ccch1mneyyy/dsh-TUI">ccch1mneyyy/dsh-TUI</a></b> · ⭐4466 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

DSH'nin resmî olarak en çok önerilen TUI eklentisi — yüksek performans, düşük ek yük, sevimli piksel balinası, akıcı fare etkileşimi. npm üzerinden tek komutla kurulum. / DSH 官方首推的 TUI 插件，高性能低占用，可爱像素鲸鱼，流畅鼠标交互，npm 一键安装

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | TypeScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **4466**   |
| Son gönderme   | 2026-10-13 |
| İlk listelenme | 2026-10-12 |

🏷 `claude-code` · `coding-agent` · `deepseek` · `deepseek-harness` · `dsh-plugin` · `ink` · `react` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ccch1mneyyy--dsh-tui/18fd45f8f1eaca04.png" width="100%" alt="ccch1mneyyy/dsh-TUI screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/strukto-ai/mirage">strukto-ai/mirage</a></b> · ⭐3680 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Yıldızlar      | **3680**   |
| Son gönderme   | 2026-10-13 |
| İlk listelenme | 2026-10-13 |

🏷 `agent-sandbox` · `agent-tools` · `ai-agents` · `bash` · `claude-code` · `dsh` · `dsh-plugin` · `fuse`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-tauri/deepseek-harness-desktop">dsh-tauri/deepseek-harness-desktop</a></b> · ⭐3001 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

DeepSeek Harness Tauri masaüstü sürümü | Yalnızca 8 MB yükleyici, sıfır ortam kurulumu, hazır eklentiler, Windows / macOS / Linux.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | TypeScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **3001**   |
| Son gönderme   | 2026-10-13 |
| İlk listelenme | 2026-10-12 |

🏷 `deepseek` · `deepseek-harness` · `desktop` · `dsh` · `dsh-desktop` · `dsh-plugin` · `tauri`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dsh-tauri--deepseek-harness-desktop/f281725e73da1059.png" width="100%" alt="dsh-tauri/deepseek-harness-desktop screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xmanrui/dsh-im">xmanrui/dsh-im</a></b> · ⭐1912 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

QR kodu veya bot kimlik bilgileriyle IM botlarını DeepSeek Harness'e bağlayın (飞书、微信、钉钉、企业微信、QQ、Slack、Telegram、Discord ve WhatsApp desteklenir). IM botlarını QR kodu veya kimlik bilgileriyle DeepSeek Harness'e bağlayın (9 kanal).

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | JavaScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **1912**   |
| Son gönderme   | 2026-10-12 |
| İlk listelenme | 2026-10-13 |

🏷 `ai-agents` · `chatbot` · `cordis` · `deepseek` · `deepseek-harness` · `dingtalk-bot` · `discord-bot` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xmanrui--dsh-im/cba81787088f67af.jpg" width="100%" alt="xmanrui/dsh-im screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/AdamPlatin123/dsh-plugin-radar">AdamPlatin123/dsh-plugin-radar</a></b> · ⭐1466 · Python · 🔎 inferred · 0 天</summary>

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
| Yıldızlar      | **1466**   |
| Son gönderme   | 2026-10-12 |
| İlk listelenme | 2026-10-13 |

🏷 `agent-plugins` · `continuous-validation` · `deepseek-harness` · `dsh` · `dsh-plugin` · `ecosystem-radar` · `plugin-registry`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/adamplatin123--dsh-plugin-radar/fb6ad7eb8891212c.jpg" width="100%" alt="AdamPlatin123/dsh-plugin-radar screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/EthanYoQ/AI-Novel-Writer">EthanYoQ/AI-Novel-Writer</a></b> · ⭐1425 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

AI Roman Yazma Yazılımı: ilhamları, karakterleri, dünya kurulumunu, taslakları, bölüm yazımını, incelemeyi ve revizyonu denetlenebilir bir iş akışında düzenler; Windows/macOS masaüstü sürümleri sunar ve yerel ile çevrim içi modelleri destekler. AI Roman Yazma Yazılımı: İlhamları, karakterleri, dünya kurulumunu, taslakları, bölüm yazımını, incelemeyi ve revizyonu denetlenebilir bir iş akışında düzenler. Windows/macOS için masaüstü uygulamaları, Ollama entegrasyonu ve DeepSeek Harness (DSH) eklentisi önizlemesi sunar.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | TypeScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **1425**   |
| Son gönderme   | 2026-10-12 |
| İlk listelenme | 2026-10-13 |

🏷 `ai-writing` · `creative-writing` · `deepseek-harness` · `dsh-plugin` · `electron` · `fiction-writing` · `local-first` · `long-form-fiction`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ethanyoq--ai-novel-writer/97081b4a6febc6aa.png" width="100%" alt="EthanYoQ/AI-Novel-Writer screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/vshulcz/deja-vu">vshulcz/deja-vu</a></b> · ⭐1182 · Go · 🔎 inferred · 0 天</summary>

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
| Yıldızlar      | **1182**   |
| Son gönderme   | 2026-10-12 |
| İlk listelenme | 2026-10-04 |

🏷 `agent-memory` · `ai-memory` · `claude-code` · `claude-code-hooks` · `claude-code-plugins` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/8033ba54a9424c88.png" width="100%" alt="vshulcz/deja-vu screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/5fb930f1983f270b.gif" width="100%" alt="vshulcz/deja-vu animation"><br><sub>animasyonlu kayıt</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/platonai/Browser4">platonai/Browser4</a></b> · ⭐1152 · Kotlin · 🔎 inferred · 0 天</summary>

##### 📝 Özet

Browser4 — an AI-native browser engine for autonomous agents, intelligent extraction, and large-scale web automation.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | Kotlin                                                                                          |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **1152**   |
| Son gönderme   | 2026-10-12 |
| İlk listelenme | 2026-10-13 |

🏷 `agentic-ai` · `agentic-browser` · `ai-browser` · `browser-agent` · `browser-infra` · `browser-use-agent` · `chrome-browser` · `chrome-devtools-protocol`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/platonai--browser4/491fddf43874c5c7.jpg" width="100%" alt="platonai/Browser4 screenshot"></td>
<td align="center" valign="top"><a href="https://img.youtube.com/vi/_BcryqWzVMI/0.jpg"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/platonai--browser4/491fddf43874c5c7.jpg" width="100%" alt="video"></a><br><sub><a href="https://img.youtube.com/vi/_BcryqWzVMI/0.jpg">Şurada izle: img.youtube.com</a> · oynatma barındırıcı sitede açılır; GitHub bunu satır içinde gömemez</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/vibeinging/dsh-desktop">vibeinging/dsh-desktop</a></b> · ⭐594 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

DeepSeek Harness Masaüstü Uygulaması: DSH Sessions, projeler, dosyalar, web araştırması, eklentiler ve Office yapıtları için yerel AI masaüstü çalışma alanı.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | JavaScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **594**    |
| Son gönderme   | 2026-10-12 |
| İlk listelenme | 2026-10-13 |

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

📚 AI Agents'ın doğrulanmış hata ayıklama deneyimlerini eşzamansız olarak paylaşması ve araması için git destekli, sıfır bağımlılıklı mikro ders kitaplığı. | https://misakanet.org

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
| Son gönderme   | 2026-10-12 |
| İlk listelenme | 2026-10-13 |

🏷 `action` · `agents` · `cloudflare-workers` · `codex` · `cordis-plugin` · `d1` · `deepseek-harness` · `deepseek-harness-plugin`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ikalus1988--misakanet/f6853900d49aba17.jpg" width="100%" alt="Ikalus1988/MisakaNet screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/cv-superding/dsh-deepseek-web-login">cv-superding/dsh-deepseek-web-login</a></b> · ⭐261 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

Resmî olmayan DSH (DeepSeek Harness) eklentisi: chat.deepseek.com web modellerini bir LLM sağlayıcısı olarak kullanın - tarayıcı oturumu açma yakalama, PoW çözme, SSE akışı, isteme tabanlı araç çağrıları.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | JavaScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **261**    |
| Son gönderme   | 2026-10-12 |
| İlk listelenme | 2026-10-13 |

🏷 `browser-automation` · `cordis` · `cordis-plugin` · `deepseek` · `deepseek-harness` · `dsh` · `llm-provider`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/cv-superding--dsh-deepseek-web-login/b95392c45786ce03.png" width="100%" alt="cv-superding/dsh-deepseek-web-login screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/acryldev/acryl">acryldev/acryl</a></b> · ⭐255 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

ACRYL - Agent Context Relay Yielding Lifecycles. Tek kalıcı çalışma alanı, tek kanonik bağlam, herhangi bir kodlama ajanı.

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
| Son gönderme   | 2026-10-12 |
| İlk listelenme | 2026-10-13 |

🏷 `acryl` · `agent-context-relay` · `agentic` · `agentic-ai` · `agentic-coding` · `agentic-development-environment` · `agentic-workflow` · `agentic-workflows`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/acryldev--acryl/47cfe6b23e87eea1.png" width="100%" alt="acryldev/acryl screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/PerryLink/dsh-research-report">PerryLink/dsh-research-report</a></b> · ⭐214 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

DeepSeek Harness için doğrulanabilir araştırma raporu motoru: içerik adresli kanıt defteri (iddia-anlık görüntü bağlama, kurcalamaya karşı kanıt) ve iddia başına doğrulama kararları ile sürümlendirilmiş mühürlü raporlar; bildirimle mühürlenmiş bir dizin.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | TypeScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **214**    |
| Son gönderme   | 2026-10-12 |
| İlk listelenme | 2026-10-13 |

🏷 `ai-agent` · `ai-agents` · `audit` · `citation-verification` · `cordis` · `deepseek-harness` · `developer-tools` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-research-report/2a270ca82dba24d3.png" width="100%" alt="PerryLink/dsh-research-report screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-research-report/dafefe1b3e0cd96e.gif" width="100%" alt="PerryLink/dsh-research-report animation"><br><sub>animasyonlu kayıt</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Hilbert-beinghappy/seektty">Hilbert-beinghappy/seektty</a></b> · ⭐197 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

DeepSeek Harness için Claude Code tarzı terminal arayüzü; Windows, macOS ve Linux desteği sunar, şeffaf terminal, VS Code temaları ve özel renk şemalarıyla uyumludur.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | TypeScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **197**    |
| Son gönderme   | 2026-10-12 |
| İlk listelenme | 2026-10-13 |

🏷 `agentic-ai` · `ai-agent` · `claude-code-style` · `cli` · `coding-agent` · `cross-platform` · `deepseek` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hilbert-beinghappy--seektty/c8ebb5a8f31f3724.png" width="100%" alt="Hilbert-beinghappy/seektty screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xiajiajun516/dsh-config-manager">xiajiajun516/dsh-config-manager</a></b> · ⭐184 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

DeepSeek Harness (DSH) backup & restore plugin — export, import, migrate and sync your complete DSH configuration, plugins, MCP servers, skills and workspace. One-click migration to another machine.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | TypeScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **184**    |
| Son gönderme   | 2026-10-13 |
| İlk listelenme | 2026-10-13 |

🏷 `backup` · `cli` · `config-manager` · `configuration` · `cordis` · `deepseek` · `deepseek-harness` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xiajiajun516--dsh-config-manager/52a2f3587f8e40b4.png" width="100%" alt="xiajiajun516/dsh-config-manager screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Totoro-qaq/dsh-plugin-bridge">Totoro-qaq/dsh-plugin-bridge</a></b> · ⭐165 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

Önizlenebilir ön ayarlar arası oturum geçişi için DeepSeek Harness eklentisi. Sabit şemalı aktarımlar durumu, kaynak modelin niyetini ve çözümlenmemiş görselleri korur; özgün oturum değiştirilmeden kalır.

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
| Son gönderme   | 2026-10-12 |
| İlk listelenme | 2026-10-12 |

🏷 `context-migration` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `preset-migration` · `session-migration`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/totoro-qaq--dsh-plugin-bridge/568de849cd2e9608.png" width="100%" alt="Totoro-qaq/dsh-plugin-bridge screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/totoro-qaq--dsh-plugin-bridge/b4a12cab0ba15f06.gif" width="100%" alt="Totoro-qaq/dsh-plugin-bridge animation"><br><sub>animasyonlu kayıt</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Nwflower/dsh-claude-style">Nwflower/dsh-claude-style</a></b> · ⭐144 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Yıldızlar      | **144**    |
| Son gönderme   | 2026-10-12 |
| İlk listelenme | 2026-10-12 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-desktop` · `cordis` · `dark-mode` · `deepseek-harness` · `desktop-theme`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Nwflower/dsh-claude-style/master/docs/screenshots/claude-home-dark.png" width="100%" alt="Nwflower/dsh-claude-style screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Nwflower/dsh-claude-style/master/docs/gifs/idle.gif" width="100%" alt="Nwflower/dsh-claude-style animation"><br><sub>animasyonlu kayıt</sub></td>
</tr></table>

<sub>Yeniden dağıtıma izin veren bir lisans belirtilmediği için varlığa upstream deposundan doğrudan bağlantı veriliyor.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/FeatherHunter/dsh-mattpocock-skills-deck">FeatherHunter/dsh-mattpocock-skills-deck</a></b> · ⭐141 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

Kurulumla birlikte mattpocock/skills v1.3.1'in 27 mühendislik ve verimlilik becerisi gelir; becerileri elle yüklemeniz gerekmez. 40 milyar token ile oluşturulan bu eklenti, özgün becerilerin üzerine 10 kat geliştirme verimliliği sunar ve yeni başlayanların bu beceri paketine daha hızlı alışmasına da yardımcı olur. GitHub issue'larını tam olarak destekler; Markdown önizleme sürümündedir; GitLab henüz desteklenmemektedir. Kullanımınız ve desteğiniz için teşekkürler 💗

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | JavaScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **141**    |
| Son gönderme   | 2026-10-12 |
| İlk listelenme | 2026-10-13 |

🏷 `agent` · `ai` · `claude` · `deepseek-harness` · `dsh` · `dsh-better-sidebar` · `dsh-plugin` · `github-issues`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/featherhunter--dsh-mattpocock-skills-deck/c4bd78003446c161.png" width="100%" alt="FeatherHunter/dsh-mattpocock-skills-deck screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/PerryLink/dsh-memento">PerryLink/dsh-memento</a></b> · ⭐141 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

DeepSeek Harness için sınırlı, katmanlı, onay kontrollü ve denetlenebilir oturumlar arası bellek: sıfır bağımlılıklı bir SQLite sağlayıcısı, bellek aracı ve dondurulmuş anlık görüntü enjeksiyonuna sahip bir ctx.memory yetenek arayüzü. Bakım durumu: 2026-10-05 tarihinden beri FROZEN.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | JavaScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **141**    |
| Son gönderme   | 2026-10-12 |
| İlk listelenme | 2026-10-13 |

🏷 `agent-memory` · `ai-agent` · `ai-agents` · `approval` · `audit` · `cordis` · `deepseek-harness` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-memento/f63bd5eb5a8052b8.png" width="100%" alt="PerryLink/dsh-memento screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-memento/0ce3328d348abdce.gif" width="100%" alt="PerryLink/dsh-memento animation"><br><sub>animasyonlu kayıt</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/AskTheWay/dsh-auto-memory">AskTheWay/dsh-auto-memory</a></b> · ⭐106 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

DeepSeek Harness (dsh) için Claude Code tarzı otomatik bellek eklentisi: türlendirilmiş bellek dosyaları + sistem istemine otomatik olarak eklenen MEMORY.md dizini. Yalnızca dosya kullanır, harici hizmet yoktur.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | TypeScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **106**    |
| Son gönderme   | 2026-10-12 |
| İlk listelenme | 2026-10-13 |

🏷 `agent-harness` · `agent-memory` · `ai-agent` · `ai-tools` · `auto-memory` · `claude-code` · `coding-agent` · `context-engineering`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/asktheway--dsh-auto-memory/1ff60db2b929f245.png" width="100%" alt="AskTheWay/dsh-auto-memory screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Noob-stupid/dsh-plugin-gating-hub">Noob-stupid/dsh-plugin-gating-hub</a></b> · ⭐100 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

DSH plugin - framework upgrade safety & plugin gating: contract pre-check, rollback point, auto-rollback on failure, evidence-based auto-disable; plus a multi-source plugin market. Unofficial. | DSH 插件：框架升级安全 + 插件门控——升级前契约预检、回滚点、失败自动回滚、有确证证据才自动禁用；另带多源插件市场。非官方社区项目。

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
| Son gönderme   | 2026-10-12 |
| İlk listelenme | 2026-10-13 |

🏷 `ai-empower` · `cli` · `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-plugins` · `framework-upgrade` · `marketplace`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/noob-stupid--dsh-plugin-gating-hub/0b18270cf916dc1c.png" width="100%" alt="Noob-stupid/dsh-plugin-gating-hub screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Fishsb/dsh-prompt-enhancer">Fishsb/dsh-prompt-enhancer</a></b> · ⭐90 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

DeepSeek Harness (DSH) eklentisi: ✨ tek tıklamayla istem güçlendirme + 💬 ses tanıma (konuşma bitince otomatik durur · bulut/yerel çift motor) · ayrıca 🔁 hizmet arızasında tek tıklamayla yeniden başlatma

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | JavaScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **90**     |
| Son gönderme   | 2026-10-12 |
| İlk listelenme | 2026-10-13 |

🏷 `deepseek` · `deepseek-harness` · `dsh-plugin` · `plugin` · `prompt-engineering`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Fishsb/dsh-prompt-enhancer/main/docs/screenshots/voice-main.png" width="100%" alt="Fishsb/dsh-prompt-enhancer screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

<sub>Yeniden dağıtıma izin veren bir lisans belirtilmediği için varlığa upstream deposundan doğrudan bağlantı veriliyor.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/kukucaiCndy/Corum-Harness">kukucaiCndy/Corum-Harness</a></b> · ⭐69 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Yıldızlar      | **69**     |
| Son gönderme   | 2026-10-12 |
| İlk listelenme | 2026-10-11 |

🏷 `agent` · `agent-os` · `ai-agent` · `cordis` · `desktop-app` · `dsh` · `electron` · `harness`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/kukucaicndy--corum-harness/b8971b2831acec9e.png" width="100%" alt="kukucaiCndy/Corum-Harness screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/PerryLink/dsh-fund-research">PerryLink/dsh-fund-research</a></b> · ⭐68 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

DeepSeek Harness eklentisi olarak Çin kamuya açık yatırım fonları için deterministik araştırma raporları: bir fon kodu girilir, sürümlendirilmiş bir Markdown raporu çıkar; performans ayrıştırması, portföy penetrasyonu, stil atfı ve açık veri boşluğu beyanları içerir. Metrikler model tarafından değil, kod içinde hesaplanır.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | TypeScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **68**     |
| Son gönderme   | 2026-10-12 |
| İlk listelenme | 2026-10-13 |

🏷 `ai-agent` · `ai-agents` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `finance` · `fund-research`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-fund-research/9a258f42b5375ed7.png" width="100%" alt="PerryLink/dsh-fund-research screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-fund-research/c127c0b5eda50892.gif" width="100%" alt="PerryLink/dsh-fund-research animation"><br><sub>animasyonlu kayıt</sub></td>
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
| Son gönderme   | 2026-10-12 |
| İlk listelenme | 2026-10-06 |

🏷 `agent-framework` · `awesome-list` · `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/whyihaveyou--dsh-suite/e9daf3bb6313ff1b.png" width="100%" alt="whyihaveyou/dsh-suite screenshot"></td>
<td align="center" valign="top"><sub>medya yayınlanmadı</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/PolinniZhong/dsh-knit">PolinniZhong/dsh-knit</a></b> · ⭐54 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Özet

AI coding agent'ları için göreve duyarlı çalışma alanı bağlamı alma ve yaşam döngüsü izleme: mevcut göreve en uygun belgeleri, kodu ve medyayı bulur, düzenler ve sürekli izler. Tamamen yerel, sıfır model çağrısı, sıfır ağ. AI coding agent'ları için göreve duyarlı çalışma alanı bağlamı alma ve yaşam döngüsü izleme. Eldeki görevle en ilgili çalışma alanı bağlamını yerel ve deterministik biçimde bulun, düzenleyin ve izleyin — sıfır model çağrısı, sıfır ağ.

##### 📌 Temel bilgiler

| Alan     | Değer                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------- |
| Kategori | `DSH ve Cordis eklenti ekosistemleri`                                                           |
| Kanıt    | `bir mod, eklenti veya hook bildirdi, ancak özellikle mod yüzeyi hakkında hiçbir şey söylemedi` |
| Dil      | JavaScript                                                                                      |

##### 📊 Veri

| Metrik         | Değer      |
| -------------- | ---------- |
| Yıldızlar      | **54**     |
| Son gönderme   | 2026-10-12 |
| İlk listelenme | 2026-10-12 |

🏷 `agent-tools` · `ai-agent` · `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-better-sidebar`

---

<table><tr><th align="center" width="50%">🖼 Görsel</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/polinnizhong--dsh-knit/e98f690af54d1e8d.png" width="100%" alt="PolinniZhong/dsh-knit screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/polinnizhong--dsh-knit/338cb6ef3e90368c.gif" width="100%" alt="PolinniZhong/dsh-knit animation"><br><sub>animasyonlu kayıt</sub></td>
</tr></table>

</details>

<details>
<summary><b>Bu kategoride daha fazlası</b> <sub>· 74</sub></summary>

- [hashgraph-online/awesome-ai-plugins](https://github.com/hashgraph-online/awesome-ai-plugins) - Claude Code, OpenAI Codex / ChatGPT, Gemini, Antigravity, Pi / Oh My Pi, Grok…
- [bruc3van/awesome-dsh-plugin](https://github.com/bruc3van/awesome-dsh-plugin) - 30 秒找到真正适合你的 DeepSeek Harness插件。每天自动抓取 GitHub 上的 `dsh-plugin`…
- [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) - DSH eklenti pazarı / DSH Plugin Marketplace: DeepSeek Harness Web GUI içinde…
- [daha1216/dsh-adult-tension](https://github.com/daha1216/dsh-adult-tension) - DeepSeek.
- [arcships/rutis](https://github.com/arcships/rutis) - Kendi kendini yineleyen yazılımlar için bir eklenti çalışma zamanı — ajanların…
- [adamkhalile/luau-docs-oracle](https://github.com/adamkhalile/luau-docs-oracle) - Best Roblox Luau Bug Checker and API Verifier 2026 DevForum MCP Tool.
- [PerryLink/dsh-data-quality](https://github.com/PerryLink/dsh-data-quality) - DeepSeek Harness eklentisi: deterministik veri profilleme, temizleme ve…
- [KongFangXun/sofagent](https://github.com/KongFangXun/sofagent) - sofagent, AI kodlama ajanları için açık kaynaklı bir FDE Harness.
- [BotHarness/DeepSeekBot](https://github.com/BotHarness/DeepSeekBot) - DeepSeek Harness üzerine kurulmuş açık kaynaklı GrokBot alternatifi.
- [kejixiaoliang/awesome-dsh-plugins](https://github.com/kejixiaoliang/awesome-dsh-plugins) - DeepSeek Harness (DSH) eklentileri seçkisi — 14 kategoride 280.
- [PerryLink/dsh-plugin-guide](https://github.com/PerryLink/dsh-plugin-guide) - DeepSeek Harness (dsh) eklenti geliştirme bilgi tabanı: 10 bölümlük geliştirme…
- [hyzyn/dsh-plugin-kit](https://github.com/hyzyn/dsh-plugin-kit) - Plugin family for the DeepSeek Harness (DSH) Web GUI: a pnpm monorepo with a…
- [NekroAI/nekro-nxt](https://github.com/NekroAI/nekro-nxt) - NekroNXT: DeepSeek Harness (DSH) tabanlı çok platformlu grup sohbeti aracısı…
- [KannaKuron/dsh-gitbash-shell](https://github.com/KannaKuron/dsh-gitbash-shell) - DSH eklentisi: Windows üzerindeki tüm ajan modları için Git Bash kabuğu.
- [AskTheWay/dsh-jev-interceptor](https://github.com/AskTheWay/dsh-jev-interceptor) - ⚡ DeepSeek Harness.
- [wingsky-1/dsh-plugin-hub](https://github.com/wingsky-1/dsh-plugin-hub) - DSH (DeepSeek Harness) web GUI eklenti koleksiyonu — görev bildirimleri…
- [HaoyueQin/dsh-usage-statistics-panel](https://github.com/HaoyueQin/dsh-usage-statistics-panel) - DSH web eklentisi: GitHub tarzı etkinlik ısı haritası, önbellek isabet oranı…
- [pigeon189/zcode-fox-widget](https://github.com/pigeon189/zcode-fox-widget) - ZCode狐娘小挂件 —— ZCode 桌面余额挂件：DeepSeek 峰谷计价 · GLM Plan · CommandCode 三重额度多账号池 ·…
- [StvLi/dsh-ros2](https://github.com/StvLi/dsh-ros2) - Deepseek Harness ROS 2 eklentisi, sorunları verimli bir şekilde teşhis etmek ve…
- [liustack/pptwise](https://github.com/liustack/pptwise) - HTML değil, gerçek bir PowerPoint. Yapay zekânıza nelerin ele alınacağını…
- [PerryLink/dsh-session-sync](https://github.com/PerryLink/dsh-session-sync) - Cihazlar arası DeepSeek Harness oturum senkronizasyonu: yalnızca eklemeli, her…
- [Roarpeng/GraphFlow](https://github.com/Roarpeng/GraphFlow) - Kodlama aracıları için yerel öncelikli kod bilgi grafiği ve bağlam harness.
- [YELEBAI/dsh-plugin-marketplace](https://github.com/YELEBAI/dsh-plugin-marketplace) - Verified plugin marketplace and autonomous registry for DeepSeek Harness.
- [KCNyu/clawock](https://github.com/KCNyu/clawock) - AI argues. Code settles. The losses stay on the page.
- [KannaKuron/dsh-better-workspace](https://github.com/KannaKuron/dsh-better-workspace) - DSH web eklentisi: kenar çubuğu için hiyerarşik çalışma alanı ağacı — / içeren…
- [dshworks/awesome-dsh-plugins](https://github.com/dshworks/awesome-dsh-plugins) - Spam-filtered, open-data registry of DeepSeek Harness (dsh) plugins, bundles…
- [billLiao/awesome-dsh-plugin](https://github.com/billLiao/awesome-dsh-plugin) - A curated list of plugins for DeepSeek Harness (dsh) — 精选 DeepSeek Harness 插件列表.
- [ddtcorex/govard](https://github.com/ddtcorex/govard) - Magento, Laravel, Symfony, Next.js, WordPress ve daha fazlası için Go tabanlı…
- [Ianzhyh/workbuddy-to-dsh](https://github.com/Ianzhyh/workbuddy-to-dsh) - Yerel WorkBuddy masaüstü uygulamasında oturum açmış modelleri.
- [PerryLink/dsh-translate](https://github.com/PerryLink/dsh-translate) - DeepSeek Harness için sağlayıcı parametresi çevirisi ve deterministik JSON…
- [HackSing/dsh-plugins](https://github.com/HackSing/dsh-plugins) - DeepSeek Harness (DSH) eklentileri için iki dilli, sürekli güncellenen dizin.
- [muyuanjin/dsh-ptc-plus](https://github.com/muyuanjin/dsh-ptc-plus) - A session-bound agent-native REPL for DeepSeek Harness PTC mode.
- [PerryLink/dsh-score](https://github.com/PerryLink/dsh-score) - DeepSeek Harness eklentileri için çok boyutlu kalite puanlaması: bir depoyu…
- [PerryLink/dsh-test-drive](https://github.com/PerryLink/dsh-test-drive) - DeepSeek Harness eklentileri için yalıtılmış yükleme ve duman test sürüşleri…
- [wycto/dsh-dock](https://github.com/wycto/dsh-dock) - dsh-dock · DeepSeek Harness işlev yuvası eklentisi: tüm küçük işlevleri tek bir…
- [MicroMilo/upstream-radar](https://github.com/MicroMilo/upstream-radar) - DeepSeek Harness eklentileri için her zaman açık uyumluluk testi: kesin…
- [liang-today/dsh-liangxiang](https://github.com/liang-today/dsh-liangxiang) - Birçok koku güç oluşturur, Liangzi görünür hale gelir.
- [vecnode/vncode](https://github.com/vecnode/vncode) - vncode 🤖 Agent-Human IDE ⌨️ Eklentileri, Skills ve Interfaces.
- [bonerush/dsh-obsidian-mem](https://github.com/bonerush/dsh-obsidian-mem) - Proje belgelerini ve uzun süreli belleği özel bir Obsidian kasasında düz…
- [Icather/dsh-clean-desktop-shell](https://github.com/Icather/dsh-clean-desktop-shell) - DSH 纯净桌面壳：双击像普通软件一样一键启动，后端活性实时监测 + 托盘快捷启停，零视觉改造.
- [unStone/dsh-xray](https://github.com/unStone/dsh-xray) - DeepSeek Harness eklentileri için X ışını: beyan edilen yetenekler ve gerçek…
- [ayingQAQ/dsh-web-launcher](https://github.com/ayingQAQ/dsh-web-launcher) - Windows üzerindeki DeepSeek Harness Web için tek tıklamalı başlatıcı｜Arka…
- [cherrchen/dsh-plugin-multi-root-workspace](https://github.com/cherrchen/dsh-plugin-multi-root-workspace) - Çok klasörlü çalışma alanı: DSH (DeepSeek Harness) aracısının yalnızca ana…
- [chnjames/dsh-plugin-market](https://github.com/chnjames/dsh-plugin-market) - DSH 插件市场 — DeepSeek Harness 设置内一键安装社区插件，并提供公开目录站（浏览 / 复制安装命令）.
- [kelemiao/dsh-animation-optimization](https://github.com/kelemiao/dsh-animation-optimization) - DSH animasyon optimizasyonu: akış animasyonu ve Claude Code tarzı görünüm…
- [wads-dev/dsh-live-voice](https://github.com/wads-dev/dsh-live-voice) - DSH için yerel öncelikli sesli konuşmalar.
- [KannaKuron/dsh-ide-git](https://github.com/KannaKuron/dsh-ide-git) - DSH eklentisi: yerel bir dsh-better-sidebar sekmesi olarak IDE düzeyinde Git…
- [KannaKuron/dsh-ptc-cordis-preset](https://github.com/KannaKuron/dsh-ptc-cordis-preset) - PTC modu temelinde yaratıcı mod: DSH eklentisi;
- [ywsldxk/dsh-plugin-stars](https://github.com/ywsldxk/dsh-plugin-stars) - DeepSeek Harness (DSH) plugin leaderboard &amp; directory｜DeepSeek…
- [ItQianChen/dsh-github-flow](https://github.com/ItQianChen/dsh-github-flow) - DeepSeek Harness Agent.
- [majiayu000/dsh-plugin-registry](https://github.com/majiayu000/dsh-plugin-registry) - Searchable DeepSeek Harness plugin registry with curated listings and…
- [PerryLink/dsh-plugin-doctor](https://github.com/PerryLink/dsh-plugin-doctor) - DeepSeek Harness (dsh) eklentileri için sıfır bağımlılıklı doğrulama standardı…
- [PerryLink/perrylink](https://github.com/PerryLink/perrylink) - DeepSeek Harness eklenti ekosistemi: 101 depoluk bir ailede 86 açık kaynaklı…
- [TheYoungChen/dsh-plugin-market](https://github.com/TheYoungChen/dsh-plugin-market) - DeepSeek Harness eklenti pazarı - dsh-plugin konusu eklentilerine göz atın…
- [viztor/dsh-opencode-patch](https://github.com/viztor/dsh-opencode-patch) - DeepSeek Harness üzerinde OpenCode — OpenCode Zen + Go ücretsiz katman…
- [AI-Scarlett/DSH-Store](https://github.com/AI-Scarlett/DSH-Store) - DSH STORE — DeepSeek Harness için üçüncü taraf eklenti pazaryeri ve korumalı…
- [Atelyx/Atelyx](https://github.com/Atelyx/Atelyx) - Atelyx, insan odaklı ve genişletilebilir bir masaüstü çalışma alanıdır…
- [Djokovical5294/DeepSeek-Harness-Token-Free](https://github.com/Djokovical5294/DeepSeek-Harness-Token-Free) - DeepSeek Harness.
- [dushaobindoudou/dsh-bots](https://github.com/dushaobindoudou/dsh-bots) - dsh Bots çalışma alanı: sdk-bots orkestrasyon ağ geçidini dsh web kabuğuna…
- [LeiSureYu/dsh-smart-download](https://github.com/LeiSureYu/dsh-smart-download) - DSH 多线程下载插件已适配dsh0.2,0：内置 aria2，智能探测文件大小自动选择下载策略.
- [lmzhen/dsh-evolution](https://github.com/lmzhen/dsh-evolution) - DeepSeek Harness için özel olarak oluşturulmuş, Hermes.
- [sakanamaru/dsh-minato](https://github.com/sakanamaru/dsh-minato) - dsh-minato — DeepSeek Harness (dsh) için topluluk sürümü yerel dağıtım ve…
- [skkjkk/dsh-usage-dashboard](https://github.com/skkjkk/dsh-usage-dashboard) - DSH (DeepSeek Harness) usage statistics dashboard plugin: token / cost /…
- [tianyagk/dsh-tradewatcher](https://github.com/tianyagk/dsh-tradewatcher) - DeepSeek Harness (DSH) web eklentisi: market-dashboard kenar çubuğu sekmesi…
- [Wanbinyu/wanbinyu-harness-toolbox](https://github.com/Wanbinyu/wanbinyu-harness-toolbox) - Wanbinyu tarafından sürdürülen DeepSeek Harness için bağımsız üçüncü taraf…
- [x5427876/dsh-opencode-free](https://github.com/x5427876/dsh-opencode-free) - Anonim erişim veya isteğe bağlı bir API anahtarıyla DeepSeek Harness içinde…
- [argszero/cordis-plugin-sandbox-grant-advisor](https://github.com/argszero/cordis-plugin-sandbox-grant-advisor) - DeepSeek Harness eklentisi: Windows sandbox ACL sağlama hatasını…
- [argszero/cordis-plugin-tool-deadline-guard](https://github.com/argszero/cordis-plugin-tool-deadline-guard) - Hiçbir son tarih bildirmeyen dsh araç çağrıları için dağıtım düzeyinde son…
- [xinvxueyuan/cordis-plugin-github](https://github.com/xinvxueyuan/cordis-plugin-github) - Cordis / DeepSeek Harness eklentisi — AI ajanları için normalleştirilmiş GitHub…
- [KunoLu/sbtd-plugins](https://github.com/KunoLu/sbtd-plugins) - SBTD host plugins (OMP + DSH) and shared workflow kit.
- [helloHupc/dsh-plugin-hub](https://github.com/helloHupc/dsh-plugin-hub) - DSH eklenti toplama sitesi: tüm ağdaki DeepSeek Harness eklentilerini bir araya…
- [tellmewhattodo/dsh-serenity-plugin](https://github.com/tellmewhattodo/dsh-serenity-plugin) - dsh-serenity-plugin.
- [arkme-senx/arkme-dsh-plugin](https://github.com/arkme-senx/arkme-dsh-plugin) - DeepSeek Harness için Arkme hesabı, kayıtlar, sohbet ve interwoven-moments…
- [SCP-008-1/dshop](https://github.com/SCP-008-1/dshop) - dsh eklenti mağazası - GitHub topic:dsh-plugin temelinde otomatik keşif ve…

</details>

<a id="writing"></a>

## Yazılar, tartışmalar ve videolar

Mod yeteneği hakkında yazılar, tartışmalar ve videolar.

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925102">Claude Code Mods</a></b> · ⭐6 · 👁️ observed · 11 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50003222">What the Hell Are Claude Mods? [video]</a></b> · ⭐4 · 👁️ observed · 4 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49999983">A Claude Code mod plays MIDI music when it works</a></b> · ⭐3 · 👁️ observed · 5 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925800">Claude Code Mods: plugins may now modify deeper behavior</a></b> · ⭐3 · 👁️ observed · 11 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49926243">Getting started with Claude Code mods</a></b> · ⭐3 · 👁️ observed · 11 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49945600">Show HN: Terminal Gym – a Claude mod that makes you do pushups between prompts</a></b> · ⭐3 · 👁️ observed · 9 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49971594">Terminal Steps: A Claude mod for a daily step goal, synced from Apple Health</a></b> · ⭐3 · 👁️ observed · 7 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50024345">Agent-config&amp;Claude Code mods</a></b> · ⭐2 · 👁️ observed · 3 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49940121">Getting started with Claude Code mods</a></b> · ⭐2 · 👁️ observed · 10 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49927599">Pi-autoresearch ported to Claude Code 1:1 using the new mods API</a></b> · ⭐2 · 👁️ observed · 11 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49934165">Show HN: What&#x27;s Agent Doing – a Claude Code UI mod that explains each step</a></b> · ⭐2 · 👁️ observed · 10 天</summary>

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

| Dil        | Kayıtlar | Örnekler                                                                                                        |
| ---------- | -------- | --------------------------------------------------------------------------------------------------------------- |
| TypeScript | 372      | `anthropics/claude-code`, `anthropics/claude-code-action`, `PerryLink/dsh-mcp-panel`                            |
| JavaScript | 81       | `karanb192/awesome-claude-code-mods`, `karanb192/claude-code-mods`, `ucsandman/claude-harness`                  |
| Python     | 40       | `anthropics/claude-agent-sdk-python`, `anthropics/claude-code-security-review`, `alexgreensh/token-optimizer`   |
| Shell      | 27       | `anthropics/claude-agent-sdk-typescript`, `0xDarkMatter/claude-mods`, `BeLazy167/claude-mods-skill`             |
| HTML       | 14       | `darrell-tw/darrelltw-mods`, `omarcevi/claudemods`, `testy-cool/awesome-claude-code-mods`                       |
| Rust       | 5        | `persiyanov/herdr-reviewr`, `cc-friend/ccost`, `ericbust/namedrop`                                              |
| Go         | 4        | `mitre/claude-statusline`, `esengine/DeepSeek-Reasonix`, `vshulcz/deja-vu`                                      |
| PowerShell | 3        | `Gabriel-Dalton/claude-statusline-tokens`, `markallisongit/claude-statusline`, `rainyfei/claude-statusline-win` |
| C          | 2        | `reporails/arcade`, `tylergraydev/cc-mods`                                                                      |
| C#         | 1        | `sakanamaru/dsh-minato`                                                                                         |
| Kotlin     | 1        | `platonai/Browser4`                                                                                             |
| MDX        | 1        | `jkf87/mod-guide`                                                                                               |
| Swift      | 1        | `peaceinitiativemenhadenoil263/claude-status-bar`                                                               |

<sub>Yalnızca dil belirten girdiler sayılır. Belgeler ve tartışma girdileri bu tablonun dışında tutulur.</sub>

## Katkıda bulunma

Düzeltmeler memnuniyetle karşılanır ve bu listeyi iyileştirmenin en hızlı yoludur. Bir girdi yanlış sınıflandırılmış veya yanlış derecelendirilmişse ya da bir proje ad çakışması nedeniyle yanlışlıkla dışlanmışsa bir issue veya pull request açın — otomatik filtrelerin en çok yanılma ihtimali olan kategori sonuncusudur.

---

<sub>Independent community project. Not affiliated with, endorsed by, or reviewed by Anthropic. Claude Code, Claude and Anthropic are trademarks of Anthropic. Product behaviour changes without notice; verify anything load-bearing against the official documentation. Assets remain the property of their upstream projects and are reproduced only where a licence permits.</sub>

<sub>Son güncelleme · 2026-10-13T08:29:52+08:00</sub>
