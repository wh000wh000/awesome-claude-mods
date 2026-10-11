<p align="center">
  <img src="../assets/readme/hero.png" width="100%" alt="Mod Claude Keren">
</p>

<h1 align="center">Mod Claude Keren</h1>

<p align="center"><b>Indeks mod Claude Code, plugin, dan perubahan perilaku mendalam yang ditimbulkannya, dengan pemeringkatan berdasarkan bukti.</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-534-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="../LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
  <a href="https://wh000wh000.github.io/awesome-claude-mods/"><img src="https://img.shields.io/badge/site-searchable-1f6feb" alt="site"></a>
</p>

<p align="center"><sub><a href="../README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.pt-BR.md">Português</a> · <a href="README.ru.md">Русский</a> · <a href="README.it.md">Italiano</a> · <a href="README.ar.md">العربية</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.tr.md">Türkçe</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <b>Bahasa Indonesia</b> · <a href="README.pl.md">Polski</a> · <a href="README.nl.md">Nederlands</a> · <a href="README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **Indeks aktif** · Sinkronisasi terakhir: `2026-10-11T23:26:48+08:00` (UTC+8)
> · Entri: **534** · Ditambahkan pada pembaruan terbaru: **0** · Bahasa implementasi: **12**

<sub>Setiap entri di bawah dikumpulkan, difilter, dan diperiksa ulang secara otomatis. Tidak ada konten berbayar di sini.</sub>

<a id="featured"></a>

## Pilihan saat ini

<sub>Satu entri per kategori, diurutkan berdasarkan tingkat bukti dan jumlah bintang, lalu dihitung ulang setiap kali diperbarui. Ini adalah pemeringkatan, bukan dukungan; setiap pilihan tertaut ke kartu lengkapnya di bawah. Proyek yang memublikasikan tangkapan layar atau rekaman lebih diutamakan agar panel ini tetap visual.</sub>

