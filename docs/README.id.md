<p align="center">
  <img src="../assets/readme/hero.png" width="100%" alt="Mod Claude Keren">
</p>

<h1 align="center">Mod Claude Keren</h1>

<p align="center"><b>Indeks mod Claude Code, plugin, dan perubahan perilaku mendalam yang ditimbulkannya, dengan pemeringkatan berdasarkan bukti.</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-595-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="../LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
  <a href="https://wh000wh000.github.io/awesome-claude-mods/"><img src="https://img.shields.io/badge/site-searchable-1f6feb" alt="site"></a>
</p>

<p align="center"><sub><a href="../README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.pt-BR.md">Português</a> · <a href="README.ru.md">Русский</a> · <a href="README.it.md">Italiano</a> · <a href="README.ar.md">العربية</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.tr.md">Türkçe</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <b>Bahasa Indonesia</b> · <a href="README.pl.md">Polski</a> · <a href="README.nl.md">Nederlands</a> · <a href="README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **Indeks aktif** · Sinkronisasi terakhir: `2026-10-11T16:50:06+08:00` (UTC+8)
> · Entri: **595** · Ditambahkan pada pembaruan terbaru: **0** · Bahasa implementasi: **14**

<sub>Setiap entri di bawah dikumpulkan, difilter, dan diperiksa ulang secara otomatis. Tidak ada konten berbayar di sini.</sub>

<a id="featured"></a>

## Pilihan saat ini

<sub>Satu entri per kategori, diurutkan berdasarkan tingkat bukti dan jumlah bintang, lalu dihitung ulang setiap kali diperbarui. Ini adalah pemeringkatan, bukan dukungan; setiap pilihan tertaut ke kartu lengkapnya di bawah. Proyek yang memublikasikan tangkapan layar atau rekaman lebih diutamakan agar panel ini tetap visual.</sub>

<table>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action">
<b>🏛️ <a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b>
<sub>⭐9472 · TypeScript · ✅ official</sub>
</td>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer">
<b>🧩 <a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b>
<sub>⭐2534 · Python · 👁️ observed</sub>
<sub>Temukan token hantu. Perbaiki. Bertahan dari kompaksi. Hindari penurunan kualitas konteks.</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo">
<b>🧵 <a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b>
<sub>⭐74314 · TypeScript · 👁️ observed</sub>
<sub>🌊 Agent harness orisinal. Terapkan swarm multipemain yang cerdas, koordinasikan alur kerja otonom, dan bangun sistem AI percakapan. Menampilkan memori adaptif,…</sub>
</td>
<td width="50%" valign="top">
<b>📰 <a href="https://news.ycombinator.com/item?id=49925102">Claude Code Mods</a></b>
<sub>⭐6 · 👁️ observed</sub>
</td>
</tr>
</table>

## Isi