<table>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action">
<b>🏛️ <a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b>
<sub>⭐9474 · TypeScript · ✅ official</sub>
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
<sub>⭐74336 · TypeScript · 👁️ observed</sub>
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
- [Resmi: repositori dan catatan rilis milik Anthropic sendiri](#resmi-repositori-dan-catatan-rilis-milik-anthropic-sendiri) — **14**
- [Mod: dibuat dengan kemampuan mod](#mod-dibuat-dengan-kemampuan-mod) — **408**
- [Ekosistem plugin DSH dan Cordis](#ekosistem-plugin-dsh-dan-cordis) — **101**
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
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></b> · ⭐150172 · TypeScript · ✅ official · 0 天</summary>

##### 📝 Ringkasan

Claude Code adalah alat pemrograman agentik yang berjalan di terminal Anda, memahami basis kode Anda, dan membantu Anda memprogram lebih cepat dengan menjalankan tugas rutin, menjelaskan kode yang kompleks, serta menangani alur kerja git — semuanya melalui perintah bahasa alami.

<sub>🔧 Ditemukan digunakan dalam kode: `feed.xml`, `mods/diff/README.md`</sub>

##### 📌 Fakta dasar

| Bidang   | Nilai                                                         |
| -------- | ------------------------------------------------------------- |
| Kategori | `Resmi: repositori dan catatan rilis milik Anthropic sendiri` |
| Bukti    | `dipublikasikan oleh Anthropic sendiri`                       |
| Bahasa   | TypeScript                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **150172** |
| Push terakhir            | 2026-10-10 |
| Pertama kali dicantumkan | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b> · ⭐9474 · TypeScript · ✅ official · 1 天</summary>

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
| Bintang                  | **9474**   |
| Push terakhir            | 2026-10-09 |
| Pertama kali dicantumkan | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-python">anthropics/claude-agent-sdk-python</a></b> · ⭐8248 · Python · ✅ official · 1 天</summary>

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
| Bintang                  | **8248**   |
| Push terakhir            | 2026-10-09 |
| Pertama kali dicantumkan | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-security-review">anthropics/claude-code-security-review</a></b> · ⭐6342 · Python · ✅ official · 241 天</summary>

##### 📝 Ringkasan

Action tinjauan keamanan bertenaga AI GitHub menggunakan Claude untuk menganalisis perubahan kode terhadap kerentanan keamanan.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                         |
| -------- | ------------------------------------------------------------- |
| Kategori | `Resmi: repositori dan catatan rilis milik Anthropic sendiri` |
| Bukti    | `dipublikasikan oleh Anthropic sendiri`                       |
| Bahasa   | Python                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **6342**   |
| Push terakhir            | 2026-02-11 |
| Pertama kali dicantumkan | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-typescript">anthropics/claude-agent-sdk-typescript</a></b> · ⭐1797 · Shell · ✅ official · 1 天</summary>

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
| Bintang                  | **1797**   |
| Push terakhir            | 2026-10-09 |
| Pertama kali dicantumkan | 2026-10-11 |

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
| Pertama kali dicantumkan | 2026-10-11 |

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
<summary><b>Lainnya dalam kategori ini</b> <sub>· 2</sub></summary>

- [Claude Code 2.1.295 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Menambahkan `$.ui.notify` untuk mod: memunculkan notifikasi native melalui…
- [Claude Code 2.1.296 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Memperbaiki Esc atau interupsi selama hook `UserPromptSubmit` atau hook…

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
<summary>🧩 <b><a href="https://github.com/karanb192/awesome-claude-code-mods">karanb192/awesome-claude-code-mods</a></b> · ⭐486 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Ringkasan

Katalog komunitas mod Claude Code publik (function hooks), dipindai dari GitHub beserta informasi tentang apa yang dapat dibaca, ditulis, dijalankan, atau dikirim melalui jaringan oleh setiap mod. Jelajahi https://mods.aidojo.si/

<sub>🔧 Ditemukan digunakan dalam kode: `data/seeds.txt`, `data/duplicates.txt`, `README.md`, `data/repos.txt`</sub>

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Mod: dibuat dengan kemampuan mod`                                |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |
| Bahasa   | JavaScript                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **486**    |
| Push terakhir            | 2026-10-11 |
| Pertama kali dicantumkan | 2026-10-04 |

🏷 `anthropic` · `awesome` · `awesome-list` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/aqua5230/usage">aqua5230/usage</a></b> · ⭐338 · Python · 👁️ observed · 0 天</summary>

##### 📝 Ringkasan

macOS menu bar & Windows tray app pinning Claude Code, Codex, Antigravity & Grok CLI quota, burn rate, and cost to your screen. Local-first, no LLM API calls. HTML reports, 14 themes.

<sub>🔧 Ditemukan digunakan dalam kode: `claude_pane/usage-dash/hooks/register.tsx`</sub>

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Mod: dibuat dengan kemampuan mod`                                |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |
| Bahasa   | Python                                                            |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **338**    |
| Push terakhir            | 2026-10-11 |
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `ai-tools` · `anthropic` · `catppuccin` · `claude` · `claude-code` · `codex` · `cost-tracking` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aqua5230--usage/6cfdc327f46c7392.png" width="100%" alt="aqua5230/usage screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aqua5230--usage/75f19ddf3cb83f7d.gif" width="100%" alt="aqua5230/usage animation"><br><sub>rekaman animasi</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hamzafer/claude-code-mods">hamzafer/claude-code-mods</a></b> · ⭐186 · TypeScript · 👁️ observed · 2 天</summary>

##### 📝 Ringkasan

Claude Code mods: plugins built on hooks that add live lines above the prompt, guards, panes and games. Context bar, usage meter, Codex review watch, Markdown preview, Spotify now playing and more.

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
| Bintang                  | **186**    |
| Push terakhir            | 2026-10-09 |
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugins` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/c683a5d95e78d920.png" width="100%" alt="hamzafer/claude-code-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/0b4dc7c7692bd024.gif" width="100%" alt="hamzafer/claude-code-mods animation"><br><sub>rekaman animasi</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/cache-tax">karanb192/cache-tax</a></b> · ⭐132 · TypeScript · 👁️ observed · 7 天</summary>

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
| Bintang                  | **132**    |
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
| Push terakhir            | 2026-10-11 |
| Pertama kali dicantumkan | 2026-10-10 |

🏷 `agentic-ai` · `ai-agents` · `browser-automation` · `claude-code` · `claude-code-mod` · `cli` · `code-generation` · `developer-tools`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hellosverre/claude-skins">hellosverre/claude-skins</a></b> · ⭐96 · TypeScript · 👁️ observed · 0 天</summary>

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
| Bintang                  | **96**     |
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

A collection of claude code mods

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
| Pertama kali dicantumkan | 2026-10-11 |

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NahumLitvin/prismantis">NahumLitvin/prismantis</a></b> · ⭐75 · TypeScript · 👁️ observed · 0 天</summary>

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
| Bintang                  | **75**     |
| Push terakhir            | 2026-10-11 |
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `markdown` · `mermaid` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/f6e44059e77434b4.png" width="100%" alt="NahumLitvin/prismantis screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/9df6377936558503.gif" width="100%" alt="NahumLitvin/prismantis animation"><br><sub>rekaman animasi</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/scasella/claude-flightdeck">scasella/claude-flightdeck</a></b> · ⭐66 · TypeScript · 👁️ observed · 8 天</summary>

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
| Bintang                  | **66**     |
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
<summary>🧩 <b><a href="https://github.com/darrell-tw/darrelltw-mods">darrell-tw/darrelltw-mods</a></b> · ⭐65 · HTML · 👁️ observed · 5 天</summary>

##### 📝 Ringkasan

Claude Code mods by Darrell Wang — bands above the prompt, zero model tokens. 台股／美股看板 + more to come.

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
| Pertama kali dicantumkan | 2026-10-11 |

</details>

<details>
<summary>🧩 <b><a href="https://github.com/0xDarkMatter/claude-mods">0xDarkMatter/claude-mods</a></b> · ⭐59 · Shell · 👁️ observed · 4 天</summary>

##### 📝 Ringkasan

Expert skills, agents, commands, rules, hooks & output styles for Claude Code — session continuity + modern CLI tooling for real-world dev workflows

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
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `agent-skills` · `ai-agents` · `ai-tools` · `anthropic` · `claude` · `claude-code` · `claude-skills` · `developer-tools`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/zycck/claude-mods">zycck/claude-mods</a></b> · ⭐46 · TypeScript · 👁️ observed · 2 天</summary>

##### 📝 Ringkasan

Claude Code mods: live plan progress bars above the prompt

<sub>🔧 Ditemukan digunakan dalam kode: `README.md`</sub>

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
| Pertama kali dicantumkan | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/49f09d1600b02c7a.gif" width="100%" alt="zycck/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/25f4230871cb30f6.gif" width="100%" alt="zycck/claude-mods animation"><br><sub>rekaman animasi · <a href="https://raw.githubusercontent.com/zycck/claude-mods/main/media/plan-progress.mp4">Buka video</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/iamumeransari/claude-show-your-work">iamumeransari/claude-show-your-work</a></b> · ⭐44 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Ringkasan

Claude Code menampilkan gambar dan memutar video langsung di terminal Anda: tangkapan layar, rekaman Playwright, dan QA sebelum/sesudah yang disinkronkan. Ghostty & kitty.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Mod: dibuat dengan kemampuan mod`                                |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |
| Bahasa   | TypeScript                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **44**     |
| Push terakhir            | 2026-10-11 |
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/iamumeransari--claude-show-your-work/7a0af2143a7dfd15.jpg" width="100%" alt="iamumeransari/claude-show-your-work screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
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
<summary>🧩 <b><a href="https://github.com/dgokcin/claude-pokemon-mod">dgokcin/claude-pokemon-mod</a></b> · ⭐25 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Ringkasan

A pixel Pokémon that lives above the prompt in Claude Code

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Mod: dibuat dengan kemampuan mod`                                |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |
| Bahasa   | JavaScript                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **25**     |
| Push terakhir            | 2026-10-11 |
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `claude-code-mod` · `claude-code-mods`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/dgokcin/claude-pokemon-mod/main/gifs/pikachu-haiku.gif" width="100%" alt="dgokcin/claude-pokemon-mod screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/dgokcin/claude-pokemon-mod/main/gifs/pikachu-haiku.gif" width="100%" alt="dgokcin/claude-pokemon-mod animation"><br><sub>rekaman animasi</sub></td>
</tr></table>

<sub>Aset ditautkan langsung dari repositori upstream karena tidak ada lisensi yang mengizinkan redistribusi yang dinyatakan.</sub>

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
| Push terakhir            | 2026-10-11 |
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `developer-tools` · `eye-candy` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/52396333a085f3d5.gif" width="100%" alt="NovusEdge/glowup screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/4905ed24c2c755ad.gif" width="100%" alt="NovusEdge/glowup animation"><br><sub>rekaman animasi</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/artemnovichkov/xcode-mods">artemnovichkov/xcode-mods</a></b> · ⭐20 · TypeScript · 👁️ observed · 9 天</summary>

##### 📝 Ringkasan

Xcode's build, tests, console and SwiftUI previews inside Claude Code

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
| Pertama kali dicantumkan | 2026-10-11 |

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

Claude Code mods: 21 styles and a full set of features you turn on when you need them, for the terminal and the desktop app. · 一键为 Claude 换上新风格，并提供一整套按需开启的功能。

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
| Pertama kali dicantumkan | 2026-10-11 |

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

Ten Claude Code mods, beginner guides, creation prompts, safe demos, and a build-your-own template.

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
| Pertama kali dicantumkan | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/promptadvisers/claude-mods-starter-kit/main/assets/cover.jpg" width="100%" alt="promptadvisers/claude-mods-starter-kit screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

<sub>Aset ditautkan langsung dari repositori upstream karena tidak ada lisensi yang mengizinkan redistribusi yang dinyatakan.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/JetsonChan/CC-Usage-Band">JetsonChan/CC-Usage-Band</a></b> · ⭐13 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Ringkasan

Claude Code mods: usage-band shows your 5h/7d limits, context window and cache hit rate above the prompt

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Mod: dibuat dengan kemampuan mod`                                |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |
| Bahasa   | TypeScript                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **13**     |
| Push terakhir            | 2026-10-03 |
| Pertama kali dicantumkan | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/jetsonchan--cc-usage-band/e9d74f1543fa7c25.png" width="100%" alt="JetsonChan/CC-Usage-Band screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/aieo-product/claude_qamods">aieo-product/claude_qamods</a></b> · ⭐11 · TypeScript · 👁️ observed · 4 天</summary>

##### 📝 Ringkasan

Claude Code mods that make Claude's questions easier to read and answer (qa-guide).

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
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `askuserquestion` · `claude-code` · `claude-code-plugin` · `mod`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aieo-product--claude_qamods/e57e7bee7cb5c173.png" width="100%" alt="aieo-product/claude_qamods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aieo-product--claude_qamods/eb4a2b15bdb5ff3e.gif" width="100%" alt="aieo-product/claude_qamods animation"><br><sub>rekaman animasi · <a href="https://raw.githubusercontent.com/aieo-product/claude_qamods/main/docs/media/qa-guide-pv-16x9.mp4">Buka video</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/augiefra/claude-mods">augiefra/claude-mods</a></b> · ⭐11 · JavaScript · 👁️ observed · 0 天</summary>

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
| Push terakhir            | 2026-10-11 |
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

Ten open-source mods for Claude Code: live panes, bands, status lines and tool-call guards. Burn meter, launch codes, session wrapped, boss fight, code pet and more.

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
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mods` · `claude-code-plugins`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/onewave-ai--claude-code-mods/763e0352f43b1cbc.png" width="100%" alt="OneWave-AI/claude-code-mods screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-computer-use-threads">promptadvisers/claude-mods-computer-use-threads</a></b> · ⭐11 · JavaScript · 👁️ observed · 6 天</summary>

##### 📝 Ringkasan

Two Claude Code mods: Codex computer-use bridge and coordinated Claude sessions. Source, build prompts, setup and tests.

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
| Pertama kali dicantumkan | 2026-10-11 |

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

A UI around your Claude Code and Codex terminals that your agents build, so the only model in your head is yours.

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
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `ai-coding` · `ai-tools` · `browser-terminal` · `claude-code` · `codex` · `coding-agent` · `developer-tools` · `devtools`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/deepsteve--deepsteve/adee5ea71e2e3289.png" width="100%" alt="deepsteve/deepsteve screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/ersinkoc/claude-mods">ersinkoc/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 1 天</summary>

##### 📝 Ringkasan

KOZMOS — live, visual mods for Claude Code (CLI + desktop): bands above the prompt, sidebars, status ticker, companions, guards and sound.

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
| Pertama kali dicantumkan | 2026-10-11 |

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

Six Claude Code mods in one plugin (Token Weather, Cache Keeper, Wait What, Prompt Queue, Snake, Blast Radius) with per-mod switches, plus a mods-vs-hooks report.

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
| Pertama kali dicantumkan | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/az9713--claude-mod-pack/7889282e792ed11e.png" width="100%" alt="az9713/claude-mod-pack screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/devbrother2024/devbrothers-mods">devbrother2024/devbrothers-mods</a></b> · ⭐7 · TypeScript · 👁️ observed · 7 天</summary>

##### 📝 Ringkasan

개발동생의 Claude Code mods 모음. 택시 팩: 미터기, 내비, 과속 단속 카메라, 블랙박스

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
| Pertama kali dicantumkan | 2026-10-11 |

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

Claude Code mods: 像素螃蟹用量面板 usage-hud + 终端里可点的 HTML 链接和一键复制代码卡片 html-shelf

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
| Pertama kali dicantumkan | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ronanworks--claude-code-mods/c6d323f2b976bd4e.gif" width="100%" alt="ronanworks/claude-code-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ronanworks--claude-code-mods/c6d323f2b976bd4e.gif" width="100%" alt="ronanworks/claude-code-mods animation"><br><sub>rekaman animasi</sub></td>
</tr></table>

</details>

<details>
<summary><b>Lainnya dalam kategori ini</b> <sub>· 374</sub></summary>

- [whyashthakker/awesome-claude-code-mods](https://github.com/whyashthakker/awesome-claude-code-mods) - Collection of 100+ mods you can use with Claude Code.
- [karanb192/claude-code-mods](https://github.com/karanb192/claude-code-mods) - Mod Claude dan alat untuk membangunnya: skill builder, lalu mod.
- [ucsandman/claude-harness](https://github.com/ucsandman/claude-harness) - The Claude Code harness I run every day, published under this name since day…
- [kagamiurayama/claude-code-roof-mod](https://github.com/kagamiurayama/claude-code-roof-mod) - 用 Claude Mods 给 Claude Code 换屋顶：不改二进制，把系统提示和英文提醒换成你自己的字（2.1.287+）.
- [nateherkai/claude-code-mods](https://github.com/nateherkai/claude-code-mods) - Four Claude Code mods: Cache Keeper, Recording Mode, Goal Meter, and Collision…
- [Hangghost/learning-hacker-claude-mod](https://github.com/Hangghost/learning-hacker-claude-mod) - Learning Hacker 的 Claude Code mods：把 agent 的運作畫成看得懂的東西.
- [kakha13/claude](https://github.com/kakha13/claude) - Claude Code mods that fix and translate your prompts before Claude reads them.
- [rashedInt32/glass](https://github.com/rashedInt32/glass) - Tampilan aplikasi desktop untuk transkrip terminal Claude Code, sebagai mod.
- [xuanji86/claude-agentpane](https://github.com/xuanji86/claude-agentpane) - Panel samping untuk Claude Code: subagen yang dijalankan sesi, apa yang sedang…
- [AgriciDaniel/claude-mods-brain](https://github.com/AgriciDaniel/claude-mods-brain) - Source-cited Obsidian knowledge base about Claude Code mods: how they work, how…
- [letswritetw/claude-mod-open-todos](https://github.com/letswritetw/claude-mod-open-todos) - Panel bilah samping Claude Desktop (tab Code): mencantumkan semua tugas…
- [nekyialabs/claude-code-toolkit](https://github.com/nekyialabs/claude-code-toolkit) - Claude Code mods and skills from Nekyia Labs, built and used daily by AIs…
- [BeLazy167/claude-mods-skill](https://github.com/BeLazy167/claude-mods-skill) - Skill that teaches Claude Code agents to build Claude Mods.
- [letswritetw/claude-mod-token-usage](https://github.com/letswritetw/claude-mod-token-usage) - Bilah penggunaan di atas kotak input Claude Desktop (tab Code): kuota 5j / 7h…
- [omarcevi/claudemods](https://github.com/omarcevi/claudemods) - Mod, plugin &amp; skill Claude komunitas, dapat diinstal dari satu marketplace.
- [KilimcininKorOglu/claude-code-mods](https://github.com/KilimcininKorOglu/claude-code-mods) - Claude Mods (function-hooks plugins) for Claude Code.
- [baselane-sh/mods-catalog](https://github.com/baselane-sh/mods-catalog) - The Baselane mods gallery: Claude Code mods, checked and pinned.
- [eighteyes/cactus](https://github.com/eighteyes/cactus) - Antrean keputusan CLI/TUI untuk manusia yang bekerja dengan agen percakapan.
- [xuanji86/claude-statuspane](https://github.com/xuanji86/claude-statuspane) - Kartu status mengambang untuk Claude Code—model, konteks, batas laju, biaya…
- [arasovic/claude-code-mods](https://github.com/arasovic/claude-code-mods) - Mod untuk Claude Code: plugin hook fungsi yang menambahkan panel langsung dan…
- [danyuchn/claude-mods](https://github.com/danyuchn/claude-mods) - Claude Code mods: screen-guard masks names and secrets while you screen-share;
- [helenkwok/gsd-status-mod](https://github.com/helenkwok/gsd-status-mod) - Dashboard GSD langsung untuk Claude Code: peta jalan, pohon agen dengan…
- [magidandrew/cx](https://github.com/magidandrew/cx) - Claude Code Extensions. Unlock the full power of Claude.
- [markneonin/paneline](https://github.com/markneonin/paneline) - Mod (plugin) Claude Code yang menambahkan panel samping dengan tab Activity…
- [mishgoldenberg/claude-mods](https://github.com/mishgoldenberg/claude-mods) - Panels, guardrails and quality-of-life mods for Claude Code: context, usage…
- [ofeklevy11/claude-code-hud](https://github.com/ofeklevy11/claude-code-hud) - Two Claude Code mods above the prompt box: context-window meter, 5-hour limit…
- [VedantAndhale/claude-pro-kit](https://github.com/VedantAndhale/claude-pro-kit) - Make the Claude Pro plan last longer: Claude Code mods for an exact usage HUD…
- [xuanji86/claude-mdview](https://github.com/xuanji86/claude-mdview) - Baca file markdown yang diberi nama oleh Claude Code, tampilkan di samping…
- [leopiney/wolfbud-claude-mod](https://github.com/leopiney/wolfbud-claude-mod) - Rekan kerja suara untuk Claude Code. Bicarakan berbagai hal dengan serigala 3D…
- [borabiricik/claude-mods](https://github.com/borabiricik/claude-mods) - Claude Code mods: typing-speed, a live typing speedometer with per-prompt stats.
- [charimsma/dopa-mode](https://github.com/charimsma/dopa-mode) - Kembang api untuk Claude Code: setiap penekanan tombol, pemanggilan tool…
- [DrishtantKaushal/AwesomeClaudeCodeMods](https://github.com/DrishtantKaushal/AwesomeClaudeCodeMods) - Discover Claude Code mods, plugins and extensions with animated demos, category…
- [galElmalah/claude-mods](https://github.com/galElmalah/claude-mods) - Claude Code mod: mermaid diagrams drawn inline in the transcript.
- [ha-ptt0601/cc-mods](https://github.com/ha-ptt0601/cc-mods) - Mod Claude Code kecil (plugin function-hook): session-switcher dan lainnya.
- [hahmjuntae/claude-mods-image-preview](https://github.com/hahmjuntae/claude-mods-image-preview) - Claude Code mod: pasted image thumbnails above the prompt, in any terminal.
- [Jhonatan-de-Souza/ClaudeMods](https://github.com/Jhonatan-de-Souza/ClaudeMods) - Claude Code mods: Claude Tools menu, Zen mode, terminal themes, effort and mode…
- [LeeHigma0201/claude-code-mods](https://github.com/LeeHigma0201/claude-code-mods) - Claude Code mods: mod-scout.
- [Nongfsq/frank-claude-cockpit](https://github.com/Nongfsq/frank-claude-cockpit) - Two Claude Code mods for running many sessions at once: a context card above…
- [ayagmar/claude-modmgr](https://github.com/ayagmar/claude-modmgr) - modmgr: discover, inspect, toggle and update Claude Code mods.
- [Boom-Vitt/boombignose-mods](https://github.com/Boom-Vitt/boombignose-mods) - Claude Code mods: context bar, agents panel, PDPA blur.
- [claude-code-mods/best-claude-code-mods](https://github.com/claude-code-mods/best-claude-code-mods) - Best Claude Code Mods: hand-picked, validated, pinned.
- [dominicrico/jev-router](https://github.com/dominicrico/jev-router) - Plugin Claude Code: perutean model Claude otomatis.
- [FynnXland/fynn-mods](https://github.com/FynnXland/fynn-mods) - Enam mod untuk Claude Code: maskot Clawd animasi, bar batas penggunaan dan…
- [GoneTone/cc-askpass](https://github.com/GoneTone/cc-askpass) - Mod Claude Code yang memungkinkan Claude menjalankan perintah yang memerlukan…
- [Hula-Hoop-AI/supermods](https://github.com/Hula-Hoop-AI/supermods) - A marketplace of mods for Claude Code: a step debugger for the agent loop, git…
- [ice-lfernandes/claude-code-mods](https://github.com/ice-lfernandes/claude-code-mods) - Enam mod Claude Code: batas rencana dan konteks di atas prompt, pelatih daftar…
- [mertkayacs/ultramod](https://github.com/mertkayacs/ultramod) - Paket mod serba ada terbaik untuk Claude Code: batas penggunaan dan HUD…
- [mthli/cc-shorts](https://github.com/mthli/cc-shorts) - Putar YouTube Shorts di Claude Code Anda 💃.
- [NarenDawar/narens-claude-toolkit](https://github.com/NarenDawar/narens-claude-toolkit) - Toolkit Claude milik Naren: skills, mods, dan servers MCP untuk Claude Code.
- [neteye-platform/cc-split-diff-view](https://github.com/neteye-platform/cc-split-diff-view) - Mod Claude Code yang menggambar perbedaan Edit dan Write dalam dua kolom…
- [raresmun/claude-mods](https://github.com/raresmun/claude-mods) - Mods for Claude Code: Clawd, a tiny pixel mascot who acts out what Claude is…
- [reporails/arcade](https://github.com/reporails/arcade) - Classic desktop games as Claude Code mods, played in a pane while Claude works.
- [testy-cool/awesome-claude-code-mods](https://github.com/testy-cool/awesome-claude-code-mods) - Daftar pilihan mod Claude Code yang dapat dipasang sebagai pasar plugin: tema…
- [xsyetopz/dotclaude](https://github.com/xsyetopz/dotclaude) - Plugin Claude Code yang sangat berpendirian, dirancang oleh seorang Rustacean…
- [yash-gadodia/claude-mods](https://github.com/yash-gadodia/claude-mods) - Claude Code mods that keep an agent honest — function hooks that guard scope…
- [alexcz-a11y/claude-mods](https://github.com/alexcz-a11y/claude-mods) - My collection of Claude Code mods, one mod per directory.
- [ArgonQQ/sipp](https://github.com/ArgonQQ/sipp) - 💧 Pengingat air pasif-agresif untuk Claude Code. Nol token, penilaian maksimum.
- [chenyuxiaojin/cyxj-notch](https://github.com/chenyuxiaojin/cyxj-notch) - Dasbor notch macOS untuk Claude Code: batas penggunaan, sesi terbuka, progres…
- [DarioFontanel/claude-code-mods](https://github.com/DarioFontanel/claude-code-mods) - Mod per Claude Code: barra della prompt cache, prossimi passi, bottoni rapidi e…
- [dougcunha/claude-mods](https://github.com/dougcunha/claude-mods) - Mods for Claude Code: panes, commands and hooks built with the plugin…
- [ElirazKed/claude-code-pr-watch](https://github.com/ElirazKed/claude-code-pr-watch) - Mod Claude Code: panel langsung berisi PR GitHub yang dibuka atau didorong oleh…
- [estruyf/claude-stats-mod](https://github.com/estruyf/claude-stats-mod) - Mod Claude Code yang menggambar batas penggunaan dan pengeluaran Anda di bilah…
- [herman925/925-cc-plugins](https://github.com/herman925/925-cc-plugins) - Mod Claude Code milik Herman (marketplace herman-mods).
- [homieyangg/claude-code-mods](https://github.com/homieyangg/claude-code-mods) - Claude Code mods: progress bars for plans, a ledger of what Claude left…
- [i-harsha-reddy/naruto-mod](https://github.com/i-harsha-reddy/naruto-mod) - Pendamping Naruto bergaya pixel-art untuk Claude Code: 20 ninja, 60 jutsu…
- [lorenzh/rabe](https://github.com/lorenzh/rabe) - Lihat apa yang dijalankan Claude Code di latar belakang: subagen, pekerjaan…
- [MankhongGarden/claude-code-mods-field-notes](https://github.com/MankhongGarden/claude-code-mods-field-notes) - Catatan lapangan hari pertama tentang mod Claude Code di Windows: bilah bahan…
- [MichaelP17/claude-mods](https://github.com/MichaelP17/claude-mods) - Mods I made and personally use in my Claude Code setup.
- [patitow/claude-mod-cost-visibility](https://github.com/patitow/claude-mod-cost-visibility) - Mod Claude Code: meter biaya langsung, konteks &amp; kuota paket di atas prompt.
- [rbartoli/agent-usage-guard](https://github.com/rbartoli/agent-usage-guard) - Mod Claude Code yang menahan fan-out subagent, prompt konteks berat, dan loop…
- [schreibse/claude-code-mods](https://github.com/schreibse/claude-code-mods) - code-mods for claude.
- [shimo4228/harness-scope](https://github.com/shimo4228/harness-scope) - Mod Claude Code yang mengaktifkan atau menonaktifkan skill, agen, aturan, dan…
- [simplecore-inc/claude-mods](https://github.com/simplecore-inc/claude-mods) - Plugin Claude Code (mod): beralih di antara beberapa akun Claude, memantau…
- [Singh-AP/awesome-claude-mods](https://github.com/Singh-AP/awesome-claude-mods) - 🧩 Mod Claude Code yang telah diuji dan dapat dipasang dengan satu perintah…
- [Sma1lboy/claude-mods](https://github.com/Sma1lboy/claude-mods) - Mods for Claude Code: plugins built on function hooks.
- [smukh/roll-credits](https://github.com/smukh/roll-credits) - Kredit bergaya film untuk sesi coding Anda.
- [Szotasz/claude-mods](https://github.com/Szotasz/claude-mods) - Saját Claude Code mod-ok pluginpiaca.
- [theonly1me/claude-code-mods](https://github.com/theonly1me/claude-code-mods) - A bunch of claude code mods built by me.
- [timoncool/givememod](https://github.com/timoncool/givememod) - Mod Code Claude sesuai permintaan — keterampilan yang membaca percakapan Anda…
- [Unayung/cc-mods-youtube](https://github.com/Unayung/cc-mods-youtube) - A cliamp-backed YouTube player inside Claude Code (Claude Code mod).
- [VladLeus/claude-mods](https://github.com/VladLeus/claude-mods) - Claude Code mods: agent-fleet dashboard and autopilot (local-mods marketplace).
- [vynnlee/mods](https://github.com/vynnlee/mods) - Claude Code mods by vynnlee. One folder per mod, installable from one…
- [yodakeisuke/claudelingo](https://github.com/yodakeisuke/claudelingo) - Pelajari bahasa asing sambil bekerja dengan Claude Code.
- [alaturqua/tower-mods](https://github.com/alaturqua/tower-mods) - Mod Claude Code untuk menjalankan banyak sesi di banyak repo dari satu menara…
- [alexlifexyz/p3c-guard](https://github.com/alexlifexyz/p3c-guard) - Saat Agen menulis Java, kode yang melanggar aturan Alibaba Java (p3c) tidak…
- [andrewbakercloudscale/claude-code-cost-sidebar](https://github.com/andrewbakercloudscale/claude-code-cost-sidebar) - Sidebar biaya, token, dan penggunaan konteks live untuk Claude Code: mod yang…
- [aosmcleod/next-up-mod](https://github.com/aosmcleod/next-up-mod) - Mod Claude Code: backlog tindak lanjut yang disarankan Claude di seluruh sesi…
- [BjoernSchotte/ccmod-amp](https://github.com/BjoernSchotte/ccmod-amp) - Radio internet di dalam Claude Code: sidebar cliamp, pemutar mini, favorit…
- [Bocskay-Botond/claude-code-mods](https://github.com/Bocskay-Botond/claude-code-mods) - Mod Claude Code yang menyenangkan dan berguna: makhluk piksel di atas prompt…
- [CalvoSeko/claude-factory-mod](https://github.com/CalvoSeko/claude-factory-mod) - agent-graph: a Claude Code mod for designing and running graphs of agents…
- [chrisluo5311/squad-chat](https://github.com/chrisluo5311/squad-chat) - Claude sedang memasak. Chat dengan skuad Anda.
- [darkomarijaan/nexus-mod](https://github.com/darkomarijaan/nexus-mod) - Mod Claude Code all-in-one: HUD langsung, perlindungan keamanan.
- [DarkVelours/claude-code-galactic-battle](https://github.com/DarkVelours/claude-code-galactic-battle) - Pertempuran luar angkasa di atas prompt Claude Code saat sedang bekerja.
- [Davron2004/slash-coverage](https://github.com/Davron2004/slash-coverage) - Lihat file mana yang ada dalam konteks setiap agen Claude Code, dan seberapa…
- [dbroadhurst/claude-mod-todos](https://github.com/dbroadhurst/claude-mod-todos) - Claude Code mod: a pane summarising the remaining todos, with Do, Chat, Defer…
- [drakulavich/cogload](https://github.com/drakulavich/cogload) - Tetap tenang. Termometer untuk hari-hari Claude Code Anda: setiap jam diberi…
- [EgonLeitner/dashband](https://github.com/EgonLeitner/dashband) - Batas prompt cache, konteks, dan rencana untuk Claude Code sekilas, di footer…
- [enhki/claude-mods](https://github.com/enhki/claude-mods) - Mod kecil Claude Code untuk terminal dan aplikasi desktop.
- [ewxgwy1987/claude-code-progress-board](https://github.com/ewxgwy1987/claude-code-progress-board) - Mod Claude Code: panel kemajuan untuk tugas, subagen, proses alur kerja…
- [ewxgwy1987/claude-code-session-toc](https://github.com/ewxgwy1987/claude-code-session-toc) - Mod Claude Code: daftar isi seluruh sesi yang dapat diklik dan memiliki stempel…
- [ewxgwy1987/claude-code-usage-meter](https://github.com/ewxgwy1987/claude-code-usage-meter) - Mod Claude Code: batas laju rencana, isi konteks, biaya sesi, dan token per…
- [Exdenta/ambient-spanish](https://github.com/Exdenta/ambient-spanish) - Skill + mod Claude CLI yang menambahkan kata-kata Spanyol ke balasan agen.
- [FrBmt-BIGetNouf/alarum-claude-mod](https://github.com/FrBmt-BIGetNouf/alarum-claude-mod) - Your Alarum events above Claude Code.
- [FrBmt-BIGetNouf/floatee-claude-mod](https://github.com/FrBmt-BIGetNouf/floatee-claude-mod) - Backlog Floatee Anda di atas prompt Claude Code: jalankan, pandu, dan centang…
- [gonzalonicolasr/claude-code-nerv](https://github.com/gonzalonicolasr/claude-code-nerv) - Bilah samping bergaya Evangelion untuk Claude Code: konteks, kuota, aktivitas…
- [gregdotca/ccmod-the-machine](https://github.com/gregdotca/ccmod-the-machine) - Mod kode Claude yang menata ulang tampilannya menjadi The Machine dari Person…
- [HyunjunJeon/claude-workflow-mods](https://github.com/HyunjunJeon/claude-workflow-mods) - dag-workflow: mod Claude Code untuk alur kerja DAG subagent yang wajib dan…
- [ibrahimkobeissy/claude-mods](https://github.com/ibrahimkobeissy/claude-mods) - Mod sumber terbuka untuk Claude Code: panel, baris status, toast, penjaga alat…
- [jonyfs/astrolabe](https://github.com/jonyfs/astrolabe) - 🧭 Mod Claude Code: status sesi, kemajuan Spec Kit live, dan tata kelola jendela…
- [kongyo2/context-view](https://github.com/kongyo2/context-view) - Jendela konteks sebagai satu baris di atas prompt, digambar seperti meter milik…
- [kyledarling-io/claude-code-desktop-hud](https://github.com/kyledarling-io/claude-code-desktop-hud) - HUD tugas langsung untuk Claude Code Desktop: strip di atas prompt saat Claude…
- [m4cd4r4/clear-resume](https://github.com/m4cd4r4/clear-resume) - Plugin gratis dan open-source untuk Claude Code.
- [maxsoldev/pstash](https://github.com/maxsoldev/pstash) - Stash prompts for later and pop them back into Claude Code.
- [Mechazawa/claude-inline-images](https://github.com/Mechazawa/claude-inline-images) - Mod Claude Code yang menampilkan gambar secara inline di Ghostty dan kitty.
- [meganemura/pull-request-pane](https://github.com/meganemura/pull-request-pane) - Mod Claude yang menampilkan pull request GitHub milik sesi dalam panel di…
- [nkapila6/sfx-gen](https://github.com/nkapila6/sfx-gen) - Claude Code mod: generate sound effects from text prompts with a local Stable…
- [NotRedFox/NotRedFoxs-Claude-skills](https://github.com/NotRedFox/NotRedFoxs-Claude-skills) - Keahlian Claude Code: pemeriksa fakta dokumen, auditor kode, log memori bug…
- [pepperonas/loc-today](https://github.com/pepperonas/loc-today) - Mod Claude Code: baris kode hari ini oleh Claude — baru, diedit, dihapus — di…
- [pepperonas/path-links](https://github.com/pepperonas/path-links) - Mod Claude Code: jalur yang dapat diklik dalam balasan — klik folder untuk…
- [rezzminator/buddy](https://github.com/rezzminator/buddy) - Plugin teman Claude Code: pendamping ASCII di atas prompt Anda yang mengingat…
- [roma-vibe/jev-governor](https://github.com/roma-vibe/jev-governor) - Mod Claude Code: perutean model/upaya yang dipandu Jev, pemadatan konteks…
- [samfrmr/barmkin-mod](https://github.com/samfrmr/barmkin-mod) - Mod Code Claude: lapisan keamanan untuk Code Claude — penyamaran rahasia…
- [Sennjen/claude-sdlc](https://github.com/Sennjen/claude-sdlc) - Plugin dan mod Claude Code: SDLC AI-native.
- [SeongGwangJu/k-mods](https://github.com/SeongGwangJu/k-mods) - Koleksi mod Claude Code yang luar biasa | Koleksi mod Claude Code.
- [soulrocha/Claude-code-hero-journey](https://github.com/soulrocha/Claude-code-hero-journey) - 🦀 Mod HUD RPG yang nyaman untuk Claude Code.
- [Spardutti/claude-mods](https://github.com/Spardutti/claude-mods) - Claude Code mods: live panels and hooks for daily work.
- [tanujarun/it-speaks](https://github.com/tanujarun/it-speaks) - It Speaks: mod Claude Code yang membacakan balasan Claude dan prompt Anda saat…
- [timoncool/slapbox](https://github.com/timoncool/slapbox) - 🍑 Pukul Claude saat ia melakukan kesalahan — mod pelepas stres untuk Claude…
- [TroyJLorents-GH/mod-squad](https://github.com/TroyJLorents-GH/mod-squad) - Mod Claude Code: plugin kecil untuk panel langsung, pengaturan perutean model…
- [valeryia-piatrova/token-hamster](https://github.com/valeryia-piatrova/token-hamster) - 🐹 Mod &amp; plugin Claude Code: monitor penggunaan, pelacak token &amp; baris status.
- [y-hirakaw/claude-code-mods](https://github.com/y-hirakaw/claude-code-mods) - Mod Claude Code. touch-map: lihat berkas mana yang dicantumkan, dibaca, diedit…
- [yuntaengtaeng/snitch](https://github.com/yuntaengtaeng/snitch) - Mod Code Claude yang melaporkan berkas mana yang diubah Claude dan alasannya…
- [alan-oliv/claude-mods](https://github.com/alan-oliv/claude-mods) - Mod Code Claude: kartu statistik sesi di atas perintah.
- [Aler1x/claude-cat](https://github.com/Aler1x/claude-cat) - Kucing braille animasi di atas prompt Claude Code.
- [alinaqi/mixture-of-models-claude-mod](https://github.com/alinaqi/mixture-of-models-claude-mod) - Mod Claude Code: mengarahkan pekerjaan ringan ke GLM/Kimi melalui Claude Code…
- [aloki-alok/omni-cat](https://github.com/aloki-alok/omni-cat) - Kucing piksel di atas prompt Code Claude Anda yang menjalankan panggilan uji…
- [ambervdberg/smartcompact](https://github.com/ambervdberg/smartcompact) - Mod Claude Code yang memilih waktu yang tepat untuk melakukan pemadatan agar…
- [an80sPWNstar/claude-mods](https://github.com/an80sPWNstar/claude-mods) - Mod Claude untuk Claude Code: token-meter.
- [anderson-spider/claude-mods](https://github.com/anderson-spider/claude-mods) - Marketplace plugin Code Claude oleh anderson-spider.
- [andrej-kolic/claude-mods](https://github.com/andrej-kolic/claude-mods) - General-purpose mods for Claude Code: bands, panes, toasts and hooks.
- [Ashley-Pettit/lgtm-flash](https://github.com/Ashley-Pettit/lgtm-flash) - Kapal LGTM Lines berlayar melewati setelah setiap perubahan kode — mod Code…
- [Ashley-Pettit/villager-hp](https://github.com/Ashley-Pettit/villager-hp) - Batas penggunaan Claude Anda sebagai kartu kesehatan penduduk desa animasi…
- [Atanur/deskfit](https://github.com/Atanur/deskfit) - Latihan singkat saat Claude bekerja: target harian, streak, badge, dan…
- [atharv6f/waypoint](https://github.com/atharv6f/waypoint) - Kemajuan rencana, tugas, dan agen di samping perintah Code Claude — mod Code…
- [aycandv/claude-usage-meter](https://github.com/aycandv/claude-usage-meter) - Papan penggunaan untuk Claude Code: pengeluaran per model.
- [barneym/claude-context-bar](https://github.com/barneym/claude-context-bar) - Mod Claude Code: uraian live context-window di atas prompt.
- [bastianfuchs/claude-code-cache-warm](https://github.com/bastianfuchs/claude-code-cache-warm) - Mod Claude Code yang menampilkan hitung mundur cache prompt di footer dan…
- [benjaminr/nowplaying](https://github.com/benjaminr/nowplaying) - Mod Now Playing untuk Claude Code: Apple Music dan Spotify di atas prompt…
- [benlrice/logpane](https://github.com/benlrice/logpane) - Claude Code mod: a pane that tails the files your Bash calls write to.
- [broening/claude-mods](https://github.com/broening/claude-mods) - Mod untuk Claude Code: Cache-Uhr, Blast Radius, Vorschlaege, Arbeitsliste, Grill.
- [Carismarkus/clowl](https://github.com/Carismarkus/clowl) - Hanya seekor owl untuk Claude Code Anda.
- [cGradying/claude-code-cockpit](https://github.com/cGradying/claude-code-cockpit) - Pita Claude Code satu baris.
- [ChaseWNorton/claude-doom](https://github.com/ChaseWNorton/claude-doom) - Engine Doom asli dengan Freedoom, dapat dimainkan di dalam Claude Code.
- [cldotdev/claude-todo-list](https://github.com/cldotdev/claude-todo-list) - Mod Claude Code yang menyimpan daftar berjalan item terbuka dalam percakapan…
- [comertial/claude-pending-changes](https://github.com/comertial/claude-pending-changes) - Tinjau setiap file yang disentuh Claude, seperti pull request, tanpa…
- [comertial/comertial-mods](https://github.com/comertial/comertial-mods) - Mod Claude Code untuk Engineer sungguhan.
- [davidurco/cc-tamagotchi](https://github.com/davidurco/cc-tamagotchi) - Tamagotchi yang hidup di dalam Claude Code: ia menetas, memakan kode yang…
- [degterev/swiftui-preview-mod](https://github.com/degterev/swiftui-preview-mod) - Claude Code mod: SwiftUI previews rendered by Xcode, shown in a terminal pane.
- [devohmycode/ccmods](https://github.com/devohmycode/ccmods) - Mod Claude Code yang ditulis sebagai hook fungsi, serta marketplace yang…
- [dot-agi/arrester](https://github.com/dot-agi/arrester) - Mod Claude Code: setelah guard memblokir pemanggilan alat, mod ini menghentikan…
- [dot-agi/downrange](https://github.com/dot-agi/downrange) - Mod Claude Code: pekerjaan latar belakang dalam satu tampilan, dengan kemajuan…
- [dot-agi/high-command](https://github.com/dot-agi/high-command) - Mod Claude Code: satu kotak masuk untuk pesan dari rekan tim, subagen bernama…
- [dot-agi/sandbox-tuner](https://github.com/dot-agi/sandbox-tuner) - Mod Claude Code: menjelaskan pemblokiran sandbox dan mengubah pemblokiran…
- [dricosnyman/claude-favourites](https://github.com/dricosnyman/claude-favourites) - Favorit untuk Claude Code: ikon sekali klik untuk perintah dan skill Anda.
- [Egrn/claude-code-mutedit](https://github.com/Egrn/claude-code-mutedit) - Hei, dibisukan! Buang diff, pangkas riff, tak ada lagi edit, kurangi kredit.
- [EmanueleNene/claude-mods](https://github.com/EmanueleNene/claude-mods) - Mod kode Claude: delete-guard (mengonfirmasi penghapusan file) dan octopus-crew…
- [eric1hua/claudemods-desktop-statusline](https://github.com/eric1hua/claudemods-desktop-statusline) - Mod Claude Code: penggunaan langganan (5h / 7d) sebagai pita di atas prompt di…
- [ErnestTramp/claude-critters](https://github.com/ErnestTramp/claude-critters) - Mod Claude Code: agen latar belakang Anda sebagai makhluk piksel, satu sprite…
- [floheissler/cc-worktree-radar](https://github.com/floheissler/cc-worktree-radar) - Radar langsung cabang paralel dan worktree Anda di atas prompt: mana yang dapat…
- [gaius-codius/ostrakon](https://github.com/gaius-codius/ostrakon) - Mod Code Claude untuk menangkap pemikiran di tengah pekerjaan, memilahnya di…
- [GeckoKing9/claude-code-copy-button](https://github.com/GeckoKing9/claude-code-copy-button) - Ctrl+klik untuk menyalin tautan pada setiap blok kode dalam balasan Claude Code…
- [Gharib89/claude-mods](https://github.com/Gharib89/claude-mods) - Mod kode Claude (plugin function-hook), dipasang melalui satu marketplace.
- [gotzastory/my-mods](https://github.com/gotzastory/my-mods) - Mod Code Claude: context-bar-plus (bilah konteks, kuota, mode subagen).
- [Hsiang-LinC/vault-jot](https://github.com/Hsiang-LinC/vault-jot) - Mod Claude Code: tangkap ide ke inbox vault Obsidian dari sesi mana pun.
- [Huuuuung/think-meter](https://github.com/Huuuuung/think-meter) - Mod Claude Code: berapa lama setiap jawaban berlangsung, berapa lama Claude…
- [huynl-96/claude-mods](https://github.com/huynl-96/claude-mods) - Mod kode Claude: streamer-mode menyembunyikan panel privat, band, dan baris…
- [iceberggymnast/claude-code-mods](https://github.com/iceberggymnast/claude-code-mods) - Claude Code function-hook plugins (mods).
- [icedevil2001/auto-continue](https://github.com/icedevil2001/auto-continue) - Mod Claude Code: menunggu hingga batas penggunaan 5 jam terlewati dan mengirim…
- [imsungbin/quackpit-mod](https://github.com/imsungbin/quackpit-mod) - Kokpit di atas perintah Code Claude Anda. Bebek membaca pengukur.
- [its-coughfee/pulse-file-tree](https://github.com/its-coughfee/pulse-file-tree) - Claude Code mod: sidebar file tree that pulses on files Claude just edited.
- [jasonwblock/sdlc-tracker](https://github.com/jasonwblock/sdlc-tracker) - SDLC Tracker: mod Claude Code dengan panel samping yang menampilkan status…
- [jduerrmann/agent-crew](https://github.com/jduerrmann/agent-crew) - Mod kode Claude: satu panel untuk setiap subagen, file yang mereka sentuh…
- [jessetsai1024/claude-ctx-panel](https://github.com/jessetsai1024/claude-ctx-panel) - Panel penggunaan context di bilah samping: total, kategori, pertumbuhan tiap…
- [jessetsai1024/claude-files](https://github.com/jessetsai1024/claude-files) - Daftar file di bilah samping: file apa yang dibuat, diubah, atau dihapus dalam…
- [jessetsai1024/claude-maomao](https://github.com/jessetsai1024/claude-maomao) - 毛毛 bergaya 8-bit (kelinci lop Belanda hitam-putih) berlari dan melompat di atas…
- [jessetsai1024/claude-prompts](https://github.com/jessetsai1024/claude-prompts) - “Yang pernah saya tanyakan” di bilah samping: setiap kalimat yang diketik…
- [jessetsai1024/claude-timeline](https://github.com/jessetsai1024/claude-timeline) - Linimasa di bilah samping: ke mana waktu putaran ini digunakan.
- [jessetsai1024/claude-tokens](https://github.com/jessetsai1024/claude-tokens) - Pertukaran token di bilah samping: berapa token yang dikirim percakapan utama…
- [jessetsai1024/claude-whisper](https://github.com/jessetsai1024/claude-whisper) - Tas kacang jujur untuk claude code: setelah setiap putaran selesai menjawab…
- [jimmysteinmetz/b-sides](https://github.com/jimmysteinmetz/b-sides) - Mod kecil untuk Claude Code, seperti perintah slash baru dan panel samping.
- [KaiC5504/clawd-bar](https://github.com/KaiC5504/clawd-bar) - Clawd tinggal di pita di atas prompt Claude Code Anda: memeragakan sesi…
- [kajidog/cc-mods-tts](https://github.com/kajidog/cc-mods-tts) - Mod yang membacakan respons dan notifikasi Claude Code menggunakan VOICEVOX /…
- [kbrdn1/claude-crosstalk](https://github.com/kbrdn1/claude-crosstalk) - Mod Claude untuk membaca dan bergabung dalam percakapan antara sesi Claude Code…
- [ke11/claude-mods](https://github.com/ke11/claude-mods) - Mod Claude Code. PixBar: makhluk piksel di atas prompt Anda yang bergerak…
- [Khanthtutzin/subagent-crew](https://github.com/Khanthtutzin/subagent-crew) - Mod Claude Code: menjalankan subagen sebagai maskot pixel Claude di atas prompt.
- [KKK12142/claude-mods](https://github.com/KKK12142/claude-mods) - Mod kode Claude (usage-meter, ...).
- [krishna-goutham-tls/cc-mods](https://github.com/krishna-goutham-tls/cc-mods) - Dua mod kode Claude: folio, panel file di samping chat, dan tint, penataan…
- [kuehn-lars/cc-graph](https://github.com/kuehn-lars/cc-graph) - cc-graph: grafik langsung tentang apa yang diketahui Claude Code.
- [leonidb/claude-code-mods](https://github.com/leonidb/claude-code-mods) - Jangan biarkan perhatian Anda teralihkan saat menunggu jawaban Code Claude.
- [linsanmufilm-svg/claude-mods](https://github.com/linsanmufilm-svg/claude-mods) - Sanmu.
- [Lucas-CX/awesome-claude-mods](https://github.com/Lucas-CX/awesome-claude-mods) - Panduan Mod Claude Code yang dikurasi komunitas: kasus penggunaan, demo asli…
- [M-i-k-e-l/agent-state](https://github.com/M-i-k-e-l/agent-state) - Mod Claude Code yang menampilkan apa yang sedang dilakukan Claude di subtitel…
- [malinfossum/mango-buddy](https://github.com/malinfossum/mango-buddy) - Kucing hitam berbulu lebat di atas prompt Claude Code Anda.
- [MarcusJellinghaus/claude-mode-gate](https://github.com/MarcusJellinghaus/claude-mode-gate) - Mod Claude Code dengan profil izin yang dapat diganti: dasar yang aman, profil…
- [MDmubarak786/claude-mods](https://github.com/MDmubarak786/claude-mods) - Mod komunitas untuk Claude Code: penjaga, panel, dan perintah yang berjalan di…
- [merrickxxx/grill-pane](https://github.com/merrickxxx/grill-pane) - Claude Code mod: grilling interviews with clickable answers in a side pane.
- [michaelblaess/turbo-mod](https://github.com/michaelblaess/turbo-mod) - Panel samping untuk Code Claude: file yang ditulis Claude, pembagian terminal…
- [micke-dahlgren/token-range-monitor](https://github.com/micke-dahlgren/token-range-monitor) - Mod Claude Code: memproyeksikan sisa batas mingguan dan 5 jam Claude Anda saat…
- [mmedum/glimt](https://github.com/mmedum/glimt) - Panel samping yang tenang untuk Claude Code: apa yang sedang dilakukan sesi…
- [mmedum/nuet](https://github.com/mmedum/nuet) - Waktu redup di atas setiap prompt dan setiap balasan dalam transkrip Code…
- [mmedum/spor](https://github.com/mmedum/spor) - Mengembalikan apa yang disembunyikan Claude Code: file yang dibaca Claude…
- [moinsen-dev/speckit-xref](https://github.com/moinsen-dev/speckit-xref) - Keep the code on the spec: a Claude Code mod and a GitHub Spec Kit extension…
- [mrsono0/ctx-footer](https://github.com/mrsono0/ctx-footer) - Mod Code Claude: penggunaan jendela konteks di slot mode footer perintah.
- [muellerei/enable-todo-tools](https://github.com/muellerei/enable-todo-tools) - Mod Claude Code yang mengaktifkan kembali alat todo untuk model yang tidak…
- [muellerei/sweet-spot](https://github.com/muellerei/sweet-spot) - Claude Code mod that waits for a safe pause, then hands your session over or…
- [muellerei/task-line](https://github.com/muellerei/task-line) - Mod Claude Code: satu baris per tugas di atas prompt dengan tugas saat ini…
- [nachtgold/claude-code-connect-four](https://github.com/nachtgold/claude-code-connect-four) - Mainkan Connect Four melawan AI di dalam Claude Code (/connect-four).
- [naoanao/agent-cross-check](https://github.com/naoanao/agent-cross-check) - Mod Claude Code: ketika agen coding lain melakukan commit ke repo Anda, Claude…
- [naoanao/shared-repo-guard](https://github.com/naoanao/shared-repo-guard) - Mod Claude Code untuk repo yang dibagikan oleh beberapa agen AI: menghentikan…
- [nerevar48/nerevar-mods](https://github.com/nerevar48/nerevar-mods) - Marketplace mod Claude Code.
- [NicBritz/claude-code-mods](https://github.com/NicBritz/claude-code-mods) - Fun, free mods for Claude Code that never spend a token.
- [nu0ma/query-guard](https://github.com/nu0ma/query-guard) - Pagar pengaman untuk SQL di Claude Code: meminta konfirmasi sebelum Claude…
- [OG-Matcha/tessera](https://github.com/OG-Matcha/tessera) - Satu mod untuk Claude Code, Windows dan CJK terlebih dahulu: pratinjau gambar…
- [onk3sh/fix-on-edit](https://github.com/onk3sh/fix-on-edit)
- [osaki42/awesome-claude-mods](https://github.com/osaki42/awesome-claude-mods) - Mod Claude Code terbaik, diurutkan berdasarkan manfaatnya bagi Anda.
- [Para-FR/claude-code-mods-fr](https://github.com/Para-FR/claude-code-mods-fr) - Dua Mod Claude untuk Claude Code: garde-du-corps.
- [paragpandyareal/swear-slap](https://github.com/paragpandyareal/swear-slap) - Memaki Claude Code dan tangan kartun membalas dengan tamparan.
- [philarete173/claude_mods](https://github.com/philarete173/claude_mods) - Panel samping statistik sesi langsung untuk tab Code aplikasi desktop Claude…
- [pradyb/claude-mods](https://github.com/pradyb/claude-mods) - Mod untuk Code Claude: safety-guard memblokir perintah destruktif dan akses…
- [rajib2k5/claude-market-watch](https://github.com/rajib2k5/claude-market-watch) - Mod Claude Code: ticker saham langsung, panel /quote, peringatan harga, pita…
- [ray-amjad/cache-clock](https://github.com/ray-amjad/cache-clock) - Claude Code mod: a band above the prompt showing context used and a countdown…
- [ray-amjad/diagram-pane](https://github.com/ray-amjad/diagram-pane) - Claude Code mod: a side pane that pins every diagram Claude draws and keeps a…
- [ray-amjad/dream-pass](https://github.com/ray-amjad/dream-pass) - Claude Code mod: a dreaming pass that merges, rewrites and prunes Claude.
- [ray-amjad/memory-fork](https://github.com/ray-amjad/memory-fork) - Mod Claude Code: terus memperbarui auto-memory di latar belakang setelah setiap…
- [ray-amjad/prompt-bouncer](https://github.com/ray-amjad/prompt-bouncer) - Claude Code mod: drops vague prompts before Claude sees them, and suggests the…
- [RedRoosterKey/claude-code-ssh-usage-band](https://github.com/RedRoosterKey/claude-code-ssh-usage-band) - Mod Claude Code: host SSH, RAM, dan batas penggunaan 5j/7h dalam satu baris di…
- [Risdon8/push-ups](https://github.com/Risdon8/push-ups) - Mod Code Claude: push-up yang harus dilakukan saat Claude bekerja. Tanpa token.
- [Rohitp/claude-mods](https://github.com/Rohitp/claude-mods) - Mods for claude code.
- [saadk408/stepline](https://github.com/saadk408/stepline) - Mod Claude Code: mengubah rencana yang Anda setujui dalam mode plan menjadi…
- [saksham10arora-dotcom/awesome-claude-mods](https://github.com/saksham10arora-dotcom/awesome-claude-mods) - Daftar pilihan mod Claude Code. Setiap entri dikloning dan diperiksa dengan…
- [saksham10arora-dotcom/claude-frugal](https://github.com/saksham10arora-dotcom/claude-frugal) - Mode tanpa biaya: agen pembantu berjalan di Haiku, dan file serta log besar…
- [saksham10arora-dotcom/claude-lofi](https://github.com/saksham10arora-dotcom/claude-lofi) - Soundtrack lofi yang mengikuti sesi: tenang, fokus, mengalir, plus isyarat…
- [saksham10arora-dotcom/claude-teach-me](https://github.com/saksham10arora-dotcom/claude-teach-me) - Belajar sambil Claude melakukan coding: setelah giliran yang mengubah kode…
- [saksham10arora-dotcom/claude-vhs](https://github.com/saksham10arora-dotcom/claude-vhs) - Rekaman setiap edit yang dibuat Claude: putar ulang setiap perubahan saat…
- [sam-ruff/account-switcher-claude-code-mod](https://github.com/sam-ruff/account-switcher-claude-code-mod) - Mod untuk claude code yang memungkinkan Anda berpindah antar akun.
- [samaphp/session-links](https://github.com/samaphp/session-links) - Setiap tautan yang disebutkan sesi Anda, dalam satu baris di atas prompt.
- [sawzhang/hello-mod](https://github.com/sawzhang/hello-mod) - Demo minimal fungsi hook Claude Code: panel token/biaya real-time di atas…
- [shahsanket2107/clarvis](https://github.com/shahsanket2107/clarvis) - Clarvis: mod penggemar Avengers tidak resmi untuk Code Claude.
- [shengyy/ccoverhead](https://github.com/shengyy/ccoverhead) - Mod Claude Code untuk konteks, pertumbuhan, kuota, cache, biaya native, dan…
- [shezis/claude-model-router](https://github.com/shezis/claude-model-router) - Mod Code Claude: teruskan giliran sederhana dan subagen ke model yang lebih…
- [speti4/doom-pane](https://github.com/speti4/doom-pane) - DOOM asli dalam panel Claude Code tanpa perlu memasang apa pun: mesinnya…
- [steven-ngle/blade-of-commits](https://github.com/steven-ngle/blade-of-commits) - Pesan commit sekali klik untuk Claude Code dengan Malenia pixel-art yang menari.
- [Tanish-Dev/claude-usage-band](https://github.com/Tanish-Dev/claude-usage-band) - Clawd Meter — mod kode Claude yang menampilkan penggunaan paket Claude Anda…
- [TFoxik/claude-model-router](https://github.com/TFoxik/claude-model-router) - Mod Claude Code yang memilih model dan upaya untuk setiap jenis pekerjaan…
- [thangdo19/claude-code-mods](https://github.com/thangdo19/claude-code-mods) - Small mods that change how Claude Code looks and sounds.
- [TheBabaYaga/claude-session-flow](https://github.com/TheBabaYaga/claude-session-flow) - Mod Claude Code yang menampilkan sesi saat ini dalam sebuah panel: setiap…
- [theishandubey/claude-mods](https://github.com/theishandubey/claude-mods) - Marketplace plugin Claude Code untuk mod: plugin function-hooks yang menggambar…
- [thinhkhuat/prompt-enhancer](https://github.com/thinhkhuat/prompt-enhancer) - Claude Code mod: rewrites a rough prompt in place, naming fitting skills, open…
- [tomfluff/claude-read-along](https://github.com/tomfluff/claude-read-along) - Listen to Claude Code.
- [trietsch/claude-customizations](https://github.com/trietsch/claude-customizations) - Kustomisasi untuk Code Claude.
- [VaitaR/claude-code-limits](https://github.com/VaitaR/claude-code-limits) - Mod Claude Code: kuota 5h/7d, context window, sisa waktu prompt-cache, dan…
- [VAlux/claude-session-progress](https://github.com/VAlux/claude-session-progress) - Mod Claude Code: pita kemajuan animasi dan ringkasan penyelesaian untuk tugas…
- [Vansitha/clawd-watch](https://github.com/Vansitha/clawd-watch) - Tiga mod Claude Code kecil: lihat kapan subagen Anda selesai, antrekan pesan…
- [varunmoka7/image-shrinker](https://github.com/varunmoka7/image-shrinker) - Mengecilkan tangkapan layar besar sebelum Claude membacanya, sehingga sesi…
- [varunmoka7/layman](https://github.com/varunmoka7/layman) - Katakan &quot;Saya tersesat&quot; dan Claude akan menjelaskan kembali balasan terakhirnya…
- [varunmoka7/next-steps-autopilot](https://github.com/varunmoka7/next-steps-autopilot) - Menampilkan prompt berikutnya yang disarankan di atas kotak prompt.
- [varunmoka7/side-chat](https://github.com/varunmoka7/side-chat) - Ajukan pertanyaan sampingan kepada Claude di panel di sebelah pekerjaan Anda.
- [Victormartinsilva/MODS-CLAUDECODE](https://github.com/Victormartinsilva/MODS-CLAUDECODE) - Marketplace mod Claude Code dengan instalasi satu langkah dan panduan video…
- [vihrea1337/headroom](https://github.com/vihrea1337/headroom) - Hitung mundur batas laju dan prakiraan laju penggunaan untuk Claude Code.
- [WeaponizedLego/claude-code-mods](https://github.com/WeaponizedLego/claude-code-mods) - My Claude Code mods.
- [wnsogabriel/claude-mods](https://github.com/wnsogabriel/claude-mods) - Mods para o Claude Code: faixa de limites de uso (5h/semanal) e painel de…
- [wukonigcom/quanta-costa](https://github.com/wukonigcom/quanta-costa) - 🧾 Plugin Code Claude: batas penggunaan Claude Pro/Max Anda dengan perkiraan…
- [xinhuagu/oh-my-claude-mods](https://github.com/xinhuagu/oh-my-claude-mods) - Mod untuk Claude Code. agent-crew: lihat subagen Anda bekerja sebagai kru…
- [yeonwooook/claude-study-latex](https://github.com/yeonwooook/claude-study-latex) - Matematika LaTeX sebaris dan tampilan, serta gambar TikZ opsional, dalam…
- [YohanGarcia/agent-taskboard](https://github.com/YohanGarcia/agent-taskboard) - Papan tugas live untuk Claude Code: rencanakan sebelum membangun, ikuti setiap…
- [zaripovfarrukh/claude-code-mods](https://github.com/zaripovfarrukh/claude-code-mods)
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - Kumpulan pilihan sumber daya terbaik untuk agen-agen paling hebat, Claude Code…
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) - Plugin Claude Code yang menampilkan apa yang sedang terjadi — penggunaan…
- [sirmalloc/ccstatusline](https://github.com/sirmalloc/ccstatusline) - 🚀 Statusline yang indah dan sangat dapat disesuaikan untuk Claude Code CLI…
- [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) - Semua bagian system prompt Claude Code, 27 deskripsi alat bawaan, prompt…
- [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) - 45+ kiat untuk memaksimalkan Claude Code, dari dasar hingga tingkat lanjut…
- [op7418/guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill) - 🪧 Claude Code / Codex skill — generate Xiaohongshu carousels &amp; WeChat 21:9+1:1…
- [Owloops/claude-powerline](https://github.com/Owloops/claude-powerline) - Powerline bergaya vim yang indah untuk Claude Code.
- [persiyanov/herdr-reviewr](https://github.com/persiyanov/herdr-reviewr) - Tinjau diff agen pengodean Anda di panel terminal dan kirim komentar baris…
- [uppinote20/claude-dashboard](https://github.com/uppinote20/claude-dashboard) - Plugin baris status komprehensif untuk Claude Code dengan penggunaan konteks…
- [starbaser/ccproxy](https://github.com/starbaser/ccproxy) - Build mods for Claude Code: Hook any request, modify any response, /model…
- [NYCU-Chung/cc-statusline](https://github.com/NYCU-Chung/cc-statusline) - A comprehensive statusline dashboard for Claude Code — session info, quota…
- [gwittebolle/claude-carbon](https://github.com/gwittebolle/claude-carbon) - claude-carbon: track the carbon footprint of your Claude Code sessions.
- [AwesomeZun/CC-statusline](https://github.com/AwesomeZun/CC-statusline) - An aesthetic statusline for Claude Code by awesomejun.
- [a86582751/dsh-nexttavern](https://github.com/a86582751/dsh-nexttavern) - Agent roleplay cerita panjang untuk DeepSeek Harness (plugin tavern DSH): impor…
- [JohnnyVizz/claude-kit](https://github.com/JohnnyVizz/claude-kit) - Public Claude Code skills and mods.
- [escapeboy/claude-code-kit](https://github.com/escapeboy/claude-code-kit) - Skills, mods, subagents, hooks, slash commands and guides for Claude Code…
- [mvalentsev/awesome-free-ai-coding](https://github.com/mvalentsev/awesome-free-ai-coding) - 📡 Legal free LLM APIs &amp; coding agents — self-updating, probe-verified twice a…
- [backstabslash/goccc](https://github.com/backstabslash/goccc) - Kalkulator biaya cepat tanpa dependensi dan statusline yang dapat disesuaikan…
- [kylesnowschwartz/tail-claude-hud](https://github.com/kylesnowschwartz/tail-claude-hud) - Statusline terminal untuk sesi Claude Code.
- [arturogarrido/claudinho](https://github.com/arturogarrido/claudinho) - ⚽ Skor langsung football(soccer), jadwal pertandingan, dan klasemen untuk…
- [WormAlien/hub-cc](https://github.com/WormAlien/hub-cc) - Control plane lokal untuk Claude Code di Windows dan macOS: alihkan gateway LLM…
- [johncattrall/keymap-ai](https://github.com/johncattrall/keymap-ai) - Agent Skill that turns your coding agent into a keyboard firmware expert.
- [philoserf/claude-code-config](https://github.com/philoserf/claude-code-config) - Konfigurasi Claude Code pribadi yang diberi versi di dalam ~/.claude — agent…
- [ashafizullah/claude-code-muslim-mods](https://github.com/ashafizullah/claude-code-muslim-mods) - Waktu salat, tanggal Hijriah, adhkar, ayat harian, puasa sunnah, Ramadan…
- [GooDAnDReaDY/dsh-image-gen](https://github.com/GooDAnDReaDY/dsh-image-gen) - Image generation &amp; visual processing suite for DeepSeek Harness: pluggable…
- [GoSlowPoke168/claude-statusline](https://github.com/GoSlowPoke168/claude-statusline) - Statusline truecolor dua baris untuk Claude Code.
- [proDreams/dsh-tidewatch](https://github.com/proDreams/dsh-tidewatch) - Kartu pasang surut waktu sibuk/tidak sibuk mengambang untuk DeepSeek Harness…
- [hoobnn/hoobnn-agent-mods](https://github.com/hoobnn/hoobnn-agent-mods) - 适用于 Claude Code、pi 和 DeepSeek Harness 的插件合集：状态栏 HUD、任务进度条、Tailscale 节点状态等 ·…
- [pierrebelin/claude-code-toolkit](https://github.com/pierrebelin/claude-code-toolkit) - Perangkat Claude Code portabel untuk .NET DDD/Clean Architecture: agen TDD…
- [jcdendrite/claude-config](https://github.com/jcdendrite/claude-config) - Konfigurasi global Claude Code yang portabel: skill khusus, hook PreToolUse…
- [mutlumehmet/claude-plugins](https://github.com/mutlumehmet/claude-plugins) - Plugin Claude Code yang saya gunakan setiap hari: skills dan mod, dirapikan…
- [manson341349-beep/claude-desktop-mods](https://github.com/manson341349-beep/claude-desktop-mods) - Unofficial mods for the Code tab of Claude Desktop — usage-pet: a usage band…
- [bbeygel/claude-code-tama](https://github.com/bbeygel/claude-code-tama) - Tama, a Tamagotchi companion mod for Claude Code.
- [darthmolen/hytale-claude-code-marketplace](https://github.com/darthmolen/hytale-claude-code-marketplace) - Marketplace for Claude Code Plugins and Skills to facilitate mods of the game…
- [frsorrentino/fable-director](https://github.com/frsorrentino/fable-director) - Tata kelola token untuk Claude Code: model teratas mengarahkan, eksekusi…
- [jeancarlo-javier/claude-status-bar](https://github.com/jeancarlo-javier/claude-status-bar) - Statusline fase alur kerja langsung untuk Claude Code.
- [romnycristopher/claude-am-mods](https://github.com/romnycristopher/claude-am-mods) - Repository for Claude Code Awesome Media mods.
- [rootstudioyaml/sprag](https://github.com/rootstudioyaml/sprag) - Pangkas pengeluaran token Claude Code &amp; Codex: merutekan lookup dan test run ke…
- [tedserbinski/claude-code-statusline](https://github.com/tedserbinski/claude-code-statusline) - Konfigurasi status line yang sederhana dan berguna untuk Claude Code.
- [aquahitt/claude-code-limit-alerts](https://github.com/aquahitt/claude-code-limit-alerts) - Peringatan batas penggunaan untuk Claude Code: notifikasi macOS, peringatan…
- [crosscountryridinggirlwonder916/claude-statusline](https://github.com/crosscountryridinggirlwonder916/claude-statusline) - Menampilkan statusline Claude Code dengan batas laju, direktori saat ini, dan…
- [fbincon/claude-code-statusline](https://github.com/fbincon/claude-code-statusline) - Status line Claude Code yang dapat dikonfigurasi untuk Linux, WSL, Windows, dan…
- [JairoTorregrosa/claude-statusline](https://github.com/JairoTorregrosa/claude-statusline) - statusline Rust yang cepat untuk Claude Code — mengutamakan payload, git…
- [jsh135790/claude-code-capsule-panel](https://github.com/jsh135790/claude-code-capsule-panel) - Dashboard penggunaan live untuk Claude Code — rincian konteks, hit cache…
- [jv-k/claude-gauge](https://github.com/jv-k/claude-gauge) - Baris status dan baris token untuk Claude Code: konteks, penggunaan 5 jam dan…
- [kyllian330/claude-statusline](https://github.com/kyllian330/claude-statusline) - Menampilkan detail status utama Code Claude termasuk model, konteks, batas…
- [Obednal97/claude-statusline-kit](https://github.com/Obednal97/claude-statusline-kit) - Baris status Claude Code multi-baris: pengeluaran, konteks %, git, dan akun…
- [salvanya/claude_code_statusline](https://github.com/salvanya/claude_code_statusline) - Statusline dengan informasi berguna untuk claude code.
- [tc3oliver/claude-team-kit](https://github.com/tc3oliver/claude-team-kit) - Tim agen native. Di bawah kendali. Batas pekerja yang ketat, visibilitas tim…
- [yedidya-buildfy/claude-addons](https://github.com/yedidya-buildfy/claude-addons) - Add-on Claude Code: pemantau titik berwarna status tab + statusline GSD bawaan.
- [zach-source/claude-factory](https://github.com/zach-source/claude-factory) - Definable software factories for Claude Code on herdr: xstate station graphs, a…
- [akhilnalliboina/claude-usage-statusline](https://github.com/akhilnalliboina/claude-usage-statusline) - Baris status penggunaan Code Claude untuk macOS dan Linux, dikemas sebagai…
- [alexleveled/claude-read-aloud](https://github.com/alexleveled/claude-read-aloud) - Hear Claude Code.
- [andkirby/claude-statusline](https://github.com/andkirby/claude-statusline) - Statusline kustom untuk Claude Code — bilah konteks dengan persentase…
- [AsyrafHussin/claude-code-statusline](https://github.com/AsyrafHussin/claude-code-statusline) - Baris status yang rapi dan informatif untuk Claude Code — menampilkan proyek…
- [BedirYilmaz/claude-crt-hud-mod](https://github.com/BedirYilmaz/claude-crt-hud-mod) - Mod CRT HUD Claude: panel status bergaya CRT untuk Code Claude, di terminal dan…
- [bunderlog/claude-plugins](https://github.com/bunderlog/claude-plugins) - Marketplace plugin Claude Code dengan baloo: keahlian, agen yang memverifikasi…
- [ctfbio/claude-code-statusline](https://github.com/ctfbio/claude-code-statusline) - Statusline Claude Code tingkat profesional: durasi sesi, biaya multi-mata uang…
- [cvrt-gmbh/claude-statusline](https://github.com/cvrt-gmbh/claude-statusline) - Baris status yang memperhatikan langganan untuk Claude Code.
- [diegorv/koko.claude-statusline](https://github.com/diegorv/koko.claude-statusline) - Baris status terminal yang lengkap untuk Claude Code — Bun + TypeScript, tanpa…
- [ejklock/claude-mermaid-render](https://github.com/ejklock/claude-mermaid-render) - Plugin Claude Code yang menampilkan diagram Mermaid dengan indah dalam…
- [filtercoffeeway/claude-kit](https://github.com/filtercoffeeway/claude-kit) - Tools, skill, dan agent untuk Claude Code — dimulai dengan baris status yang…
- [giribboy77-arch/claude-statusline](https://github.com/giribboy77-arch/claude-statusline) - Statusline khusus Claude Code (model, effort, konteks, cache, batas penggunaan).
- [hardtomakeanadress/claude-code-deepseek-cost](https://github.com/hardtomakeanadress/claude-code-deepseek-cost) - Pengeluaran DeepSeek API yang sebenarnya untuk Claude Code: menetapkan ulang…
- [hieuvo/claude-imgview](https://github.com/hieuvo/claude-imgview) - Pratinjau gambar di dalam Code Claude: arahkan kursor ke chip di bawah balasan…
- [ihororlovskyi/claude-statusline](https://github.com/ihororlovskyi/claude-statusline) - Baris status Claude Code dengan baris panel agen.
- [izahamyatim/claude-plugin-fizzy](https://github.com/izahamyatim/claude-plugin-fizzy) - 🚀 Sinkronkan todo Claude ke Fizzy.do untuk visibilitas tim secara langsung…
- [konnichiwab/claude-code-config](https://github.com/konnichiwab/claude-code-config) - Menu pengaturan, baris status, dan konfigurasi Claude Code.
- [Leechlike-intangibleasset343/claude-code-statusline](https://github.com/Leechlike-intangibleasset343/claude-code-statusline) - Lacak status Claude Code dengan dasbor ringkas yang menampilkan konteks, biaya…
- [msetsma/claude-style](https://github.com/msetsma/claude-style) - Claude Code style mod: prompt bubbles, tool-call cards and rails, framed bands…
- [msinclair-sudo/claude-code-setup](https://github.com/msinclair-sudo/claude-code-setup) - Penginstal lingkungan Claude Code: skills, statusline, hooks, permissions, dan…
- [OpenClawFarm/claude-statusline](https://github.com/OpenClawFarm/claude-statusline) - Baris status bergaya HUD untuk Code Claude — kesehatan jaringan, TPS, konteks…
- [oshnilia/claude-plugins](https://github.com/oshnilia/claude-plugins) - Plugin dan mod Claude Code untuk memahami apa yang dilakukan Claude: format…
- [pbhwheeler/claude-config](https://github.com/pbhwheeler/claude-config) - Portable Claude Code config: settings.json, hooks, status line, and a bootstrap…
- [pirncedark/afu-claude-statusline](https://github.com/pirncedark/afu-claude-statusline) - Bilah status multi-baris berwarna-warni untuk Claude Code.
- [rainyfei/claude-statusline-win](https://github.com/rainyfei/claude-statusline-win) - Baris status Claude Code untuk Windows (PowerShell): bilah penggunaan, hitung…
- [Sofia-D4L/claude-conf](https://github.com/Sofia-D4L/claude-conf) - Konfigurasi portabel Claude Code (statusline + penginstal).
- [SohamShirsat/claude-cockpit](https://github.com/SohamShirsat/claude-cockpit) - Dasbor kecil untuk Claude Code: konteks %, hitung mundur cache, penggunaan 5…
- [speti4/claude-statusline](https://github.com/speti4/claude-statusline) - Bilah status terminal khusus untuk Claude Code: model, direktori, status git…
- [thaiquangquy/claude.me](https://github.com/thaiquangquy/claude.me) - Konfigurasi Claude Code portabel: CLAUDE.md, settings, statusline, skills.
- [Tina0529/claude-session-radar](https://github.com/Tina0529/claude-session-radar) - Mod desktop Code Claude (macOS): notifikasi sesi klik-untuk-melompat, panel…
- [unlocked-spark/claude-code-earshot](https://github.com/unlocked-spark/claude-code-earshot) - Mod pendamping pembaca layar untuk Code Claude (Unlocked Spark Foundation).
- [viplav-artha/claude-code-lessons](https://github.com/viplav-artha/claude-code-lessons) - Pendalaman praktis dan terverifikasi tentang Claude Code — CLAUDE.md, subagent…
- [vladimir-ks/ai-agile-claude-code-statusline](https://github.com/vladimir-ks/ai-agile-claude-code-statusline) - Pelacakan biaya secara waktu nyata dan baris status pemantauan sesi untuk…
- [warodan/vscode-claude-code-patch](https://github.com/warodan/vscode-claude-code-patch) - Skill Claude Code (VS Code, Windows): pratinjau gambar dan tombol buka di bawah…
- [ymoud/claude-code-statusline](https://github.com/ymoud/claude-code-statusline) - Baris status Code Claude: folder, cabang git, model, penggunaan jendela…
- [YoniYon00/claude-feedback-rings](https://github.com/YoniYon00/claude-feedback-rings) - Context Rot Detector 2026 - Monitor Memori AI &amp; Batas Laju Proaktif untuk Agen…
- [zhuyansen/awesome-claude-code-hooks](https://github.com/zhuyansen/awesome-claude-code-hooks) - Hook, subagen, dan statusline Claude Code: koleksi dan alat sumber terbuka…
- [tronschell/statusline.sh](https://github.com/tronschell/statusline.sh) - Builder visual untuk statusline Claude Code.
- [Magnus-Gille/tokenatlas](https://github.com/Magnus-Gille/tokenatlas) - Statusline Claude Code yang menampilkan penggunaan token waktu nyata dan…
- [ishuagrawal/clawdhouse](https://github.com/ishuagrawal/clawdhouse) - Mods for Claude Code: panes, bands and buddies built on function hooks.
- [ashishsk93/baton-mods](https://github.com/ashishsk93/baton-mods) - Pass tasks between your Claude Code sessions.
- [lahoramaker/mods-mcp](https://github.com/lahoramaker/mods-mcp) - This in a MCP server to control MODS, the modular cross platforms tool for…
- [Rimcat-JA/translate-ck3-mods](https://github.com/Rimcat-JA/translate-ck3-mods) - Codex and Claude Code skill for translating CK3 mods with a local LLM.
- [sTomerG/agent-kit](https://github.com/sTomerG/agent-kit) - Open-source mods and other extensions for Claude Code.
- [Apparux/cc-fusion](https://github.com/Apparux/cc-fusion) - Statusline Claude Code: keindahan CCometixLine + fungsionalitas HUD Claude.
- [charlie947/mod-maker](https://github.com/charlie947/mod-maker) - Mod Maker: find what you ask Claude Code again and again, and turn it into a…
- [Niedvin/ClauDiscobombulating](https://github.com/Niedvin/ClauDiscobombulating) - prompt-bar mod for Claude Code: usage limits, cache timer + alert, model/effort…

</details>

<a id="dsh-cordis"></a>

## Ekosistem plugin DSH dan Cordis

DeepSeek Harness dan Cordis mencapai tempat yang sama dari arah yang berbeda: bagi keduanya, plugin adalah mekanisme mod, sehingga plugin di sana setara dengan mod di sini.

<details>
<summary>🧵 <b><a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b> · ⭐74336 · TypeScript · 👁️ observed · 0 天</summary>

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
| Bintang                  | **74336**  |
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
<summary>🧵 <b><a href="https://github.com/nexu-io/open-design">nexu-io/open-design</a></b> · ⭐100521 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Bintang                  | **100521** |
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
<summary>🧵 <b><a href="https://github.com/morluto/rea">morluto/rea</a></b> · ⭐91711 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Bintang                  | **91711**  |
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
<summary>🧵 <b><a href="https://github.com/tt-a1i/archify">tt-a1i/archify</a></b> · ⭐81929 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Bintang                  | **81929**  |
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
<summary>🧵 <b><a href="https://github.com/esengine/DeepSeek-Reasonix">esengine/DeepSeek-Reasonix</a></b> · ⭐35760 · Go · 🔎 inferred · 0 天</summary>

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
| Bintang                  | **35760**  |
| Push terakhir            | 2026-10-11 |
| Pertama kali dicantumkan | 2026-10-06 |

🏷 `agent` · `agent-framework` · `ai-agent` · `ai-coding` · `cli` · `coding-agent` · `deepseek` · `developer-tools`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/titanwings/distilly">titanwings/distilly</a></b> · ⭐25495 · Python · 🔎 inferred · 19 天</summary>

##### 📝 Ringkasan

Distilly — Distill how they think into reusable Skills for any Agent or Bot. Formerly Colleague Skill（原同事 Skill）.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | Python                                                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **25495**  |
| Push terakhir            | 2026-09-22 |
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `agent-skills` · `agentic-ai` · `ai-agent` · `ai-agents` · `ai-assistants` · `ai-persona` · `claude-code` · `claude-skills`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/titanwings--distilly/bf54e387044cab88.png" width="100%" alt="titanwings/distilly screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/awesome-dsh-plugin/awesome-dsh-plugin">awesome-dsh-plugin/awesome-dsh-plugin</a></b> · ⭐18380 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

A curated list of plugins for DeepSeek Harness (dsh) · DeepSeek Harness 插件精选列表

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | JavaScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **18380**  |
| Push terakhir            | 2026-10-11 |
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `awesome` · `awesome-list` · `deepseek-harness` · `dsh` · `dsh-plugin`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/zhu1090093659/dsh-web">zhu1090093659/dsh-web</a></b> · ⭐8629 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Bintang                  | **8629**   |
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
<summary>🧵 <b><a href="https://github.com/Ebony-Vinyl/dsh-our-free-model">Ebony-Vinyl/dsh-our-free-model</a></b> · ⭐8510 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

在 dsh 里装上这个插件即可，无需登录、注册或填 API Key，就能使用包括 DeepSeek V4.1 Flash、Kimi K3 在内的前沿模型——完全免费，不限量。 All you do is install this plugin in dsh: no login, no sign-up, no API key — the frontier models are just there, DeepSeek V4.1 Flash and Kimi K3 among them. Completely free, with no usage cap.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | JavaScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **8510**   |
| Push terakhir            | 2026-10-11 |
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `ai-agents` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-plugin` · `free-model` · `llm`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ebony-vinyl--dsh-our-free-model/212e73dc2aecbd46.png" width="100%" alt="Ebony-Vinyl/dsh-our-free-model screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-market/dsh-market">dsh-market/dsh-market</a></b> · ⭐6159 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

Pasar plugin di dalam DeepSeek Harness — jelajahi, cari, instal sekali klik · Pasar plugin visual DSH

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | TypeScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **6159**   |
| Push terakhir            | 2026-10-11 |
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `deepseek-harness` · `dsh-plugin` · `marketplace`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dsh-market--dsh-market/06b60aace017dab8.png" width="100%" alt="dsh-market/dsh-market screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/MeteorNOX/DeepSeek-Balance-Whale-Widget">MeteorNOX/DeepSeek-Balance-Whale-Widget</a></b> · ⭐4486 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

DeepSeek Harness（DSH）adalah gadis paus kecil yang tinggal di pojok kanan bawah antarmuka DSH, membantu memantau saldo akun DeepSeek Anda. Kenyal dan interaktif, mendukung seret untuk menempel, pembalikan saat menempel di kiri, animasi pengguliran angka, serta aktif otomatis mengikuti antarmuka. Disarankan langsung memanggilnya saat memasang dsh

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | JavaScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **4486**   |
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
<summary>🧵 <b><a href="https://github.com/ccch1mneyyy/dsh-TUI">ccch1mneyyy/dsh-TUI</a></b> · ⭐4286 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Bintang                  | **4286**   |
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
<summary>🧵 <b><a href="https://github.com/omdsh-dev/DSH-better-sidebar">omdsh-dev/DSH-better-sidebar</a></b> · ⭐4107 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

开放的侧边栏底座，支持三方拓展注册新侧边栏页面。内置文件渲染编辑/终端/侧边对话/Git/子代理页面 ｜ Open sidebar foundation, supports third-party extensions to register new sidebar pages. Built-in file rendering/editing, terminal, side chat, Git, and sub-agent pages.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | TypeScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **4107**   |
| Push terakhir            | 2026-10-11 |
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `deepseek` · `deepseek-harness` · `dsh` · `dsh-better-sidebar` · `dsh-plugin` · `sidebar`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/omdsh-dev--dsh-better-sidebar/0f9147e51f645f82.png" width="100%" alt="omdsh-dev/DSH-better-sidebar screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/omdsh-dev--dsh-better-sidebar/db34cbdf93687219.gif" width="100%" alt="omdsh-dev/DSH-better-sidebar animation"><br><sub>rekaman animasi · <a href="https://github.com/user-attachments/assets/23187822-047e-45cc-b480-fe997bd55b86">Buka video</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-tauri/deepseek-harness-desktop">dsh-tauri/deepseek-harness-desktop</a></b> · ⭐3119 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

DeepSeek Harness Tauri versi desktop | Installer hanya 8mb, tanpa penyiapan lingkungan, plugin prasetel, Windows / macOS / Linux.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | TypeScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **3119**   |
| Push terakhir            | 2026-10-11 |
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `deepseek` · `deepseek-harness` · `desktop` · `dsh` · `dsh-desktop` · `dsh-plugin` · `tauri`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dsh-tauri--deepseek-harness-desktop/f281725e73da1059.png" width="100%" alt="dsh-tauri/deepseek-harness-desktop screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/EthanYoQ/AI-Novel-Writer">EthanYoQ/AI-Novel-Writer</a></b> · ⭐1406 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Bintang                  | **1406**   |
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
<summary>🧵 <b><a href="https://github.com/vshulcz/deja-vu">vshulcz/deja-vu</a></b> · ⭐1171 · Go · 🔎 inferred · 0 天</summary>

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
| Bintang                  | **1171**   |
| Push terakhir            | 2026-10-11 |
| Pertama kali dicantumkan | 2026-10-04 |

🏷 `agent-memory` · `ai-memory` · `claude-code` · `claude-code-hooks` · `claude-code-plugins` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/8033ba54a9424c88.png" width="100%" alt="vshulcz/deja-vu screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/5fb930f1983f270b.gif" width="100%" alt="vshulcz/deja-vu animation"><br><sub>rekaman animasi</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/myYangyunfan/dsh_desktop">myYangyunfan/dsh_desktop</a></b> · ⭐704 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Bintang                  | **704**    |
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
<summary>🧵 <b><a href="https://github.com/Ikalus1988/MisakaNet">Ikalus1988/MisakaNet</a></b> · ⭐526 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

📚 A zero-dependency, git-backed micro-lesson library for AI Agents to asynchronously share and search verified debugging experience. | https://misakanet.org

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | Python                                                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **526**    |
| Push terakhir            | 2026-10-11 |
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `action` · `agents` · `cloudflare-workers` · `codex` · `cordis-plugin` · `d1` · `deepseek-harness` · `deepseek-harness-plugin`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ikalus1988--misakanet/f6853900d49aba17.jpg" width="100%" alt="Ikalus1988/MisakaNet screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/T-Auto/dsh-ops">T-Auto/dsh-ops</a></b> · ⭐334 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

A toolkit for low-level operations in DSH, designed to reduce token usage and task execution time / DSH 底层操作工具插件，旨在减少 Token 消耗与任务耗时

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | JavaScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **334**    |
| Push terakhir            | 2026-10-11 |
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `dsh` · `dsh-plugin` · `dsh-plugins`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://github.com/user-attachments/assets/7c9ba485-5323-42a2-b5a8-6dcda07f91c4" width="100%" alt="T-Auto/dsh-ops screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

<sub>Aset ditautkan langsung dari repositori upstream karena tidak ada lisensi yang mengizinkan redistribusi yang dinyatakan.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xing-shuyin/pi-web-ui">xing-shuyin/pi-web-ui</a></b> · ⭐284 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

Cukup buka browser — selesaikan semua pekerjaan Anda.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | TypeScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **284**    |
| Push terakhir            | 2026-10-11 |
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `dsh` · `dsh-desktop` · `dsh-plugin` · `pi` · `pi-web` · `pi-web-ui`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xing-shuyin--pi-web-ui/926fb8bfa4f6062a.jpg" width="100%" alt="xing-shuyin/pi-web-ui screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
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
| Push terakhir            | 2026-10-11 |
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

Delegasi tugas berbasis pergeseran waktu untuk DeepSeek Harness (dsh): rencanakan tugas kapan saja, biarkan tugas berjalan tanpa pengawasan di luar jam sibuk, lalu kembali untuk melihat laporannya. Diputuskan oleh manusia, mendukung desktop + web.

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
<summary>🧵 <b><a href="https://github.com/morluto/flameox">morluto/flameox</a></b> · ⭐133 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

Bukti runtime yang membantu agent melacak, membuat profil, dan mengurangi hotspot dalam kode aplikasi dan native, kernel GPU, serta tumpukan inferensi.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | Python                                                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **133**    |
| Push terakhir            | 2026-10-11 |
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `benchmarking` · `coding-agents` · `cordis` · `debugging` · `developer-tools` · `dsh` · `dsh-plugin` · `gpu-profiling`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--flameox/2914b7977590380e.png" width="100%" alt="morluto/flameox screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Nwflower/dsh-claude-style">Nwflower/dsh-claude-style</a></b> · ⭐132 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Bintang                  | **132**    |
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
<summary>🧵 <b><a href="https://github.com/Sutera-Diffusus/dsh-whale-musume">Sutera-Diffusus/dsh-whale-musume</a></b> · ⭐120 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

Plugin hewan peliharaan desktop DeepSeek Harness: paus bertenaga Yuanqi menemani Anda menulis kode sebagai maskot dasbor 🐋 Mendukung DSH desktop 0.2.0-rc.2 dan Web versi lama (desktop pet / mascot, local-first)

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | JavaScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **120**    |
| Push terakhir            | 2026-10-11 |
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `ai-assistant` · `ai-companion` · `cordis` · `cute` · `deepseek` · `deepseek-harness` · `desktop-app` · `desktop-mascot`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/sutera-diffusus--dsh-whale-musume/cb85aa05cce65f77.png" width="100%" alt="Sutera-Diffusus/dsh-whale-musume screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/WestFox-AwA/dsh-prompt-optimizer">WestFox-AwA/dsh-prompt-optimizer</a></b> · ⭐113 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

Plugin DSH · pengoptimal injeksi 0.8 (jalur utama): Anda berbicara seperti biasa, lalu setelah Anda mengirim dan sebelum AI menerima, plugin ini memperjelas "apa yang sebenarnya dibutuhkan pada giliran ini", kemudian menyerahkan pemahaman tersebut kepada AI yang bekerja (injeksi konteks) — kata-kata asli tidak ditulis ulang, setiap poin disertai dasar kata demi kata. Mencakup antarmuka kontrol (tingkat/izin/model/konteks/alat hanya-baca), lapisan overlay intersepsi (lapisan pemikiran + lapisan keluaran), serta penggunaan token sebenarnya. Dapat meningkatkan kestabilan kinerja sebagian besar model secara nyata, terutama DeepSeek-V4.1-Flash, dengan peningkatan yang terlihat

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | JavaScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **113**    |
| Push terakhir            | 2026-10-11 |
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `agent-workflow` · `ai-agent` · `cordis` · `deepseek` · `dsh` · `dsh-plugin` · `llm` · `prompt-engineering`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/westfox-awa--dsh-prompt-optimizer/3098cfd264cf8ca0.png" width="100%" alt="WestFox-AwA/dsh-prompt-optimizer screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/JingbiaoMei/Tokdash">JingbiaoMei/Tokdash</a></b> · ⭐85 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

Agent Dashboard: Visualization and analytics for Sessions and Quota Usage. Track, analyze, and optimize token usage across providers with heatmaps, cost tracking, token counting and quota resets..

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | Python                                                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **85**     |
| Push terakhir            | 2026-10-11 |
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `agent` · `analytics` · `anthropic` · `claude-code` · `claude-code-plugin` · `codex` · `codex-cli` · `dashboard`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/jingbiaomei--tokdash/cb7e85100dfe6e93.png" width="100%" alt="JingbiaoMei/Tokdash screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/kukucaiCndy/Corum-Harness">kukucaiCndy/Corum-Harness</a></b> · ⭐66 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Bintang                  | **66**     |
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
<summary>🧵 <b><a href="https://github.com/whyihaveyou/dsh-suite">whyihaveyou/dsh-suite</a></b> · ⭐59 · HTML · 🔎 inferred · 0 天</summary>

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
| Bintang                  | **59**     |
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

dsh-agent-team gives DeepSeek Harness agents that don't reset: durable Members with their own memory, notes, and skills across sessions, rollovers, and restarts. You set the direction; agents coordinate through Channels and Tasks.

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
<summary>🧵 <b><a href="https://github.com/universe-st/dsh-game-material-master">universe-st/dsh-game-material-master</a></b> · ⭐43 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

Plugin master aset game dsh. Terhubung ke model pembuatan gambar seedream dan model pembuatan video minimax, serta dapat menghasilkan berbagai aset game.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | JavaScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **43**     |
| Push terakhir            | 2026-10-11 |
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `chroma-key` · `cordis` · `deepseek-harness` · `dsh-plugin` · `ffmpeg` · `game-assets` · `image-generation` · `koishi`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/universe-st--dsh-game-material-master/9ce5badff3c3ac1c.png" width="100%" alt="universe-st/dsh-game-material-master screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary><b>Lainnya dalam kategori ini</b> <sub>· 67</sub></summary>

- [kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net) - A pre-execution guard for AI coding agents.
- [hashgraph-online/awesome-ai-plugins](https://github.com/hashgraph-online/awesome-ai-plugins) - Daftar pilihan plugin AI terbaik yang luar biasa untuk asisten AI termasuk…
- [imsai-sh/awesome-deepseek-harness-plugins](https://github.com/imsai-sh/awesome-deepseek-harness-plugins) - DeepSeek Harness plugin store, marketplace and hub — 11,000+ dsh plugins with…
- [FishBottle7/opencode2dsh](https://github.com/FishBottle7/opencode2dsh) - Plugin DSH — model OpenCode Zen gratis untuk DeepSeek Harness (DSH).
- [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) - Pasar plugin DSH / DSH Plugin Marketplace: jelajahi, instal, dan perbarui semua…
- [arcships/rutis](https://github.com/arcships/rutis) - Runtime plugin untuk perangkat lunak yang melakukan iterasi sendiri — lapisan…
- [like-study1/Oh-My-DSH](https://github.com/like-study1/Oh-My-DSH) - 🐳 DeepSeek Harness 插件聚合社区 — 自动同步 dsh-plugin 生态 · 精选目录 · 每 4 小时自动维护 | Oh-My-DSH…
- [PensiveFei/dsh-secure-audit](https://github.com/PensiveFei/dsh-secure-audit) - Read-only security &amp; compliance plugin for DeepSeek Harness: prompt-injection…
- [kejixiaoliang/awesome-dsh-plugins](https://github.com/kejixiaoliang/awesome-dsh-plugins) - Direktori pilihan plugin DeepSeek Harness (DSH) — lebih dari 280 plugin…
- [HOWILLMAKEIT/dsh-model-context-catalog](https://github.com/HOWILLMAKEIT/dsh-model-context-catalog) - Plugin DeepSeek Harness: mempertahankan jendela konteks yang akurat untuk model…
- [Vncntvx/dsh-zotero](https://github.com/Vncntvx/dsh-zotero) - Toolkit Zotero untuk DeepSeek harness;
- [KannaKuron/dsh-gitbash-shell](https://github.com/KannaKuron/dsh-gitbash-shell) - Plugin DSH: shell Git Bash untuk semua mode agen di Windows.
- [PensiveFei/deep-read-summarize](https://github.com/PensiveFei/deep-read-summarize) - Alur kerja pembacaan mendalam &amp; peringkasan untuk buku/makalah/video/web…
- [gulagala001/oh-my-dsh](https://github.com/gulagala001/oh-my-dsh) - 让你的 DSH，火力全开。长上下文、任务验证、提示词优化、代码理解、电脑操作与四套完整主题.
- [ZhangFengshun/dsh-remote-ssh](https://github.com/ZhangFengshun/dsh-remote-ssh) - Plugin web DSH: pengembangan jarak jauh serupa VSCode Remote-SSH.
- [NekroAI/nekro-nxt](https://github.com/NekroAI/nekro-nxt) - NekroNXT: sistem agen obrolan grup multi-platform berbasis DeepSeek Harness…
- [omdsh-dev/dsh-office](https://github.com/omdsh-dev/dsh-office) - Paket tiga alat perkantoran! Alat dokumen Office untuk DeepSeek Harness (dsh)…
- [zaofan-make/dsh-qqbot](https://github.com/zaofan-make/dsh-qqbot) - AI 统管 QQ 群组：审核放行、群发文件、沟通其他 web 会话的 AI！ ；气氛组担当：表情包自动入库、AI 自己决定开口、多预设多人格轮班陪聊!
- [dphmoblie/deepseek-harness-android](https://github.com/dphmoblie/deepseek-harness-android) - dsh versi Android: mengintegrasikan DeepSeek Harness, lingkungan runtime…
- [wingsky-1/dsh-plugin-hub](https://github.com/wingsky-1/dsh-plugin-hub) - Kumpulan plugin GUI web DSH (DeepSeek Harness) — notifikasi tugas, penggunaan…
- [gjj-star/dsh-conversation-navigator](https://github.com/gjj-star/dsh-conversation-navigator) - Navigasi sesi DSH.
- [HaoyueQin/dsh-usage-statistics-panel](https://github.com/HaoyueQin/dsh-usage-statistics-panel) - Plugin web DSH: statistik penggunaan token per hari dengan heatmap aktivitas…
- [awesome-deepseekharness/awesome-deepseek-harness](https://github.com/awesome-deepseekharness/awesome-deepseek-harness) - Plugin, alat, skill, dan sumber belajar DeepSeek Harness (dsh) pilihan…
- [CLICGGER-TYPES/dsh-piggy](https://github.com/CLICGGER-TYPES/dsh-piggy) - 🐖 DeepSeek Harness 养成插件，也可作为 Windows/Linux/macOS 桌面宠物运行；支持成长、学习、打工、钓鱼、图鉴与换肤.
- [hyqhyq3/dsh-mcp-manager](https://github.com/hyqhyq3/dsh-mcp-manager) - Plugin pengelola server MCP untuk DeepSeek Harness: halaman Settings → MCP…
- [Wenaixi/dsh-superpower](https://github.com/Wenaixi/dsh-superpower) - Plugin DeepSeek Harness: 15 keterampilan rekayasa obra/superpowers, deskripsi…
- [harrylabsj/kiwi](https://github.com/harrylabsj/kiwi) - Runtime negosiasi perdagangan A2A + plugin DeepSeek Harness (dsh).
- [Imzl-zl/dsh-toolbox-ui](https://github.com/Imzl-zl/dsh-toolbox-ui) - Toolbox panel for DeepSeek Harness Web: MCP manager.
- [mistnest/dsh-cuigengji-plugin](https://github.com/mistnest/dsh-cuigengji-plugin) - Cui Geng Ji: meja kerja novel untuk Da Fei Yu.
- [Y1X1n/dsh-prompt-optimizer](https://github.com/Y1X1n/dsh-prompt-optimizer) - Plugin DeepSeek Harness · Tombol «optimalkan» sekali klik pada bilah pengiriman…
- [liustack/pptwise](https://github.com/liustack/pptwise) - PowerPoint sungguhan, bukan HTML. Beri tahu AI Anda apa yang harus dibahas dan…
- [Roarpeng/GraphFlow](https://github.com/Roarpeng/GraphFlow) - Local-first code knowledge graph and context harness for coding agents.
- [AmethystLuna/embedded-workbench](https://github.com/AmethystLuna/embedded-workbench) - Plugin rekayasa AI Embedded C/C++ — skill firmware.
- [Ianzhyh/workbuddy-to-dsh](https://github.com/Ianzhyh/workbuddy-to-dsh) - 把本机 WorkBuddy 桌面端已登录的模型（DeepSeek / GLM / Kimi / MiniMax 等）变成本地的 OpenAI 与…
- [Sivan757/dsh-agent-plugins-market](https://github.com/Sivan757/dsh-agent-plugins-market) - Pengelola skills, subagen, MCP, dan LSP lengkap untuk DeepSeek Harness (DSH)…
- [WTStarMark/dsh-plugin-mesh](https://github.com/WTStarMark/dsh-plugin-mesh) - 把带 dsh 系列 GitHub 标签的仓库，画成一张可交互的生态网络图.
- [sueccku/dsh-plugin-wps-office-next](https://github.com/sueccku/dsh-plugin-wps-office-next) - 在 DeepSeek Harness（DSH）里用中文对话操作 WPS 表格 / 文字 / 演示：读写数据、排版、公式图表、批量转 PDF.
- [MichaelShii/dsh-plugin-teamflow](https://github.com/MichaelShii/dsh-plugin-teamflow) - dsh plugin teamflow.
- [MicroMilo/upstream-radar](https://github.com/MicroMilo/upstream-radar) - Pengujian kompatibilitas yang selalu aktif untuk plugin DeepSeek Harness: rilis…
- [falling-ts/dsh-force-compact](https://github.com/falling-ts/dsh-force-compact) - Pemadatan konteks agresif untuk agent yang mengutamakan lokal.
- [GooDAnDReaDY/dsh-subscriptions](https://github.com/GooDAnDReaDY/dsh-subscriptions) - OAuth subscription LLM providers for DeepSeek Harness: ChatGPT Codex, Claude…
- [chengshenyangtai/dsh-workbuddy-trae-qoder-connect](https://github.com/chengshenyangtai/dsh-workbuddy-trae-qoder-connect) - 把 WorkBuddy（多账号/企业版）、Trae CN / TRAE SOLO CN、Qoder CN 三家订阅聚合进同一个 DSH…
- [unStone/dsh-xray](https://github.com/unStone/dsh-xray) - X-ray untuk plugin DeepSeek Harness: kapabilitas yang dideklarasikan…
- [zzhang82/Agent-Memory-Bridge](https://github.com/zzhang82/Agent-Memory-Bridge) - Persistent engineering memory for coding agents over MCP.
- [dsh-plugin-lab/dsh-workbuddy-bridge](https://github.com/dsh-plugin-lab/dsh-workbuddy-bridge) - Plugin DSH: menghubungkan model dari aplikasi desktop WorkBuddy ke DeepSeek…
- [lkhfrgc/scholar-llm-wiki](https://github.com/lkhfrgc/scholar-llm-wiki) - Toolkit basis pengetahuan untuk riset dan tinjauan literatur.
- [xbzbing/dsh-git-panel](https://github.com/xbzbing/dsh-git-panel) - DSH 插件：Web GUI 里的 IDE 风格 Git 面板——分支/提交历史总览、变更提交与 amend、文件浏览、代码与图片新旧差异对照、输入框分支标记…
- [xyrrrrr-r/dsh-eval-control](https://github.com/xyrrrrr-r/dsh-eval-control) - Host-side DSH evaluation control plugin for aeval：一次评测试次的配置注入、预算封顶与证据归属.
- [AmethystLuna/logicprobe](https://github.com/AmethystLuna/logicprobe) - Verifikasi klaim desain dan kode: bandingkan klaim faktual dengan kode sumber…
- [cherrchen/dsh-plugin-multi-root-workspace](https://github.com/cherrchen/dsh-plugin-multi-root-workspace) - Workspace multi-folder: memungkinkan Agent DSH (DeepSeek Harness) tidak hanya…
- [PerryLink/dsh-plugin-doctor](https://github.com/PerryLink/dsh-plugin-doctor) - Standar verifikasi tanpa dependensi untuk plugin DeepSeek Harness (dsh)…
- [Retr67/dsh-opencode-models](https://github.com/Retr67/dsh-opencode-models) - DeepSeek Harness (DSH) plugin: one-click OpenCode Go model sync in the settings…
- [umineko987/dsh-search-enhance](https://github.com/umineko987/dsh-search-enhance) - 提供 Grok-compatible 网页搜索、保留来源分页、Context7 与 Exa 文档检索、有界网页提取、站点映射、离线研究计划和只读诊断.
- [viztor/dsh-opencode-patch](https://github.com/viztor/dsh-opencode-patch) - OpenCode di DeepSeek Harness — plugin DSH yang menjaga OpenCode Zen + model…
- [AI-Scarlett/DSH-Store](https://github.com/AI-Scarlett/DSH-Store) - DSH STORE — marketplace plugin pihak ketiga dan pengelola siklus hidup dengan…
- [Atelyx/Atelyx](https://github.com/Atelyx/Atelyx) - Atelyx adalah meja kerja desktop yang dapat diperluas dan berpusat pada…
- [dsh-cc/dsh-cc](https://github.com/dsh-cc/dsh-cc) - Agen coding lengkap untuk DeepSeek Harness — alur kerja bergaya Claude Code…
- [ItQianChen/dsh-github-flow](https://github.com/ItQianChen/dsh-github-flow) - 让 DeepSeek Harness Agent 拥有操作 GitHub 的原生手脚!
- [sakanamaru/dsh-minato](https://github.com/sakanamaru/dsh-minato) - dsh-minato — rangkaian instalasi dan operasi pemeliharaan lokal versi komunitas…
- [SuperWheel/cliworker-now](https://github.com/SuperWheel/cliworker-now) - DeepSeek Harness 多 CLI 智能体侧栏插件：独立对话、账号管理、角色预设与任务续聊.
- [tianyagk/dsh-tradewatcher](https://github.com/tianyagk/dsh-tradewatcher) - Plugin web DeepSeek Harness (DSH): tab sidebar market-dashboard untuk memantau…
- [argszero/cordis-plugin-empty-response-retry](https://github.com/argszero/cordis-plugin-empty-response-retry) - Membuat upaya model kosong tanpa atribusi dapat dicoba ulang, untuk satu celah…
- [eovidiu/cordis-ios](https://github.com/eovidiu/cordis-ios) - Plugin yang membersihkan dirinya sendiri: port Code Swift 6 dari kerangka…
- [Magica-Chen/dsh-preset-codex-claude](https://github.com/Magica-Chen/dsh-preset-codex-claude) - Preset agen DeepSeek Harness: Codex dan Claude Code sebagai subagen delegasi…
- [validation-engineering/cordis-verus](https://github.com/validation-engineering/cordis-verus) - Runtime plugin Rust dengan kernel siklus hidup yang diverifikasi Verus dan…
- [helloHupc/dsh-plugin-hub](https://github.com/helloHupc/dsh-plugin-hub) - DSH 插件聚合站:全网 DeepSeek Harness 插件聚合检索,多源自动去重分类,每小时刷新 |…
- [ArisaYamatogi/dsh-lecture-copilot](https://github.com/ArisaYamatogi/dsh-lecture-copilot) - A Dsh plugin that automatically records, translates lecture and generates notes…

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49934165">Show HN: What&#x27;s Agent Doing – a Claude Code UI mod that explains each step</a></b> · ⭐2 · 👁️ observed · 9 天</summary>

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
| TypeScript | 338   | `anthropics/claude-code`, `anthropics/claude-code-action`, `hamzafer/claude-code-mods`                        |
| JavaScript | 79    | `karanb192/awesome-claude-code-mods`, `karanb192/claude-code-mods`, `ucsandman/claude-harness`                |
| Python     | 40    | `anthropics/claude-agent-sdk-python`, `anthropics/claude-code-security-review`, `alexgreensh/token-optimizer` |
| Shell      | 24    | `anthropics/claude-agent-sdk-typescript`, `0xDarkMatter/claude-mods`, `BeLazy167/claude-mods-skill`           |
| HTML       | 12    | `awss1i/assay`, `darrell-tw/darrelltw-mods`, `omarcevi/claudemods`                                            |
| Go         | 5     | `backstabslash/goccc`, `kylesnowschwartz/tail-claude-hud`, `bunderlog/claude-plugins`                         |
| Rust       | 5     | `persiyanov/herdr-reviewr`, `JairoTorregrosa/claude-statusline`, `OpenClawFarm/claude-statusline`             |
| PowerShell | 2     | `GoSlowPoke168/claude-statusline`, `rainyfei/claude-statusline-win`                                           |
| C          | 1     | `reporails/arcade`                                                                                            |
| C#         | 1     | `sakanamaru/dsh-minato`                                                                                       |
| Kotlin     | 1     | `dphmoblie/deepseek-harness-android`                                                                          |
| Swift      | 1     | `eovidiu/cordis-ios`                                                                                          |

<sub>Hanya entri yang menyatakan bahasa yang dihitung. Entri dokumentasi dan diskusi tidak disertakan dalam tabel ini.</sub>

## Berkontribusi

Koreksi sangat diterima dan merupakan cara tercepat untuk meningkatkan daftar ini. Buka issue atau pull request jika suatu entri salah kategorisasi, salah tingkat, atau jika sebuah proyek keliru dikecualikan karena benturan nama — kategori terakhir itulah yang paling mungkin salah akibat filter otomatis.

---

<sub>Proyek komunitas independen. Tidak berafiliasi dengan, tidak didukung oleh, dan tidak ditinjau oleh Anthropic. Claude Code, Claude, dan Anthropic adalah merek dagang milik Anthropic. Perilaku produk dapat berubah tanpa pemberitahuan; verifikasi hal-hal penting terhadap dokumentasi resmi. Aset tetap menjadi milik proyek upstream masing-masing dan hanya direproduksi jika diizinkan oleh lisensinya.</sub>

<sub>Terakhir diperbarui · 2026-10-11T23:26:48+08:00</sub>