- [Apa itu mod Claude Code](#apa-itu-mod-claude-code)
- [Cara entri dinilai](#cara-entri-dinilai)
- [Resmi: repositori dan catatan rilis milik Anthropic sendiri](#resmi-repositori-dan-catatan-rilis-milik-anthropic-sendiri) — **16**
- [Mod: dibuat dengan kemampuan mod](#mod-dibuat-dengan-kemampuan-mod) — **465**
- [Ekosistem plugin DSH dan Cordis](#ekosistem-plugin-dsh-dan-cordis) — **103**
- [Tulisan, diskusi, dan video](#tulisan-diskusi-dan-video) — **11**
- [Proyek berdasarkan bahasa implementasi](#proyek-berdasarkan-bahasa-implementasi)

## Apa itu mod Claude Code

Claude Code mendapatkan **mod** pada 2.1.287: ekstensi yang dapat mengubah perilaku lebih mendalam daripada yang bisa dilakukan plugin, serta menggambar antarmukanya sendiri.

Mod dapat meng-hook `ui.render` untuk menggambar **row, band, pane, atau card** di sekitar prompt, membaca teks yang terakhir Anda pilih dengan `$.ui.selection()`, membuat rekan satu tim dengan `agent.spawn`, dan memiliki region `Client` sendiri. Mod yang gagal menggambar akan gagal sendirian — `ui.fault` mencegah satu mod yang rusak menghentikan sesi.

Daftar ini mencakup mod, surface plugin dan hook yang menjadi landasannya, serta padanan DSH dan Cordis. Daftar ini sengaja **tidak** mencakup ekosistem Claude Code yang lebih luas: prompt pack bukanlah mod.

## Cara entri dinilai

Sebagian besar daftar di bidang ini hanya menyatakan bahwa sesuatu termasuk di dalamnya. Daftar ini menjelaskan seberapa banyak yang benar-benar telah diverifikasi, lalu memungkinkan Anda memfilternya sesuai kebutuhan. Suatu tingkat menggambarkan buktinya, bukan kualitas proyeknya — mod yang dibuat dengan baik tetapi belum pernah dibahas siapa pun tetap `inferred`.

| Nilai                                                                                         | Artinya                                                                                                                                                                                                                                     |
| --------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `dipublikasikan oleh Anthropic sendiri`                                                       | Dipublikasikan oleh Anthropic sendiri, atau dibaca langsung dari changelog resmi.                                                                                                                                                           |
| `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod`                             | Teksnya sendiri menyebut bagian dari mod surface — `ui.render`, `ui.fault`, `agent.spawn`, `$.ui.selection()`, pane, band, atau card — sehingga pembuatnya sedang menjelaskan sesuatu yang dibuat untuk digunakan pada API yang sebenarnya. |
| `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` | Menyebut dirinya sebagai mod, plugin, atau hook, tetapi tidak ada bagian teksnya yang menyebut mod surface secara spesifik. Nyata, tetapi belum terkonfirmasi.                                                                              |
| `cocok hanya berdasarkan kosakata`                                                            | Cocok hanya berdasarkan kosakata. Disertakan agar filter dapat diaudit, bukan karena entri ini dianggap benar.                                                                                                                              |

<a id="official"></a>

## Resmi: repositori dan catatan rilis milik Anthropic sendiri

Anthropic's own Claude Code repositories, and the releases that defined the mod surface. Read from the source rather than summarised.

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></b> · ⭐150110 · TypeScript · ✅ official · 0 天</summary>

##### 📝 Ringkasan

Claude Code adalah alat pemrograman agentik yang berjalan di terminal Anda, memahami basis kode Anda, dan membantu Anda memprogram lebih cepat dengan menjalankan tugas rutin, menjelaskan kode yang kompleks, serta menangani alur kerja git — semuanya melalui perintah bahasa alami.

<sub>🔧 Ditemukan digunakan dalam kode: `feed.xml`</sub>

##### 📌 Fakta dasar

| Bidang   | Nilai                                                         |
| -------- | ------------------------------------------------------------- |
| Kategori | `Resmi: repositori dan catatan rilis milik Anthropic sendiri` |
| Bukti    | `dipublikasikan oleh Anthropic sendiri`                       |
| Bahasa   | TypeScript                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **150110** |
| Push terakhir            | 2026-10-10 |
| Pertama kali dicantumkan | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b> · ⭐9472 · TypeScript · ✅ official · 1 天</summary>

##### 📝 Ringkasan

Tidak ada deskripsi upstream yang dipublikasikan.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                         |
| -------- | ------------------------------------------------------------- |
| Kategori | `Resmi: repositori dan catatan rilis milik Anthropic sendiri` |
| Bukti    | `dipublikasikan oleh Anthropic sendiri`                       |
| Bahasa   | TypeScript                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **9472**   |
| Push terakhir            | 2026-10-09 |
| Pertama kali dicantumkan | 2026-10-04 |

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-python">anthropics/claude-agent-sdk-python</a></b> · ⭐8247 · Python · ✅ official · 1 天</summary>

##### 📝 Ringkasan

Tidak ada deskripsi upstream yang dipublikasikan.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                         |
| -------- | ------------------------------------------------------------- |
| Kategori | `Resmi: repositori dan catatan rilis milik Anthropic sendiri` |
| Bukti    | `dipublikasikan oleh Anthropic sendiri`                       |
| Bahasa   | Python                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **8247**   |
| Push terakhir            | 2026-10-09 |
| Pertama kali dicantumkan | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-security-review">anthropics/claude-code-security-review</a></b> · ⭐6340 · Python · ✅ official · 241 天</summary>

##### 📝 Ringkasan

GitHub Action tinjauan keamanan bertenaga AI yang menggunakan Claude untuk menganalisis perubahan kode terhadap kerentanan keamanan.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                         |
| -------- | ------------------------------------------------------------- |
| Kategori | `Resmi: repositori dan catatan rilis milik Anthropic sendiri` |
| Bukti    | `dipublikasikan oleh Anthropic sendiri`                       |
| Bahasa   | Python                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **6340**   |
| Push terakhir            | 2026-02-11 |
| Pertama kali dicantumkan | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-typescript">anthropics/claude-agent-sdk-typescript</a></b> · ⭐1798 · Shell · ✅ official · 1 天</summary>

##### 📝 Ringkasan

Tidak ada deskripsi upstream yang dipublikasikan.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                         |
| -------- | ------------------------------------------------------------- |
| Kategori | `Resmi: repositori dan catatan rilis milik Anthropic sendiri` |
| Bukti    | `dipublikasikan oleh Anthropic sendiri`                       |
| Bahasa   | Shell                                                         |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **1798**   |
| Push terakhir            | 2026-10-09 |
| Pertama kali dicantumkan | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/model-cards">anthropics/model-cards</a></b> · ⭐25 · ✅ official · 309 天</summary>

##### 📝 Ringkasan

Materi pelengkap untuk Claude Model Cards

##### 📌 Fakta dasar

| Bidang   | Nilai                                                         |
| -------- | ------------------------------------------------------------- |
| Kategori | `Resmi: repositori dan catatan rilis milik Anthropic sendiri` |
| Bukti    | `dipublikasikan oleh Anthropic sendiri`                       |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **25**     |
| Push terakhir            | 2025-12-05 |
| Pertama kali dicantumkan | 2026-10-05 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.287 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Ringkasan

Menambahkan Claude Mods: plugin kini dapat memodifikasi perilaku yang lebih mendalam. Menambahkan You should know, mod bawaan yang membuat agen sampingan mengawasi Anda dan menandai hal-hal yang mungkin terlewat oleh Anda atau Claude. Aktifkan dengan `/plugin enable cc-plugin-you-should-know@builtin` (untuk sesi pihak pertama dengan telemetri aktif)

##### 📌 Fakta dasar

| Bidang   | Nilai                                                         |
| -------- | ------------------------------------------------------------- |
| Kategori | `Resmi: repositori dan catatan rilis milik Anthropic sendiri` |
| Bukti    | `dipublikasikan oleh Anthropic sendiri`                       |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Pertama kali dicantumkan | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.288 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Ringkasan

Menambahkan `$.ui.selection()` untuk mod: mengembalikan teks yang terakhir Anda pilih dalam mode layar penuh dan, ketika pilihan tersebut berada dalam satu baris transkrip, baris itu. Memperbaiki tombol mod yang terkadang menjalankan tindakan tombol lain ketika ditekan pada tampilan yang digambar sebelum Claude Code dimulai ulang. Memperbaiki sesi layar penuh yang keluar dengan "unrecoverable interface error" ketika membuka dialog tugas latar belakang saat plugin atau mod menampilkan baris di atas prompt. Memperbaiki `claude plugin test` yang melaporkan mod sebagai dinonaktifkan dari jarak jauh padahal hanya membaca pengaturan tersimpan yang sudah kedaluwarsa

##### 📌 Fakta dasar

| Bidang   | Nilai                                                         |
| -------- | ------------------------------------------------------------- |
| Kategori | `Resmi: repositori dan catatan rilis milik Anthropic sendiri` |
| Bukti    | `dipublikasikan oleh Anthropic sendiri`                       |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Pertama kali dicantumkan | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.289 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Ringkasan

Memperbaiki aturan deny atau ask pada bagian bersarang dari perintah shell gabungan yang tidak bertahan melewati persetujuan mod yang dipasang pengguna di mesin terkelola. Memperbaiki mod terpasang yang tidak dimuat pada sesi pertama setelah peningkatan. Menambahkan `agent.spawn` untuk rekan satu tim, satu id agen di seluruh peristiwa hook plugin, serta status idle dan waiting di `$.agent.list()`. Memperbaiki sesi yang berakhir dengan "unrecoverable interface error" ketika nilai yang ditulis hook `ui.render` milik mod menyebabkan baris gagal saat digambar; mesin kini menggambar barisnya sendiri. Memperbaiki konten rata kanan di panel atau pita mod yang tergambar di bawah tanda tutup atau `\[-\]`, wh

##### 📌 Fakta dasar

| Bidang   | Nilai                                                         |
| -------- | ------------------------------------------------------------- |
| Kategori | `Resmi: repositori dan catatan rilis milik Anthropic sendiri` |
| Bukti    | `dipublikasikan oleh Anthropic sendiri`                       |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Pertama kali dicantumkan | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.290 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Ringkasan

Menambahkan `serverToolUses` ke hasil hook `turn.step` milik mod: alat tersebut memanggil API yang dijalankan sendiri (penasihat), masing-masing dengan id, nama, input, waktu mulai, dan waktu selesai. Menambahkan `ceiling` ke pertanyaan dan putusan yang dibaca hook `tool.check` milik mod, dengan menyebutkan persetujuan yang diwajibkan organisasi untuk sebuah alat. Menambahkan tipe `ThemeKey` dan `Color` ke definisi tipe hook plugin, sehingga editor menampilkan warna tema yang dapat disebutkan oleh gambar mod. Menambahkan ke `claude plugin validate`: setiap hook yang didaftarkan mod di lokasi gating dicantumkan bersama keterangan apakah hook tersebut memiliki `.catch` (`gatingHooks` di bawah `--json`). Memperbaiki hasil `turn.step` milik mod

##### 📌 Fakta dasar

| Bidang   | Nilai                                                         |
| -------- | ------------------------------------------------------------- |
| Kategori | `Resmi: repositori dan catatan rilis milik Anthropic sendiri` |
| Bukti    | `dipublikasikan oleh Anthropic sendiri`                       |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Pertama kali dicantumkan | 2026-10-06 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.292 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Ringkasan

Menambahkan `prompt.autocomplete`, sebuah event yang di-hook mod untuk menambahkan barisnya sendiri ke daftar autocomplete kotak prompt Menambahkan caching prompt ke `$.model.complete` untuk mod: `prompt` dan `system` mengambil blok teks, dan `cache: true` pada sebuah blok melakukan cache permintaan hingga blok tersebut Menambahkan agen workflow ke hook mod `agent.spawn`, dengan run dan indeksnya, sehingga mod dapat menolaknya Memperbaiki baris Write, Edit, NotebookEdit dan LSP, serta baris Read, Grep dan Glob tunggal, menyembunyikan mengapa mod menolak panggilan: baris sekarang menampilkan alasannya Memperbaiki hook `config.set`, `state.set`, `env.set` atau `agent.spawn` milik mod yang menolak afte

##### 📌 Fakta dasar

| Bidang   | Nilai                                                         |
| -------- | ------------------------------------------------------------- |
| Kategori | `Resmi: repositori dan catatan rilis milik Anthropic sendiri` |
| Bukti    | `dipublikasikan oleh Anthropic sendiri`                       |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Pertama kali dicantumkan | 2026-10-07 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.293 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Ringkasan

Menambahkan `isDeferred` ke `$.tool.register` untuk mod: `false` mencantumkan skema alat di prompt sejak awal, bukan di balik pencarian alat Memperbaiki hook mod pada event `classic.*` yang terlewati saat worker hook plugin dimulai ulang, sehingga hook pengaturan harus menjawab tanpanya Memperbaiki `claude plugin test` yang gagal untuk mod yang memanggil `$.session.append`; pengujian dapat membaca kembali baris yang ditambahkan dengan `mock.session` baru

##### 📌 Fakta dasar

| Bidang   | Nilai                                                         |
| -------- | ------------------------------------------------------------- |
| Kategori | `Resmi: repositori dan catatan rilis milik Anthropic sendiri` |
| Bukti    | `dipublikasikan oleh Anthropic sendiri`                       |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Pertama kali dicantumkan | 2026-10-08 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/Enc-hanted/dsh-pulse">Enc-hanted/dsh-pulse</a></b> · ⭐3 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

Observatorium penggunaan & biaya lintas sesi untuk profil web DeepSeek Harness — dasbor tren/heatmap, harga jam sibuk per model (CNY/USD), saldo DeepSeek resmi dengan rekonsiliasi pengeluaran.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Resmi: repositori dan catatan rilis milik Anthropic sendiri`                                 |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | JavaScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **3**      |
| Push terakhir            | 2026-10-11 |
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `billing` · `cordis` · `cost` · `cost-estimation` · `dashboard` · `deepseek` · `deepseek-harness` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/enc-hanted--dsh-pulse/4a81f8e7c5f01f18.png" width="100%" alt="Enc-hanted/dsh-pulse screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary><b>Lainnya dalam kategori ini</b> <sub>· 3</sub></summary>

- [Claude Code 2.1.295 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Menambahkan `$.ui.notify` untuk mod: memunculkan notifikasi native melalui…
- [Claude Code 2.1.296 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Memperbaiki Esc atau interupsi selama hook `UserPromptSubmit` atau hook…
- [X-C1811/dsh-web-search-plugin](https://github.com/X-C1811/dsh-web-search-plugin) - Give your DeepSeek Harness agent more ways to search the web.

</details>

<a id="mods"></a>

## Mod: dibuat dengan kemampuan mod

Setiap entri di sini menunjukkan bukti penggunaan kemampuan yang diperoleh Claude Code pada 2.1.287: kemampuan tersebut menggambar melalui `ui.render`, memiliki panel, pita, atau kartu, membaca `$.ui.selection()`, memunculkan rekan satu tim dengan `agent.spawn`, atau menyatakan dengan jelas bahwa itu adalah mod.

<details>
<summary>🧩 <b><a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b> · ⭐2534 · Python · 👁️ observed · 0 天</summary>

##### 📝 Ringkasan

Temukan token hantu. Perbaiki. Bertahan dari kompaksi. Hindari penurunan kualitas konteks.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Mod: dibuat dengan kemampuan mod`                                |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |
| Bahasa   | Python                                                            |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **2534**   |
| Push terakhir            | 2026-10-10 |
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `agentskills` · `claude-code` · `claude-code-mod` · `claude-code-skill` · `claude-plugin` · `codex` · `context-engineering` · `context-window`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer animation"><br><sub>rekaman animasi</sub></td>
</tr></table>

<sub>Aset ditautkan langsung dari repositori upstream karena tidak ada lisensi yang mengizinkan redistribusi yang dinyatakan.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/awesome-claude-code-mods">karanb192/awesome-claude-code-mods</a></b> · ⭐479 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Ringkasan

Katalog komunitas mod Claude Code publik (function hooks), dipindai dari GitHub beserta informasi tentang apa yang dapat dibaca, ditulis, dijalankan, atau dikirim melalui jaringan oleh setiap mod. Jelajahi https://mods.aidojo.si/

<sub>🔧 Ditemukan digunakan dalam kode: `data/seeds.txt`, `data/duplicates.txt`, `README.md`, `contributing.md`</sub>

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Mod: dibuat dengan kemampuan mod`                                |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |
| Bahasa   | JavaScript                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **479**    |
| Push terakhir            | 2026-10-11 |
| Pertama kali dicantumkan | 2026-10-04 |

🏷 `anthropic` · `awesome` · `awesome-list` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hamzafer/claude-code-mods">hamzafer/claude-code-mods</a></b> · ⭐183 · TypeScript · 👁️ observed · 1 天</summary>

##### 📝 Ringkasan

Mod Claude Code: plugin yang dibangun di atas hook yang menambahkan baris live di atas prompt, guard, panel, dan game. Bilah konteks, meter penggunaan, pengawas review Codex, pratinjau Markdown, Spotify now playing, dan lainnya.

<sub>🔧 Ditemukan digunakan dalam kode: `mods/next-steps/hooks/register.tsx`, `mods/agent-radar/hooks/register.tsx`</sub>

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Mod: dibuat dengan kemampuan mod`                                |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |
| Bahasa   | TypeScript                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **183**    |
| Push terakhir            | 2026-10-09 |
| Pertama kali dicantumkan | 2026-10-04 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugins` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/c683a5d95e78d920.png" width="100%" alt="hamzafer/claude-code-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/0b4dc7c7692bd024.gif" width="100%" alt="hamzafer/claude-code-mods animation"><br><sub>rekaman animasi</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/cache-tax">karanb192/cache-tax</a></b> · ⭐123 · TypeScript · 👁️ observed · 6 天</summary>

##### 📝 Ringkasan

Jaga cache prompt Claude Code tetap hangat selama jeda dan tampilkan perkiraan biaya sebelum pengiriman dingin.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Mod: dibuat dengan kemampuan mod`                                |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |
| Bahasa   | TypeScript                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **123**    |
| Push terakhir            | 2026-10-04 |
| Pertama kali dicantumkan | 2026-10-10 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `function-hooks` · `prompt-caching`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/karanb192--cache-tax/9ba5b1dbc9440791.png" width="100%" alt="karanb192/cache-tax screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/karanb192--cache-tax/e1a7cdd41b0efd1b.gif" width="100%" alt="karanb192/cache-tax animation"><br><sub>rekaman animasi · <a href="https://raw.githubusercontent.com/karanb192/cache-tax/main/docs/assets/cache-cost-explainer.mp4">Buka video</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/awss1i/assay">awss1i/assay</a></b> · ⭐104 · HTML · 👁️ observed · 0 天</summary>

##### 📝 Ringkasan

QA CLI native-agent untuk halaman web. Deterministik, tanpa perlu menulis tes, tanpa LLM.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Mod: dibuat dengan kemampuan mod`                                |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |
| Bahasa   | HTML                                                              |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **104**    |
| Push terakhir            | 2026-10-10 |
| Pertama kali dicantumkan | 2026-10-10 |

🏷 `agentic-ai` · `ai-agents` · `browser-automation` · `claude-code` · `claude-code-mod` · `cli` · `code-generation` · `developer-tools`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hellosverre/claude-skins">hellosverre/claude-skins</a></b> · ⭐91 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Ringkasan

Skin untuk Claude Code: baris alat dengan ikon, kartu diff, tabel, dan grafik Mermaid, pita penggunaan, serta lima belas tema. /skin menggantinya secara langsung.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Mod: dibuat dengan kemampuan mod`                                |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |
| Bahasa   | TypeScript                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **91**     |
| Push terakhir            | 2026-10-10 |
| Pertama kali dicantumkan | 2026-10-10 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hellosverre--claude-skins/e70c992c52ca2e70.gif" width="100%" alt="hellosverre/claude-skins animation"><br><sub>rekaman animasi</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Tickloop/claude-mods">Tickloop/claude-mods</a></b> · ⭐77 · TypeScript · 👁️ observed · 2 天</summary>

##### 📝 Ringkasan

Kumpulan mod claude code

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Mod: dibuat dengan kemampuan mod`                                |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |
| Bahasa   | TypeScript                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **77**     |
| Push terakhir            | 2026-10-08 |
| Pertama kali dicantumkan | 2026-10-08 |

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NahumLitvin/prismantis">NahumLitvin/prismantis</a></b> · ⭐74 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Ringkasan

Balasan Claude Code penuh warna dan dapat dikustomisasi temanya: tabel, kode, diagram, grafik, dan baris alat dalam 15 tema, dengan tombol salin. Mod Claude Code.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Mod: dibuat dengan kemampuan mod`                                |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |
| Bahasa   | TypeScript                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **74**     |
| Push terakhir            | 2026-10-10 |
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `markdown` · `mermaid` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/f6e44059e77434b4.png" width="100%" alt="NahumLitvin/prismantis screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/9df6377936558503.gif" width="100%" alt="NahumLitvin/prismantis animation"><br><sub>rekaman animasi</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/darrell-tw/darrelltw-mods">darrell-tw/darrelltw-mods</a></b> · ⭐65 · HTML · 👁️ observed · 5 天</summary>

##### 📝 Ringkasan

Mod Claude Code oleh Darrell Wang — pita di atas prompt, tanpa token model. Papan saham Taiwan／AS + lebih banyak yang akan datang.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Mod: dibuat dengan kemampuan mod`                                |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |
| Bahasa   | HTML                                                              |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **65**     |
| Push terakhir            | 2026-10-05 |
| Pertama kali dicantumkan | 2026-10-04 |

</details>

<details>
<summary>🧩 <b><a href="https://github.com/scasella/claude-flightdeck">scasella/claude-flightdeck</a></b> · ⭐65 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Ringkasan

Mod Claude Code yang menampilkan dasbor agen langsung di terminal Anda: konteks dan biaya, linimasa penasihat, setiap pemeriksaan izin, kartu subagen, dan swimlane.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Mod: dibuat dengan kemampuan mod`                                |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |
| Bahasa   | TypeScript                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **65**     |
| Push terakhir            | 2026-10-02 |
| Pertama kali dicantumkan | 2026-10-10 |

🏷 `agent-observability` · `agent-visualization` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/scasella--claude-flightdeck/8c83ca6b4347b2f9.gif" width="100%" alt="scasella/claude-flightdeck screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/scasella--claude-flightdeck/8c83ca6b4347b2f9.gif" width="100%" alt="scasella/claude-flightdeck animation"><br><sub>rekaman animasi</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/0xDarkMatter/claude-mods">0xDarkMatter/claude-mods</a></b> · ⭐59 · Shell · 👁️ observed · 4 天</summary>

##### 📝 Ringkasan

Skill, agen, perintah, aturan, hook & gaya output ahli untuk Claude Code — kesinambungan sesi + tooling CLI modern untuk alur kerja pengembangan dunia nyata

<sub>🔧 Ditemukan digunakan dalam kode: `justfile`, `skills/auto-skill/SKILL.md`, `skills/task-runner/SKILL.md`, `skills/find-replace/SKILL.md`</sub>

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Mod: dibuat dengan kemampuan mod`                                |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |
| Bahasa   | Shell                                                             |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **59**     |
| Push terakhir            | 2026-10-07 |
| Pertama kali dicantumkan | 2026-10-04 |

🏷 `agent-skills` · `ai-agents` · `ai-tools` · `anthropic` · `claude` · `claude-code` · `claude-skills` · `developer-tools`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/whyashthakker/awesome-claude-code-mods">whyashthakker/awesome-claude-code-mods</a></b> · ⭐46 · TypeScript · 👁️ observed · 7 天</summary>

##### 📝 Ringkasan

Koleksi lebih dari 100 mod yang dapat Anda gunakan dengan Claude Code.

<sub>🔧 Ditemukan digunakan dalam kode: `README.md`, `docs/COMMUNITY_MODS.md`, `mods/agent-board/hooks/register.js`, `mods/desktop-agent-desk/hooks/register.js`</sub>

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Mod: dibuat dengan kemampuan mod`                                |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |
| Bahasa   | TypeScript                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **46**     |
| Push terakhir            | 2026-10-03 |
| Pertama kali dicantumkan | 2026-10-04 |

🏷 `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/zycck/claude-mods">zycck/claude-mods</a></b> · ⭐46 · TypeScript · 👁️ observed · 2 天</summary>

##### 📝 Ringkasan

Mod Claude Code: bilah kemajuan rencana langsung di atas prompt

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Mod: dibuat dengan kemampuan mod`                                |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |
| Bahasa   | TypeScript                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **46**     |
| Push terakhir            | 2026-10-08 |
| Pertama kali dicantumkan | 2026-10-04 |

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/49f09d1600b02c7a.gif" width="100%" alt="zycck/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/25f4230871cb30f6.gif" width="100%" alt="zycck/claude-mods animation"><br><sub>rekaman animasi · <a href="https://raw.githubusercontent.com/zycck/claude-mods/main/media/plan-progress.mp4">Buka video</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/henrik-thevibe/Claude-Fables">henrik-thevibe/Claude-Fables</a></b> · ⭐32 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Ringkasan

Saksikan Claude Code membuat kartun kecil saat Anda bekerja.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Mod: dibuat dengan kemampuan mod`                                |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |
| Bahasa   | TypeScript                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **32**     |
| Push terakhir            | 2026-10-02 |
| Pertama kali dicantumkan | 2026-10-10 |

🏷 `ai-narration` · `claude` · `claude-code` · `claude-code-plugin` · `claude-mod` · `claude-mods` · `developer-tools` · `fun`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/henrik-thevibe--claude-fables/283c6335f0455468.png" width="100%" alt="henrik-thevibe/Claude-Fables screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/henrik-thevibe--claude-fables/630db5cb89b1339d.gif" width="100%" alt="henrik-thevibe/Claude-Fables animation"><br><sub>rekaman animasi</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/oikon48/prompt-rail">oikon48/prompt-rail</a></b> · ⭐27 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Ringkasan

Panel prompt dari sesi Claude Code Anda: arahkan kursor untuk membaca, klik untuk melompat (function hooks / Mods)

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Mod: dibuat dengan kemampuan mod`                                |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |
| Bahasa   | TypeScript                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **27**     |
| Push terakhir            | 2026-10-03 |
| Pertama kali dicantumkan | 2026-10-04 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `function-hooks`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/oikon48--prompt-rail/d6ee96dd984886df.png" width="100%" alt="oikon48/prompt-rail screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/oikon48--prompt-rail/87309761ea9d1f19.gif" width="100%" alt="oikon48/prompt-rail animation"><br><sub>rekaman animasi</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NovusEdge/glowup">NovusEdge/glowup</a></b> · ⭐23 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Ringkasan

Peningkatan tampilan untuk Claude Code: panel kokpit langsung, tema yang dapat dibagikan, dan hewan peliharaan piksel yang memerankan apa yang sedang dilakukan Claude

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Mod: dibuat dengan kemampuan mod`                                |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |
| Bahasa   | TypeScript                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **23**     |
| Push terakhir            | 2026-10-10 |
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `developer-tools` · `eye-candy` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/52396333a085f3d5.gif" width="100%" alt="NovusEdge/glowup screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/4905ed24c2c755ad.gif" width="100%" alt="NovusEdge/glowup animation"><br><sub>rekaman animasi</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/artemnovichkov/xcode-mods">artemnovichkov/xcode-mods</a></b> · ⭐20 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Ringkasan

Build, pengujian, konsol, dan pratinjau SwiftUI Xcode di dalam Claude Code

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Mod: dibuat dengan kemampuan mod`                                |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |
| Bahasa   | TypeScript                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **20**     |
| Push terakhir            | 2026-10-02 |
| Pertama kali dicantumkan | 2026-10-04 |

🏷 `claude-code` · `claude-code-mods` · `claude-code-plugin` · `ghostty` · `ios` · `mcp` · `swift` · `swiftui`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/artemnovichkov--xcode-mods/bc34e8dd0f730ea2.png" width="100%" alt="artemnovichkov/xcode-mods screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/lemomo-ai/lemo-mod">lemomo-ai/lemo-mod</a></b> · ⭐20 · TypeScript · 👁️ observed · 7 天</summary>

##### 📝 Ringkasan

Mod Claude Code: 21 gaya dan serangkaian fitur lengkap yang dapat Anda aktifkan saat diperlukan, untuk terminal dan aplikasi desktop. · Ubah Claude ke gaya baru dengan sekali klik, serta sediakan serangkaian fitur yang dapat diaktifkan sesuai kebutuhan.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Mod: dibuat dengan kemampuan mod`                                |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |
| Bahasa   | TypeScript                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **20**     |
| Push terakhir            | 2026-10-04 |
| Pertama kali dicantumkan | 2026-10-04 |

🏷 `claude` · `claude-code` · `claude-code-mods` · `claude-code-plugins` · `developer-tools` · `mods` · `pixel-art` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/lemomo-ai--lemo-mod/d6e9ce6141976f64.png" width="100%" alt="lemomo-ai/lemo-mod screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-starter-kit">promptadvisers/claude-mods-starter-kit</a></b> · ⭐20 · JavaScript · 👁️ observed · 8 天</summary>

##### 📝 Ringkasan

Sepuluh mod Claude Code, panduan pemula, prompt pembuatan, demo aman, dan template buat-sendiri.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Mod: dibuat dengan kemampuan mod`                                |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |
| Bahasa   | JavaScript                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **20**     |
| Push terakhir            | 2026-10-02 |
| Pertama kali dicantumkan | 2026-10-04 |

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/promptadvisers/claude-mods-starter-kit/main/assets/cover.jpg" width="100%" alt="promptadvisers/claude-mods-starter-kit screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

<sub>Aset ditautkan langsung dari repositori upstream karena tidak ada lisensi yang mengizinkan redistribusi yang dinyatakan.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/JetsonChan/CC-Usage-Band">JetsonChan/CC-Usage-Band</a></b> · ⭐12 · TypeScript · 👁️ observed · 7 天</summary>

##### 📝 Ringkasan

Mod Claude Code: usage-band menampilkan batas 5 jam/7 hari Anda, jendela konteks, dan rasio cache hit di atas prompt

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Mod: dibuat dengan kemampuan mod`                                |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |
| Bahasa   | TypeScript                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **12**     |
| Push terakhir            | 2026-10-03 |
| Pertama kali dicantumkan | 2026-10-04 |

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/jetsonchan--cc-usage-band/e9d74f1543fa7c25.png" width="100%" alt="JetsonChan/CC-Usage-Band screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/aieo-product/claude_qamods">aieo-product/claude_qamods</a></b> · ⭐11 · TypeScript · 👁️ observed · 4 天</summary>

##### 📝 Ringkasan

Mod Claude Code yang membuat pertanyaan Claude lebih mudah dibaca dan dijawab (qa-guide).

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Mod: dibuat dengan kemampuan mod`                                |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |
| Bahasa   | TypeScript                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **11**     |
| Push terakhir            | 2026-10-07 |
| Pertama kali dicantumkan | 2026-10-04 |

🏷 `askuserquestion` · `claude-code` · `claude-code-plugin` · `mod`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aieo-product--claude_qamods/e57e7bee7cb5c173.png" width="100%" alt="aieo-product/claude_qamods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aieo-product--claude_qamods/eb4a2b15bdb5ff3e.gif" width="100%" alt="aieo-product/claude_qamods animation"><br><sub>rekaman animasi · <a href="https://raw.githubusercontent.com/aieo-product/claude_qamods/main/docs/media/qa-guide-pv-16x9.mp4">Buka video</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/augiefra/claude-mods">augiefra/claude-mods</a></b> · ⭐11 · JavaScript · 👁️ observed · 1 天</summary>

##### 📝 Ringkasan

Mod Claude Code: konteks dalam token, batas 5 jam dan mingguan dibandingkan dengan waktu, hitung mundur cache prompt, biaya sesi dan agen yang sedang berjalan, dalam satu bilah di atas prompt.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Mod: dibuat dengan kemampuan mod`                                |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |
| Bahasa   | JavaScript                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **11**     |
| Push terakhir            | 2026-10-09 |
| Pertama kali dicantumkan | 2026-10-04 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `claude-code-plugins` · `claude-code-statusline`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/augiefra--claude-mods/5e1358adde3e377d.png" width="100%" alt="augiefra/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/augiefra--claude-mods/27f137c61fc42d0c.gif" width="100%" alt="augiefra/claude-mods animation"><br><sub>rekaman animasi</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/OneWave-AI/claude-code-mods">OneWave-AI/claude-code-mods</a></b> · ⭐11 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Ringkasan

Sepuluh mod open-source untuk Claude Code: panel langsung, pita, baris status, dan pengaman pemanggilan alat. Meter pembakaran, kode peluncuran, sesi selesai, pertarungan bos, hewan peliharaan kode, dan lainnya.

<sub>🔧 Ditemukan digunakan dalam kode: `swarm/README.md`</sub>

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Mod: dibuat dengan kemampuan mod`                                |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |
| Bahasa   | TypeScript                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **11**     |
| Push terakhir            | 2026-10-03 |
| Pertama kali dicantumkan | 2026-10-04 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mods` · `claude-code-plugins`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/onewave-ai--claude-code-mods/763e0352f43b1cbc.png" width="100%" alt="OneWave-AI/claude-code-mods screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-computer-use-threads">promptadvisers/claude-mods-computer-use-threads</a></b> · ⭐11 · JavaScript · 👁️ observed · 5 天</summary>

##### 📝 Ringkasan

Dua mod Claude Code: jembatan penggunaan komputer Codex dan sesi Claude yang terkoordinasi. Sumber, prompt build, penyiapan, dan pengujian.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Mod: dibuat dengan kemampuan mod`                                |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |
| Bahasa   | JavaScript                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **11**     |
| Push terakhir            | 2026-10-05 |
| Pertama kali dicantumkan | 2026-10-06 |

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/promptadvisers--claude-mods-computer-use-threads/c08dc292e500cd09.png" width="100%" alt="promptadvisers/claude-mods-computer-use-threads screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/furqan-khan07/pixelband">furqan-khan07/pixelband</a></b> · ⭐10 · TypeScript · 👁️ observed · 7 天</summary>

##### 📝 Ringkasan

Pixel art animasi di atas prompt Claude Code Anda yang bereaksi saat Claude bekerja. Tujuh adegan, atau gambar maupun GIF Anda sendiri. Nol token.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Mod: dibuat dengan kemampuan mod`                                |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |
| Bahasa   | TypeScript                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **10**     |
| Push terakhir            | 2026-10-04 |
| Pertama kali dicantumkan | 2026-10-10 |

🏷 `animation` · `ascii-art` · `claude` · `claude-code` · `claude-mods` · `pixel-art` · `plugin` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/furqan-khan07--pixelband/a2bacbca880dcd7d.gif" width="100%" alt="furqan-khan07/pixelband screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/furqan-khan07--pixelband/53dd07a5a38530b0.gif" width="100%" alt="furqan-khan07/pixelband animation"><br><sub>rekaman animasi</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/deepsteve/deepsteve">deepsteve/deepsteve</a></b> · ⭐9 · JavaScript · 👁️ observed · 2 天</summary>

##### 📝 Ringkasan

UI di sekitar terminal Claude Code dan Codex Anda yang dibangun oleh agen, sehingga satu-satunya model di kepala Anda adalah milik Anda sendiri.

<sub>🔧 Ditemukan digunakan dalam kode: `CLAUDE.md`</sub>

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Mod: dibuat dengan kemampuan mod`                                |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |
| Bahasa   | JavaScript                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **9**      |
| Push terakhir            | 2026-10-08 |
| Pertama kali dicantumkan | 2026-10-04 |

🏷 `ai-coding` · `ai-tools` · `browser-terminal` · `claude-code` · `codex` · `coding-agent` · `developer-tools` · `devtools`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/deepsteve--deepsteve/adee5ea71e2e3289.png" width="100%" alt="deepsteve/deepsteve screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/ersinkoc/claude-mods">ersinkoc/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Ringkasan

KOZMOS — mod visual langsung untuk Claude Code (CLI + desktop): pita di atas prompt, bilah sisi, ticker status, pendamping, penjaga, dan suara.

<sub>🔧 Ditemukan digunakan dalam kode: `mods/compass/README.md`, `mods/blackbox/README.md`, `mods/orrery/README.md`</sub>

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Mod: dibuat dengan kemampuan mod`                                |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |
| Bahasa   | TypeScript                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **9**      |
| Push terakhir            | 2026-10-10 |
| Pertama kali dicantumkan | 2026-10-09 |

🏷 `anthropic` · `claude-code` · `claude-code-mods` · `claude-code-plugin` · `tui`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ersinkoc--claude-mods/ece950c6b8ad049e.png" width="100%" alt="ersinkoc/claude-mods screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Arunjay4213/claude-mods">Arunjay4213/claude-mods</a></b> · ⭐8 · TypeScript · 👁️ observed · 25 天</summary>

##### 📝 Ringkasan

Pelacak sesi untuk Claude Code yang dibuat sebagai mod: jendela konteks, laju penggunaan kuota rencana, biaya per giliran

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Mod: dibuat dengan kemampuan mod`                                |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |
| Bahasa   | TypeScript                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **8**      |
| Push terakhir            | 2026-09-15 |
| Pertama kali dicantumkan | 2026-10-04 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `developer-tools` · `function-hooks` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Arunjay4213/claude-mods/main/docs/demo.gif" width="100%" alt="Arunjay4213/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Arunjay4213/claude-mods/main/docs/demo.gif" width="100%" alt="Arunjay4213/claude-mods animation"><br><sub>rekaman animasi</sub></td>
</tr></table>

<sub>Aset ditautkan langsung dari repositori upstream karena tidak ada lisensi yang mengizinkan redistribusi yang dinyatakan.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/az9713/claude-mod-pack">az9713/claude-mod-pack</a></b> · ⭐8 · TypeScript · 👁️ observed · 7 天</summary>

##### 📝 Ringkasan

Enam mod Claude Code dalam satu plugin (Token Weather, Cache Keeper, Wait What, Prompt Queue, Snake, Blast Radius) dengan switch per mod, plus laporan mods-vs-hooks.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Mod: dibuat dengan kemampuan mod`                                |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |
| Bahasa   | TypeScript                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **8**      |
| Push terakhir            | 2026-10-04 |
| Pertama kali dicantumkan | 2026-10-06 |

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/az9713--claude-mod-pack/7889282e792ed11e.png" width="100%" alt="az9713/claude-mod-pack screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/devbrother2024/devbrothers-mods">devbrother2024/devbrothers-mods</a></b> · ⭐7 · TypeScript · 👁️ observed · 6 天</summary>

##### 📝 Ringkasan

Kumpulan mod Claude Code milik 개발동생. Paket taksi: meteran, navigasi, kamera tilang, dashcam

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Mod: dibuat dengan kemampuan mod`                                |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |
| Bahasa   | TypeScript                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **7**      |
| Push terakhir            | 2026-10-04 |
| Pertama kali dicantumkan | 2026-10-04 |

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/devbrother2024--devbrothers-mods/10df726087fd2881.webp" width="100%" alt="devbrother2024/devbrothers-mods screenshot"></td>
<td align="center" valign="top"><a href="https://www.youtube.com/@%EA%B0%9C%EB%B0%9C%EB%8F%99%EC%83%9D"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/devbrother2024--devbrothers-mods/10df726087fd2881.webp" width="100%" alt="video"></a><br><sub><a href="https://www.youtube.com/@%EA%B0%9C%EB%B0%9C%EB%8F%99%EC%83%9D">Tonton di youtube.com</a> · pemutaran dibuka di situs host; GitHub tidak dapat menyematkannya secara sebaris</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/nogu66/md-prompt">nogu66/md-prompt</a></b> · ⭐7 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Ringkasan

Markdown, ditampilkan ke kotak prompt Claude Code saat Anda mengetik. Kode berpagar menjadi kartu dengan penyorotan sintaks bahkan sebelum Anda menutup pagar.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Mod: dibuat dengan kemampuan mod`                                |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |
| Bahasa   | TypeScript                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **7**      |
| Push terakhir            | 2026-10-03 |
| Pertama kali dicantumkan | 2026-10-10 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `function-hooks`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nogu66--md-prompt/b729912bc80aeee4.png" width="100%" alt="nogu66/md-prompt screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nogu66--md-prompt/408107e3aa381332.gif" width="100%" alt="nogu66/md-prompt animation"><br><sub>rekaman animasi</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/ronanworks/claude-code-mods">ronanworks/claude-code-mods</a></b> · ⭐7 · TypeScript · 👁️ observed · 3 天</summary>

##### 📝 Ringkasan

Mod Claude Code: panel penggunaan pixel crab usage-hud + tautan HTML yang bisa diklik di terminal dan kartu kode sekali salin html-shelf

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Mod: dibuat dengan kemampuan mod`                                |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |
| Bahasa   | TypeScript                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **7**      |
| Push terakhir            | 2026-10-08 |
| Pertama kali dicantumkan | 2026-10-07 |

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ronanworks--claude-code-mods/34d0d4bdc2328b61.gif" width="100%" alt="ronanworks/claude-code-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ronanworks--claude-code-mods/c6d323f2b976bd4e.gif" width="100%" alt="ronanworks/claude-code-mods animation"><br><sub>rekaman animasi</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/arasovic/claude-code-mods">arasovic/claude-code-mods</a></b> · ⭐6 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Ringkasan

Mod untuk Claude Code: plugin hook fungsi yang menambahkan panel langsung dan perilaku ke UI terminal

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Mod: dibuat dengan kemampuan mod`                                |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |
| Bahasa   | TypeScript                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **6**      |
| Push terakhir            | 2026-10-10 |
| Pertama kali dicantumkan | 2026-10-04 |

🏷 `ai-agents` · `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-mods` · `claude-code-plugin` · `claude-code-plugins`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/arasovic--claude-code-mods/a8e330d8ce6f7bad.png" width="100%" alt="arasovic/claude-code-mods screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/helenkwok/gsd-status-mod">helenkwok/gsd-status-mod</a></b> · ⭐6 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Ringkasan

Dashboard GSD langsung untuk Claude Code: peta jalan, pohon agen dengan percabangan, konteks dan biaya, aliran kerja, serta pembaca markdown untuk .planning. Hanya-baca.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Mod: dibuat dengan kemampuan mod`                                |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |
| Bahasa   | TypeScript                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **6**      |
| Push terakhir            | 2026-10-11 |
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `agents` · `claude-code` · `claude-code-mod` · `claude-code-plugin` · `dashboard` · `gsd` · `markdown-reader` · `planning`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/helenkwok--gsd-status-mod/4626cb34617b7732.png" width="100%" alt="helenkwok/gsd-status-mod screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/helenkwok--gsd-status-mod/a31036b15398e820.gif" width="100%" alt="helenkwok/gsd-status-mod animation"><br><sub>rekaman animasi</sub></td>
</tr></table>

</details>

<details>
<summary><b>Lainnya dalam kategori ini</b> <sub>· 431</sub></summary>

- [karanb192/claude-code-mods](https://github.com/karanb192/claude-code-mods) - Mod Claude dan alat untuk membangunnya: skill builder, lalu mod.
- [ucsandman/claude-harness](https://github.com/ucsandman/claude-harness) - Harness Claude Code yang saya jalankan setiap hari, diterbitkan dengan nama ini…
- [kagamiurayama/claude-code-roof-mod](https://github.com/kagamiurayama/claude-code-roof-mod) - Ubah atap Claude Code dengan Claude Mods: tanpa mengubah biner, ganti prompt…
- [nateherkai/claude-code-mods](https://github.com/nateherkai/claude-code-mods) - Empat mod Claude Code: Cache Keeper, Recording Mode, Goal Meter, dan Collision…
- [Hangghost/learning-hacker-claude-mod](https://github.com/Hangghost/learning-hacker-claude-mod) - Mod Claude Code dari Learning Hacker: menggambarkan operasi agen agar mudah…
- [kakha13/claude](https://github.com/kakha13/claude) - Mod Claude Code yang memperbaiki dan menerjemahkan prompt Anda sebelum Claude…
- [rashedInt32/glass](https://github.com/rashedInt32/glass) - A desktop-app look for Claude Code.
- [xuanji86/claude-agentpane](https://github.com/xuanji86/claude-agentpane) - Panel samping untuk Claude Code: subagen yang dijalankan sesi, apa yang sedang…
- [AgriciDaniel/claude-mods-brain](https://github.com/AgriciDaniel/claude-mods-brain) - Basis pengetahuan Obsidian dengan sumber kutipan tentang mod Claude Code: cara…
- [letswritetw/claude-mod-open-todos](https://github.com/letswritetw/claude-mod-open-todos) - Panel bilah samping Claude Desktop (tab Code): mencantumkan semua tugas…
- [nekyialabs/claude-code-toolkit](https://github.com/nekyialabs/claude-code-toolkit) - Mod dan skill Claude Code dari Nekyia Labs, dibuat dan digunakan setiap hari…
- [BeLazy167/claude-mods-skill](https://github.com/BeLazy167/claude-mods-skill) - Skill yang mengajarkan agen Claude Code untuk membuat Mod Claude.
- [letswritetw/claude-mod-token-usage](https://github.com/letswritetw/claude-mod-token-usage) - Bilah penggunaan di atas kotak input Claude Desktop (tab Code): kuota 5j / 7h…
- [KilimcininKorOglu/claude-code-mods](https://github.com/KilimcininKorOglu/claude-code-mods) - Mod Claude (plugin function-hooks) untuk Claude Code.
- [omarcevi/claudemods](https://github.com/omarcevi/claudemods) - Mod, plugin &amp; skill Claude komunitas, dapat diinstal dari satu marketplace.
- [baselane-sh/mods-catalog](https://github.com/baselane-sh/mods-catalog) - Galeri mod Baselane: mod Claude Code yang telah diperiksa dan disematkan.
- [eighteyes/cactus](https://github.com/eighteyes/cactus) - Antrean keputusan CLI/TUI untuk manusia yang bekerja dengan agen percakapan.
- [jkf87/ide-mod](https://github.com/jkf87/ide-mod) - Mod panel IDE Claude Code: papan agent, pohon file dan penampil HWP/PDF, status…
- [xuanji86/claude-statuspane](https://github.com/xuanji86/claude-statuspane) - Kartu status mengambang untuk Claude Code—model, konteks, batas laju, biaya…
- [danyuchn/claude-mods](https://github.com/danyuchn/claude-mods) - Mod Claude Code: screen-guard menyamarkan nama dan rahasia saat Anda berbagi…
- [magidandrew/cx](https://github.com/magidandrew/cx) - Ekstensi Claude Code. Buka seluruh kekuatan Claude.
- [markneonin/paneline](https://github.com/markneonin/paneline) - Mod (plugin) Claude Code yang menambahkan panel samping dengan tab Activity…
- [mishgoldenberg/claude-mods](https://github.com/mishgoldenberg/claude-mods) - Panel, pagar pengaman, dan mod peningkat kenyamanan untuk Claude Code: konteks…
- [ofeklevy11/claude-code-hud](https://github.com/ofeklevy11/claude-code-hud) - Dua mod Claude Code di atas kotak prompt: pengukur jendela konteks, batas 5…
- [Shuffzord/RoadRaven](https://github.com/Shuffzord/RoadRaven) - Rencana Anda, yang memantau dirinya sendiri.
- [xuanji86/claude-mdview](https://github.com/xuanji86/claude-mdview) - Baca file markdown yang diberi nama oleh Claude Code, tampilkan di samping…
- [leopiney/wolfbud-claude-mod](https://github.com/leopiney/wolfbud-claude-mod) - Rekan kerja suara untuk Claude Code. Bicarakan berbagai hal dengan serigala 3D…
- [borabiricik/claude-mods](https://github.com/borabiricik/claude-mods) - Mod Claude Code: typing-speed, speedometer pengetikan langsung dengan statistik…
- [charimsma/dopa-mode](https://github.com/charimsma/dopa-mode) - Kembang api untuk Claude Code: setiap penekanan tombol, pemanggilan tool…
- [DrishtantKaushal/AwesomeClaudeCodeMods](https://github.com/DrishtantKaushal/AwesomeClaudeCodeMods) - Temukan mod, plugin, dan ekstensi Claude Code dengan demo animasi, daftar…
- [galElmalah/claude-mods](https://github.com/galElmalah/claude-mods) - Mod Claude Code: diagram mermaid yang digambar sebaris dalam transkrip.
- [ha-ptt0601/cc-mods](https://github.com/ha-ptt0601/cc-mods) - Mod Claude Code kecil (plugin function-hook): session-switcher dan lainnya.
- [hahmjuntae/claude-mods-image-preview](https://github.com/hahmjuntae/claude-mods-image-preview) - Mod Claude Code: thumbnail gambar yang ditempel di atas prompt, di terminal apa…
- [HMarzban/claude-mod](https://github.com/HMarzban/claude-mod) - See what your next Claude Code message costs: a live band above the prompt with…
- [LeeHigma0201/claude-code-mods](https://github.com/LeeHigma0201/claude-code-mods) - Mod Claude Code: mod-scout (menemukan mod yang paling sering Anda gunakan)…
- [Nongfsq/frank-claude-cockpit](https://github.com/Nongfsq/frank-claude-cockpit) - Dua mod Claude Code untuk menjalankan banyak sesi sekaligus: kartu konteks di…
- [scodge-24/workface](https://github.com/scodge-24/workface) - Mod Claude Code: kontrol konten autocompaction dari TUI secara native.
- [VedantAndhale/claude-pro-kit](https://github.com/VedantAndhale/claude-pro-kit) - Buat paket Pro Claude bertahan lebih lama: mod Claude Code untuk HUD penggunaan…
- [Antreas-Strb/glanceflow](https://github.com/Antreas-Strb/glanceflow) - GlanceFlow untuk Claude Code: checklist tenang di atas prompt yang menampilkan…
- [claude-code-mods/best-claude-code-mods](https://github.com/claude-code-mods/best-claude-code-mods) - Mod Kode Claude terbaik: dipilih langsung, divalidasi, disematkan.
- [dominicrico/jev-router](https://github.com/dominicrico/jev-router) - Plugin Claude Code: perutean model Claude otomatis.
- [FynnXland/fynn-mods](https://github.com/FynnXland/fynn-mods) - Enam mod untuk Claude Code: maskot Clawd animasi, bar batas penggunaan dan…
- [Hula-Hoop-AI/supermods](https://github.com/Hula-Hoop-AI/supermods) - Marketplace mod untuk Claude Code: step debugger untuk loop agent, petunjuk…
- [Jhonatan-de-Souza/ClaudeMods](https://github.com/Jhonatan-de-Souza/ClaudeMods) - Mod Claude Code: menu Tools Claude, mode Zen, tema terminal, kontrol usaha dan…
- [mertkayacs/ultramod](https://github.com/mertkayacs/ultramod) - Paket mod serba ada terbaik untuk Claude Code: batas penggunaan dan HUD…
- [mthli/cc-shorts](https://github.com/mthli/cc-shorts) - Putar YouTube Shorts di Claude Code Anda 💃.
- [NarenDawar/narens-claude-toolkit](https://github.com/NarenDawar/narens-claude-toolkit) - Toolkit Claude milik Naren: skills, mods, dan servers MCP untuk Claude Code.
- [neteye-platform/cc-split-diff-view](https://github.com/neteye-platform/cc-split-diff-view) - Mod Claude Code yang menggambar perbedaan Edit dan Write dalam dua kolom…
- [raresmun/claude-mods](https://github.com/raresmun/claude-mods) - Mod untuk Claude Code: Clawd, maskot piksel kecil yang memeragakan apa yang…
- [reporails/arcade](https://github.com/reporails/arcade) - Game desktop klasik sebagai mod Claude Code, dimainkan di panel saat Claude…
- [testy-cool/awesome-claude-code-mods](https://github.com/testy-cool/awesome-claude-code-mods) - Daftar pilihan mod Claude Code yang dapat dipasang sebagai pasar plugin: tema…
- [xsyetopz/dotclaude](https://github.com/xsyetopz/dotclaude) - Plugin Claude Code yang sangat berpendirian, dirancang oleh seorang Rustacean…
- [yash-gadodia/claude-mods](https://github.com/yash-gadodia/claude-mods) - Mod Claude Code yang menjaga agent tetap jujur — function hooks yang menjaga…
- [alexcz-a11y/claude-mods](https://github.com/alexcz-a11y/claude-mods) - Koleksi mod Claude Code saya, satu mod per direktori.
- [Ankitrai97/rai-claude-mods](https://github.com/Ankitrai97/rai-claude-mods) - Lima mod Claude Code gratis: Simple Mode, Usage Tally, Context Handoff, Inbox…
- [ArgonQQ/sipp](https://github.com/ArgonQQ/sipp) - 💧 A passive-aggressive water reminder for Claude Code.
- [CodyAMaughan/meme-factory](https://github.com/CodyAMaughan/meme-factory) - Baru keluar dari pabrik. Mod Claude Code: minta meme, lalu terus bekerja.
- [DarioFontanel/claude-code-mods](https://github.com/DarioFontanel/claude-code-mods) - Mod untuk Claude Code: bilah prompt cache, langkah berikutnya, tombol cepat…
- [estruyf/claude-stats-mod](https://github.com/estruyf/claude-stats-mod) - Mod Claude Code yang menggambar batas penggunaan dan pengeluaran Anda di bilah…
- [hellosverre/mod-store](https://github.com/hellosverre/mod-store) - App store untuk mod Claude Code, di dalam Claude Code: /mods untuk menjelajah…
- [herman925/925-cc-plugins](https://github.com/herman925/925-cc-plugins) - Mod Claude Code milik Herman (marketplace herman-mods).
- [homieyangg/claude-code-mods](https://github.com/homieyangg/claude-code-mods) - Mod Claude Code: bilah kemajuan untuk rencana, buku besar tentang apa yang…
- [i-harsha-reddy/naruto-mod](https://github.com/i-harsha-reddy/naruto-mod) - Pendamping Naruto bergaya pixel-art untuk Claude Code: 20 ninja, 60 jutsu…
- [ice-lfernandes/claude-code-mods](https://github.com/ice-lfernandes/claude-code-mods) - Enam mod Claude Code: batas rencana dan konteks di atas prompt, pelatih daftar…
- [macleodlabs-ai/claudeflow](https://github.com/macleodlabs-ai/claudeflow) - Mod Claude Code oleh MacLeod Labs: streams mengurai pekerjaan sesi yang saling…
- [MankhongGarden/claude-code-mods-field-notes](https://github.com/MankhongGarden/claude-code-mods-field-notes) - Catatan lapangan hari pertama tentang mod Claude Code di Windows: bilah bahan…
- [MichaelP17/claude-mods](https://github.com/MichaelP17/claude-mods) - Mod yang saya buat dan gunakan sendiri dalam penyiapan Claude Code saya.
- [patitow/claude-mod-cost-visibility](https://github.com/patitow/claude-mod-cost-visibility) - Mod Claude Code: meter biaya langsung, konteks &amp; kuota paket di atas prompt.
- [rbartoli/agent-usage-guard](https://github.com/rbartoli/agent-usage-guard) - Mod Claude Code yang menahan fan-out subagent, prompt konteks berat, dan loop…
- [schreibse/claude-code-mods](https://github.com/schreibse/claude-code-mods) - code-mods untuk claude.
- [shimo4228/harness-scope](https://github.com/shimo4228/harness-scope) - Mod Claude Code yang mengaktifkan atau menonaktifkan skill, agen, aturan, dan…
- [Sma1lboy/claude-mods](https://github.com/Sma1lboy/claude-mods) - Mod untuk Claude Code: plugin yang dibangun berdasarkan hook fungsi.
- [smukh/roll-credits](https://github.com/smukh/roll-credits) - Kredit bergaya film untuk sesi coding Anda.
- [Szotasz/claude-mods](https://github.com/Szotasz/claude-mods) - Saját Claude Code mod-ok pluginpiaca.
- [theonly1me/claude-code-mods](https://github.com/theonly1me/claude-code-mods) - Sekumpulan mod claude code yang saya buat.
- [Unayung/cc-mods-youtube](https://github.com/Unayung/cc-mods-youtube) - Pemutar YouTube berbasis cliamp di dalam Claude Code (mod Claude Code).
- [VladLeus/claude-mods](https://github.com/VladLeus/claude-mods) - Mod Claude Code: dasbor agent-fleet dan autopilot (marketplace local-mods).
- [vynnlee/mods](https://github.com/vynnlee/mods) - Mod Claude Code oleh vynnlee. Satu folder per mod, dapat dipasang dari satu…
- [yodakeisuke/claudelingo](https://github.com/yodakeisuke/claudelingo) - Pelajari bahasa asing sambil bekerja dengan Claude Code.
- [AlexeyHRDesign/colorwheel](https://github.com/AlexeyHRDesign/colorwheel) - Balasan bertema, diagram lebar penuh, serta konteks dan batas Anda dalam sekali…
- [alexlifexyz/p3c-guard](https://github.com/alexlifexyz/p3c-guard) - Saat Agen menulis Java, kode yang melanggar aturan Alibaba Java (p3c) tidak…
- [andrewbakercloudscale/claude-code-cost-sidebar](https://github.com/andrewbakercloudscale/claude-code-cost-sidebar) - Sidebar biaya, token, dan penggunaan konteks live untuk Claude Code: mod yang…
- [aosmcleod/next-up-mod](https://github.com/aosmcleod/next-up-mod) - Mod Claude Code: backlog tindak lanjut yang disarankan Claude di seluruh sesi…
- [ben-rogerson/claude-counter-strike](https://github.com/ben-rogerson/claude-counter-strike) - Panggilan radio Counter-Strike 1.6 untuk Claude Code - &quot;Fire in the hole&quot; saat…
- [BjoernSchotte/ccmod-amp](https://github.com/BjoernSchotte/ccmod-amp) - Radio internet di dalam Claude Code: sidebar cliamp, pemutar mini, favorit…
- [BuddyLim/claude-code-mod-lens](https://github.com/BuddyLim/claude-code-mod-lens) - A Claude Code mod: a code review pane with the changed files, inline…
- [cephalofoil/kitt](https://github.com/cephalofoil/kitt) - Penyiapan Herdr + mod kode Claude untuk pekerjaan pengembangan produk.
- [chenyuxiaojin/cyxj-notch](https://github.com/chenyuxiaojin/cyxj-notch) - Dasbor notch macOS untuk Claude Code: batas penggunaan, sesi terbuka, progres…
- [chrisluo5311/squad-chat](https://github.com/chrisluo5311/squad-chat) - Claude sedang memasak. Chat dengan skuad Anda.
- [crebot51/jack-mods](https://github.com/crebot51/jack-mods) - jack 的 Claude Code mods 合集.
- [danielpg95/modster-hunter](https://github.com/danielpg95/modster-hunter) - Mod Claude Code: tangkap Modsters pixel-art dalam game idle saat Claude bekerja.
- [darkomarijaan/nexus-mod](https://github.com/darkomarijaan/nexus-mod) - All-in-one Claude Code mod: a live HUD, safety guards.
- [Davron2004/slash-coverage](https://github.com/Davron2004/slash-coverage) - Lihat file mana yang ada dalam konteks setiap agen Claude Code, dan seberapa…
- [dougcunha/claude-mods](https://github.com/dougcunha/claude-mods) - Mod untuk Claude Code: panel, perintah, dan hook yang dibuat dengan plugin…
- [drakulavich/cogload](https://github.com/drakulavich/cogload) - Tetap tenang. Termometer untuk hari-hari Claude Code Anda: setiap jam diberi…
- [EgonLeitner/dashband](https://github.com/EgonLeitner/dashband) - Prompt cache, context and plan limits at a glance for Claude Code, in the…
- [ElirazKed/claude-code-pr-watch](https://github.com/ElirazKed/claude-code-pr-watch) - Mod Claude Code: panel langsung berisi PR GitHub yang dibuka atau didorong oleh…
- [enhki/claude-mods](https://github.com/enhki/claude-mods) - Mod kecil Claude Code untuk terminal dan aplikasi desktop.
- [ewxgwy1987/claude-code-mods](https://github.com/ewxgwy1987/claude-code-mods) - Kumpulan mod Claude Code, masing-masing dalam repositorinya sendiri…
- [ewxgwy1987/claude-code-progress-board](https://github.com/ewxgwy1987/claude-code-progress-board) - Mod Claude Code: panel kemajuan untuk tugas, subagen, proses alur kerja…
- [ewxgwy1987/claude-code-session-toc](https://github.com/ewxgwy1987/claude-code-session-toc) - Mod Claude Code: daftar isi seluruh sesi yang dapat diklik dan memiliki stempel…
- [ewxgwy1987/claude-code-usage-meter](https://github.com/ewxgwy1987/claude-code-usage-meter) - Mod Claude Code: batas laju rencana, isi konteks, biaya sesi, dan token per…
- [Exdenta/ambient-spanish](https://github.com/Exdenta/ambient-spanish) - Skill + mod Claude CLI yang menambahkan kata-kata Spanyol ke balasan agen.
- [gregdotca/ccmod-the-machine](https://github.com/gregdotca/ccmod-the-machine) - Mod kode Claude yang menata ulang tampilannya menjadi The Machine dari Person…
- [hellosverre/smart-compact](https://github.com/hellosverre/smart-compact) - Mod Claude Code: melakukan compact pada saat yang tepat.
- [HyunjunJeon/claude-workflow-mods](https://github.com/HyunjunJeon/claude-workflow-mods) - dag-workflow: Claude Code mod for mandatory, verified DAG workflows of…
- [ibrahimkobeissy/claude-mods](https://github.com/ibrahimkobeissy/claude-mods) - Mod sumber terbuka untuk Claude Code: panel, baris status, toast, penjaga alat…
- [jduerrmann/agent-crew](https://github.com/jduerrmann/agent-crew) - Mod kode Claude: satu panel untuk setiap subagen, file yang mereka sentuh…
- [jonyfs/astrolabe](https://github.com/jonyfs/astrolabe) - 🧭 Mod Claude Code: status sesi, kemajuan Spec Kit live, dan tata kelola jendela…
- [kongyo2/context-view](https://github.com/kongyo2/context-view) - Jendela konteks sebagai satu baris di atas prompt, digambar seperti meter milik…
- [lorenzh/rabe](https://github.com/lorenzh/rabe) - Lihat apa yang dijalankan Claude Code di latar belakang: subagen, pekerjaan…
- [m4cd4r4/clear-resume](https://github.com/m4cd4r4/clear-resume) - Plugin gratis dan open-source untuk Claude Code.
- [meganemura/pull-request-pane](https://github.com/meganemura/pull-request-pane) - Mod Claude yang menampilkan pull request GitHub milik sesi dalam panel di…
- [nkapila6/sfx-gen](https://github.com/nkapila6/sfx-gen) - Claude Code mod: generate sound effects from text prompts with a local Stable…
- [NMenzel/claude-devtools-mod](https://github.com/NMenzel/claude-devtools-mod) - Claude DevTools: debugger untuk tool call Claude Code.
- [NotRedFox/NotRedFoxs-Claude-skills](https://github.com/NotRedFox/NotRedFoxs-Claude-skills) - Keahlian Claude Code: pemeriksa fakta dokumen, auditor kode, log memori bug…
- [pepperonas/loc-today](https://github.com/pepperonas/loc-today) - Claude Code mod: today.
- [pepperonas/path-links](https://github.com/pepperonas/path-links) - Mod Claude Code: jalur yang dapat diklik dalam balasan — klik folder untuk…
- [rezzminator/buddy](https://github.com/rezzminator/buddy) - Plugin teman Claude Code: pendamping ASCII di atas prompt Anda yang mengingat…
- [rezzminator/tool-visibility-controller](https://github.com/rezzminator/tool-visibility-controller) - Plugin Claude Code untuk visibilitas alat per agen — sembunyikan dan tolak…
- [samfrmr/barmkin-mod](https://github.com/samfrmr/barmkin-mod) - Mod kode Claude: lapisan keamanan untuk Claude Code — penyamaran rahasia…
- [Sennjen/claude-sdlc](https://github.com/Sennjen/claude-sdlc) - Plugin dan mod Claude Code: SDLC AI-native.
- [SeongGwangJu/k-mods](https://github.com/SeongGwangJu/k-mods) - Koleksi mod Claude Code yang luar biasa | Koleksi mod Claude Code.
- [simplecore-inc/claude-mods](https://github.com/simplecore-inc/claude-mods) - Plugin Claude Code (mod): beralih di antara beberapa akun Claude, memantau…
- [Singh-AP/awesome-claude-mods](https://github.com/Singh-AP/awesome-claude-mods) - 🧩 Mod Claude Code yang telah diuji dan dapat dipasang dengan satu perintah…
- [tanujarun/it-speaks](https://github.com/tanujarun/it-speaks) - It Speaks: mod Claude Code yang membacakan balasan Claude dan prompt Anda saat…
- [timoncool/slapbox](https://github.com/timoncool/slapbox) - 🍑 Pukul Claude saat ia melakukan kesalahan — mod pelepas stres untuk Claude…
- [tommy5dollar/effort-router](https://github.com/tommy5dollar/effort-router) - Buat penggunaan Claude Code Anda bertahan hingga dua kali lebih lama.
- [TroyJLorents-GH/mod-squad](https://github.com/TroyJLorents-GH/mod-squad) - Mod Claude Code: plugin kecil untuk panel langsung, pengaturan perutean model…
- [valeryia-piatrova/token-hamster](https://github.com/valeryia-piatrova/token-hamster) - 🐹 Mod &amp; plugin Claude Code: monitor penggunaan, pelacak token &amp; baris status.
- [VictorGambarini/jev-mod](https://github.com/VictorGambarini/jev-mod) - A Claude Code mod that hands the small decisions to a cheap decision model…
- [vumichien/claude-code-mods-kit](https://github.com/vumichien/claude-code-mods-kit) - Tiga mod Code Claude gratis: sembunyikan nilai .env dari hasil alat, pantau…
- [y-hirakaw/claude-code-mods](https://github.com/y-hirakaw/claude-code-mods) - Mod Claude Code. touch-map: lihat berkas mana yang dicantumkan, dibaca, diedit…
- [Yanir-R/catchup](https://github.com/Yanir-R/catchup) - Mod Claude Code yang merangkum pesan agen yang belum Anda baca, dalam bahasa…
- [Yuvalz19500/claude-mods](https://github.com/Yuvalz19500/claude-mods) - Mod untuk Claude Code: panel langsung, pita, dan hook. Marketplace plugin.
- [0xnicholasy/claude-mods](https://github.com/0xnicholasy/claude-mods) - Marketplace plugin Claude Code untuk mod milik 0xnicholasy.
- [AbyssCN/claude-lead-harness](https://github.com/AbyssCN/claude-lead-harness) - Mod kode Claude + driver cheap-executor: satu sesi Claude sebagai pemimpin…
- [AdamCaviness/cache-magic](https://github.com/AdamCaviness/cache-magic) - Mod Claude Code yang menawarkan alternatif fleksibel untuk idleCompaction…
- [akixi-maison/usage-mods](https://github.com/akixi-maison/usage-mods) - Mod Claude Code: bilah kemajuan penggunaan (context, 5h, 7d) dan tombol ringkas…
- [alan-oliv/claude-mods](https://github.com/alan-oliv/claude-mods) - Claude Code mods: session stat cards above the prompt.
- [Aler1x/claude-cat](https://github.com/Aler1x/claude-cat) - Kucing braille animasi di atas prompt Claude Code.
- [alinaqi/mixture-of-models-claude-mod](https://github.com/alinaqi/mixture-of-models-claude-mod) - Mod Claude Code: mengarahkan pekerjaan ringan ke GLM/Kimi melalui Claude Code…
- [aloki-alok/omni-cat](https://github.com/aloki-alok/omni-cat) - Kucing piksel di atas prompt Code Claude Anda yang menjalankan panggilan uji…
- [ambervdberg/smartcompact](https://github.com/ambervdberg/smartcompact) - Mod Claude Code yang memilih waktu yang tepat untuk melakukan pemadatan agar…
- [an80sPWNstar/claude-mods](https://github.com/an80sPWNstar/claude-mods) - Mod Claude untuk Claude Code: token-meter.
- [anderson-spider/claude-mods](https://github.com/anderson-spider/claude-mods) - Marketplace plugin Claude Code oleh anderson-spider.
- [androidZzT/claude-trading-mods](https://github.com/androidZzT/claude-trading-mods) - Mod Claude Code untuk memantau pasar dari terminal: panel A股/港股/美股 dengan tren…
- [angomedia/claude-mods](https://github.com/angomedia/claude-mods) - Mod untuk Claude Code.
- [Ashley-Pettit/lgtm-flash](https://github.com/Ashley-Pettit/lgtm-flash) - Kapal LGTM Lines berlayar melewati setelah setiap perubahan kode — mod Code…
- [Ashley-Pettit/villager-hp](https://github.com/Ashley-Pettit/villager-hp) - Batas penggunaan Claude Anda sebagai kartu kesehatan penduduk desa animasi…
- [AskTinNguyen/ather-mods](https://github.com/AskTinNguyen/ather-mods) - Mod Claude Code untuk tim S2 (marketplace ather).
- [Atanur/deskfit](https://github.com/Atanur/deskfit) - Latihan singkat saat Claude bekerja: target harian, streak, badge, dan…
- [atharv6f/waypoint](https://github.com/atharv6f/waypoint) - Plan, task and agent progress beside the Claude Code prompt — a Claude Code mod.
- [aycandv/claude-usage-meter](https://github.com/aycandv/claude-usage-meter) - Papan penggunaan untuk Claude Code: pengeluaran per model.
- [barneym/claude-context-bar](https://github.com/barneym/claude-context-bar) - Mod Claude Code: uraian live context-window di atas prompt.
- [benjaminr/nowplaying](https://github.com/benjaminr/nowplaying) - Mod Now Playing untuk Claude Code: Apple Music dan Spotify di atas prompt…
- [bennewton999/claude-code-mods](https://github.com/bennewton999/claude-code-mods) - Lima mod Claude Code untuk menjalankan banyak sesi sekaligus: papan armada…
- [berkayburakk/berko-mods](https://github.com/berkayburakk/berko-mods) - Paket mod Claude Code dari video Berko: Mask, View, Guard, Saving, Chime + mod…
- [bhargava-gumpula/claude-mods](https://github.com/bhargava-gumpula/claude-mods) - Mod Code Claude: pita penggunaan, daftar obrolan, /cube, /handoff, pembersihan…
- [broening/claude-mods](https://github.com/broening/claude-mods) - Mod untuk Claude Code: Cache-Uhr, Blast Radius, Vorschlaege, Arbeitsliste, Grill.
- [Carismarkus/clowl](https://github.com/Carismarkus/clowl) - Hanya seekor owl untuk Claude Code Anda.
- [cGradying/claude-code-cockpit](https://github.com/cGradying/claude-code-cockpit) - Pita Claude Code satu baris.
- [ChaseWNorton/claude-doom](https://github.com/ChaseWNorton/claude-doom) - Engine Doom asli dengan Freedoom, dapat dimainkan di dalam Claude Code.
- [cldotdev/claude-todo-list](https://github.com/cldotdev/claude-todo-list) - A Claude Code mod that keeps a running list of the open items in a conversation…
- [d3nims/d3nim-claude-mods](https://github.com/d3nims/d3nim-claude-mods) - d3nim 팀 전용 Claude Code mods (usage-meter: 파란 불꽃 / 테리어 사용량 밴드).
- [Dandeppert/Claude-mods](https://github.com/Dandeppert/Claude-mods)
- [danielgillaspia01-web/claude-mods](https://github.com/danielgillaspia01-web/claude-mods)
- [davidurco/cc-tamagotchi](https://github.com/davidurco/cc-tamagotchi) - Tamagotchi yang hidup di dalam Claude Code: ia menetas, memakan kode yang…
- [Demo-0416/claude-code-mods](https://github.com/Demo-0416/claude-code-mods) - Mods for Claude Code, as a plugin marketplace.
- [derekwden-droid/message-timestamps](https://github.com/derekwden-droid/message-timestamps) - Mod kode Claude: menampilkan waktu pada setiap prompt dan balasan di terminal…
- [devohmycode/ccmods](https://github.com/devohmycode/ccmods) - Mod Claude Code yang ditulis sebagai hook fungsi, serta marketplace yang…
- [DiegoCarrillo32/claude-plugins](https://github.com/DiegoCarrillo32/claude-plugins) - Mod kode Claude dan sistem desain: crab-crew dan sistem desain Crab Crew.
- [DiegoHeer/claude-mods](https://github.com/DiegoHeer/claude-mods) - Mod Claude Code saya, dibagikan sebagai marketplace plugin.
- [dot-agi/arrester](https://github.com/dot-agi/arrester) - Mod Claude Code: setelah guard memblokir pemanggilan alat, mod ini menghentikan…
- [dot-agi/downrange](https://github.com/dot-agi/downrange) - Mod Claude Code: pekerjaan latar belakang dalam satu tampilan, dengan kemajuan…
- [dot-agi/high-command](https://github.com/dot-agi/high-command) - Mod Claude Code: satu kotak masuk untuk pesan dari rekan tim, subagen bernama…
- [dot-agi/sandbox-tuner](https://github.com/dot-agi/sandbox-tuner) - Mod Claude Code: menjelaskan pemblokiran sandbox dan mengubah pemblokiran…
- [Egrn/claude-code-mutedit](https://github.com/Egrn/claude-code-mutedit) - Hei, dibisukan! Buang diff, pangkas riff, tak ada lagi edit, kurangi kredit.
- [elec100-design/claude-mods](https://github.com/elec100-design/claude-mods) - claude용 mods.
- [eric1hua/claudemods-desktop-statusline](https://github.com/eric1hua/claudemods-desktop-statusline) - Mod Claude Code: penggunaan langganan (5h / 7d) sebagai pita di atas prompt di…
- [evasuka/work-meter](https://github.com/evasuka/work-meter) - Mod Claude Code: menampilkan kemajuan pekerjaan dan sisa kuota akun di atas…
- [fanoisme/claude-mods](https://github.com/fanoisme/claude-mods) - Mod dengan desain gerak untuk Code Claude: monitor langsung dan responsif untuk…
- [floheissler/cc-worktree-radar](https://github.com/floheissler/cc-worktree-radar) - Radar langsung cabang paralel dan worktree Anda di atas prompt: mana yang dapat…
- [gaius-codius/ostrakon](https://github.com/gaius-codius/ostrakon) - A Claude Code mod for capturing thoughts mid-work, triaging them across…
- [GarvitNangru/claude-code-mods](https://github.com/GarvitNangru/claude-code-mods) - Mod dan skin untuk Claude Code: bilah progres langsung untuk tugas Claude, tema…
- [Gat0rRex/claude-mods](https://github.com/Gat0rRex/claude-mods) - Mod Claude Code (plugin function-hook): pita konteks, hal-hal yang belum…
- [gauravruhela07/claude-mods](https://github.com/gauravruhela07/claude-mods) - Tujuh mod Claude Code: savvy-progress, skins, filetree, cache-tax…
- [GeckoKing9/claude-code-copy-button](https://github.com/GeckoKing9/claude-code-copy-button) - Ctrl+klik untuk menyalin tautan pada setiap blok kode dalam balasan Claude Code…
- [Gersom/claude-mod-agent-radar](https://github.com/Gersom/claude-mod-agent-radar) - Mod de Claude Code: monitor visual y pasivo del agente principal y sus…
- [Gersom/claude-mod-cache-watch](https://github.com/Gersom/claude-mod-cache-watch) - Mod Claude Code: panel yang menunjukkan apakah cache prompt sedang hangat atau…
- [Gersom/claude-mod-usage-meter](https://github.com/Gersom/claude-mod-usage-meter) - Mod de Claude Code: recuadro con el % de contexto y de los límites de 5 horas y…
- [Gersom/gersom-claude-mods](https://github.com/Gersom/gersom-claude-mods) - Mod untuk Claude Code: plugin hook, seperti usage-meter.
- [gonzalonicolasr/claude-code-nerv](https://github.com/gonzalonicolasr/claude-code-nerv) - Bilah samping bergaya Evangelion untuk Claude Code: konteks, kuota, aktivitas…
- [gotzastory/my-mods](https://github.com/gotzastory/my-mods) - Claude Code mods: context-bar-plus (context bar, quota, subagent modes).
- [hahahahahahahahah6/mod-audit](https://github.com/hahahahahahahahah6/mod-audit) - Static supply-chain auditor for Claude Code Mods — local, offline, stdlib-only.
- [hb03/claude-mods](https://github.com/hb03/claude-mods) - Mod berbahasa Jerman untuk Claude Code: petunjuk konteks/cache, poin terbuka…
- [helenkwok/open-links](https://github.com/helenkwok/open-links) - Claude Code mod: file paths in Claude.
- [hellosverre/redgreen](https://github.com/hellosverre/redgreen) - Hasil pengujian di panel Claude Code: kegagalan, detailnya, dan riwayat proses…
- [Huuuuung/think-meter](https://github.com/Huuuuung/think-meter) - Mod Claude Code: berapa lama setiap jawaban berlangsung, berapa lama Claude…
- [hyperbola-bear/claude-mods](https://github.com/hyperbola-bear/claude-mods) - for my claude mods.
- [icedevil2001/auto-continue](https://github.com/icedevil2001/auto-continue) - Claude Code mod: waits out the 5-hour usage limit and sends &quot;continue&quot; for you.
- [icedevil2001/claude-mods](https://github.com/icedevil2001/claude-mods) - Small mods for Claude Code, starting with auto-continue after the 5-hour limit.
- [im-adarsh/claude-mods](https://github.com/im-adarsh/claude-mods)
- [imsungbin/quackpit-mod](https://github.com/imsungbin/quackpit-mod) - A cockpit above your Claude Code prompt. The duck reads the gauges.
- [itaym967/rtl-questions](https://github.com/itaym967/rtl-questions) - Claude Code mod: shows Claude.
- [jakerains/claudemods](https://github.com/jakerains/claudemods) - Mod kode Claude kecil: pengukur konteks dan penggunaan plan, pengukur…
- [jeffyfung/claude-mods](https://github.com/jeffyfung/claude-mods) - Tempat untuk menyimpan mod claude saya.
- [jessetsai1024/claude-ctx-panel](https://github.com/jessetsai1024/claude-ctx-panel) - Panel penggunaan context di bilah samping: total, kategori, pertumbuhan tiap…
- [jessetsai1024/claude-files](https://github.com/jessetsai1024/claude-files) - Daftar file di bilah samping: file apa yang dibuat, diubah, atau dihapus dalam…
- [jessetsai1024/claude-maomao](https://github.com/jessetsai1024/claude-maomao) - 毛毛 bergaya 8-bit (kelinci lop Belanda hitam-putih) berlari dan melompat di atas…
- [jessetsai1024/claude-prompts](https://github.com/jessetsai1024/claude-prompts) - “Yang pernah saya tanyakan” di bilah samping: setiap kalimat yang diketik…
- [jessetsai1024/claude-timeline](https://github.com/jessetsai1024/claude-timeline) - Linimasa di bilah samping: ke mana waktu putaran ini digunakan.
- [jessetsai1024/claude-tokens](https://github.com/jessetsai1024/claude-tokens) - Pertukaran token di bilah samping: berapa token yang dikirim percakapan utama…
- [jessetsai1024/claude-whisper](https://github.com/jessetsai1024/claude-whisper) - Tas kacang jujur untuk claude code: setelah setiap putaran selesai menjawab…
- [jimmysteinmetz/b-sides](https://github.com/jimmysteinmetz/b-sides) - Mod kecil untuk Claude Code, seperti perintah slash baru dan panel samping.
- [jjjung0921/claude-mods](https://github.com/jjjung0921/claude-mods)
- [jkf87/mod-guide](https://github.com/jkf87/mod-guide) - Panduan komunitas tidak resmi untuk mod Claude Code (function hooks) dalam 6…
- [jorgehsy/claude-mods](https://github.com/jorgehsy/claude-mods) - Katalog mod untuk Claude Code.
- [jpo-oss/claude-games](https://github.com/jpo-oss/claude-games) - Game multiplayer untuk dimainkan di dalam Claude Code saat bekerja.
- [juampymdd/claude-code-model-picker](https://github.com/juampymdd/claude-code-model-picker) - Mod Claude Code: memilih model dan versi untuk permintaan berikutnya dari bilah…
- [KaiC5504/clawd-bar](https://github.com/KaiC5504/clawd-bar) - Clawd tinggal di pita di atas prompt Claude Code Anda: memeragakan sesi…
- [kajidog/cc-mods-tts](https://github.com/kajidog/cc-mods-tts) - Mod yang membacakan respons dan notifikasi Claude Code menggunakan VOICEVOX /…
- [kbrdn1/claude-crosstalk](https://github.com/kbrdn1/claude-crosstalk) - Mod Claude untuk membaca dan bergabung dalam percakapan antara sesi Claude Code…
- [Khanthtutzin/subagent-crew](https://github.com/Khanthtutzin/subagent-crew) - Mod Claude Code: menjalankan subagen sebagai maskot pixel Claude di atas prompt.
- [KingP1197/claude-mods](https://github.com/KingP1197/claude-mods) - Mod Claude untuk kemudahan/peningkatan kualitas penggunaan.
- [krishna-goutham-tls/cc-mods](https://github.com/krishna-goutham-tls/cc-mods) - Dua mod kode Claude: folio, panel file di samping chat, dan tint, penataan…
- [kyledarling-io/claude-code-desktop-hud](https://github.com/kyledarling-io/claude-code-desktop-hud) - HUD tugas langsung untuk Claude Code Desktop: strip di atas prompt saat Claude…
- [leonidb/claude-code-mods](https://github.com/leonidb/claude-code-mods) - Don&#x27;t let your attention wander off while waiting for Claude Code&#x27;s answer.
- [LordMordelon/claude-mods](https://github.com/LordMordelon/claude-mods) - Mod Claude Code untuk proyek Angel (Vremia).
- [Lucas-CX/awesome-claude-mods](https://github.com/Lucas-CX/awesome-claude-mods) - Panduan Mod Claude Code yang dikurasi komunitas: kasus penggunaan, demo asli…
- [M-i-k-e-l/agent-state](https://github.com/M-i-k-e-l/agent-state) - Mod Claude Code yang menampilkan apa yang sedang dilakukan Claude di subtitel…
- [malinfossum/mango-buddy](https://github.com/malinfossum/mango-buddy) - Kucing hitam berbulu lebat di atas prompt Claude Code Anda.
- [marcelmatula/claude-mods](https://github.com/marcelmatula/claude-mods) - Mod Claude Code milik Marcel dalam satu pasar plugin (marcel-mods).
- [MarcusJellinghaus/claude-mode-gate](https://github.com/MarcusJellinghaus/claude-mode-gate) - Mod Claude Code dengan profil izin yang dapat diganti: dasar yang aman, profil…
- [martin-macak/claude-code-mod-tracking](https://github.com/martin-macak/claude-code-mod-tracking) - Claude Code mod for tracking related artifacts and references.
- [MDmubarak786/claude-mods](https://github.com/MDmubarak786/claude-mods) - Mod komunitas untuk Claude Code: penjaga, panel, dan perintah yang berjalan di…
- [michaelblaess/turbo-mod](https://github.com/michaelblaess/turbo-mod) - Side pane for Claude Code: files Claude wrote, terminal splits, git repo status…
- [minhdevtree/claude-lens](https://github.com/minhdevtree/claude-lens) - A Claude Code mod that shows images, SVGs and PDF pages where they appear…
- [mmedum/glimt](https://github.com/mmedum/glimt) - Panel samping yang tenang untuk Claude Code: apa yang sedang dilakukan sesi…
- [mmedum/spor](https://github.com/mmedum/spor) - Mengembalikan apa yang disembunyikan Claude Code: file yang dibaca Claude…
- [mrsono0/ctx-footer](https://github.com/mrsono0/ctx-footer) - Claude Code mod: context window usage in the prompt footer mode slot.
- [muellerei/enable-todo-tools](https://github.com/muellerei/enable-todo-tools) - Mod Claude Code yang mengaktifkan kembali alat todo untuk model yang tidak…
- [muellerei/task-line](https://github.com/muellerei/task-line) - Mod Claude Code: satu baris per tugas di atas prompt dengan tugas saat ini…
- [nachtgold/claude-code-connect-four](https://github.com/nachtgold/claude-code-connect-four) - Mainkan Connect Four melawan AI di dalam Claude Code (/connect-four).
- [naoanao/agent-cross-check](https://github.com/naoanao/agent-cross-check) - Mod Claude Code: ketika agen coding lain melakukan commit ke repo Anda, Claude…
- [naoanao/shared-repo-guard](https://github.com/naoanao/shared-repo-guard) - Mod Claude Code untuk repo yang dibagikan oleh beberapa agen AI: menghentikan…
- [niksavis/handily](https://github.com/niksavis/handily) - Mod Claude Code yang menampilkan item kerja, tugas, dan sesi Anda, untuk…
- [nu0ma/query-guard](https://github.com/nu0ma/query-guard) - Pagar pengaman untuk SQL di Claude Code: meminta konfirmasi sebelum Claude…
- [OG-Matcha/tessera](https://github.com/OG-Matcha/tessera) - Satu mod untuk Claude Code, Windows dan CJK terlebih dahulu: pratinjau gambar…
- [oguz-hd/claude-code-chime](https://github.com/oguz-hd/claude-code-chime) - Chime untuk Claude Code: suara saat Claude selesai, membutuhkan input Anda…
- [ohade/claude-mods](https://github.com/ohade/claude-mods) - Mod Claude Code: gambar mini dan baris status.
- [onk3sh/fix-on-edit](https://github.com/onk3sh/fix-on-edit)
- [Open01277/claude-mods](https://github.com/Open01277/claude-mods)
- [osaki42/awesome-claude-mods](https://github.com/osaki42/awesome-claude-mods) - Mod Claude Code terbaik, diurutkan berdasarkan manfaatnya bagi Anda.
- [pablodiazjorge/impact-radius](https://github.com/pablodiazjorge/impact-radius) - Mod kode Claude yang menahan perintah shell berisiko.
- [Para-FR/claude-code-mods-fr](https://github.com/Para-FR/claude-code-mods-fr) - Dua Mod Claude untuk Claude Code: garde-du-corps.
- [Paradox07127/claude-utopia](https://github.com/Paradox07127/claude-utopia) - Mod Claude Code dengan telemetri agen, dashboard linimasa, peninjauan lintas…
- [paragpandyareal/swear-slap](https://github.com/paragpandyareal/swear-slap) - Memaki Claude Code dan tangan kartun membalas dengan tamparan.
- [paulpc2/claude-code-mods](https://github.com/paulpc2/claude-code-mods) - Mod Claude Code: usage-both menampilkan penggunaan 5 jam dan mingguan di atas…
- [philarete173/claude_mods](https://github.com/philarete173/claude_mods) - Panel samping statistik sesi langsung untuk tab Code aplikasi desktop Claude…
- [pkkid/claude-mods](https://github.com/pkkid/claude-mods) - Berbagai mod dan skill untuk pengaturan Claude Desktop saya.
- [pokhriyal-anmol/claude-token-window](https://github.com/pokhriyal-anmol/claude-token-window) - Claude Code mod: input and output tokens in your current 5-hour window, per…
- [pompeitech/affreschi](https://github.com/pompeitech/affreschi) - Claude Code mods for the pompeitech interface, themed on the Vesuvius design…
- [pradyb/claude-mods](https://github.com/pradyb/claude-mods) - Mod untuk Code Claude: safety-guard memblokir perintah destruktif dan akses…
- [qazwsx1121/Claude-Code-mods](https://github.com/qazwsx1121/Claude-Code-mods)
- [rafagomes/claude-code-mods](https://github.com/rafagomes/claude-code-mods) - Mod untuk Claude Code: plugin function-hook yang berjalan di dalam sesi…
- [rajib2k5/claude-market-watch](https://github.com/rajib2k5/claude-market-watch) - Mod Claude Code: ticker saham langsung, panel /quote, peringatan harga, pita…
- [RedRoosterKey/claude-code-ssh-usage-band](https://github.com/RedRoosterKey/claude-code-ssh-usage-band) - Mod Claude Code: host SSH, RAM, dan batas penggunaan 5j/7h dalam satu baris di…
- [RexWei1016/claude-project-progress](https://github.com/RexWei1016/claude-project-progress) - Claude Code mod: project progress pane from GitHub milestones, issues, PRs and…
- [Risdon8/push-ups](https://github.com/Risdon8/push-ups) - Mod Code Claude: push-up yang harus dilakukan saat Claude bekerja. Tanpa token.
- [robinade/claude-mods-ko](https://github.com/robinade/claude-mods-ko) - 6 mod Claude Code edisi Korea: pencatatan asumsi, bahasa sederhana, rak ide…
- [Rsclub22/claude-mods](https://github.com/Rsclub22/claude-mods)
- [RyanWeera/ai-router](https://github.com/RyanWeera/ai-router) - Mod Claude Code yang mengarahkan tugas ke model AI lain.
- [ryx2/slopshopper](https://github.com/ryx2/slopshopper) - Toko mod untuk Claude Code: mengambil mod dari GitHub, menampilkannya dalam…
- [saadk408/stepline](https://github.com/saadk408/stepline) - Mod Claude Code: mengubah rencana yang Anda setujui dalam mode plan menjadi…
- [saksham10arora-dotcom/awesome-claude-mods](https://github.com/saksham10arora-dotcom/awesome-claude-mods) - Daftar pilihan mod Claude Code. Setiap entri dikloning dan diperiksa dengan…
- [saksham10arora-dotcom/claude-frugal](https://github.com/saksham10arora-dotcom/claude-frugal) - Mode tanpa biaya: agen pembantu berjalan di Haiku, dan file serta log besar…
- [saksham10arora-dotcom/claude-lofi](https://github.com/saksham10arora-dotcom/claude-lofi) - Soundtrack lofi yang mengikuti sesi: tenang, fokus, mengalir, plus isyarat…
- [saksham10arora-dotcom/claude-teach-me](https://github.com/saksham10arora-dotcom/claude-teach-me) - Belajar sambil Claude melakukan coding: setelah giliran yang mengubah kode…
- [saksham10arora-dotcom/claude-vhs](https://github.com/saksham10arora-dotcom/claude-vhs) - Rekaman setiap edit yang dibuat Claude: putar ulang setiap perubahan saat…
- [samaphp/session-links](https://github.com/samaphp/session-links) - Setiap tautan yang disebutkan sesi Anda, dalam satu baris di atas prompt.
- [sawzhang/hello-mod](https://github.com/sawzhang/hello-mod) - Demo minimal fungsi hook Claude Code: panel token/biaya real-time di atas…
- [SentientNr6/claude-mods](https://github.com/SentientNr6/claude-mods) - A collection of plugins for Claude.
- [shahsanket2107/clarvis](https://github.com/shahsanket2107/clarvis) - Clarvis: an unofficial Avengers fan mod for Claude Code.
- [shawnbotha/claude-mods](https://github.com/shawnbotha/claude-mods) - Berbagai mod Claude.
- [shengyy/ccoverhead](https://github.com/shengyy/ccoverhead) - Mod Claude Code untuk konteks, pertumbuhan, kuota, cache, biaya native, dan…
- [shezis/claude-api-cost-compare](https://github.com/shezis/claude-api-cost-compare) - Claude Code mod: see what your session would cost on the Claude, OpenAI…
- [shezis/claude-model-router](https://github.com/shezis/claude-model-router) - Claude Code mod: route simple turns and subagents to cheaper models, never…
- [soulrocha/Claude-code-hero-journey](https://github.com/soulrocha/Claude-code-hero-journey) - 🦀 Mod HUD RPG yang nyaman untuk Claude Code.
- [steven-ngle/blade-of-commits](https://github.com/steven-ngle/blade-of-commits) - Pesan commit sekali klik untuk Claude Code dengan Malenia pixel-art yang menari.
- [stillgbx/still-mods](https://github.com/stillgbx/still-mods) - mod Claude Code.
- [su-record/claude-mods](https://github.com/su-record/claude-mods) - Mod Claude Code pribadi.
- [sushant-kum/ccstatus](https://github.com/sushant-kum/ccstatus) - A configurable status bar for Claude Code — band, native status line, pane, and…
- [SyntacticFlow/claude-mods](https://github.com/SyntacticFlow/claude-mods) - Plugin untuk Claude Code.
- [systemNEO/claude-code-mods](https://github.com/systemNEO/claude-code-mods) - Mod untuk Claude Code: delete-guard.
- [takiguchi-yu/claude-mods](https://github.com/takiguchi-yu/claude-mods) - Tempat penyimpanan mod Claude Code yang digunakan secara lokal.
- [Tanish-Dev/claude-usage-band](https://github.com/Tanish-Dev/claude-usage-band) - Mod Claude Code: lihat penggunaan paket Claude Anda.
- [tanwar-harsh/luff-crew-monitor](https://github.com/tanwar-harsh/luff-crew-monitor) - Mod Claude Code: panel kru langsung untuk setiap subagen.
- [TheBabaYaga/claude-session-flow](https://github.com/TheBabaYaga/claude-session-flow) - Mod Claude Code yang menampilkan sesi saat ini dalam sebuah panel: setiap…
- [theishandubey/claude-mods](https://github.com/theishandubey/claude-mods) - Marketplace plugin Claude Code untuk mod: plugin function-hooks yang menggambar…
- [timoncool/givememod](https://github.com/timoncool/givememod) - Mod Claude Code sesuai permintaan — skill yang membaca percakapan Anda dan…
- [tksunw/usage-reporter](https://github.com/tksunw/usage-reporter) - Mod Claude Code yang menulis batas penggunaan Claude Anda ke file yang dapat…
- [Tora29/my-claude-tools](https://github.com/Tora29/my-claude-tools) - Claude Mods を管理するrepo.
- [trietsch/claude-customizations](https://github.com/trietsch/claude-customizations) - Customizations for Claude Code.
- [Tum4s/sprout](https://github.com/Tum4s/sprout) - Mod Claude Code: sebuah band dan panel yang melacak subagen Anda, beserta file…
- [tusharck/mods-for-claude](https://github.com/tusharck/mods-for-claude) - Katalog terkurasi mod Claude Code, masing-masing dengan prompt salin-tempel…
- [ulttla/claude-mod-repo](https://github.com/ulttla/claude-mod-repo) - Claude Code mods: a context and plan-limit meter above the prompt, and auto-pin…
- [VaitaR/claude-code-limits](https://github.com/VaitaR/claude-code-limits) - Mod Claude Code: kuota 5h/7d, context window, sisa waktu prompt-cache, dan…
- [VAlux/claude-session-progress](https://github.com/VAlux/claude-session-progress) - Mod Claude Code: pita kemajuan animasi dan ringkasan penyelesaian untuk tugas…
- [Vansitha/clawd-watch](https://github.com/Vansitha/clawd-watch) - Tiga mod Claude Code kecil: lihat kapan subagen Anda selesai, antrekan pesan…
- [varunmoka7/image-shrinker](https://github.com/varunmoka7/image-shrinker) - Shrinks big screenshots before Claude reads them, so long sessions last longer…
- [varunmoka7/layman](https://github.com/varunmoka7/layman) - Katakan &quot;Saya tersesat&quot; dan Claude akan menjelaskan kembali balasan terakhirnya…
- [varunmoka7/next-steps-autopilot](https://github.com/varunmoka7/next-steps-autopilot) - Shows suggested next prompts above the prompt box.
- [varunmoka7/side-chat](https://github.com/varunmoka7/side-chat) - Ajukan pertanyaan sampingan kepada Claude di panel di sebelah pekerjaan Anda.
- [Victormartinsilva/MODS-CLAUDECODE](https://github.com/Victormartinsilva/MODS-CLAUDECODE) - Marketplace mod Claude Code dengan instalasi satu langkah dan panduan video…
- [vihrea1337/headroom](https://github.com/vihrea1337/headroom) - Hitung mundur batas laju dan prakiraan laju penggunaan untuk Claude Code.
- [vinkdc/roclaude](https://github.com/vinkdc/roclaude) - Lapisan keamanan Roblox Studio untuk Claude Code: audit RemoteEvent, undo…
- [Wasif-ZA/claude-mods](https://github.com/Wasif-ZA/claude-mods)
- [wipeer/claude-mods](https://github.com/wipeer/claude-mods) - Mod peningkat kenyamanan kecil untuk Claude Code.
- [wukonigcom/quanta-costa](https://github.com/wukonigcom/quanta-costa) - 🧾 Claude Code plugin: your Claude Pro/Max usage limits with a pace forecast…
- [xinhuagu/oh-my-claude-mods](https://github.com/xinhuagu/oh-my-claude-mods) - Mod untuk Claude Code. agent-crew: lihat subagen Anda bekerja sebagai kru…
- [yeonwooook/claude-study-latex](https://github.com/yeonwooook/claude-study-latex) - Inline and display LaTeX math, plus optional TikZ figures, in Claude.
- [YohanGarcia/agent-taskboard](https://github.com/YohanGarcia/agent-taskboard) - Papan tugas live untuk Claude Code: rencanakan sebelum membangun, ikuti setiap…
- [yuntaengtaeng/snitch](https://github.com/yuntaengtaeng/snitch) - Claude Code mod that reports which files Claude changed and why, live subagent…
- [zexion7873/usage-band](https://github.com/zexion7873/usage-band) - Pita selalu aktif di atas prompt Claude Code: pengisian konteks dan jendela…
- [zh10only1/claude-code-mods](https://github.com/zh10only1/claude-code-mods) - Mod Claude Code pribadi (marketplace plugin).
- [zwbao/zebra-mod](https://github.com/zwbao/zebra-mod) - zebra-mod: mod Claude Code yang mengubah Claude Code menjadi workstation…
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - Kumpulan pilihan sumber daya terbaik untuk agen-agen paling hebat, Claude Code…
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) - Plugin Claude Code yang menampilkan apa yang sedang terjadi — penggunaan…
- [sirmalloc/ccstatusline](https://github.com/sirmalloc/ccstatusline) - 🚀 Statusline yang indah dan sangat dapat disesuaikan untuk Claude Code CLI…
- [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) - Semua bagian system prompt Claude Code, 27 deskripsi alat bawaan, prompt…
- [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) - 45+ kiat untuk memaksimalkan Claude Code, dari dasar hingga tingkat lanjut…
- [op7418/guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill) - 🪧 Claude Code / skill Codex — buat carousel Xiaohongshu &amp; pasangan sampul…
- [Owloops/claude-powerline](https://github.com/Owloops/claude-powerline) - Powerline bergaya vim yang indah untuk Claude Code.
- [persiyanov/herdr-reviewr](https://github.com/persiyanov/herdr-reviewr) - Tinjau diff agen pengodean Anda di panel terminal dan kirim komentar baris…
- [uppinote20/claude-dashboard](https://github.com/uppinote20/claude-dashboard) - Plugin baris status komprehensif untuk Claude Code dengan penggunaan konteks…
- [stormzhang/token-tracker](https://github.com/stormzhang/token-tracker) - Pelacakan token lokal Claude Code &amp; Codex — bilah status.
- [starbaser/ccproxy](https://github.com/starbaser/ccproxy) - Buat mod untuk Claude Code: kaitkan permintaan apa pun, ubah respons apa pun…
- [NYCU-Chung/cc-statusline](https://github.com/NYCU-Chung/cc-statusline) - Dasbor baris status komprehensif untuk Claude Code — info sesi, bilah kuota…
- [gwittebolle/claude-carbon](https://github.com/gwittebolle/claude-carbon) - claude-carbon: lacak jejak karbon sesi Claude Code Anda.
- [AwesomeZun/CC-statusline](https://github.com/AwesomeZun/CC-statusline) - Statusline estetis untuk Claude Code oleh awesomejun.
- [a86582751/dsh-nexttavern](https://github.com/a86582751/dsh-nexttavern) - DeepSeek Harness 长篇角色扮演agent（DSH酒馆插件）：SillyTavern…
- [JohnnyVizz/claude-kit](https://github.com/JohnnyVizz/claude-kit) - Skill dan mod Claude Code publik.
- [escapeboy/claude-code-kit](https://github.com/escapeboy/claude-code-kit) - Skills, mod, subagen, hook, perintah garis miring, dan panduan untuk Claude…
- [mvalentsev/awesome-free-ai-coding](https://github.com/mvalentsev/awesome-free-ai-coding) - 📡 LLM APIs legal gratis &amp; agent coding — diperbarui sendiri, diverifikasi…
- [kylesnowschwartz/tail-claude-hud](https://github.com/kylesnowschwartz/tail-claude-hud) - Statusline terminal untuk sesi Claude Code.
- [arturogarrido/claudinho](https://github.com/arturogarrido/claudinho) - ⚽ Skor langsung football(soccer), jadwal pertandingan, dan klasemen untuk…
- [WormAlien/hub-cc](https://github.com/WormAlien/hub-cc) - Control plane lokal untuk Claude Code di Windows dan macOS: alihkan gateway LLM…
- [johncattrall/keymap-ai](https://github.com/johncattrall/keymap-ai) - Agent Skill yang mengubah agen coding Anda menjadi ahli firmware keyboard.
- [philoserf/claude-code-config](https://github.com/philoserf/claude-code-config) - Konfigurasi Claude Code pribadi yang diberi versi di dalam ~/.claude — agent…
- [ashafizullah/claude-code-muslim-mods](https://github.com/ashafizullah/claude-code-muslim-mods) - Waktu salat, tanggal Hijriah, adhkar, ayat harian, puasa sunnah, Ramadan…
- [livlign/ccbit](https://github.com/livlign/ccbit) - Baris status yang menyadari sesi untuk Claude Code.
- [benz-ai-x/dsh-research-graph](https://github.com/benz-ai-x/dsh-research-graph) - DSH Research Graph · 研图 — plugin DeepSeek Harness untuk topik riset, kartu…
- [GoSlowPoke168/claude-statusline](https://github.com/GoSlowPoke168/claude-statusline) - Two-line truecolor statusline for Claude Code.
- [pierrebelin/claude-code-toolkit](https://github.com/pierrebelin/claude-code-toolkit) - Perangkat Claude Code portabel untuk .NET DDD/Clean Architecture: agen TDD…
- [essedev/relay](https://github.com/essedev/relay) - Native macOS terminal for running many coding agents in parallel.
- [hoobnn/hoobnn-agent-mods](https://github.com/hoobnn/hoobnn-agent-mods) - Kumpulan plugin untuk Claude Code, pi, dan DeepSeek Harness: HUD bilah status…
- [jcdendrite/claude-config](https://github.com/jcdendrite/claude-config) - Konfigurasi global Claude Code yang portabel: skill khusus, hook PreToolUse…
- [JMOKSZ/dsh-lark-bridge](https://github.com/JMOKSZ/dsh-lark-bridge) - Feishu (Lark) entry point for DeepSeek Harness: drive dsh agents from a Feishu…
- [mutlumehmet/claude-plugins](https://github.com/mutlumehmet/claude-plugins) - Plugin Claude Code yang saya gunakan setiap hari: skills dan mod, dirapikan…
- [34823/tg-pane](https://github.com/34823/tg-pane) - Telegram di dalam Claude Code: baca chat dan channel dalam sebuah pane…
- [bbeygel/claude-code-tama](https://github.com/bbeygel/claude-code-tama) - Tama, a Tamagotchi companion mod for Claude Code.
- [codextde/godmode-bot](https://github.com/codextde/godmode-bot) - An AI teammate you can trust to get work done — Claude Code + browser-use + a…
- [darthmolen/hytale-claude-code-marketplace](https://github.com/darthmolen/hytale-claude-code-marketplace) - Marketplace untuk Plugin dan Skill Claude Code guna memfasilitasi mod game…
- [frsorrentino/fable-director](https://github.com/frsorrentino/fable-director) - Tata kelola token untuk Claude Code: model teratas mengarahkan, eksekusi…
- [hopp1395/cc-outline](https://github.com/hopp1395/cc-outline) - Penampil panel terpisah untuk Claude Code di Windows Terminal dan tmux: sesi…
- [jeancarlo-javier/claude-status-bar](https://github.com/jeancarlo-javier/claude-status-bar) - Statusline fase alur kerja langsung untuk Claude Code.
- [manson341349-beep/claude-desktop-mods](https://github.com/manson341349-beep/claude-desktop-mods) - Mod tidak resmi untuk tab Code Claude Desktop — usage-pet: pita penggunaan…
- [romnycristopher/claude-am-mods](https://github.com/romnycristopher/claude-am-mods) - Repositori untuk mod Awesome Media Claude Code.
- [rootstudioyaml/sprag](https://github.com/rootstudioyaml/sprag) - Pangkas pengeluaran token Claude Code &amp; Codex: merutekan lookup dan test run ke…
- [tedserbinski/claude-code-statusline](https://github.com/tedserbinski/claude-code-statusline) - Konfigurasi status line yang sederhana dan berguna untuk Claude Code.
- [aquahitt/claude-code-limit-alerts](https://github.com/aquahitt/claude-code-limit-alerts) - Peringatan batas penggunaan untuk Claude Code: notifikasi macOS, peringatan…
- [fbincon/claude-code-statusline](https://github.com/fbincon/claude-code-statusline) - Status line Claude Code yang dapat dikonfigurasi untuk Linux, WSL, Windows, dan…
- [JairoTorregrosa/claude-statusline](https://github.com/JairoTorregrosa/claude-statusline) - statusline Rust yang cepat untuk Claude Code — mengutamakan payload, git…
- [JohnnyTh/claude-status-bar](https://github.com/JohnnyTh/claude-status-bar) - Statusline Code Claude dengan bilah konteks, sparkline token &amp; pelacak biaya.
- [jsh135790/claude-code-capsule-panel](https://github.com/jsh135790/claude-code-capsule-panel) - Dashboard penggunaan live untuk Claude Code — rincian konteks, hit cache…
- [jv-k/claude-gauge](https://github.com/jv-k/claude-gauge) - Baris status dan baris token untuk Claude Code: konteks, penggunaan 5 jam dan…
- [kyllian330/claude-statusline](https://github.com/kyllian330/claude-statusline) - Menampilkan detail status utama Code Claude termasuk model, konteks, batas…
- [Ma1achy/claude-statusline](https://github.com/Ma1achy/claude-statusline) - status line Code Claude yang ramah dan dapat diutak-atik — bilah truecolor…
- [Obednal97/claude-statusline-kit](https://github.com/Obednal97/claude-statusline-kit) - Baris status Claude Code multi-baris: pengeluaran, konteks %, git, dan akun…
- [salvanya/claude_code_statusline](https://github.com/salvanya/claude_code_statusline) - Statusline dengan informasi berguna untuk claude code.
- [Screddyice/claude-code-harness](https://github.com/Screddyice/claude-code-harness) - Templat awal untuk mengatur ruang kerja Claude Code multi-perusahaan: templat…
- [tc3oliver/claude-team-kit](https://github.com/tc3oliver/claude-team-kit) - Tim agen native. Di bawah kendali. Batas pekerja yang ketat, visibilitas tim…
- [andkirby/claude-statusline](https://github.com/andkirby/claude-statusline) - Statusline kustom untuk Claude Code — bilah konteks dengan persentase…
- [AsyrafHussin/claude-code-statusline](https://github.com/AsyrafHussin/claude-code-statusline) - Baris status yang rapi dan informatif untuk Claude Code — menampilkan proyek…
- [bunderlog/claude-plugins](https://github.com/bunderlog/claude-plugins) - Marketplace plugin Claude Code dengan baloo: keahlian, agen yang memverifikasi…
- [ctfbio/claude-code-statusline](https://github.com/ctfbio/claude-code-statusline) - Statusline Claude Code tingkat profesional: durasi sesi, biaya multi-mata uang…
- [cvrt-gmbh/claude-statusline](https://github.com/cvrt-gmbh/claude-statusline) - Baris status yang memperhatikan langganan untuk Claude Code.
- [diegorv/koko.claude-statusline](https://github.com/diegorv/koko.claude-statusline) - Baris status terminal yang lengkap untuk Claude Code — Bun + TypeScript, tanpa…
- [ejklock/claude-mermaid-render](https://github.com/ejklock/claude-mermaid-render) - Plugin Claude Code yang menampilkan diagram Mermaid dengan indah dalam…
- [filtercoffeeway/claude-kit](https://github.com/filtercoffeeway/claude-kit) - Tools, skill, dan agent untuk Claude Code — dimulai dengan baris status yang…
- [giribboy77-arch/claude-statusline](https://github.com/giribboy77-arch/claude-statusline) - Claude Code 커스텀 상태줄 (모델, effort, 컨텍스트, 캐시, 사용량 한도).
- [Guidin9/claude-usage-footer](https://github.com/Guidin9/claude-usage-footer) - Plugin Claude Code: selalu lihat sisa batas penggunaan Claude 5 jam Anda di…
- [hardtomakeanadress/claude-code-deepseek-cost](https://github.com/hardtomakeanadress/claude-code-deepseek-cost) - Pengeluaran DeepSeek API yang sebenarnya untuk Claude Code: menetapkan ulang…
- [hieuvo/claude-imgview](https://github.com/hieuvo/claude-imgview) - Preview images inside Claude Code: hover a chip under a reply to pop the…
- [HiramAA/claude-desktop-mods](https://github.com/HiramAA/claude-desktop-mods) - Mod untuk Claude Code dan Claude Desktop di Windows dengan WSL: Docker dan…
- [ihororlovskyi/claude-statusline](https://github.com/ihororlovskyi/claude-statusline) - Baris status Claude Code dengan baris panel agen.
- [izahamyatim/claude-plugin-fizzy](https://github.com/izahamyatim/claude-plugin-fizzy) - 🚀 Sinkronkan todo Claude ke Fizzy.do untuk visibilitas tim secara langsung…
- [kernastra/claudecode](https://github.com/kernastra/claudecode) - Sekumpulan skill, mod, dan pengaya lain untuk Claude Code yang telah saya buat…
- [Kimmihappy793/claude-status-line](https://github.com/Kimmihappy793/claude-status-line) - Tampilkan bilah status terperinci berkode warna untuk Claude Code yang…
- [konnichiwab/claude-code-config](https://github.com/konnichiwab/claude-code-config) - Menu pengaturan, baris status, dan konfigurasi Claude Code.
- [mgstegmaier/claude-plugins](https://github.com/mgstegmaier/claude-plugins) - plugin claude, skill, mod, dan lainnya buatan sendiri tanpa kurungan.
- [msinclair-sudo/claude-code-setup](https://github.com/msinclair-sudo/claude-code-setup) - Penginstal lingkungan Claude Code: skills, statusline, hooks, permissions, dan…
- [OpenClawFarm/claude-statusline](https://github.com/OpenClawFarm/claude-statusline) - HUD-style status line for Claude Code — network health, TPS, context, quotas…
- [oshnilia/claude-plugins](https://github.com/oshnilia/claude-plugins) - Plugin dan mod Claude Code untuk memahami apa yang dilakukan Claude: format…
- [peaceinitiativemenhadenoil263/claude-status-bar](https://github.com/peaceinitiativemenhadenoil263/claude-status-bar) - Pantau status Claude Code dari bilah menu macOS dengan indikator waktu nyata…
- [pirncedark/afu-claude-statusline](https://github.com/pirncedark/afu-claude-statusline) - Bilah status multi-baris berwarna-warni untuk Claude Code.
- [rainyfei/claude-statusline-win](https://github.com/rainyfei/claude-statusline-win) - Baris status Claude Code untuk Windows (PowerShell): bilah penggunaan, hitung…
- [roy651/cc-plugins](https://github.com/roy651/cc-plugins) - Mod Bearings dan Glossary untuk Claude Code.
- [satoramoto/awesome-claude](https://github.com/satoramoto/awesome-claude) - Konfigurasi dan mod Claude Code, dengan kit komponen bersama, playground, dan…
- [thaiquangquy/claude.me](https://github.com/thaiquangquy/claude.me) - Konfigurasi Claude Code portabel: CLAUDE.md, settings, statusline, skills.
- [Tina0529/claude-session-radar](https://github.com/Tina0529/claude-session-radar) - Claude Code desktop (macOS) mod: click-to-jump session notifications…
- [Undone-drawknife974/claude-code-statusline](https://github.com/Undone-drawknife974/claude-code-statusline) - Lacak penggunaan konteks Claude Code, biaya sesi, dan reset batas laju dengan…
- [viplav-artha/claude-code-lessons](https://github.com/viplav-artha/claude-code-lessons) - A hands-on, verified deep-dive into Claude Code — CLAUDE.md, subagents, skills…
- [vladimir-ks/ai-agile-claude-code-statusline](https://github.com/vladimir-ks/ai-agile-claude-code-statusline) - Pelacakan biaya secara waktu nyata dan baris status pemantauan sesi untuk…
- [wmkeza/claude-plugins](https://github.com/wmkeza/claude-plugins) - wmkeza.
- [xinvxueyuan/cordis-plugin-secret](https://github.com/xinvxueyuan/cordis-plugin-secret) - Plugin Cordis / DeepSeek Harness — agen meminta rahasia kepada manusia dalam…
- [yacb2/claude-statusline](https://github.com/yacb2/claude-statusline) - Baris status Claude Code tiga baris: kedalaman konteks, batas laju lintas sesi…
- [YoniYon00/claude-feedback-rings](https://github.com/YoniYon00/claude-feedback-rings) - Context Rot Detector 2026 - Monitor Memori AI &amp; Batas Laju Proaktif untuk Agen…
- [zhuyansen/awesome-claude-code-hooks](https://github.com/zhuyansen/awesome-claude-code-hooks) - Hook, subagen, dan statusline Claude Code: koleksi dan alat sumber terbuka…
- [zoo3323/claude-statusline](https://github.com/zoo3323/claude-statusline) - Baris status Claude Code — pengukur penggunaan Claude/Codex yang tetap aktif…
- [tronschell/statusline.sh](https://github.com/tronschell/statusline.sh) - Builder visual untuk statusline Claude Code.
- [Magnus-Gille/tokenatlas](https://github.com/Magnus-Gille/tokenatlas) - Statusline Claude Code yang menampilkan penggunaan token waktu nyata dan…
- [ishuagrawal/clawdhouse](https://github.com/ishuagrawal/clawdhouse) - Mod untuk Claude Code: panel, pita, dan buddy yang dibangun di atas hook fungsi.
- [ashishsk93/baton-mods](https://github.com/ashishsk93/baton-mods) - Oper tugas antar sesi Claude Code Anda.
- [lahoramaker/mods-mcp](https://github.com/lahoramaker/mods-mcp) - Gunakan ini di server MCP untuk mengendalikan MODS, alat lintas platform…
- [Rimcat-JA/translate-ck3-mods](https://github.com/Rimcat-JA/translate-ck3-mods) - Skill Codex dan Claude Code untuk menerjemahkan mod CK3 dengan LLM lokal.
- [sTomerG/agent-kit](https://github.com/sTomerG/agent-kit) - Mod open-source dan ekstensi lainnya untuk Claude Code.
- [Apparux/cc-fusion](https://github.com/Apparux/cc-fusion) - Claude Code statusline: CCometixLine beauty + Claude HUD functionality.
- [charlie947/mod-maker](https://github.com/charlie947/mod-maker) - Mod Maker: temukan apa yang Anda minta kepada Claude Code berulang kali, dan…
- [Niedvin/ClauDiscobombulating](https://github.com/Niedvin/ClauDiscobombulating) - prompt-bar mod for Claude Code: usage limits, cache timer + alert, model/effort…

</details>

<a id="dsh-cordis"></a>

## Ekosistem plugin DSH dan Cordis

DeepSeek Harness dan Cordis mencapai tempat yang sama dari arah yang berbeda: bagi keduanya, plugin adalah mekanisme mod, sehingga plugin di sana setara dengan mod di sini.

<details>
<summary>🧵 <b><a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b> · ⭐74314 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Ringkasan

🌊 Agent harness orisinal. Terapkan swarm multipemain yang cerdas, koordinasikan alur kerja otonom, dan bangun sistem AI percakapan. Menampilkan memori adaptif, kecerdasan yang belajar mandiri, federasi, integrasi vector RAG, serta dukungan native untuk Claude Code / Codex / Hermes dan banyak lagi

<sub>🔧 Ditemukan digunakan dalam kode: `plugins/ruflo-swarm/README.md`, `plugins/ruflo-swarm/hooks/model/members.ts`, `v3/docs/validation/mod-api-coverage-2026-10.md`, `plugins/ruflo-swarm/hooks/register.ts`</sub>

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                 |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |
| Bahasa   | TypeScript                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **74314**  |
| Push terakhir            | 2026-10-11 |
| Pertama kali dicantumkan | 2026-10-04 |

🏷 `agentic-ai` · `agentic-framework` · `agentic-workflow` · `agents` · `ai-agents` · `ai-assistant` · `ai-skills` · `autonomous-agents`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/2ca82c9c9a7fca31.gif" width="100%" alt="ruvnet/ruflo animation"><br><sub>rekaman animasi</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/nexu-io/open-design">nexu-io/open-design</a></b> · ⭐100464 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

🎨 Plugin Desain DeepSeek Harness terbaik. Alternatif sumber terbuka untuk Claude Design. 🖥️ Aplikasi desktop local-first. 🖼️ Agen pemrograman Anda menjadi mesin desain: prototipe, landing page, dasbor, slide, gambar & video — file nyata, ekspor HTML/PDF/PPTX/MP4. 🤖 Claude Code / Codex / Cursor / DeepSeek Harness / OpenCode & 20+ CLI melalui BYOK.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | TypeScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **100464** |
| Push terakhir            | 2026-10-11 |
| Pertama kali dicantumkan | 2026-10-04 |

🏷 `agent-skills` · `ai-design` · `byok` · `claude-code-for-design` · `claude-design` · `codex-design` · `coding-agents` · `cursor-design`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nexu-io--open-design/a1049df34322d3ce.png" width="100%" alt="nexu-io/open-design screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/tt-a1i/archify">tt-a1i/archify</a></b> · ⭐81801 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

Ubah ide, rencana, atau basis kode apa pun menjadi diagram interaktif yang indah. Keahlian agen untuk Claude Code, Codex, dan lainnya.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | JavaScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **81801**  |
| Push terakhir            | 2026-10-11 |
| Pertama kali dicantumkan | 2026-10-04 |

🏷 `agent-skills` · `ai-agents` · `architecture-diagram` · `claude-code` · `claude-skills` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tt-a1i--archify/71b7d4b2427db202.png" width="100%" alt="tt-a1i/archify screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/morluto/rea">morluto/rea</a></b> · ⭐81717 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

Rekayasa balik apa pun dengan agen, mulai dari perilaku aplikasi hingga biner native.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | TypeScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **81717**  |
| Push terakhir            | 2026-10-11 |
| Pertama kali dicantumkan | 2026-10-05 |

🏷 `agent-skills` · `ai-agents` · `binary-analysis` · `claude-code` · `cli` · `codex` · `cordis` · `ctf`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--rea/f46ca8b1518ae39f.png" width="100%" alt="morluto/rea screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/esengine/DeepSeek-Reasonix">esengine/DeepSeek-Reasonix</a></b> · ⭐35757 · Go · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

Agen pemrograman yang andal untuk tugas rekayasa perangkat lunak yang kompleks.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | Go                                                                                            |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **35757**  |
| Push terakhir            | 2026-10-11 |
| Pertama kali dicantumkan | 2026-10-06 |

🏷 `agent` · `agent-framework` · `ai-agent` · `ai-coding` · `cli` · `coding-agent` · `deepseek` · `developer-tools`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/anywhere-labs/dsh-desktop">anywhere-labs/dsh-desktop</a></b> · ⭐30392 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

Solusi desktop modern yang dibuat untuk ekosistem plugin DeepSeek Harness (DSH). Segalanya adalah “plugin”, desktop itu sendiri juga adalah “plugin”.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | TypeScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **30392**  |
| Push terakhir            | 2026-10-10 |
| Pertama kali dicantumkan | 2026-10-10 |

🏷 `cordis` · `cordis-plugin` · `deepseek` · `deepseek-harness` · `desktop` · `dsh` · `dsh-plugin` · `dsh-plugin-desktop`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anywhere-labs--dsh-desktop/b72e79b4c3cadb81.png" width="100%" alt="anywhere-labs/dsh-desktop screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/titanwings/distilly">titanwings/distilly</a></b> · ⭐25484 · Python · 🔎 inferred · 18 天</summary>

##### 📝 Ringkasan

Distilly — Saring cara mereka berpikir menjadi Skills yang dapat digunakan kembali untuk Agen atau Bot apa pun. Sebelumnya Colleague Skill（原同事 Skill）.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | Python                                                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **25484**  |
| Push terakhir            | 2026-09-22 |
| Pertama kali dicantumkan | 2026-10-04 |

🏷 `agent-skills` · `agentic-ai` · `ai-agent` · `ai-agents` · `ai-assistants` · `ai-persona` · `claude-code` · `claude-skills`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/titanwings--distilly/bf54e387044cab88.png" width="100%" alt="titanwings/distilly screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/zhu1090093659/dsh-web">zhu1090093659/dsh-web</a></b> · ⭐8616 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

Ekosistem agregasi plugin web DeepSeek Harness (DSH) · Segalanya adalah plugin, didistribusikan melalui Creative Workshop｜｜Ekosistem Agregasi Plugin Web DeepSeek Harness (DSH) · Segalanya adalah plugin, didistribusikan melalui Creative Workshop

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | TypeScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **8616**   |
| Push terakhir            | 2026-10-10 |
| Pertama kali dicantumkan | 2026-10-04 |

🏷 `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-web` · `dsh-web-ui`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zhu1090093659--dsh-web/5153c3c61827ebb8.jpg" width="100%" alt="zhu1090093659/dsh-web screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/anbeime/skill">anbeime/skill</a></b> · ⭐7821 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

收录最全、更新最快的技能Skills商店：精选原创技能包（涵盖文档处理、内容创作、编程开发、机器学习、自动化工作流），全部打包好可直接安装使用！同时自动抓取GitHub上万个Skills项目，按分类、更新时间、Star数量整理。The most comprehensive and frequently updated AI Agent skill library, featuring curated skill packs across document processing, content creation, programming, machine learning, automated workflows, and many more domains.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | Python                                                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **7821**   |
| Push terakhir            | 2026-10-11 |
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `agent-skills` · `claude-skills` · `codex` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh-plugin` · `finance-skill`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/anbeime/skill/main/images/wechat-qr.jpg" width="100%" alt="anbeime/skill screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

<sub>Aset ditautkan langsung dari repositori upstream karena tidak ada lisensi yang mengizinkan redistribusi yang dinyatakan.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/MeteorNOX/DeepSeek-Balance-Whale-Widget">MeteorNOX/DeepSeek-Balance-Whale-Widget</a></b> · ⭐4456 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

DeepSeek Harness（DSH）一只住在 DSH 界面右下角的小鲸鱼娘，帮你盯着DeepSeek账户余额。QQ弹弹，支持拖拽吸附、左吸附翻转、数字滚动动画，随界面自动启用，建议直接喊来你的dsh安装

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | JavaScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **4456**   |
| Push terakhir            | 2026-10-11 |
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-plugin` · `dsh-plugins` · `floating-widget`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/meteornox--deepseek-balance-whale-widget/c17efbb95a7522ee.png" width="100%" alt="MeteorNOX/DeepSeek-Balance-Whale-Widget screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ccch1mneyyy/dsh-TUI">ccch1mneyyy/dsh-TUI</a></b> · ⭐4278 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

Plugin TUI rekomendasi teratas resmi DSH — performa tinggi, overhead rendah, paus piksel lucu, interaksi mouse yang mulus. Instal satu perintah via npm. / Plugin TUI yang menjadi rekomendasi utama resmi DSH, performa tinggi dan penggunaan rendah, paus piksel lucu, interaksi mouse mulus, instal satu perintah dengan npm

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | TypeScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **4278**   |
| Push terakhir            | 2026-10-11 |
| Pertama kali dicantumkan | 2026-10-10 |

🏷 `claude-code` · `coding-agent` · `deepseek` · `deepseek-harness` · `dsh-plugin` · `ink` · `react` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ccch1mneyyy--dsh-tui/18fd45f8f1eaca04.png" width="100%" alt="ccch1mneyyy/dsh-TUI screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xmanrui/dsh-im">xmanrui/dsh-im</a></b> · ⭐1788 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

Hubungkan bot IM ke DeepSeek Harness melalui kode QR atau kredensial (mendukung 飞书, 微信, 钉钉, 企业微信, QQ, Slack, Telegram, Discord, dan WhatsApp). Hubungkan bot IM ke DeepSeek Harness melalui kode QR atau kredensial (9 saluran).

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | JavaScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **1788**   |
| Push terakhir            | 2026-10-11 |
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `ai-agents` · `chatbot` · `cordis` · `deepseek` · `deepseek-harness` · `dingtalk-bot` · `discord-bot` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xmanrui--dsh-im/cba81787088f67af.jpg" width="100%" alt="xmanrui/dsh-im screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/anywhere-labs/Agents-Anywhere">anywhere-labs/Agents-Anywhere</a></b> · ⭐1557 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

跨设备的开源Agent工作台

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | TypeScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **1557**   |
| Push terakhir            | 2026-10-11 |
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `acp` · `agentclientprotocol` · `agents` · `claudecode` · `codex` · `codex-app` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/anywhere-labs/Agents-Anywhere/main/docs/images/readme-hero-zh.webp" width="100%" alt="anywhere-labs/Agents-Anywhere screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

<sub>Aset ditautkan langsung dari repositori upstream karena tidak ada lisensi yang mengizinkan redistribusi yang dinyatakan.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/EthanYoQ/AI-Novel-Writer">EthanYoQ/AI-Novel-Writer</a></b> · ⭐1397 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

Perangkat lunak penulisan novel AI: mengatur inspirasi, karakter, pembangunan dunia, kerangka, penulisan bab, peninjauan, dan revisi menjadi alur kerja yang dapat dikendalikan; menyediakan versi desktop Windows/macOS, serta mendukung model lokal dan daring. Perangkat Lunak Penulisan Novel AI: Mengatur inspirasi, karakter, pembangunan dunia, kerangka, penulisan bab, peninjauan, dan revisi menjadi alur kerja yang dapat dikendalikan. Menyediakan aplikasi desktop untuk Windows/macOS, integrasi Ollama, dan pratinjau plugin DeepSeek Harness (DSH).

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | TypeScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **1397**   |
| Push terakhir            | 2026-10-11 |
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `ai-writing` · `creative-writing` · `deepseek-harness` · `dsh-plugin` · `electron` · `fiction-writing` · `local-first` · `long-form-fiction`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ethanyoq--ai-novel-writer/97081b4a6febc6aa.png" width="100%" alt="EthanYoQ/AI-Novel-Writer screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/vshulcz/deja-vu">vshulcz/deja-vu</a></b> · ⭐1169 · Go · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

Memori untuk Claude Code, Codex, Cursor dan 38 agen coding lainnya, dibuat dari riwayat sesi yang sudah ada di disk Anda. Pencarian lokal, MCP dan hook, tanpa LLM, satu biner Go.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | Go                                                                                            |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **1169**   |
| Push terakhir            | 2026-10-10 |
| Pertama kali dicantumkan | 2026-10-04 |

🏷 `agent-memory` · `ai-memory` · `claude-code` · `claude-code-hooks` · `claude-code-plugins` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/8033ba54a9424c88.png" width="100%" alt="vshulcz/deja-vu screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/5fb930f1983f270b.gif" width="100%" alt="vshulcz/deja-vu animation"><br><sub>rekaman animasi</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/LivXue/dsh-plugin-shop">LivXue/dsh-plugin-shop</a></b> · ⭐1009 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

The most comprehensive DeepSeek Harness plugin market — refreshed daily, sourced across the Internet, reviewed before publishing.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | TypeScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **1009**   |
| Push terakhir            | 2026-10-11 |
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `agent` · `deepseek` · `deepseek-harness` · `deepseek-harness-plugin` · `dsh` · `dsh-plugin` · `harness`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/livxue--dsh-plugin-shop/0cd59c71bcc6f86e.png" width="100%" alt="LivXue/dsh-plugin-shop screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/myYangyunfan/dsh_desktop">myYangyunfan/dsh_desktop</a></b> · ⭐703 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

Klien desktop DeepSeek Harness (dsh) Windows - Node.js + dsh CLI terbundel, peluncuran sekali klik

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | JavaScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **703**    |
| Push terakhir            | 2026-10-11 |
| Pertama kali dicantumkan | 2026-10-10 |

🏷 `ai-agent` · `cordis` · `deepseek` · `deepseek-harness` · `desktop` · `desktop-app` · `dsh` · `dsh-desktop`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/myyangyunfan--dsh_desktop/822cff4e94634530.png" width="100%" alt="myYangyunfan/dsh_desktop screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/tingly-dev/tingly-box">tingly-dev/tingly-box</a></b> · ⭐351 · Go · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

Kecerdasan Anda, Diorkestrasi. Setiap pembuat. Setiap tim. Setiap agen. Untuk Semua Orang.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | Go                                                                                            |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **351**    |
| Push terakhir            | 2026-10-11 |
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `claude-code` · `dsh` · `dsh-plugin` · `gateway` · `golang` · `harness` · `llm` · `open-source`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tingly-dev--tingly-box/54666b3bdc5c6195.png" width="100%" alt="tingly-dev/tingly-box screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tingly-dev--tingly-box/0ef2aa2f5bc4239d.gif" width="100%" alt="tingly-dev/tingly-box animation"><br><sub>rekaman animasi</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/zhaoolee/notes">zhaoolee/notes</a></b> · ⭐277 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

开源版锤子便签，复刻锤科美学，一键Docker私有化部署，支持skill调用，支持dsh plugin，支持多租户，一键生成公众号格式，支持导出便签为图片

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | TypeScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **277**    |
| Push terakhir            | 2026-10-11 |
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `dsh-plugin` · `notes` · `smartisan`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zhaoolee--notes/ea0ae0d3af2430c1.png" width="100%" alt="zhaoolee/notes screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zhaoolee--notes/a1cc07be6396cb67.gif" width="100%" alt="zhaoolee/notes animation"><br><sub>rekaman animasi</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/acryldev/acryl">acryldev/acryl</a></b> · ⭐255 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

ACRYL - Agent Context Relay Yielding Lifecycles. Satu ruang kerja persisten, satu konteks kanonis, agen coding apa pun.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | TypeScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **255**    |
| Push terakhir            | 2026-10-11 |
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `acryl` · `agent-context-relay` · `agentic` · `agentic-ai` · `agentic-coding` · `agentic-development-environment` · `agentic-workflow` · `agentic-workflows`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/acryldev--acryl/47cfe6b23e87eea1.png" width="100%" alt="acryldev/acryl screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/luobosibing2/dsh-jev-plugin">luobosibing2/dsh-jev-plugin</a></b> · ⭐203 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

Plugin DeepSeek Harness (DSH) native yang mengintegrasikan TypeSafe Jev atau API Decision seperti luna sebagai lapisan keputusan System One untuk pemilihan, pengawasan, koreksi, dan persetujuan agen.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | JavaScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **203**    |
| Push terakhir            | 2026-10-10 |
| Pertama kali dicantumkan | 2026-10-10 |

🏷 `agent-harness` · `ai-agents` · `cordis` · `decisions-api` · `deepseek-harness` · `dsh` · `dsh-jev` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/luobosibing2--dsh-jev-plugin/e27235473aa310aa.png" width="100%" alt="luobosibing2/dsh-jev-plugin screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/KelaoHu/dsh-lowtide">KelaoHu/dsh-lowtide</a></b> · ⭐170 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

Time-shifting task delegation for DeepSeek Harness (dsh): plan tasks at leisure, they run unattended off-peak, come back to a report. Human-adjudicated, desktop + web.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | TypeScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **170**    |
| Push terakhir            | 2026-10-11 |
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `ai-agent` · `automation` · `batch-processing` · `cordis` · `deepseek` · `deepseek-harness` · `dsh-plugin` · `llm`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/kelaohu--dsh-lowtide/3d2509a82d1a3f11.png" width="100%" alt="KelaoHu/dsh-lowtide screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Totoro-qaq/dsh-plugin-bridge">Totoro-qaq/dsh-plugin-bridge</a></b> · ⭐165 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

Plugin DeepSeek Harness untuk migrasi sesi lintas preset yang dapat dipratinjau. Serah terima dengan skema tetap mempertahankan status, maksud model sumber, dan gambar yang belum terselesaikan; sesi asli tetap tidak tersentuh.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | JavaScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **165**    |
| Push terakhir            | 2026-10-11 |
| Pertama kali dicantumkan | 2026-10-10 |

🏷 `context-migration` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `preset-migration` · `session-migration`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/totoro-qaq--dsh-plugin-bridge/568de849cd2e9608.png" width="100%" alt="Totoro-qaq/dsh-plugin-bridge screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/totoro-qaq--dsh-plugin-bridge/b4a12cab0ba15f06.gif" width="100%" alt="Totoro-qaq/dsh-plugin-bridge animation"><br><sub>rekaman animasi</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/FeatherHunter/dsh-mattpocock-skills-deck">FeatherHunter/dsh-mattpocock-skills-deck</a></b> · ⭐132 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

安装即自带mattpocock/skills v1.3.1的27个工程与效率技能，无需手动装技能。400亿token打造本插件，在原始技能之上提供10倍的开发效率，也能帮助新手更快上手该技能套件。全力支持GitHub issue；Markdown为预览版；GitLab暂不支持。感谢您的使用和支持💗

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | JavaScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **132**    |
| Push terakhir            | 2026-10-11 |
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `agent` · `ai` · `claude` · `deepseek-harness` · `dsh` · `dsh-better-sidebar` · `dsh-plugin` · `github-issues`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/featherhunter--dsh-mattpocock-skills-deck/c4bd78003446c161.png" width="100%" alt="FeatherHunter/dsh-mattpocock-skills-deck screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/mexiaosqwq/dsh-web-mobile">mexiaosqwq/dsh-web-mobile</a></b> · ⭐131 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

DSH Web UI 移动端适配：窄屏好用，宽屏适用

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | JavaScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **131**    |
| Push terakhir            | 2026-10-11 |
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `deepseek-harness` · `dsh` · `dsh-plugin` · `mobile` · `mobile-ui` · `plugin` · `responsive` · `web-ui`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/mexiaosqwq--dsh-web-mobile/0edd0e3313404adf.jpg" width="100%" alt="mexiaosqwq/dsh-web-mobile screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Nwflower/dsh-claude-style">Nwflower/dsh-claude-style</a></b> · ⭐129 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

Tema desktop Claude Code untuk DeepSeek Harness｜ Tema desktop Claude Code yang dibuat untuk GUI web DeepSeek Harness

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | TypeScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **129**    |
| Push terakhir            | 2026-10-11 |
| Pertama kali dicantumkan | 2026-10-10 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-desktop` · `cordis` · `dark-mode` · `deepseek-harness` · `desktop-theme`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Nwflower/dsh-claude-style/master/docs/screenshots/claude-home-dark.png" width="100%" alt="Nwflower/dsh-claude-style screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Nwflower/dsh-claude-style/master/docs/gifs/idle.gif" width="100%" alt="Nwflower/dsh-claude-style animation"><br><sub>rekaman animasi</sub></td>
</tr></table>

<sub>Aset ditautkan langsung dari repositori upstream karena tidak ada lisensi yang mengizinkan redistribusi yang dinyatakan.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/morluto/flameox">morluto/flameox</a></b> · ⭐123 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

Bukti runtime yang membantu agen melacak, membuat profil, dan mengurangi hotspot dalam kode aplikasi dan native, kernel GPU, serta stack inferensi.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | Python                                                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **123**    |
| Push terakhir            | 2026-10-10 |
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `benchmarking` · `coding-agents` · `cordis` · `debugging` · `developer-tools` · `dsh` · `dsh-plugin` · `gpu-profiling`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--flameox/2914b7977590380e.png" width="100%" alt="morluto/flameox screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/WSK-build/DSHBox">WSK-build/DSHBox</a></b> · ⭐104 · Kotlin · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

DSHBox —  Run DeepSeek Harness locally on Android phones and tablets. It integrates and coordinates DSH, PRoot, WebView, Debian and Node.js, together with a terminal, a file manager and other tools, into a personal AI workbench. No root access, and no separate Termux installation.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | Kotlin                                                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **104**    |
| Push terakhir            | 2026-10-11 |
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `android` · `android-agent` · `android-app` · `android-application` · `deepseek-harness` · `deepseek-harness-android` · `deepseek-harness-mobile` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/wsk-build--dshbox/560dbaccacdf1506.png" width="100%" alt="WSK-build/DSHBox screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/mrRisega/dsh-remote">mrRisega/dsh-remote</a></b> · ⭐73 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

Kontrol jarak jauh DeepSeek Harness (dsh web) melalui Internet publik: dapatkan alamat terenkripsi khusus segera setelah instalasi, akses dari ponsel saat berada di luar, tanpa perlu berada di LAN/WiFi yang sama dan tanpa penetrasi intranet, dengan opsi membangun layanan sendiri. Kontrol jarak jauh DeepSeek Harness (dsh web) dari mana saja — URL publik terenkripsi, tanpa LAN.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | JavaScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **73**     |
| Push terakhir            | 2026-10-10 |
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `cordis` · `deepseek` · `deepseek-harness` · `dsh` · `dsh-plugin` · `mobile` · `mobile-web` · `pwa`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://cdn.jsdelivr.net/gh/mrRisega/dsh-remote@main/image/phone-mirror.png" width="100%" alt="mrRisega/dsh-remote screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

<sub>Aset ditautkan langsung dari repositori upstream karena tidak ada lisensi yang mengizinkan redistribusi yang dinyatakan.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/kukucaiCndy/Corum-Harness">kukucaiCndy/Corum-Harness</a></b> · ⭐63 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

Versi desktop Agent yang dibangun di atas inti Deepseek-Harness. Mewarisi semua kemampuan dasar dan melengkapi fitur terkait IDE.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | TypeScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **63**     |
| Push terakhir            | 2026-10-11 |
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `agent` · `agent-os` · `ai-agent` · `cordis` · `desktop-app` · `dsh` · `electron` · `harness`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/kukucaicndy--corum-harness/b8971b2831acec9e.png" width="100%" alt="kukucaiCndy/Corum-Harness screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/NoNameLeGo/dsh-catppuccin-theme">NoNameLeGo/dsh-catppuccin-theme</a></b> · ⭐58 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

DeepSeek Harness Web GUI 的 Catppuccin 主题插件：Latte / Frappé / Macchiato / Mocha 四种主题一键切换，内置可开关的玻璃质感（Glassmorphism）

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | TypeScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **58**     |
| Push terakhir            | 2026-10-11 |
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `catppuccin` · `deepseek-harness` · `dsh` · `dsh-plugin` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nonamelego--dsh-catppuccin-theme/c3d2472cfd609d68.png" width="100%" alt="NoNameLeGo/dsh-catppuccin-theme screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/whyihaveyou/dsh-suite">whyihaveyou/dsh-suite</a></b> · ⭐58 · HTML · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

Direktori plugin DeepSeek Harness yang terus diperbarui — diperbarui setiap jam, diuji kompatibilitasnya setiap hari, dengan toko plugin dan scaffolder di dalam aplikasi. Direktori aktif plugin DSH: diperbarui setiap jam, diuji kompatibilitasnya setiap hari, dengan toko plugin dan scaffolder bawaan.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | HTML                                                                                          |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **58**     |
| Push terakhir            | 2026-10-11 |
| Pertama kali dicantumkan | 2026-10-06 |

🏷 `agent-framework` · `awesome-list` · `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/whyihaveyou--dsh-suite/e9daf3bb6313ff1b.png" width="100%" alt="whyihaveyou/dsh-suite screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Contexera/dsh-agent-team">Contexera/dsh-agent-team</a></b> · ⭐57 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

dsh-agent-team menyediakan agen DeepSeek Harness yang tidak direset: Member yang persisten dengan memori, catatan, dan keterampilan mereka sendiri di berbagai sesi, pergantian, dan mulai ulang. Anda menentukan arah; agen berkoordinasi melalui Channels dan Tasks.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | TypeScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **57**     |
| Push terakhir            | 2026-10-11 |
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `agent-orchestration` · `agent-team` · `ai-agents` · `deepseek` · `deepseek-harness` · `dsh` · `dsh-plugin` · `multi-agent`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/contexera--dsh-agent-team/25f8cc5a2a3231a3.png" width="100%" alt="Contexera/dsh-agent-team screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/PolinniZhong/dsh-knit">PolinniZhong/dsh-knit</a></b> · ⭐53 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

Pengambilan konteks ruang kerja dan pelacakan siklus hidup yang sadar tugas untuk AI Coding Agent: menemukan, mengatur, dan terus melacak dokumen, kode, serta media yang paling relevan dengan tugas saat ini. Sepenuhnya lokal, tanpa pemanggilan model, tanpa jaringan. Pengambilan konteks ruang kerja dan pelacakan siklus hidup yang sadar tugas untuk agen coding AI. Temukan, atur, dan lacak konteks ruang kerja yang paling relevan dengan tugas yang sedang dikerjakan — secara lokal, deterministik, tanpa pemanggilan model, tanpa jaringan.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | JavaScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **53**     |
| Push terakhir            | 2026-10-11 |
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `agent-tools` · `ai-agent` · `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-better-sidebar`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/polinnizhong--dsh-knit/e98f690af54d1e8d.png" width="100%" alt="PolinniZhong/dsh-knit screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/polinnizhong--dsh-knit/338cb6ef3e90368c.gif" width="100%" alt="PolinniZhong/dsh-knit animation"><br><sub>rekaman animasi</sub></td>
</tr></table>

</details>

<details>
<summary><b>Lainnya dalam kategori ini</b> <sub>· 69</sub></summary>

- [kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net) - Pelindung sebelum eksekusi untuk agen pengodean AI.
- [hashgraph-online/awesome-ai-plugins](https://github.com/hashgraph-online/awesome-ai-plugins) - Daftar pilihan plugin AI terbaik yang luar biasa untuk asisten AI termasuk…
- [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) - Pasar plugin DSH / DSH Plugin Marketplace: jelajahi, instal, dan perbarui semua…
- [01Virex/dsh-status-rotator](https://github.com/01Virex/dsh-status-rotator) - 把 DSH Web 状态行换成 1063 条梗:打字机 + 炫彩渐变 + 弹幕 + 12 个主题词库包,设置页可视化编辑.
- [ymh0000123/dsh-theme-endfield](https://github.com/ymh0000123/dsh-theme-endfield) - Tema Web DSH bergaya situs resmi 终末地: latar kertas krem, teks hitam pekat…
- [arcships/rutis](https://github.com/arcships/rutis) - Runtime plugin untuk program yang terus berjalan — inti Rust, plugin TypeScript…
- [FeatherHunter/dsh-opencode-palette](https://github.com/FeatherHunter/dsh-opencode-palette) - 🎨 为长时间编程而生：38 款 opencode 护眼配色，一键换上 DSH | 38 eye-friendly opencode themes for…
- [kejixiaoliang/awesome-dsh-plugins](https://github.com/kejixiaoliang/awesome-dsh-plugins) - Direktori pilihan plugin DeepSeek Harness (DSH) — lebih dari 280 plugin…
- [universe-st/dsh-game-material-master](https://github.com/universe-st/dsh-game-material-master) - Plugin master aset game dsh. Terhubung ke model pembuatan gambar seedream dan…
- [Vncntvx/dsh-zotero](https://github.com/Vncntvx/dsh-zotero) - Toolkit Zotero untuk DeepSeek harness;
- [yi-yezhiqiu/dsh-prompt-market](https://github.com/yi-yezhiqiu/dsh-prompt-market) - DeepSeek Harness 提示词市场插件：对话框内一键浏览、搜索、收藏提示词，选中即写入输入框。零后端、免构建、数据只存本机.
- [KannaKuron/dsh-gitbash-shell](https://github.com/KannaKuron/dsh-gitbash-shell) - Plugin DSH: shell Git Bash untuk semua mode agen di Windows.
- [vritser/dsh-emacs](https://github.com/vritser/dsh-emacs) - An Emacs client for DeepSeek Harness.
- [NekroAI/nekro-nxt](https://github.com/NekroAI/nekro-nxt) - NekroNXT: sistem agen obrolan grup multi-platform berbasis DeepSeek Harness…
- [siweina/dsh-novel-writer](https://github.com/siweina/dsh-novel-writer) - Workbench penulisan lokal untuk penulis web novel berbahasa Mandarin (19 alat)…
- [dphmoblie/deepseek-harness-android](https://github.com/dphmoblie/deepseek-harness-android) - DeepSeek Harness versi Android dsh: mengintegrasikan lingkungan runtime Ubuntu…
- [HaoyueQin/dsh-usage-statistics-panel](https://github.com/HaoyueQin/dsh-usage-statistics-panel) - Plugin web DSH: statistik penggunaan token per hari dengan heatmap aktivitas…
- [awesome-deepseekharness/awesome-deepseek-harness](https://github.com/awesome-deepseekharness/awesome-deepseek-harness) - Community-curated DeepSeek Harness (dsh) plugins, tools, skills and learning…
- [FeatherHunter/dsh-im-companion](https://github.com/FeatherHunter/dsh-im-companion) - dsh-im-companion：以助理和家的概念增强 dsh-im——哪个工作区有助理在管、在不在线尽收眼底，搬家拖一下就行.
- [hyqhyq3/dsh-mcp-manager](https://github.com/hyqhyq3/dsh-mcp-manager) - Plugin pengelola server MCP untuk DeepSeek Harness: halaman Settings → MCP…
- [Wenaixi/dsh-superpower](https://github.com/Wenaixi/dsh-superpower) - Plugin DeepSeek Harness: 15 keterampilan rekayasa obra/superpowers, deskripsi…
- [harrylabsj/kiwi](https://github.com/harrylabsj/kiwi) - Runtime negosiasi perdagangan A2A + plugin DeepSeek Harness (dsh).
- [Imzl-zl/dsh-mcp-manager-ui](https://github.com/Imzl-zl/dsh-mcp-manager-ui) - UI manajemen server MCP untuk DeepSeek Harness Web — panel mengambang, impor…
- [liustack/pptwise](https://github.com/liustack/pptwise) - PowerPoint sungguhan, bukan HTML. Beri tahu AI Anda apa yang harus dibahas dan…
- [Wenaixi/dsh-ponytail](https://github.com/Wenaixi/dsh-ponytail) - Plugin DeepSeek Harness: mode senior malas DietrichGebert/ponytail dan port…
- [LAU-MARS/dsh-cad](https://github.com/LAU-MARS/dsh-cad) - deepseek harness 2D and 3D CAD plugin.
- [qinyre/dsh-plugin-capabilities](https://github.com/qinyre/dsh-plugin-capabilities) - 在 dsh 设置页管理技能与 MCP 服务器，支持从 Claude Code、Codex 导入.
- [billLiao/awesome-dsh-plugin](https://github.com/billLiao/awesome-dsh-plugin) - A curated list of plugins for DeepSeek Harness (dsh) — 精选 DeepSeek Harness 插件列表.
- [AmethystLuna/embedded-workbench](https://github.com/AmethystLuna/embedded-workbench) - Embedded C/C++ AI engineering plugin — firmware skills.
- [biedongbin/dsh-claude-compat](https://github.com/biedongbin/dsh-claude-compat) - DSH plugin: bridge Claude Code.
- [Ianzhyh/workbuddy-to-dsh](https://github.com/Ianzhyh/workbuddy-to-dsh) - Mengubah model yang sudah login di desktop WorkBuddy lokal.
- [Sivan757/dsh-agent-plugins-market](https://github.com/Sivan757/dsh-agent-plugins-market) - Pengelola skills, subagen, MCP, dan LSP lengkap untuk DeepSeek Harness (DSH)…
- [WTStarMark/dsh-plugin-mesh](https://github.com/WTStarMark/dsh-plugin-mesh) - 把带 dsh 系列 GitHub 标签的仓库，画成一张可交互的生态网络图.
- [MicroMilo/upstream-radar](https://github.com/MicroMilo/upstream-radar) - Pengujian kompatibilitas yang selalu aktif untuk plugin DeepSeek Harness: rilis…
- [ai-yukin/dsh-0-tools](https://github.com/ai-yukin/dsh-0-tools) - Toolkit tanpa biaya dan tanpa kerepotan untuk DeepSeek Harness (DSH): penyiapan…
- [1321928757/dsh-mysql](https://github.com/1321928757/dsh-mysql) - MySQL connector plugin for DeepSeek Harness: configure connections in settings…
- [mokuyoaxis/dsh-iris](https://github.com/mokuyoaxis/dsh-iris) - Media generation and visual understanding for DeepSeek Harness, with…
- [unStone/dsh-xray](https://github.com/unStone/dsh-xray) - X-ray untuk plugin DeepSeek Harness: kapabilitas yang dideklarasikan…
- [bonerush/dsh-obsidian-mem](https://github.com/bonerush/dsh-obsidian-mem) - Plugin host DeepSeek Harness yang menyimpan dokumen proyek dan memori jangka…
- [shenhuanageshei/dsh-team-link](https://github.com/shenhuanageshei/dsh-team-link) - Deep link sesi + ekspor sesi lengkap (markdown/JSON) + pesan lintas sesi yang…
- [wads-dev/dsh-live-voice](https://github.com/wads-dev/dsh-live-voice) - Percakapan suara local-first untuk DSH.
- [fan56/dsh-topics-memory](https://github.com/fan56/dsh-topics-memory) - Topic memory for LLM agents — edited, not accumulated: a topic keeps the…
- [KannaKuron/dsh-ide-git](https://github.com/KannaKuron/dsh-ide-git) - Plugin DSH: jendela tool Git setara IDE sebagai tab native dsh-better-sidebar…
- [lwmxiaobei/dsh-plugins](https://github.com/lwmxiaobei/dsh-plugins) - DeepSeek Harness 社区插件目录，自动汇总并基础校验 GitHub 插件，支持搜索、筛选、双语详情与最新版本安装命令复制.
- [cherrchen/dsh-plugin-multi-root-workspace](https://github.com/cherrchen/dsh-plugin-multi-root-workspace) - Workspace multi-folder: memungkinkan Agent DSH (DeepSeek Harness) tidak hanya…
- [godv61/dsh-task-engine](https://github.com/godv61/dsh-task-engine) - Plugin alur kerja engineering untuk DeepSeek Harness: tahap tugas, catatan…
- [liceses/dsh-cosplay](https://github.com/liceses/dsh-cosplay) - Plugin roleplay DSH: kartu karakter.
- [PerryLink/dsh-plugin-doctor](https://github.com/PerryLink/dsh-plugin-doctor) - Standar verifikasi tanpa dependensi untuk plugin DeepSeek Harness (dsh)…
- [viztor/dsh-opencode-patch](https://github.com/viztor/dsh-opencode-patch) - OpenCode di DeepSeek Harness — plugin DSH yang menjaga OpenCode Zen + model…
- [AI-Scarlett/DSH-Store](https://github.com/AI-Scarlett/DSH-Store) - DSH STORE — marketplace plugin pihak ketiga dan pengelola siklus hidup dengan…
- [anyuer678/dsh-logtimeline](https://github.com/anyuer678/dsh-logtimeline) - Query local log files with Chinese natural-language time expressions…
- [Atelyx/Atelyx](https://github.com/Atelyx/Atelyx) - Atelyx adalah meja kerja desktop yang dapat diperluas dan berpusat pada…
- [dsh-cc/dsh-cc](https://github.com/dsh-cc/dsh-cc) - Agen coding lengkap untuk DeepSeek Harness — alur kerja bergaya Claude Code…
- [fangwen9527/dsh-composer-ux](https://github.com/fangwen9527/dsh-composer-ux) - Plugin pengalaman input DSH Web: pergantian tombol kirim/baris baru, menu klik…
- [feely0208/deepwhale-desktop](https://github.com/feely0208/deepwhale-desktop) - 深鲸桌面 · 永久免费开源的 DeepSeek Harness 桌面壳（背景皮肤/桌面宠物/用量面板）.
- [KIDLi1412/dsh-session-cost](https://github.com/KIDLi1412/dsh-session-cost) - DSH web plugin: conversation status bar with per-session token cost estimate…
- [Luaphes/dsh-plugins-market](https://github.com/Luaphes/dsh-plugins-market) - DSH的插件创意市场来啦!～～～欢迎使用&amp;提供反馈！！DSH 插件创意市场 · DeepSeek Harness 插件发现与一键安装面板 全量嗅探官方…
- [Mzy123l/dsh-plugin-remote-access](https://github.com/Mzy123l/dsh-plugin-remote-access) - Menyediakan pintu masuk akses jarak jauh dengan 「segmen jaringan terbatas +…
- [sakanamaru/dsh-minato](https://github.com/sakanamaru/dsh-minato) - dsh-minato — rangkaian instalasi dan operasi pemeliharaan lokal versi komunitas…
- [tianyagk/dsh-tradewatcher](https://github.com/tianyagk/dsh-tradewatcher) - Plugin web DeepSeek Harness (DSH): tab sidebar market-dashboard untuk memantau…
- [xingzhen199186/dsh-mini-remote](https://github.com/xingzhen199186/dsh-mini-remote) - DSH 极简风远程移动端，提供「单帧」、「聊天」和「完整」三种模式，将注意力支配权交还给用户.
- [argszero/cordis-plugin-sandbox-grant-advisor](https://github.com/argszero/cordis-plugin-sandbox-grant-advisor) - Plugin Harness DeepSeek: mengubah kegagalan penyediaan ACL sandbox Windows…
- [argszero/cordis-plugin-empty-response-retry](https://github.com/argszero/cordis-plugin-empty-response-retry) - Membuat upaya model kosong tanpa atribusi dapat dicoba ulang, untuk satu celah…
- [denceee/dsh-everything-claude-code](https://github.com/denceee/dsh-everything-claude-code) - Mengadaptasi everything-claude-code ke DeepSeek Harness: 11 skill, preset agen…
- [eovidiu/cordis-ios](https://github.com/eovidiu/cordis-ios) - Plugins that clean up after themselves: a Swift 6 port of the cordis plugin…
- [Magica-Chen/dsh-preset-codex-claude](https://github.com/Magica-Chen/dsh-preset-codex-claude) - Preset agen DeepSeek Harness: Codex dan Claude Code sebagai subagen delegasi…
- [validation-engineering/cordis-verus](https://github.com/validation-engineering/cordis-verus) - Runtime plugin Rust dengan kernel siklus hidup yang diverifikasi Verus dan…
- [helloHupc/dsh-plugin-hub](https://github.com/helloHupc/dsh-plugin-hub) - DSH 插件聚合站:全网 DeepSeek Harness 插件聚合检索,多源自动去重分类,每小时刷新 |…
- [tellmewhattodo/dsh-serenity-plugin](https://github.com/tellmewhattodo/dsh-serenity-plugin) - dsh-serenity-plugin.

</details>

<a id="writing"></a>

## Tulisan, diskusi, dan video

Tulisan, diskusi, dan video tentang kemampuan mod.

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925102">Claude Code Mods</a></b> · ⭐6 · 👁️ observed · 9 天</summary>

##### 📝 Ringkasan

Tidak ada deskripsi upstream yang dipublikasikan.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Tulisan, diskusi, dan video`                                     |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Pertama kali dicantumkan | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50003222">What the Hell Are Claude Mods? [video]</a></b> · ⭐4 · 👁️ observed · 3 天</summary>

##### 📝 Ringkasan

Tidak ada deskripsi upstream yang dipublikasikan.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Tulisan, diskusi, dan video`                                     |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Pertama kali dicantumkan | 2026-10-09 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49999983">A Claude Code mod plays MIDI music when it works</a></b> · ⭐3 · 👁️ observed · 3 天</summary>

##### 📝 Ringkasan

Tidak ada deskripsi upstream yang dipublikasikan.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Tulisan, diskusi, dan video`                                     |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Pertama kali dicantumkan | 2026-10-08 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925800">Claude Code Mods: plugins may now modify deeper behavior</a></b> · ⭐3 · 👁️ observed · 9 天</summary>

##### 📝 Ringkasan

Tidak ada deskripsi upstream yang dipublikasikan.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Tulisan, diskusi, dan video`                                     |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Pertama kali dicantumkan | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49926243">Getting started with Claude Code mods</a></b> · ⭐3 · 👁️ observed · 9 天</summary>

##### 📝 Ringkasan

Tidak ada deskripsi upstream yang dipublikasikan.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Tulisan, diskusi, dan video`                                     |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Pertama kali dicantumkan | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49945600">Show HN: Terminal Gym – a Claude mod that makes you do pushups between prompts</a></b> · ⭐3 · 👁️ observed · 7 天</summary>

##### 📝 Ringkasan

Hai HN, saya membuat ini untuk diri sendiri dan ingin menjadikannya open-source. Masalahnya: saya ingin cara untuk mendapatkan pengingat di antara prompt karena saya sering menghabiskan waktu berjam-jam di terminal, terutama sekarang karena biasanya kami memproses begitu banyak agen secara paralel. Versi pertama adalah rep sederhana

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Tulisan, diskusi, dan video`                                     |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Pertama kali dicantumkan | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49971594">Terminal Steps: A Claude mod for a daily step goal, synced from Apple Health</a></b> · ⭐3 · 👁️ observed · 5 天</summary>

##### 📝 Ringkasan

Tidak ada deskripsi upstream yang dipublikasikan.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Tulisan, diskusi, dan video`                                     |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Pertama kali dicantumkan | 2026-10-06 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50024345">Agent-config&amp;Claude Code mods</a></b> · ⭐2 · 👁️ observed · 1 天</summary>

##### 📝 Ringkasan

Tidak ada deskripsi upstream yang dipublikasikan.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Tulisan, diskusi, dan video`                                     |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Pertama kali dicantumkan | 2026-10-10 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49940121">Getting started with Claude Code mods</a></b> · ⭐2 · 👁️ observed · 8 天</summary>

##### 📝 Ringkasan

Tidak ada deskripsi upstream yang dipublikasikan.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Tulisan, diskusi, dan video`                                     |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Pertama kali dicantumkan | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49927599">Pi-autoresearch ported to Claude Code 1:1 using the new mods API</a></b> · ⭐2 · 👁️ observed · 9 天</summary>

##### 📝 Ringkasan

Tidak ada deskripsi upstream yang dipublikasikan.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Tulisan, diskusi, dan video`                                     |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Pertama kali dicantumkan | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49934165">Show HN: What&#x27;s Agent Doing – a Claude Code UI mod that explains each step</a></b> · ⭐2 · 👁️ observed · 8 天</summary>

##### 📝 Ringkasan

Saya membuat ini karena dengan model coding terbaru, Claude masuk ke mode kerja mendalam dengan perintah-perintah yang tidak jelas sehingga saya tidak lagi tahu apa yang sedang dilakukannya. Ini adalah mod (plugin yang menggunakan hook fungsi baru milik Claude Code) yang menggambar satu baris di atas prompt: - langkah saat ini,

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Tulisan, diskusi, dan video`                                     |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Pertama kali dicantumkan | 2026-10-05 |

</details>

<a id="projects-by-implementation-language"></a>

## Proyek berdasarkan bahasa implementasi

Ekosistem ini terkonsentrasi pada Python dan TypeScript, tetapi client bertipe terus bermunculan dalam bahasa lain. Tabel ini dibuat dari entri-entri itu sendiri.

| Bahasa     | Entri | Contoh                                                                                                        |
| ---------- | ----- | ------------------------------------------------------------------------------------------------------------- |
| TypeScript | 385   | `anthropics/claude-code`, `anthropics/claude-code-action`, `hamzafer/claude-code-mods`                        |
| JavaScript | 80    | `Enc-hanted/dsh-pulse`, `X-C1811/dsh-web-search-plugin`, `karanb192/awesome-claude-code-mods`                 |
| Python     | 38    | `anthropics/claude-agent-sdk-python`, `anthropics/claude-code-security-review`, `alexgreensh/token-optimizer` |
| Shell      | 24    | `anthropics/claude-agent-sdk-typescript`, `0xDarkMatter/claude-mods`, `BeLazy167/claude-mods-skill`           |
| HTML       | 12    | `awss1i/assay`, `darrell-tw/darrelltw-mods`, `omarcevi/claudemods`                                            |
| Go         | 7     | `cephalofoil/kitt`, `kylesnowschwartz/tail-claude-hud`, `livlign/ccbit`                                       |
| Rust       | 5     | `persiyanov/herdr-reviewr`, `JairoTorregrosa/claude-statusline`, `OpenClawFarm/claude-statusline`             |
| Swift      | 4     | `bhargava-gumpula/claude-mods`, `essedev/relay`, `peaceinitiativemenhadenoil263/claude-status-bar`            |
| Kotlin     | 2     | `WSK-build/DSHBox`, `dphmoblie/deepseek-harness-android`                                                      |
| PowerShell | 2     | `GoSlowPoke168/claude-statusline`, `rainyfei/claude-statusline-win`                                           |
| C          | 1     | `reporails/arcade`                                                                                            |
| C#         | 1     | `sakanamaru/dsh-minato`                                                                                       |
| Emacs Lisp | 1     | `vritser/dsh-emacs`                                                                                           |
| MDX        | 1     | `jkf87/mod-guide`                                                                                             |

<sub>Hanya entri yang menyatakan bahasa yang dihitung. Entri dokumentasi dan diskusi tidak disertakan dalam tabel ini.</sub>

## Berkontribusi

Koreksi sangat diterima dan merupakan cara tercepat untuk meningkatkan daftar ini. Buka issue atau pull request jika suatu entri salah kategorisasi, salah tingkat, atau jika sebuah proyek keliru dikecualikan karena benturan nama — kategori terakhir itulah yang paling mungkin salah akibat filter otomatis.

---

<sub>Proyek komunitas independen. Tidak berafiliasi dengan, tidak didukung oleh, dan tidak ditinjau oleh Anthropic. Claude Code, Claude, dan Anthropic adalah merek dagang milik Anthropic. Perilaku produk dapat berubah tanpa pemberitahuan; verifikasi hal-hal penting terhadap dokumentasi resmi. Aset tetap menjadi milik proyek upstream masing-masing dan hanya direproduksi jika diizinkan oleh lisensinya.</sub>

<sub>Terakhir diperbarui · 2026-10-11T16:50:06+08:00</sub>
