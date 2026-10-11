<p align="center">
  <img src="../assets/readme/hero.png" width="100%" alt="Mod Claude Keren">
</p>

<h1 align="center">Mod Claude Keren</h1>

<p align="center"><b>Indeks mod Claude Code, plugin, dan perubahan perilaku mendalam yang ditimbulkannya, dengan pemeringkatan berdasarkan bukti.</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-506-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="../LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
  <a href="https://wh000wh000.github.io/awesome-claude-mods/"><img src="https://img.shields.io/badge/site-searchable-1f6feb" alt="site"></a>
</p>

<p align="center"><sub><a href="../README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.pt-BR.md">Português</a> · <a href="README.ru.md">Русский</a> · <a href="README.it.md">Italiano</a> · <a href="README.ar.md">العربية</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.tr.md">Türkçe</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <b>Bahasa Indonesia</b> · <a href="README.pl.md">Polski</a> · <a href="README.nl.md">Nederlands</a> · <a href="README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **Indeks aktif** · Sinkronisasi terakhir: `2026-10-11T21:12:49+08:00` (UTC+8)
> · Entri: **506** · Ditambahkan pada pembaruan terbaru: **0** · Bahasa implementasi: **12**

<sub>Setiap entri di bawah dikumpulkan, difilter, dan diperiksa ulang secara otomatis. Tidak ada konten berbayar di sini.</sub>

<a id="featured"></a>

## Pilihan saat ini

<sub>Satu entri per kategori, diurutkan berdasarkan tingkat bukti dan jumlah bintang, lalu dihitung ulang setiap kali diperbarui. Ini adalah pemeringkatan, bukan dukungan; setiap pilihan tertaut ke kartu lengkapnya di bawah. Proyek yang memublikasikan tangkapan layar atau rekaman lebih diutamakan agar panel ini tetap visual.</sub>

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
<sub>Temukan token hantu. Perbaiki. Bertahan dari kompaksi. Hindari penurunan kualitas konteks.</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo">
<b>🧵 <a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b>
<sub>⭐74325 · TypeScript · 👁️ observed</sub>
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
- [Resmi: repositori dan catatan rilis milik Anthropic sendiri](#resmi-repositori-dan-catatan-rilis-milik-anthropic-sendiri) — **15**
- [Mod: dibuat dengan kemampuan mod](#mod-dibuat-dengan-kemampuan-mod) — **381**
- [Ekosistem plugin DSH dan Cordis](#ekosistem-plugin-dsh-dan-cordis) — **99**
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
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></b> · ⭐150151 · TypeScript · ✅ official · 0 天</summary>

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
| Bintang                  | **150151** |
| Push terakhir            | 2026-10-10 |
| Pertama kali dicantumkan | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b> · ⭐9473 · TypeScript · ✅ official · 1 天</summary>

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
| Bintang                  | **9473**   |
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

An AI-powered security review GitHub Action using Claude to analyze code changes for security vulnerabilities.

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

Supplementary materials for Claude Model Cards

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
<summary><b>Lainnya dalam kategori ini</b> <sub>· 3</sub></summary>

- [Claude Code 2.1.295 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Menambahkan `$.ui.notify` untuk mod: memunculkan notifikasi native melalui…
- [Claude Code 2.1.296 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Memperbaiki Esc atau interupsi selama hook `UserPromptSubmit` atau hook…
- [riffkit/skill](https://github.com/riffkit/skill) - Official Riffkit skill — riff a winning TikTok into your own short video from…

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
<summary>🧩 <b><a href="https://github.com/karanb192/awesome-claude-code-mods">karanb192/awesome-claude-code-mods</a></b> · ⭐484 · JavaScript · 👁️ observed · 0 天</summary>

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
| Bintang                  | **484**    |
| Push terakhir            | 2026-10-11 |
| Pertama kali dicantumkan | 2026-10-04 |

🏷 `anthropic` · `awesome` · `awesome-list` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/cache-tax">karanb192/cache-tax</a></b> · ⭐127 · TypeScript · 👁️ observed · 7 天</summary>

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
| Bintang                  | **127**    |
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
<summary>🧩 <b><a href="https://github.com/hellosverre/claude-skins">hellosverre/claude-skins</a></b> · ⭐93 · TypeScript · 👁️ observed · 0 天</summary>

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
| Bintang                  | **93**     |
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
<summary>🧩 <b><a href="https://github.com/karanb192/claude-code-mods">karanb192/claude-code-mods</a></b> · ⭐40 · JavaScript · 👁️ observed · 7 天</summary>

##### 📝 Ringkasan

Mod Claude dan alat untuk membangunnya: skill builder, lalu mod

<sub>🔧 Ditemukan digunakan dalam kode: `plugins/mod-builder/skills/mod-builder/references/migrate.md`, `plugins/mod-builder/skills/mod-builder/references/nouns.md`</sub>

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Mod: dibuat dengan kemampuan mod`                                |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |
| Bahasa   | JavaScript                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **40**     |
| Push terakhir            | 2026-10-03 |
| Pertama kali dicantumkan | 2026-10-04 |

🏷 `claude` · `claude-code` · `claude-code-plugin` · `claude-mods` · `function-hooks` · `prompt-caching`

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
<summary>🧩 <b><a href="https://github.com/iamumeransari/claude-show-your-work">iamumeransari/claude-show-your-work</a></b> · ⭐24 · TypeScript · 👁️ observed · 0 天</summary>

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
| Bintang                  | **24**     |
| Push terakhir            | 2026-10-11 |
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/iamumeransari--claude-show-your-work/9ee7df00aee28636.jpg" width="100%" alt="iamumeransari/claude-show-your-work screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/iamumeransari--claude-show-your-work/adcbff13953c23f1.gif" width="100%" alt="iamumeransari/claude-show-your-work animation"><br><sub>rekaman animasi</sub></td>
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
<summary>🧩 <b><a href="https://github.com/markneonin/paneline">markneonin/paneline</a></b> · ⭐6 · TypeScript · 👁️ observed · 4 天</summary>

##### 📝 Ringkasan

Mod (plugin) Claude Code yang menambahkan panel samping dengan tab Activity, Files, Agents, Context, dan MCP, baris status di atas prompt, chat yang ditata ulang, diagram Mermaid di terminal, tabel, serta panel kode dan diff. Warna mengikuti /color dan /theme (dark, light, dan lainnya).

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
| Push terakhir            | 2026-10-06 |
| Pertama kali dicantumkan | 2026-10-10 |

🏷 `ai-agents` · `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mod` · `claude-code-mods`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/markneonin--paneline/e7976a2ea941fd17.png" width="100%" alt="markneonin/paneline screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Shuffzord/RoadRaven">Shuffzord/RoadRaven</a></b> · ⭐6 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Ringkasan

Rencana Anda, yang memantau dirinya sendiri. Pohon roadmap desktop lokal yang terus diperbarui secara langsung oleh Claude Code dan host MCP apa pun. JSON biasa, tanpa cloud.

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
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `ai-agents` · `bun` · `claude-code` · `claude-code-mod` · `claude-code-plugin` · `desktop-app` · `electrobun` · `local-first`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Shuffzord/RoadRaven/master/screenshots/events.png" width="100%" alt="Shuffzord/RoadRaven screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

<sub>Aset ditautkan langsung dari repositori upstream karena tidak ada lisensi yang mengizinkan redistribusi yang dinyatakan.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/leopiney/wolfbud-claude-mod">leopiney/wolfbud-claude-mod</a></b> · ⭐5 · TypeScript · 👁️ observed · 2 天</summary>

##### 📝 Ringkasan

Rekan kerja suara untuk Claude Code. Bicarakan berbagai hal dengan serigala 3D yang didukung AI percakapan ElevenLabs; ketika Anda setuju, ia mengirimkan prompt ke Claude dan berbicara saat Claude selesai.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Mod: dibuat dengan kemampuan mod`                                |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |
| Bahasa   | TypeScript                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **5**      |
| Push terakhir            | 2026-10-08 |
| Pertama kali dicantumkan | 2026-10-10 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin` · `claude-mods`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/leopiney/wolfbud-claude-mod/main/assets/banner.png" width="100%" alt="leopiney/wolfbud-claude-mod screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

<sub>Aset ditautkan langsung dari repositori upstream karena tidak ada lisensi yang mengizinkan redistribusi yang dinyatakan.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/HMarzban/claude-mod">HMarzban/claude-mod</a></b> · ⭐4 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Ringkasan

Lihat biaya pesan Claude Code Anda berikutnya: bilah langsung di atas prompt dengan hitung mundur prompt-cache, harga pemanasan ulang, biaya sesi, konteks, serta batas penggunaan 5 jam/mingguan.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Mod: dibuat dengan kemampuan mod`                                |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |
| Bahasa   | TypeScript                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **4**      |
| Push terakhir            | 2026-10-11 |
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `anthropic` · `claude` · `claude-ai` · `claude-code` · `claude-code-plugin` · `claude-mod` · `cost-tracking` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hmarzban--claude-mod/680a1325dcf966ff.gif" width="100%" alt="HMarzban/claude-mod screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hmarzban--claude-mod/680a1325dcf966ff.gif" width="100%" alt="HMarzban/claude-mod animation"><br><sub>rekaman animasi</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/dominicrico/jev-router">dominicrico/jev-router</a></b> · ⭐3 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Ringkasan

Plugin Claude Code: perutean model Claude otomatis. Memilih Haiku, Sonnet, atau Opus serta upaya penalaran untuk setiap prompt, langkah, dan subagent; batas upaya, pelindung cache prompt, pita status, dan tolok ukur.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Mod: dibuat dengan kemampuan mod`                                |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |
| Bahasa   | TypeScript                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **3**      |
| Push terakhir            | 2026-10-10 |
| Pertama kali dicantumkan | 2026-10-09 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-marketplace` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dominicrico--jev-router/e9ab68584ed9c404.jpg" width="100%" alt="dominicrico/jev-router screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dominicrico--jev-router/2a6620c49438b369.gif" width="100%" alt="dominicrico/jev-router animation"><br><sub>rekaman animasi</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/FynnXland/fynn-mods">FynnXland/fynn-mods</a></b> · ⭐3 · TypeScript · 👁️ observed · 1 天</summary>

##### 📝 Ringkasan

Enam mod untuk Claude Code: maskot Clawd animasi, bar batas penggunaan dan prompt-cache, pemeriksa pesan pra-kirim, balasan cepat, antrean to-do, dan buku besar biaya. Aplikasi terminal dan desktop, Inggris/Jerman.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Mod: dibuat dengan kemampuan mod`                                |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |
| Bahasa   | TypeScript                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **3**      |
| Push terakhir            | 2026-10-09 |
| Pertama kali dicantumkan | 2026-10-07 |

🏷 `ai-coding-assistant` · `claude` · `claude-ai` · `claude-code` · `claude-code-marketplace` · `claude-code-mods` · `claude-code-plugin` · `claude-code-plugins`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/fynnxland--fynn-mods/46068e3739e61a25.gif" width="100%" alt="FynnXland/fynn-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/fynnxland--fynn-mods/46068e3739e61a25.gif" width="100%" alt="FynnXland/fynn-mods animation"><br><sub>rekaman animasi</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/mertkayacs/ultramod">mertkayacs/ultramod</a></b> · ⭐3 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Ringkasan

Paket mod serba ada terbaik untuk Claude Code: batas penggunaan dan HUD konteks, pelindung dengan pembatalan untuk rm -rf dan git reset --hard, perlindungan .env dan rahasia, serta tanda terima untuk setiap giliran. Sepuluh mod, satu instalasi.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Mod: dibuat dengan kemampuan mod`                                |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |
| Bahasa   | TypeScript                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **3**      |
| Push terakhir            | 2026-10-10 |
| Pertama kali dicantumkan | 2026-10-09 |

🏷 `ai-agents` · `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/mertkayacs--ultramod/0f9d8b2253819dc8.gif" width="100%" alt="mertkayacs/ultramod screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/mertkayacs--ultramod/1537defa7233d7f2.gif" width="100%" alt="mertkayacs/ultramod animation"><br><sub>rekaman animasi</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/mthli/cc-shorts">mthli/cc-shorts</a></b> · ⭐3 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Ringkasan

Putar YouTube Shorts di Claude Code Anda 💃

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Mod: dibuat dengan kemampuan mod`                                |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |
| Bahasa   | TypeScript                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **3**      |
| Push terakhir            | 2026-10-02 |
| Pertama kali dicantumkan | 2026-10-10 |

🏷 `claude-mods` · `youtube-shorts`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/mthli--cc-shorts/ef652fff732c023d.png" width="100%" alt="mthli/cc-shorts screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/chenyuxiaojin/cyxj-notch">chenyuxiaojin/cyxj-notch</a></b> · ⭐2 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Ringkasan

Dasbor notch macOS untuk Claude Code: batas penggunaan, sesi terbuka, progres tugas, hitung mundur cache prompt, dan daftar tugas — disuplai oleh lima mod Claude Code (termasuk).

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Mod: dibuat dengan kemampuan mod`                                |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |
| Bahasa   | TypeScript                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **2**      |
| Push terakhir            | 2026-10-11 |
| Pertama kali dicantumkan | 2026-10-10 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `developer-tools` · `dynamic-island` · `macos` · `menu-bar`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/chenyuxiaojin--cyxj-notch/61834d73bebe8659.gif" width="100%" alt="chenyuxiaojin/cyxj-notch screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/chenyuxiaojin--cyxj-notch/61834d73bebe8659.gif" width="100%" alt="chenyuxiaojin/cyxj-notch animation"><br><sub>rekaman animasi</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Christandoh/context-cache">Christandoh/context-cache</a></b> · ⭐2 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Ringkasan

Claude Code mod: context usage, session / weekly / Fable limits and prompt-cache temperature above the prompt

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Mod: dibuat dengan kemampuan mod`                                |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |
| Bahasa   | TypeScript                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **2**      |
| Push terakhir            | 2026-10-11 |
| Pertama kali dicantumkan | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/christandoh--context-cache/3cdd3b2c5a09da7d.png" width="100%" alt="Christandoh/context-cache screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/CodyAMaughan/meme-factory">CodyAMaughan/meme-factory</a></b> · ⭐2 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Ringkasan

Baru keluar dari pabrik. Mod Claude Code: minta meme, lalu terus bekerja. Draf diproses di panel samping; pilih, remix, setujui, dan kirim ke Slack.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Mod: dibuat dengan kemampuan mod`                                |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |
| Bahasa   | JavaScript                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **2**      |
| Push terakhir            | 2026-10-10 |
| Pertama kali dicantumkan | 2026-10-09 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `developer-tools` · `fun` · `meme-generator` · `memes` · `slack`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/codyamaughan--meme-factory/7417dc8940c4a087.png" width="100%" alt="CodyAMaughan/meme-factory screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/codyamaughan--meme-factory/8c9d44287267796f.gif" width="100%" alt="CodyAMaughan/meme-factory animation"><br><sub>rekaman animasi</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/estruyf/claude-stats-mod">estruyf/claude-stats-mod</a></b> · ⭐2 · JavaScript · 👁️ observed · 8 天</summary>

##### 📝 Ringkasan

Mod Claude Code yang menggambar batas penggunaan dan pengeluaran Anda di bilah di atas prompt.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Mod: dibuat dengan kemampuan mod`                                |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |
| Bahasa   | JavaScript                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **2**      |
| Push terakhir            | 2026-10-02 |
| Pertama kali dicantumkan | 2026-10-10 |

🏷 `claude` · `claude-code` · `claude-mod` · `claude-mods`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/estruyf/claude-stats-mod/main/assets/desktop.png" width="100%" alt="estruyf/claude-stats-mod screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

<sub>Aset ditautkan langsung dari repositori upstream karena tidak ada lisensi yang mengizinkan redistribusi yang dinyatakan.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/i-harsha-reddy/naruto-mod">i-harsha-reddy/naruto-mod</a></b> · ⭐2 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Ringkasan

Pendamping Naruto bergaya pixel-art untuk Claude Code: 20 ninja, 60 jutsu, dilakukan saat Claude bekerja

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Mod: dibuat dengan kemampuan mod`                                |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |
| Bahasa   | TypeScript                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **2**      |
| Push terakhir            | 2026-10-10 |
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `naruto` · `pixel-art`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/i-harsha-reddy--naruto-mod/c4048227757840cb.gif" width="100%" alt="i-harsha-reddy/naruto-mod screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/i-harsha-reddy--naruto-mod/c4048227757840cb.gif" width="100%" alt="i-harsha-reddy/naruto-mod animation"><br><sub>rekaman animasi</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/lorenzh/rabe">lorenzh/rabe</a></b> · ⭐2 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Ringkasan

Lihat apa yang dijalankan Claude Code di latar belakang: subagen, pekerjaan Codex, shell, monitor, tugas cron, dan workflow.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Mod: dibuat dengan kemampuan mod`                                |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |
| Bahasa   | TypeScript                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **2**      |
| Push terakhir            | 2026-10-11 |
| Pertama kali dicantumkan | 2026-10-09 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/lorenzh--rabe/1c67cab3774edaee.gif" width="100%" alt="lorenzh/rabe screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/lorenzh--rabe/1c67cab3774edaee.gif" width="100%" alt="lorenzh/rabe animation"><br><sub>rekaman animasi</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/macleodlabs-ai/claudeflow">macleodlabs-ai/claudeflow</a></b> · ⭐2 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Ringkasan

Mod Claude Code oleh MacLeod Labs: streams mengurai pekerjaan sesi yang saling bersilangan menjadi stream berkode warna

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Mod: dibuat dengan kemampuan mod`                                |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |
| Bahasa   | TypeScript                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **2**      |
| Push terakhir            | 2026-10-11 |
| Pertama kali dicantumkan | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/macleodlabs-ai/claudeflow/main/assets/hero.jpg" width="100%" alt="macleodlabs-ai/claudeflow screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

<sub>Aset ditautkan langsung dari repositori upstream karena tidak ada lisensi yang mengizinkan redistribusi yang dinyatakan.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/MankhongGarden/claude-code-mods-field-notes">MankhongGarden/claude-code-mods-field-notes</a></b> · ⭐2 · TypeScript · 👁️ observed · 1 天</summary>

##### 📝 Ringkasan

Catatan lapangan hari pertama tentang mod Claude Code di Windows: bilah bahan bakar konteks/kuota, mod UI Thai, intro boot Matrix dan pembaru aman, plus apa yang gagal dan mengapa (panel, pita di atas prompt, Thai di Windows Terminal).

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Mod: dibuat dengan kemampuan mod`                                |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |
| Bahasa   | TypeScript                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **2**      |
| Push terakhir            | 2026-10-09 |
| Pertama kali dicantumkan | 2026-10-07 |

🏷 `anthropic` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `claude-mods` · `developer-tools` · `function-hooks`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/mankhonggarden--claude-code-mods-field-notes/832ffcdb7bad9007.png" width="100%" alt="MankhongGarden/claude-code-mods-field-notes screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary><b>Lainnya dalam kategori ini</b> <sub>· 347</sub></summary>

- [rashedInt32/glass](https://github.com/rashedInt32/glass) - Tampilan aplikasi desktop untuk transkrip terminal Claude Code, sebagai mod.
- [xuanji86/claude-agentpane](https://github.com/xuanji86/claude-agentpane) - Panel samping untuk Claude Code: subagen yang dijalankan sesi, apa yang sedang…
- [letswritetw/claude-mod-open-todos](https://github.com/letswritetw/claude-mod-open-todos) - Panel bilah samping Claude Desktop (tab Code): mencantumkan semua tugas…
- [letswritetw/claude-mod-token-usage](https://github.com/letswritetw/claude-mod-token-usage) - Bilah penggunaan di atas kotak input Claude Desktop (tab Code): kuota 5j / 7h…
- [omarcevi/claudemods](https://github.com/omarcevi/claudemods) - Mod, plugin &amp; skill Claude komunitas, dapat diinstal dari satu marketplace.
- [eighteyes/cactus](https://github.com/eighteyes/cactus) - Antrean keputusan CLI/TUI untuk manusia yang bekerja dengan agen percakapan.
- [xuanji86/claude-statuspane](https://github.com/xuanji86/claude-statuspane) - Kartu status mengambang untuk Claude Code—model, konteks, batas laju, biaya…
- [xuanji86/claude-mdview](https://github.com/xuanji86/claude-mdview) - Baca file markdown yang diberi nama oleh Claude Code, tampilkan di samping…
- [atomashevic/claude-latex-math](https://github.com/atomashevic/claude-latex-math) - Claude Code mod that typesets the LaTeX math in Claude.
- [charimsma/dopa-mode](https://github.com/charimsma/dopa-mode) - Kembang api untuk Claude Code: setiap penekanan tombol, pemanggilan tool…
- [ha-ptt0601/cc-mods](https://github.com/ha-ptt0601/cc-mods) - Mod Claude Code kecil (plugin function-hook): session-switcher dan lainnya.
- [ice-lfernandes/claude-code-mods](https://github.com/ice-lfernandes/claude-code-mods) - Enam mod Claude Code: batas rencana dan konteks di atas prompt, pelatih daftar…
- [NarenDawar/narens-claude-toolkit](https://github.com/NarenDawar/narens-claude-toolkit) - Toolkit Claude milik Naren: skills, mods, dan servers MCP untuk Claude Code.
- [neteye-platform/cc-split-diff-view](https://github.com/neteye-platform/cc-split-diff-view) - Mod Claude Code yang menggambar perbedaan Edit dan Write dalam dua kolom…
- [testy-cool/awesome-claude-code-mods](https://github.com/testy-cool/awesome-claude-code-mods) - Daftar pilihan mod Claude Code yang dapat dipasang sebagai pasar plugin: tema…
- [xsyetopz/dotclaude](https://github.com/xsyetopz/dotclaude) - Plugin Claude Code yang sangat berpendirian, dirancang oleh seorang Rustacean…
- [ArgonQQ/sipp](https://github.com/ArgonQQ/sipp) - 💧 Pengingat air pasif-agresif untuk Claude Code. Nol token, penilaian maksimum.
- [herman925/925-cc-plugins](https://github.com/herman925/925-cc-plugins) - Mod Claude Code milik Herman (marketplace herman-mods).
- [patitow/claude-mod-cost-visibility](https://github.com/patitow/claude-mod-cost-visibility) - Mod Claude Code: meter biaya langsung, konteks &amp; kuota paket di atas prompt.
- [rbartoli/agent-usage-guard](https://github.com/rbartoli/agent-usage-guard) - Mod Claude Code yang menahan fan-out subagent, prompt konteks berat, dan loop…
- [shimo4228/harness-scope](https://github.com/shimo4228/harness-scope) - Mod Claude Code yang mengaktifkan atau menonaktifkan skill, agen, aturan, dan…
- [simplecore-inc/claude-mods](https://github.com/simplecore-inc/claude-mods) - Plugin Claude Code (mod): beralih di antara beberapa akun Claude, memantau…
- [Singh-AP/awesome-claude-mods](https://github.com/Singh-AP/awesome-claude-mods) - 🧩 Mod Claude Code yang telah diuji dan dapat dipasang dengan satu perintah…
- [smukh/roll-credits](https://github.com/smukh/roll-credits) - Kredit bergaya film untuk sesi coding Anda.
- [yodakeisuke/claudelingo](https://github.com/yodakeisuke/claudelingo) - Pelajari bahasa asing sambil bekerja dengan Claude Code.
- [alaturqua/tower-mods](https://github.com/alaturqua/tower-mods) - Claude Code mods for running many sessions across many repos from one control…
- [alexlifexyz/p3c-guard](https://github.com/alexlifexyz/p3c-guard) - Saat Agen menulis Java, kode yang melanggar aturan Alibaba Java (p3c) tidak…
- [andrewbakercloudscale/claude-code-cost-sidebar](https://github.com/andrewbakercloudscale/claude-code-cost-sidebar) - Sidebar biaya, token, dan penggunaan konteks live untuk Claude Code: mod yang…
- [aosmcleod/next-up-mod](https://github.com/aosmcleod/next-up-mod) - Mod Claude Code: backlog tindak lanjut yang disarankan Claude di seluruh sesi…
- [BjoernSchotte/ccmod-amp](https://github.com/BjoernSchotte/ccmod-amp) - Radio internet di dalam Claude Code: sidebar cliamp, pemutar mini, favorit…
- [Bocskay-Botond/claude-code-mods](https://github.com/Bocskay-Botond/claude-code-mods) - Fun, useful Claude Code mods: a pixel critter above your prompt, a tools menu…
- [chrisluo5311/squad-chat](https://github.com/chrisluo5311/squad-chat) - Claude sedang memasak. Chat dengan skuad Anda.
- [crebot51/jack-mods](https://github.com/crebot51/jack-mods) - Kumpulan mod Claude Code milik jack.
- [danielpg95/modster-hunter](https://github.com/danielpg95/modster-hunter) - Mod Claude Code: tangkap Modsters pixel-art dalam game idle saat Claude bekerja.
- [darkomarijaan/nexus-mod](https://github.com/darkomarijaan/nexus-mod) - Mod Claude Code all-in-one: HUD langsung, perlindungan keamanan.
- [DarkVelours/claude-code-galactic-battle](https://github.com/DarkVelours/claude-code-galactic-battle) - Pertempuran luar angkasa di atas prompt Claude Code saat sedang bekerja.
- [Davron2004/slash-coverage](https://github.com/Davron2004/slash-coverage) - Lihat file mana yang ada dalam konteks setiap agen Claude Code, dan seberapa…
- [drakulavich/cogload](https://github.com/drakulavich/cogload) - Tetap tenang. Termometer untuk hari-hari Claude Code Anda: setiap jam diberi…
- [EgonLeitner/dashband](https://github.com/EgonLeitner/dashband) - Batas prompt cache, konteks, dan rencana untuk Claude Code sekilas, di footer…
- [ElirazKed/claude-code-pr-watch](https://github.com/ElirazKed/claude-code-pr-watch) - Mod Claude Code: panel langsung berisi PR GitHub yang dibuka atau didorong oleh…
- [enhki/claude-mods](https://github.com/enhki/claude-mods) - Mod kecil Claude Code untuk terminal dan aplikasi desktop.
- [ewxgwy1987/claude-code-mods](https://github.com/ewxgwy1987/claude-code-mods) - Kumpulan mod Claude Code, masing-masing di repositorinya sendiri: usage-meter…
- [ewxgwy1987/claude-code-progress-board](https://github.com/ewxgwy1987/claude-code-progress-board) - Mod Claude Code: panel kemajuan untuk tugas, subagen, proses alur kerja…
- [ewxgwy1987/claude-code-session-toc](https://github.com/ewxgwy1987/claude-code-session-toc) - Mod Claude Code: daftar isi seluruh sesi yang dapat diklik dan memiliki stempel…
- [ewxgwy1987/claude-code-usage-meter](https://github.com/ewxgwy1987/claude-code-usage-meter) - Mod Claude Code: batas laju rencana, isi konteks, biaya sesi, dan token per…
- [Exdenta/ambient-spanish](https://github.com/Exdenta/ambient-spanish) - Skill + mod Claude CLI yang menambahkan kata-kata Spanyol ke balasan agen.
- [FrBmt-BIGetNouf/alarum-claude-mod](https://github.com/FrBmt-BIGetNouf/alarum-claude-mod) - Sematkan Alarum.me di kode Claude CLI atau Desktop Anda.
- [FrBmt-BIGetNouf/floatee-claude-mod](https://github.com/FrBmt-BIGetNouf/floatee-claude-mod) - Your Floatee backlog above Claude Code.
- [GoneTone/cc-askpass](https://github.com/GoneTone/cc-askpass) - A Claude Code mod that lets Claude run commands that need sudo, instead of…
- [gonzalonicolasr/claude-code-nerv](https://github.com/gonzalonicolasr/claude-code-nerv) - Bilah samping bergaya Evangelion untuk Claude Code: konteks, kuota, aktivitas…
- [gregdotca/ccmod-the-machine](https://github.com/gregdotca/ccmod-the-machine) - Mod kode Claude yang menata ulang tampilannya menjadi The Machine dari Person…
- [HyunjunJeon/claude-workflow-mods](https://github.com/HyunjunJeon/claude-workflow-mods) - dag-workflow: mod Claude Code untuk alur kerja DAG subagent yang wajib dan…
- [ibrahimkobeissy/claude-mods](https://github.com/ibrahimkobeissy/claude-mods) - Mod sumber terbuka untuk Claude Code: panel, baris status, toast, penjaga alat…
- [jonyfs/astrolabe](https://github.com/jonyfs/astrolabe) - 🧭 Mod Claude Code: status sesi, kemajuan Spec Kit live, dan tata kelola jendela…
- [kongyo2/context-view](https://github.com/kongyo2/context-view) - Jendela konteks sebagai satu baris di atas prompt, digambar seperti meter milik…
- [kyledarling-io/claude-code-desktop-hud](https://github.com/kyledarling-io/claude-code-desktop-hud) - HUD tugas langsung untuk Claude Code Desktop: strip di atas prompt saat Claude…
- [m4cd4r4/clear-resume](https://github.com/m4cd4r4/clear-resume) - Plugin gratis dan open-source untuk Claude Code.
- [Mechazawa/claude-inline-images](https://github.com/Mechazawa/claude-inline-images) - Claude Code mod that shows images inline in Ghostty and kitty.
- [meganemura/pull-request-pane](https://github.com/meganemura/pull-request-pane) - Mod Claude yang menampilkan pull request GitHub milik sesi dalam panel di…
- [NotRedFox/NotRedFoxs-Claude-skills](https://github.com/NotRedFox/NotRedFoxs-Claude-skills) - Keahlian Claude Code: pemeriksa fakta dokumen, auditor kode, log memori bug…
- [pepperonas/loc-today](https://github.com/pepperonas/loc-today) - Mod Claude Code: baris kode hari ini oleh Claude — baru, diedit, dihapus — di…
- [pepperonas/path-links](https://github.com/pepperonas/path-links) - Mod Claude Code: jalur yang dapat diklik dalam balasan — klik folder untuk…
- [peterlimg/auto-effort](https://github.com/peterlimg/auto-effort) - Mod Claude Code: memilih /effort untuk setiap prompt dengan Jev.
- [rezzminator/buddy](https://github.com/rezzminator/buddy) - Plugin teman Claude Code: pendamping ASCII di atas prompt Anda yang mengingat…
- [roma-vibe/jev-governor](https://github.com/roma-vibe/jev-governor) - Claude Code mod: Jev-guided model/effort routing, verbatim context compaction…
- [samfrmr/barmkin-mod](https://github.com/samfrmr/barmkin-mod) - Mod Code Claude: lapisan keamanan untuk Code Claude — penyamaran rahasia…
- [Sennjen/claude-sdlc](https://github.com/Sennjen/claude-sdlc) - Plugin dan mod Claude Code: SDLC AI-native.
- [SeongGwangJu/k-mods](https://github.com/SeongGwangJu/k-mods) - Koleksi mod Claude Code yang luar biasa | Koleksi mod Claude Code.
- [soulrocha/Claude-code-hero-journey](https://github.com/soulrocha/Claude-code-hero-journey) - 🦀 Mod HUD RPG yang nyaman untuk Claude Code.
- [tanujarun/it-speaks](https://github.com/tanujarun/it-speaks) - It Speaks: mod Claude Code yang membacakan balasan Claude dan prompt Anda saat…
- [timoncool/givememod](https://github.com/timoncool/givememod) - Mod Code Claude sesuai permintaan — keterampilan yang membaca percakapan Anda…
- [timoncool/slapbox](https://github.com/timoncool/slapbox) - 🍑 Pukul Claude saat ia melakukan kesalahan — mod pelepas stres untuk Claude…
- [TroyJLorents-GH/mod-squad](https://github.com/TroyJLorents-GH/mod-squad) - Mod Claude Code: plugin kecil untuk panel langsung, pengaturan perutean model…
- [valeryia-piatrova/token-hamster](https://github.com/valeryia-piatrova/token-hamster) - 🐹 Mod &amp; plugin Claude Code: monitor penggunaan, pelacak token &amp; baris status.
- [vumichien/claude-code-mods-kit](https://github.com/vumichien/claude-code-mods-kit) - Tiga mod Code Claude gratis: menyembunyikan nilai .env dari hasil alat…
- [y-hirakaw/claude-code-mods](https://github.com/y-hirakaw/claude-code-mods) - Mod Claude Code. touch-map: lihat berkas mana yang dicantumkan, dibaca, diedit…
- [0xnicholasy/claude-mods](https://github.com/0xnicholasy/claude-mods) - Marketplace plugin Claude Code untuk mod milik 0xnicholasy.
- [akixi-maison/usage-mods](https://github.com/akixi-maison/usage-mods) - Mod Code Claude: bilah kemajuan penggunaan (konteks, 5j, 7h) dan tombol ringkas…
- [alan-oliv/claude-mods](https://github.com/alan-oliv/claude-mods) - Mod Code Claude: kartu statistik sesi di atas perintah.
- [Aler1x/claude-cat](https://github.com/Aler1x/claude-cat) - Kucing braille animasi di atas prompt Claude Code.
- [alinaqi/mixture-of-models-claude-mod](https://github.com/alinaqi/mixture-of-models-claude-mod) - Mod Claude Code: mengarahkan pekerjaan ringan ke GLM/Kimi melalui Claude Code…
- [aloki-alok/omni-cat](https://github.com/aloki-alok/omni-cat) - Kucing piksel di atas prompt Code Claude Anda yang menjalankan panggilan uji…
- [ambervdberg/smartcompact](https://github.com/ambervdberg/smartcompact) - Mod Claude Code yang memilih waktu yang tepat untuk melakukan pemadatan agar…
- [an80sPWNstar/claude-mods](https://github.com/an80sPWNstar/claude-mods) - Mod Claude untuk Claude Code: token-meter.
- [anderson-spider/claude-mods](https://github.com/anderson-spider/claude-mods) - Marketplace plugin Code Claude oleh anderson-spider.
- [andras-gyarmati/claude-quota-band](https://github.com/andras-gyarmati/claude-quota-band) - Mod Claude Code: penggunaan 5 jam dan mingguan dari rencana Anda sebagai satu…
- [androidZzT/claude-trading-mods](https://github.com/androidZzT/claude-trading-mods) - Mod Code Claude untuk memantau pasar dari terminal: panel A股/港股/美股 dengan tren…
- [angomedia/claude-mods](https://github.com/angomedia/claude-mods) - Mod untuk Code Claude.
- [arslan-charyyev/claude-mods](https://github.com/arslan-charyyev/claude-mods) - Mod Claude Code pribadi saya.
- [Ashley-Pettit/lgtm-flash](https://github.com/Ashley-Pettit/lgtm-flash) - Kapal LGTM Lines berlayar melewati setelah setiap perubahan kode — mod Code…
- [Ashley-Pettit/villager-hp](https://github.com/Ashley-Pettit/villager-hp) - Your Claude usage limits as an animated villager health card, with a weekly…
- [AskTinNguyen/ather-mods](https://github.com/AskTinNguyen/ather-mods) - Mod Claude Code untuk tim S2 (marketplace ather).
- [Atanur/deskfit](https://github.com/Atanur/deskfit) - Latihan singkat saat Claude bekerja: target harian, streak, badge, dan…
- [atharv6f/waypoint](https://github.com/atharv6f/waypoint) - Kemajuan rencana, tugas, dan agen di samping perintah Code Claude — mod Code…
- [aycandv/claude-usage-meter](https://github.com/aycandv/claude-usage-meter) - Papan penggunaan untuk Claude Code: pengeluaran per model.
- [barneym/claude-context-bar](https://github.com/barneym/claude-context-bar) - Mod Claude Code: uraian live context-window di atas prompt.
- [bastianfuchs/claude-code-cache-warm](https://github.com/bastianfuchs/claude-code-cache-warm) - Claude Code mod that shows the prompt-cache countdown in the footer and keeps…
- [benjaminr/nowplaying](https://github.com/benjaminr/nowplaying) - Mod Now Playing untuk Claude Code: Apple Music dan Spotify di atas prompt…
- [bitcars/ctx-bar](https://github.com/bitcars/ctx-bar) - ctx-bar: a Claude Code mod that keeps the context window visible at all times.
- [broening/claude-mods](https://github.com/broening/claude-mods) - Mod untuk Claude Code: Cache-Uhr, Blast Radius, Vorschlaege, Arbeitsliste, Grill.
- [Carismarkus/clowl](https://github.com/Carismarkus/clowl) - Hanya seekor owl untuk Claude Code Anda.
- [cGradying/claude-code-cockpit](https://github.com/cGradying/claude-code-cockpit) - Pita Claude Code satu baris.
- [chamonkey-crypto/claude-mods](https://github.com/chamonkey-crypto/claude-mods)
- [ChaseWNorton/claude-doom](https://github.com/ChaseWNorton/claude-doom) - Engine Doom asli dengan Freedoom, dapat dimainkan di dalam Claude Code.
- [christian-engels/claude-footprint](https://github.com/christian-engels/claude-footprint) - Mod Claude Code: perkiraan listrik ⚡ dan air 💧 di balik setiap giliran dan…
- [chshin84/claude-mods](https://github.com/chshin84/claude-mods) - Claude Code 단어 사전 패널과 상태 표시줄 플러그인.
- [cldotdev/claude-todo-list](https://github.com/cldotdev/claude-todo-list) - Mod Claude Code yang menyimpan daftar berjalan item terbuka dalam percakapan…
- [comertial/claude-pending-changes](https://github.com/comertial/claude-pending-changes) - Review every file Claude touches, like a pull request, without leaving the…
- [comertial/comertial-mods](https://github.com/comertial/comertial-mods) - Mod Claude Code untuk Engineer sungguhan.
- [crisguitar/claude-mods](https://github.com/crisguitar/claude-mods)
- [d3nims/d3nim-claude-mods](https://github.com/d3nims/d3nim-claude-mods) - Mod Code Claude khusus tim d3nim.
- [danielgillaspia01-web/claude-mods](https://github.com/danielgillaspia01-web/claude-mods)
- [davep-s20/claude-mods](https://github.com/davep-s20/claude-mods)
- [davidparys/claude-mods](https://github.com/davidparys/claude-mods) - Mod Claude Code: penjaga aturan menyimpan koreksi Anda sebagai aturan permanen.
- [davidurco/cc-tamagotchi](https://github.com/davidurco/cc-tamagotchi) - Tamagotchi yang hidup di dalam Claude Code: ia menetas, memakan kode yang…
- [Demo-0416/claude-code-mods](https://github.com/Demo-0416/claude-code-mods) - Mod untuk Claude Code sebagai marketplace plugin.
- [derekwden-droid/message-timestamps](https://github.com/derekwden-droid/message-timestamps) - Mod kode Claude: menampilkan waktu pada setiap prompt dan balasan di terminal…
- [devohmycode/ccmods](https://github.com/devohmycode/ccmods) - Mod Claude Code yang ditulis sebagai hook fungsi, serta marketplace yang…
- [dot-agi/arrester](https://github.com/dot-agi/arrester) - Mod Claude Code: setelah guard memblokir pemanggilan alat, mod ini menghentikan…
- [dot-agi/downrange](https://github.com/dot-agi/downrange) - Mod Claude Code: pekerjaan latar belakang dalam satu tampilan, dengan kemajuan…
- [dot-agi/high-command](https://github.com/dot-agi/high-command) - Mod Claude Code: satu kotak masuk untuk pesan dari rekan tim, subagen bernama…
- [dot-agi/sandbox-tuner](https://github.com/dot-agi/sandbox-tuner) - Mod Claude Code: menjelaskan pemblokiran sandbox dan mengubah pemblokiran…
- [dricosnyman/claude-favourites](https://github.com/dricosnyman/claude-favourites) - Favorit untuk Claude Code: ikon sekali klik untuk perintah dan skill Anda.
- [Egrn/claude-code-mutedit](https://github.com/Egrn/claude-code-mutedit) - Hei, dibisukan! Buang diff, pangkas riff, tak ada lagi edit, kurangi kredit.
- [Eiyuo/Claude-Mods](https://github.com/Eiyuo/Claude-Mods)
- [elec100-design/claude-mods](https://github.com/elec100-design/claude-mods) - mod untuk claude.
- [EmanueleNene/claude-mods](https://github.com/EmanueleNene/claude-mods) - Mod kode Claude: delete-guard (mengonfirmasi penghapusan file) dan octopus-crew…
- [eric1hua/claudemods-desktop-statusline](https://github.com/eric1hua/claudemods-desktop-statusline) - Mod Claude Code: penggunaan langganan (5h / 7d) sebagai pita di atas prompt di…
- [ErnestTramp/claude-critters](https://github.com/ErnestTramp/claude-critters) - Claude Code mod: your background agents as pixel critters, one sprite per model.
- [FeidaWang/edit-replay](https://github.com/FeidaWang/edit-replay) - Edit Replay: step through the file edits Claude made in the last turn, one diff…
- [Flo0806/fh-claude-mods](https://github.com/Flo0806/fh-claude-mods) - Marketplace Mod Claude.
- [floheissler/cc-worktree-radar](https://github.com/floheissler/cc-worktree-radar) - Radar langsung cabang paralel dan worktree Anda di atas prompt: mana yang dapat…
- [gaius-codius/ostrakon](https://github.com/gaius-codius/ostrakon) - Mod Code Claude untuk menangkap pemikiran di tengah pekerjaan, memilahnya di…
- [GarvitNangru/claude-code-mods](https://github.com/GarvitNangru/claude-code-mods) - Mod dan skin untuk Code Claude: bilah kemajuan langsung untuk tugas Claude…
- [Gat0rRex/claude-mods](https://github.com/Gat0rRex/claude-mods) - Mod Claude Code (plugin function-hook): pita konteks, hal-hal yang belum…
- [gauravruhela07/claude-mods](https://github.com/gauravruhela07/claude-mods) - Tujuh mod Code Claude: savvy-progress, skins, filetree, cache-tax…
- [GeckoKing9/claude-code-copy-button](https://github.com/GeckoKing9/claude-code-copy-button) - Ctrl+klik untuk menyalin tautan pada setiap blok kode dalam balasan Claude Code…
- [Gersom/gersom-claude-mods](https://github.com/Gersom/gersom-claude-mods) - Mod untuk Claude Code: plugin hook, seperti usage-meter.
- [Gharib89/claude-mods](https://github.com/Gharib89/claude-mods) - Mod kode Claude (plugin function-hook), dipasang melalui satu marketplace.
- [gomymy64/claude-code-mods-cheatsheet](https://github.com/gomymy64/claude-code-mods-cheatsheet)
- [gotzastory/my-mods](https://github.com/gotzastory/my-mods) - Mod Code Claude: context-bar-plus (bilah konteks, kuota, mode subagen).
- [hahahahahahahahah6/mod-audit](https://github.com/hahahahahahahahah6/mod-audit) - Auditor rantai pasokan statis untuk Mod Code Claude — lokal, luring, hanya…
- [hb03/claude-mods](https://github.com/hb03/claude-mods) - Mod berbahasa Jerman untuk Code Claude: petunjuk konteks/cache, hal-hal terbuka…
- [Hsiang-LinC/vault-jot](https://github.com/Hsiang-LinC/vault-jot) - Claude Code mod: capture ideas into an Obsidian vault inbox from any session.
- [Huuuuung/think-meter](https://github.com/Huuuuung/think-meter) - Mod Claude Code: berapa lama setiap jawaban berlangsung, berapa lama Claude…
- [huynl-96/claude-mods](https://github.com/huynl-96/claude-mods) - Mod kode Claude: streamer-mode menyembunyikan panel privat, band, dan baris…
- [hyperbola-bear/claude-mods](https://github.com/hyperbola-bear/claude-mods) - untuk mod claude saya.
- [icedevil2001/auto-continue](https://github.com/icedevil2001/auto-continue) - Mod Claude Code: menunggu hingga batas penggunaan 5 jam terlewati dan mengirim…
- [icedevil2001/claude-mods](https://github.com/icedevil2001/claude-mods) - Mod kecil untuk Code Claude, dimulai dengan kelanjutan otomatis setelah batas 5…
- [im-adarsh/claude-mods](https://github.com/im-adarsh/claude-mods)
- [imsungbin/quackpit-mod](https://github.com/imsungbin/quackpit-mod) - Kokpit di atas perintah Code Claude Anda. Bebek membaca pengukur.
- [jakerains/claudemods](https://github.com/jakerains/claudemods) - Mod Code Claude kecil: pengukur penggunaan konteks dan rencana, pengukur cache…
- [jasonwblock/sdlc-tracker](https://github.com/jasonwblock/sdlc-tracker) - SDLC Tracker: a Claude Code mod with a side pane showing where each work item…
- [jduerrmann/agent-crew](https://github.com/jduerrmann/agent-crew) - Mod kode Claude: satu panel untuk setiap subagen, file yang mereka sentuh…
- [jessetsai1024/claude-ctx-panel](https://github.com/jessetsai1024/claude-ctx-panel) - Panel penggunaan context di bilah samping: total, kategori, pertumbuhan tiap…
- [jessetsai1024/claude-files](https://github.com/jessetsai1024/claude-files) - Daftar file di bilah samping: file apa yang dibuat, diubah, atau dihapus dalam…
- [jessetsai1024/claude-maomao](https://github.com/jessetsai1024/claude-maomao) - 毛毛 bergaya 8-bit (kelinci lop Belanda hitam-putih) berlari dan melompat di atas…
- [jessetsai1024/claude-prompts](https://github.com/jessetsai1024/claude-prompts) - “Yang pernah saya tanyakan” di bilah samping: setiap kalimat yang diketik…
- [jessetsai1024/claude-timeline](https://github.com/jessetsai1024/claude-timeline) - Linimasa di bilah samping: ke mana waktu putaran ini digunakan.
- [jessetsai1024/claude-tokens](https://github.com/jessetsai1024/claude-tokens) - Pertukaran token di bilah samping: berapa token yang dikirim percakapan utama…
- [jessetsai1024/claude-whisper](https://github.com/jessetsai1024/claude-whisper) - Tas kacang jujur untuk claude code: setelah setiap putaran selesai menjawab…
- [jimmysteinmetz/b-sides](https://github.com/jimmysteinmetz/b-sides) - Mod kecil untuk Claude Code, seperti perintah slash baru dan panel samping.
- [jjjung0921/claude-mods](https://github.com/jjjung0921/claude-mods)
- [jkf87/mod-guide](https://github.com/jkf87/mod-guide) - Panduan komunitas tidak resmi untuk mod Code Claude (hook fungsi) dalam 6…
- [KaiC5504/clawd-bar](https://github.com/KaiC5504/clawd-bar) - Clawd tinggal di pita di atas prompt Claude Code Anda: memeragakan sesi…
- [kajidog/cc-mods-tts](https://github.com/kajidog/cc-mods-tts) - Mod yang membacakan respons dan notifikasi Claude Code menggunakan VOICEVOX /…
- [kbrdn1/claude-crosstalk](https://github.com/kbrdn1/claude-crosstalk) - Mod Claude untuk membaca dan bergabung dalam percakapan antara sesi Claude Code…
- [ke11/claude-mods](https://github.com/ke11/claude-mods) - Claude Code mods. PixBar: a pixel creature above your prompt that moves with…
- [Khanthtutzin/subagent-crew](https://github.com/Khanthtutzin/subagent-crew) - Mod Claude Code: menjalankan subagen sebagai maskot pixel Claude di atas prompt.
- [kkatsuyoshi/claude-mods](https://github.com/kkatsuyoshi/claude-mods) - mod claude.
- [KKK12142/claude-mods](https://github.com/KKK12142/claude-mods) - Mod kode Claude (usage-meter, ...).
- [krishna-goutham-tls/cc-mods](https://github.com/krishna-goutham-tls/cc-mods) - Dua mod kode Claude: folio, panel file di samping chat, dan tint, penataan…
- [kuehn-lars/cc-graph](https://github.com/kuehn-lars/cc-graph) - cc-graph: a live graph oh what Claude Code knows.
- [leonidb/claude-code-mods](https://github.com/leonidb/claude-code-mods) - Jangan biarkan perhatian Anda teralihkan saat menunggu jawaban Code Claude.
- [LordMordelon/claude-mods](https://github.com/LordMordelon/claude-mods) - Mod Code Claude untuk proyek-proyek Angel (Vremia).
- [Lucas-CX/awesome-claude-mods](https://github.com/Lucas-CX/awesome-claude-mods) - Panduan Mod Claude Code yang dikurasi komunitas: kasus penggunaan, demo asli…
- [M-i-k-e-l/agent-state](https://github.com/M-i-k-e-l/agent-state) - Mod Claude Code yang menampilkan apa yang sedang dilakukan Claude di subtitel…
- [malinfossum/mango-buddy](https://github.com/malinfossum/mango-buddy) - Kucing hitam berbulu lebat di atas prompt Claude Code Anda.
- [MarcusJellinghaus/claude-mode-gate](https://github.com/MarcusJellinghaus/claude-mode-gate) - Mod Claude Code dengan profil izin yang dapat diganti: dasar yang aman, profil…
- [MDmubarak786/claude-mods](https://github.com/MDmubarak786/claude-mods) - Mod komunitas untuk Claude Code: penjaga, panel, dan perintah yang berjalan di…
- [michaelblaess/turbo-mod](https://github.com/michaelblaess/turbo-mod) - Panel samping untuk Code Claude: file yang ditulis Claude, pembagian terminal…
- [micke-dahlgren/token-range-monitor](https://github.com/micke-dahlgren/token-range-monitor) - Claude Code mod: projects what will be left of your weekly and 5-hour Claude…
- [mmedum/glimt](https://github.com/mmedum/glimt) - Panel samping yang tenang untuk Claude Code: apa yang sedang dilakukan sesi…
- [mmedum/nuet](https://github.com/mmedum/nuet) - Waktu redup di atas setiap prompt dan setiap balasan dalam transkrip Code…
- [mmedum/spor](https://github.com/mmedum/spor) - Mengembalikan apa yang disembunyikan Claude Code: file yang dibaca Claude…
- [mrsono0/ctx-footer](https://github.com/mrsono0/ctx-footer) - Mod Code Claude: penggunaan jendela konteks di slot mode footer perintah.
- [muellerei/enable-todo-tools](https://github.com/muellerei/enable-todo-tools) - Mod Claude Code yang mengaktifkan kembali alat todo untuk model yang tidak…
- [muellerei/task-line](https://github.com/muellerei/task-line) - Mod Claude Code: satu baris per tugas di atas prompt dengan tugas saat ini…
- [nachtgold/claude-code-connect-four](https://github.com/nachtgold/claude-code-connect-four) - Mainkan Connect Four melawan AI di dalam Claude Code (/connect-four).
- [naoanao/agent-cross-check](https://github.com/naoanao/agent-cross-check) - Mod Claude Code: ketika agen coding lain melakukan commit ke repo Anda, Claude…
- [naoanao/shared-repo-guard](https://github.com/naoanao/shared-repo-guard) - Mod Claude Code untuk repo yang dibagikan oleh beberapa agen AI: menghentikan…
- [nerevar48/nerevar-mods](https://github.com/nerevar48/nerevar-mods) - Claude Code mods marketplace.
- [nu0ma/query-guard](https://github.com/nu0ma/query-guard) - Pagar pengaman untuk SQL di Claude Code: meminta konfirmasi sebelum Claude…
- [OG-Matcha/tessera](https://github.com/OG-Matcha/tessera) - Satu mod untuk Claude Code, Windows dan CJK terlebih dahulu: pratinjau gambar…
- [onk3sh/fix-on-edit](https://github.com/onk3sh/fix-on-edit)
- [Open01277/claude-mods](https://github.com/Open01277/claude-mods)
- [osaki42/awesome-claude-mods](https://github.com/osaki42/awesome-claude-mods) - Mod Claude Code terbaik, diurutkan berdasarkan manfaatnya bagi Anda.
- [pablodiazjorge/impact-radius](https://github.com/pablodiazjorge/impact-radius) - Mod kode Claude yang menahan perintah shell berisiko.
- [Para-FR/claude-code-mods-fr](https://github.com/Para-FR/claude-code-mods-fr) - Dua Mod Claude untuk Claude Code: garde-du-corps.
- [Paradox07127/claude-utopia](https://github.com/Paradox07127/claude-utopia) - Mod Code Claude dengan telemetri agen, dasbor linimasa, tinjauan lintas model…
- [paragpandyareal/swear-slap](https://github.com/paragpandyareal/swear-slap) - Memaki Claude Code dan tangan kartun membalas dengan tamparan.
- [paulosergio-jnr/claude-code-mods](https://github.com/paulosergio-jnr/claude-code-mods) - Claude Code Mods repo.
- [paulpc2/claude-code-mods](https://github.com/paulpc2/claude-code-mods) - Mod Code Claude: usage-both menampilkan penggunaan 5 jam dan mingguan di atas…
- [philarete173/claude_mods](https://github.com/philarete173/claude_mods) - Panel samping statistik sesi langsung untuk tab Code aplikasi desktop Claude…
- [PhilRoli/traintracker-claude](https://github.com/PhilRoli/traintracker-claude) - Claude Code mod: pause sessions before your TrainTracker train arrives.
- [pompeitech/affreschi](https://github.com/pompeitech/affreschi) - Mod Code Claude untuk antarmuka pompeitech, dengan tema berdasarkan sistem…
- [pradyb/claude-mods](https://github.com/pradyb/claude-mods) - Mod untuk Code Claude: safety-guard memblokir perintah destruktif dan akses…
- [qazwsx1121/Claude-Code-mods](https://github.com/qazwsx1121/Claude-Code-mods)
- [rafagomes/claude-code-mods](https://github.com/rafagomes/claude-code-mods) - Mod untuk Claude Code: plugin function-hook yang berjalan di dalam sesi…
- [rajib2k5/claude-market-watch](https://github.com/rajib2k5/claude-market-watch) - Mod Claude Code: ticker saham langsung, panel /quote, peringatan harga, pita…
- [ramtinJ95/claude-mods](https://github.com/ramtinJ95/claude-mods) - Claude Code mods, published as one plugin marketplace.
- [ray-amjad/memory-fork](https://github.com/ray-amjad/memory-fork) - Claude Code mod: keeps auto-memory up to date in the background after every turn.
- [RedRoosterKey/claude-code-ssh-usage-band](https://github.com/RedRoosterKey/claude-code-ssh-usage-band) - Mod Claude Code: host SSH, RAM, dan batas penggunaan 5j/7h dalam satu baris di…
- [Risdon8/push-ups](https://github.com/Risdon8/push-ups) - Mod Code Claude: push-up yang harus dilakukan saat Claude bekerja. Tanpa token.
- [robinade/claude-mods-ko](https://github.com/robinade/claude-mods-ko) - 6 mod Code Claude edisi bahasa Korea: catatan asumsi, bahasa sederhana, rak…
- [saadk408/stepline](https://github.com/saadk408/stepline) - Mod Claude Code: mengubah rencana yang Anda setujui dalam mode plan menjadi…
- [saksham10arora-dotcom/awesome-claude-mods](https://github.com/saksham10arora-dotcom/awesome-claude-mods) - Daftar pilihan mod Claude Code. Setiap entri dikloning dan diperiksa dengan…
- [saksham10arora-dotcom/claude-frugal](https://github.com/saksham10arora-dotcom/claude-frugal) - Mode tanpa biaya: agen pembantu berjalan di Haiku, dan file serta log besar…
- [saksham10arora-dotcom/claude-lofi](https://github.com/saksham10arora-dotcom/claude-lofi) - Soundtrack lofi yang mengikuti sesi: tenang, fokus, mengalir, plus isyarat…
- [saksham10arora-dotcom/claude-teach-me](https://github.com/saksham10arora-dotcom/claude-teach-me) - Belajar sambil Claude melakukan coding: setelah giliran yang mengubah kode…
- [saksham10arora-dotcom/claude-vhs](https://github.com/saksham10arora-dotcom/claude-vhs) - Rekaman setiap edit yang dibuat Claude: putar ulang setiap perubahan saat…
- [sam-ruff/account-switcher-claude-code-mod](https://github.com/sam-ruff/account-switcher-claude-code-mod) - A mod for claude code that allows you to switch between accounts.
- [samaphp/session-links](https://github.com/samaphp/session-links) - Setiap tautan yang disebutkan sesi Anda, dalam satu baris di atas prompt.
- [sawzhang/hello-mod](https://github.com/sawzhang/hello-mod) - Demo minimal fungsi hook Claude Code: panel token/biaya real-time di atas…
- [sebastian1747/claude-mod-simple-usage-bar](https://github.com/sebastian1747/claude-mod-simple-usage-bar) - Mod Kode Claude: batas 5j, mingguan, dan Fable sebagai bilah di atas prompt.
- [SeitaHigashi/claude-terminal-image](https://github.com/SeitaHigashi/claude-terminal-image) - Claude Code mod: show an image (PNG, JPEG, GIF, WebP, BMP) in a terminal pane…
- [SentientNr6/claude-mods](https://github.com/SentientNr6/claude-mods) - Kumpulan plugin untuk Claude.
- [shahsanket2107/clarvis](https://github.com/shahsanket2107/clarvis) - Clarvis: mod penggemar Avengers tidak resmi untuk Code Claude.
- [shengyy/ccoverhead](https://github.com/shengyy/ccoverhead) - Mod Claude Code untuk konteks, pertumbuhan, kuota, cache, biaya native, dan…
- [shezis/claude-model-router](https://github.com/shezis/claude-model-router) - Mod Code Claude: teruskan giliran sederhana dan subagen ke model yang lebih…
- [sidhantunnithan/jindan-cc-marketplace](https://github.com/sidhantunnithan/jindan-cc-marketplace) - Mod Code Claude pribadi.
- [speti4/doom-pane](https://github.com/speti4/doom-pane) - The original DOOM in a Claude Code pane with nothing to install: the engine…
- [steven-ngle/blade-of-commits](https://github.com/steven-ngle/blade-of-commits) - Pesan commit sekali klik untuk Claude Code dengan Malenia pixel-art yang menari.
- [su-record/claude-mods](https://github.com/su-record/claude-mods) - Mod Code Claude pribadi.
- [takiguchi-yu/claude-mods](https://github.com/takiguchi-yu/claude-mods) - Tempat penyimpanan mod Code Claude untuk digunakan secara lokal.
- [Tanish-Dev/claude-usage-band](https://github.com/Tanish-Dev/claude-usage-band) - Clawd Meter — mod kode Claude yang menampilkan penggunaan paket Claude Anda…
- [tartinerlabs/claude-code-mods](https://github.com/tartinerlabs/claude-code-mods)
- [TFoxik/claude-model-router](https://github.com/TFoxik/claude-model-router) - A Claude Code mod that picks the model and effort for each kind of work, and…
- [TheBabaYaga/claude-session-flow](https://github.com/TheBabaYaga/claude-session-flow) - Mod Claude Code yang menampilkan sesi saat ini dalam sebuah panel: setiap…
- [theishandubey/claude-mods](https://github.com/theishandubey/claude-mods) - Marketplace plugin Claude Code untuk mod: plugin function-hooks yang menggambar…
- [Tora29/my-claude-tools](https://github.com/Tora29/my-claude-tools) - Repo untuk mengelola Mod Claude.
- [trietsch/claude-customizations](https://github.com/trietsch/claude-customizations) - Kustomisasi untuk Code Claude.
- [tunglt1810/claude-gadgets](https://github.com/tunglt1810/claude-gadgets) - Beberapa mod Claude.
- [TurboKach/cc-language-improve](https://github.com/TurboKach/cc-language-improve) - Mod kode Claude yang memeriksa bahasa English pada prompt Anda saat Anda…
- [tusharck/mods-for-claude](https://github.com/tusharck/mods-for-claude) - Katalog pilihan mod Code Claude, masing-masing dengan prompt salin-tempel yang…
- [ulttla/claude-mod-repo](https://github.com/ulttla/claude-mod-repo) - Mod Code Claude: pengukur batas konteks dan rencana di atas prompt, serta pin…
- [VaitaR/claude-code-limits](https://github.com/VaitaR/claude-code-limits) - Mod Claude Code: kuota 5h/7d, context window, sisa waktu prompt-cache, dan…
- [VAlux/claude-session-progress](https://github.com/VAlux/claude-session-progress) - Mod Claude Code: pita kemajuan animasi dan ringkasan penyelesaian untuk tugas…
- [Vansitha/clawd-watch](https://github.com/Vansitha/clawd-watch) - Tiga mod Claude Code kecil: lihat kapan subagen Anda selesai, antrekan pesan…
- [varunmoka7/image-shrinker](https://github.com/varunmoka7/image-shrinker) - Mengecilkan tangkapan layar besar sebelum Claude membacanya, sehingga sesi…
- [varunmoka7/layman](https://github.com/varunmoka7/layman) - Katakan &quot;Saya tersesat&quot; dan Claude akan menjelaskan kembali balasan terakhirnya…
- [varunmoka7/next-steps-autopilot](https://github.com/varunmoka7/next-steps-autopilot) - Menampilkan prompt berikutnya yang disarankan di atas kotak prompt.
- [varunmoka7/side-chat](https://github.com/varunmoka7/side-chat) - Ajukan pertanyaan sampingan kepada Claude di panel di sebelah pekerjaan Anda.
- [Victormartinsilva/MODS-CLAUDECODE](https://github.com/Victormartinsilva/MODS-CLAUDECODE) - Marketplace mod Claude Code dengan instalasi satu langkah dan panduan video…
- [vihrea1337/headroom](https://github.com/vihrea1337/headroom) - Hitung mundur batas laju dan prakiraan laju penggunaan untuk Claude Code.
- [Wasif-ZA/claude-mods](https://github.com/Wasif-ZA/claude-mods)
- [wukonigcom/quanta-costa](https://github.com/wukonigcom/quanta-costa) - 🧾 Plugin Code Claude: batas penggunaan Claude Pro/Max Anda dengan perkiraan…
- [xinhuagu/oh-my-claude-mods](https://github.com/xinhuagu/oh-my-claude-mods) - Mod untuk Claude Code. agent-crew: lihat subagen Anda bekerja sebagai kru…
- [yeonwooook/claude-study-latex](https://github.com/yeonwooook/claude-study-latex) - Matematika LaTeX sebaris dan tampilan, serta gambar TikZ opsional, dalam…
- [YohanGarcia/agent-taskboard](https://github.com/YohanGarcia/agent-taskboard) - Papan tugas live untuk Claude Code: rencanakan sebelum membangun, ikuti setiap…
- [yuntaengtaeng/snitch](https://github.com/yuntaengtaeng/snitch) - Mod Code Claude yang melaporkan berkas mana yang diubah Claude dan alasannya…
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - Kumpulan pilihan sumber daya terbaik untuk agen-agen paling hebat, Claude Code…
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) - Plugin Claude Code yang menampilkan apa yang sedang terjadi — penggunaan…
- [sirmalloc/ccstatusline](https://github.com/sirmalloc/ccstatusline) - 🚀 Statusline yang indah dan sangat dapat disesuaikan untuk Claude Code CLI…
- [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) - Semua bagian system prompt Claude Code, 27 deskripsi alat bawaan, prompt…
- [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) - 45+ kiat untuk memaksimalkan Claude Code, dari dasar hingga tingkat lanjut…
- [Owloops/claude-powerline](https://github.com/Owloops/claude-powerline) - Powerline bergaya vim yang indah untuk Claude Code.
- [persiyanov/herdr-reviewr](https://github.com/persiyanov/herdr-reviewr) - Tinjau diff agen pengodean Anda di panel terminal dan kirim komentar baris…
- [devswha/herdr-web-ui](https://github.com/devswha/herdr-web-ui) - Browser and phone client for herdr: chat and live terminal for every agent…
- [uppinote20/claude-dashboard](https://github.com/uppinote20/claude-dashboard) - Plugin baris status komprehensif untuk Claude Code dengan penggunaan konteks…
- [a86582751/dsh-nexttavern](https://github.com/a86582751/dsh-nexttavern) - Agent roleplay cerita panjang untuk DeepSeek Harness (plugin tavern DSH): impor…
- [L-Forster/open-jet](https://github.com/L-Forster/open-jet) - An offline coding agent for local models.
- [backstabslash/goccc](https://github.com/backstabslash/goccc) - Fast, zero-dependency cost calculator and customizable statusline for Claude…
- [kylesnowschwartz/tail-claude-hud](https://github.com/kylesnowschwartz/tail-claude-hud) - Statusline terminal untuk sesi Claude Code.
- [arturogarrido/claudinho](https://github.com/arturogarrido/claudinho) - ⚽ Skor langsung football(soccer), jadwal pertandingan, dan klasemen untuk…
- [WormAlien/hub-cc](https://github.com/WormAlien/hub-cc) - Control plane lokal untuk Claude Code di Windows dan macOS: alihkan gateway LLM…
- [philoserf/claude-code-config](https://github.com/philoserf/claude-code-config) - Konfigurasi Claude Code pribadi yang diberi versi di dalam ~/.claude — agent…
- [ashafizullah/claude-code-muslim-mods](https://github.com/ashafizullah/claude-code-muslim-mods) - Waktu salat, tanggal Hijriah, adhkar, ayat harian, puasa sunnah, Ramadan…
- [livlign/ccbit](https://github.com/livlign/ccbit) - Baris status yang menyadari sesi untuk Claude Code.
- [GoSlowPoke168/claude-statusline](https://github.com/GoSlowPoke168/claude-statusline) - Statusline truecolor dua baris untuk Claude Code.
- [proDreams/dsh-tidewatch](https://github.com/proDreams/dsh-tidewatch) - A floating peak/off-peak tide card for DeepSeek Harness: i18n (en/zh/ru)…
- [pierrebelin/claude-code-toolkit](https://github.com/pierrebelin/claude-code-toolkit) - Perangkat Claude Code portabel untuk .NET DDD/Clean Architecture: agen TDD…
- [jcdendrite/claude-config](https://github.com/jcdendrite/claude-config) - Konfigurasi global Claude Code yang portabel: skill khusus, hook PreToolUse…
- [mutlumehmet/claude-plugins](https://github.com/mutlumehmet/claude-plugins) - Plugin Claude Code yang saya gunakan setiap hari: skills dan mod, dirapikan…
- [chaybits/ai-session-usage](https://github.com/chaybits/ai-session-usage) - Claude Code and ChatGPT (Codex) subscription limits in one card: a KDE Plasma 6…
- [frsorrentino/fable-director](https://github.com/frsorrentino/fable-director) - Tata kelola token untuk Claude Code: model teratas mengarahkan, eksekusi…
- [jeancarlo-javier/claude-status-bar](https://github.com/jeancarlo-javier/claude-status-bar) - Statusline fase alur kerja langsung untuk Claude Code.
- [rootstudioyaml/sprag](https://github.com/rootstudioyaml/sprag) - Pangkas pengeluaran token Claude Code &amp; Codex: merutekan lookup dan test run ke…
- [tedserbinski/claude-code-statusline](https://github.com/tedserbinski/claude-code-statusline) - Konfigurasi status line yang sederhana dan berguna untuk Claude Code.
- [aquahitt/claude-code-limit-alerts](https://github.com/aquahitt/claude-code-limit-alerts) - Peringatan batas penggunaan untuk Claude Code: notifikasi macOS, peringatan…
- [crosscountryridinggirlwonder916/claude-statusline](https://github.com/crosscountryridinggirlwonder916/claude-statusline) - Display Claude Code statusline with rate limits, current directory, and Git…
- [fbincon/claude-code-statusline](https://github.com/fbincon/claude-code-statusline) - Status line Claude Code yang dapat dikonfigurasi untuk Linux, WSL, Windows, dan…
- [JairoTorregrosa/claude-statusline](https://github.com/JairoTorregrosa/claude-statusline) - statusline Rust yang cepat untuk Claude Code — mengutamakan payload, git…
- [jsh135790/claude-code-capsule-panel](https://github.com/jsh135790/claude-code-capsule-panel) - Dashboard penggunaan live untuk Claude Code — rincian konteks, hit cache…
- [jv-k/claude-gauge](https://github.com/jv-k/claude-gauge) - Baris status dan baris token untuk Claude Code: konteks, penggunaan 5 jam dan…
- [kyllian330/claude-statusline](https://github.com/kyllian330/claude-statusline) - Menampilkan detail status utama Code Claude termasuk model, konteks, batas…
- [Ma1achy/claude-statusline](https://github.com/Ma1achy/claude-statusline) - status line Code Claude yang ramah dan dapat diutak-atik — bilah truecolor…
- [Obednal97/claude-statusline-kit](https://github.com/Obednal97/claude-statusline-kit) - Baris status Claude Code multi-baris: pengeluaran, konteks %, git, dan akun…
- [salvanya/claude_code_statusline](https://github.com/salvanya/claude_code_statusline) - Statusline dengan informasi berguna untuk claude code.
- [tc3oliver/claude-team-kit](https://github.com/tc3oliver/claude-team-kit) - Tim agen native. Di bawah kendali. Batas pekerja yang ketat, visibilitas tim…
- [yedidya-buildfy/claude-addons](https://github.com/yedidya-buildfy/claude-addons) - Add-on Claude Code: pemantau titik berwarna status tab + statusline GSD bawaan.
- [akhilnalliboina/claude-usage-statusline](https://github.com/akhilnalliboina/claude-usage-statusline) - Baris status penggunaan Code Claude untuk macOS dan Linux, dikemas sebagai…
- [andkirby/claude-statusline](https://github.com/andkirby/claude-statusline) - Statusline kustom untuk Claude Code — bilah konteks dengan persentase…
- [AsyrafHussin/claude-code-statusline](https://github.com/AsyrafHussin/claude-code-statusline) - Baris status yang rapi dan informatif untuk Claude Code — menampilkan proyek…
- [BedirYilmaz/claude-crt-hud-mod](https://github.com/BedirYilmaz/claude-crt-hud-mod) - Mod CRT HUD Claude: panel status bergaya CRT untuk Code Claude, di terminal dan…
- [bunderlog/claude-plugins](https://github.com/bunderlog/claude-plugins) - Marketplace plugin Claude Code dengan baloo: keahlian, agen yang memverifikasi…
- [ctfbio/claude-code-statusline](https://github.com/ctfbio/claude-code-statusline) - Statusline Claude Code tingkat profesional: durasi sesi, biaya multi-mata uang…
- [cvrt-gmbh/claude-statusline](https://github.com/cvrt-gmbh/claude-statusline) - Baris status yang memperhatikan langganan untuk Claude Code.
- [dave-net-positive/Claude_Code_PII_Redactor](https://github.com/dave-net-positive/Claude_Code_PII_Redactor) - Mod that detects and redacts PII in Claude Code before it reaches the model.
- [diegorv/koko.claude-statusline](https://github.com/diegorv/koko.claude-statusline) - Baris status terminal yang lengkap untuk Claude Code — Bun + TypeScript, tanpa…
- [ejklock/claude-mermaid-render](https://github.com/ejklock/claude-mermaid-render) - Plugin Claude Code yang menampilkan diagram Mermaid dengan indah dalam…
- [fbandres/ccmods](https://github.com/fbandres/ccmods) - Mods for Claude Code: live panes, gauges and more, installable as plugins.
- [filtercoffeeway/claude-kit](https://github.com/filtercoffeeway/claude-kit) - Tools, skill, dan agent untuk Claude Code — dimulai dengan baris status yang…
- [FunDrivenDev/claude-plugins](https://github.com/FunDrivenDev/claude-plugins) - Public Claude Code plugins: a context-budget status line.
- [giribboy77-arch/claude-statusline](https://github.com/giribboy77-arch/claude-statusline) - Statusline khusus Claude Code (model, effort, konteks, cache, batas penggunaan).
- [hardtomakeanadress/claude-code-deepseek-cost](https://github.com/hardtomakeanadress/claude-code-deepseek-cost) - Pengeluaran DeepSeek API yang sebenarnya untuk Claude Code: menetapkan ulang…
- [hieuvo/claude-imgview](https://github.com/hieuvo/claude-imgview) - Pratinjau gambar di dalam Code Claude: arahkan kursor ke chip di bawah balasan…
- [HiramAA/claude-desktop-mods](https://github.com/HiramAA/claude-desktop-mods) - Mod untuk Code Claude dan Desktop Claude di Windows dengan WSL: Docker dan…
- [ihororlovskyi/claude-statusline](https://github.com/ihororlovskyi/claude-statusline) - Baris status Claude Code dengan baris panel agen.
- [izahamyatim/claude-plugin-fizzy](https://github.com/izahamyatim/claude-plugin-fizzy) - 🚀 Sinkronkan todo Claude ke Fizzy.do untuk visibilitas tim secara langsung…
- [kernastra/claudecode](https://github.com/kernastra/claudecode) - Kumpulan keterampilan, mod, dan add-on Code Claude lainnya yang telah saya buat…
- [konnichiwab/claude-code-config](https://github.com/konnichiwab/claude-code-config) - Menu pengaturan, baris status, dan konfigurasi Claude Code.
- [Leechlike-intangibleasset343/claude-code-statusline](https://github.com/Leechlike-intangibleasset343/claude-code-statusline) - Track Claude Code status with a compact dashboard showing context, cost…
- [mgstegmaier/claude-plugins](https://github.com/mgstegmaier/claude-plugins) - plugin, keterampilan, mod claude buatan sendiri yang bebas kandang, dan lainnya.
- [msinclair-sudo/claude-code-setup](https://github.com/msinclair-sudo/claude-code-setup) - Penginstal lingkungan Claude Code: skills, statusline, hooks, permissions, dan…
- [muemadennis/claude-code-command-center](https://github.com/muemadennis/claude-code-command-center) - Claude Code Live Dashboard 2026: Track Costs, Tokens &amp; Git Branch Status.
- [OpenClawFarm/claude-statusline](https://github.com/OpenClawFarm/claude-statusline) - Baris status bergaya HUD untuk Code Claude — kesehatan jaringan, TPS, konteks…
- [oshnilia/claude-plugins](https://github.com/oshnilia/claude-plugins) - Plugin dan mod Claude Code untuk memahami apa yang dilakukan Claude: format…
- [pirncedark/afu-claude-statusline](https://github.com/pirncedark/afu-claude-statusline) - Bilah status multi-baris berwarna-warni untuk Claude Code.
- [rainyfei/claude-statusline-win](https://github.com/rainyfei/claude-statusline-win) - Baris status Claude Code untuk Windows (PowerShell): bilah penggunaan, hitung…
- [roy651/cc-plugins](https://github.com/roy651/cc-plugins) - Mod Bearings dan Glossary untuk Claude Code.
- [satoramoto/awesome-claude](https://github.com/satoramoto/awesome-claude) - Konfigurasi dan mod Code Claude, dengan kit komponen bersama, playground, dan…
- [Sofia-D4L/claude-conf](https://github.com/Sofia-D4L/claude-conf) - Przenośna konfiguracja Claude Code (statusline + instalator).
- [SohamShirsat/claude-cockpit](https://github.com/SohamShirsat/claude-cockpit) - A small dashboard for Claude Code: context %, cache countdown, 5-hour &amp; weekly…
- [speti4/claude-statusline](https://github.com/speti4/claude-statusline) - Custom terminal status bar for Claude Code: model, directory, git state…
- [thaiquangquy/claude.me](https://github.com/thaiquangquy/claude.me) - Konfigurasi Claude Code portabel: CLAUDE.md, settings, statusline, skills.
- [Tina0529/claude-session-radar](https://github.com/Tina0529/claude-session-radar) - Mod desktop Code Claude (macOS): notifikasi sesi klik-untuk-melompat, panel…
- [unlocked-spark/claude-code-earshot](https://github.com/unlocked-spark/claude-code-earshot) - Mod pendamping pembaca layar untuk Code Claude (Unlocked Spark Foundation).
- [viplav-artha/claude-code-lessons](https://github.com/viplav-artha/claude-code-lessons) - Pendalaman praktis dan terverifikasi tentang Claude Code — CLAUDE.md, subagent…
- [vladimir-ks/ai-agile-claude-code-statusline](https://github.com/vladimir-ks/ai-agile-claude-code-statusline) - Pelacakan biaya secara waktu nyata dan baris status pemantauan sesi untuk…
- [warodan/vscode-claude-code-patch](https://github.com/warodan/vscode-claude-code-patch) - Claude Code skill (VS Code, Windows): image previews and open buttons under…
- [ymoud/claude-code-statusline](https://github.com/ymoud/claude-code-statusline) - Baris status Code Claude: folder, cabang git, model, penggunaan jendela…
- [YoniYon00/claude-feedback-rings](https://github.com/YoniYon00/claude-feedback-rings) - Context Rot Detector 2026 - Monitor Memori AI &amp; Batas Laju Proaktif untuk Agen…
- [zhuyansen/awesome-claude-code-hooks](https://github.com/zhuyansen/awesome-claude-code-hooks) - Hook, subagen, dan statusline Claude Code: koleksi dan alat sumber terbuka…
- [tronschell/statusline.sh](https://github.com/tronschell/statusline.sh) - Builder visual untuk statusline Claude Code.
- [Magnus-Gille/tokenatlas](https://github.com/Magnus-Gille/tokenatlas) - Statusline Claude Code yang menampilkan penggunaan token waktu nyata dan…
- [Apparux/cc-fusion](https://github.com/Apparux/cc-fusion) - Statusline Claude Code: keindahan CCometixLine + fungsionalitas HUD Claude.

</details>

<a id="dsh-cordis"></a>

## Ekosistem plugin DSH dan Cordis

DeepSeek Harness dan Cordis mencapai tempat yang sama dari arah yang berbeda: bagi keduanya, plugin adalah mekanisme mod, sehingga plugin di sana setara dengan mod di sini.

<details>
<summary>🧵 <b><a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b> · ⭐74325 · TypeScript · 👁️ observed · 0 天</summary>

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
| Bintang                  | **74325**  |
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
<summary>🧵 <b><a href="https://github.com/nexu-io/open-design">nexu-io/open-design</a></b> · ⭐100497 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Bintang                  | **100497** |
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
<summary>🧵 <b><a href="https://github.com/morluto/rea">morluto/rea</a></b> · ⭐87809 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Bintang                  | **87809**  |
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
<summary>🧵 <b><a href="https://github.com/tt-a1i/archify">tt-a1i/archify</a></b> · ⭐81879 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Bintang                  | **81879**  |
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
<summary>🧵 <b><a href="https://github.com/esengine/DeepSeek-Reasonix">esengine/DeepSeek-Reasonix</a></b> · ⭐35759 · Go · 🔎 inferred · 0 天</summary>

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
| Bintang                  | **35759**  |
| Push terakhir            | 2026-10-11 |
| Pertama kali dicantumkan | 2026-10-06 |

🏷 `agent` · `agent-framework` · `ai-agent` · `ai-coding` · `cli` · `coding-agent` · `deepseek` · `developer-tools`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/zhu1090093659/dsh-web">zhu1090093659/dsh-web</a></b> · ⭐8626 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Bintang                  | **8626**   |
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
<summary>🧵 <b><a href="https://github.com/dsh-market/dsh-market">dsh-market/dsh-market</a></b> · ⭐6146 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Bintang                  | **6146**   |
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
<summary>🧵 <b><a href="https://github.com/MeteorNOX/DeepSeek-Balance-Whale-Widget">MeteorNOX/DeepSeek-Balance-Whale-Widget</a></b> · ⭐4478 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Bintang                  | **4478**   |
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
<summary>🧵 <b><a href="https://github.com/ccch1mneyyy/dsh-TUI">ccch1mneyyy/dsh-TUI</a></b> · ⭐4285 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Bintang                  | **4285**   |
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
<summary>🧵 <b><a href="https://github.com/dsh-tauri/deepseek-harness-desktop">dsh-tauri/deepseek-harness-desktop</a></b> · ⭐3153 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

DeepSeek Harness Tauri 桌面版 | Only 8mb installer, zero environment setup, preset plugins, Windows / macOS / Linux.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | TypeScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **3153**   |
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
<summary>🧵 <b><a href="https://github.com/bowenliang123/dsh-context">bowenliang123/dsh-context</a></b> · ⭐1983 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

Plugin DeepSeek Harness terbaik untuk wawasan dan pengelolaan konteks, dengan dasbor / browser / bilah sisi konteks dan perintah konteks, untuk statistik konteks, komposisi, perincian, detail evolusi, memahami bagaimana konteks dibentuk dan bagaimana konteks berevolusi. Plugin visualisasi konteks serbaguna DeepSeek Harness, dengan panel Context, browser dan bilah sisi, serta perintah Context untuk menelaah komposisi, evolusi, kompresi, pemangkasan, dan peristiwa serta tindakan lainnya pada konteks.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | TypeScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **1983**   |
| Push terakhir            | 2026-10-11 |
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `cordis-plugin` · `deepseek-harness` · `deepseek-harness-plugin` · `dsh-external` · `dsh-plugin` · `dsh-plugins`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/bowenliang123--dsh-context/573c0e5849eea852.png" width="100%" alt="bowenliang123/dsh-context screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/anywhere-labs/Agents-Anywhere">anywhere-labs/Agents-Anywhere</a></b> · ⭐1561 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Bintang                  | **1561**   |
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
<summary>🧵 <b><a href="https://github.com/AdamPlatin123/dsh-plugin-radar">AdamPlatin123/dsh-plugin-radar</a></b> · ⭐1464 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

DSH Plugin Radar — open-source ecosystem radar for DeepSeek Harness plugins: continuous discovery (21k+ candidates), k8s runtime validation (13k+ tests), 15-min snapshots; the catalog is a generated artifact — 开源 DSH 插件生态雷达：持续发现 2.1 万+ 候选、k8s 运行级实测 1.3 万+、15 分钟快照；插件目录为自动生成的产物

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | Python                                                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **1464**   |
| Push terakhir            | 2026-10-11 |
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `agent-plugins` · `continuous-validation` · `deepseek-harness` · `dsh` · `dsh-plugin` · `ecosystem-radar` · `plugin-registry`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/adamplatin123--dsh-plugin-radar/fb6ad7eb8891212c.jpg" width="100%" alt="AdamPlatin123/dsh-plugin-radar screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/EthanYoQ/AI-Novel-Writer">EthanYoQ/AI-Novel-Writer</a></b> · ⭐1401 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Bintang                  | **1401**   |
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
<summary>🧵 <b><a href="https://github.com/xing-shuyin/pi-web-ui">xing-shuyin/pi-web-ui</a></b> · ⭐283 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

Just open your browser — get all your work done.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | TypeScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **283**    |
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
<summary>🧵 <b><a href="https://github.com/FeatherHunter/dsh-mattpocock-skills-deck">FeatherHunter/dsh-mattpocock-skills-deck</a></b> · ⭐134 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

Saat dipasang, otomatis tersedia 27 skill rekayasa dan produktivitas dari mattpocock/skills v1.3.1, tanpa perlu memasang skill secara manual. Plugin ini dibuat dengan 40 miliar token dan memberikan efisiensi pengembangan 10 kali lipat dibandingkan skill asli, sekaligus membantu pemula menguasai paket skill ini lebih cepat. Dukungan penuh untuk GitHub issue; Markdown masih dalam versi pratinjau; GitLab belum didukung. Terima kasih atas penggunaan dan dukungan Anda 💗

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | JavaScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **134**    |
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
<summary>🧵 <b><a href="https://github.com/flymysql/dsh-remote">flymysql/dsh-remote</a></b> · ⭐133 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

Remote-work assistant for DeepSeek Harness (DSH): connect SSH (key or password), pick a remote workspace, operate with rw_* tools, and SFTP-mirror it into a real local DSH workspace.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | JavaScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **133**    |
| Push terakhir            | 2026-10-11 |
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `deepseek-harness` · `dsh` · `dsh-plugin` · `remote` · `sftp` · `ssh` · `tunnel` · `workspace`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/flymysql--dsh-remote/714d273f27c6d75b.png" width="100%" alt="flymysql/dsh-remote screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Nwflower/dsh-claude-style">Nwflower/dsh-claude-style</a></b> · ⭐131 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Bintang                  | **131**    |
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
<summary>🧵 <b><a href="https://github.com/morluto/flameox">morluto/flameox</a></b> · ⭐130 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

Runtime evidence that helps agents trace, profile, and burn down hotspots in application and native code, GPU kernels, and inference stacks.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | Python                                                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **130**    |
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

DSH 插件 · 注入式优化器 0.8（主线）：你照常说话，它在你发送后,AI接收前把"这一轮到底要什么"理清楚，再把这份理解交给工作 AI(上下文注入) —— 原话不改写，条条带逐字依据。含控制界面（档位/权限/模型/上下文/只读工具）、拦截浮层（思维层+产出层）与真实 token 用量。可明显提升大多数模型的发挥稳定性,尤其DeepSeek-V4.1-Flash,可有明显提升

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
<summary>🧵 <b><a href="https://github.com/kukucaiCndy/Corum-Harness">kukucaiCndy/Corum-Harness</a></b> · ⭐65 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Bintang                  | **65**     |
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
<summary>🧵 <b><a href="https://github.com/skyf0xx/hedgehog">skyf0xx/hedgehog</a></b> · ⭐44 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

HEDGEHOG codes Cleaner, Faster and with Fewer Tokens. Hedgehog's AI-driven development builds a task dependency graph from your spec-driven, BMAD-METHOD plan, so Claude Code, Cursor & Gemini CLI stay locked to it. A CLI-enforced state machine for agentic coding. Now builds DeepSeek DSH Plugins. DeepSeek Harness、DSH 插件、AI 编程、BMAD 方法. AI Copywriting

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | JavaScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **44**     |
| Push terakhir            | 2026-10-11 |
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `agent-skills` · `agentic-coding` · `ai-agents` · `ai-assisted-development` · `ai-coding` · `ai-copywriting` · `ai-engineering` · `ai-tools`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/skyf0xx--hedgehog/326d2d3a663269a4.jpg" width="100%" alt="skyf0xx/hedgehog screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/universe-st/dsh-game-material-master">universe-st/dsh-game-material-master</a></b> · ⭐42 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Bintang                  | **42**     |
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
<summary>🧵 <b><a href="https://github.com/HOWILLMAKEIT/dsh-model-context-catalog">HOWILLMAKEIT/dsh-model-context-catalog</a></b> · ⭐34 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

Plugin DeepSeek Harness: mempertahankan jendela konteks yang akurat untuk model llm-pi-ai, sehingga sesi panjang tidak keliru dianggap mengalami luapan konteks.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | JavaScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **34**     |
| Push terakhir            | 2026-10-11 |
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `context-window` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `javascript` · `llm` · `model-metadata`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/howillmakeit--dsh-model-context-catalog/6c743bbe3da63616.jpg" width="100%" alt="HOWILLMAKEIT/dsh-model-context-catalog screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/PensiveFei/deep-read-summarize">PensiveFei/deep-read-summarize</a></b> · ⭐31 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

Deep reading & summarization workflow for books/papers/videos/web — plugin parsers, MapReduce deep-read, JSON Schema output, Obsidian-ready (DSH)

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | JavaScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **31**     |
| Push terakhir            | 2026-10-11 |
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `ai-agent` · `content-summarization` · `deepseek` · `dsh-plugin` · `pipeline` · `workflow`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/pensivefei--deep-read-summarize/800b10f03f25fe11.png" width="100%" alt="PensiveFei/deep-read-summarize screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary><b>Lainnya dalam kategori ini</b> <sub>· 65</sub></summary>

- [hashgraph-online/awesome-ai-plugins](https://github.com/hashgraph-online/awesome-ai-plugins) - Daftar pilihan plugin AI terbaik yang luar biasa untuk asisten AI termasuk…
- [Dominic789654/awesome-deepseek-harness](https://github.com/Dominic789654/awesome-deepseek-harness) - A curated list of plugins, skills, MCP servers, patch/profile layers…
- [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) - Pasar plugin DSH / DSH Plugin Marketplace: jelajahi, instal, dan perbarui semua…
- [FishBottle7/opencode2dsh](https://github.com/FishBottle7/opencode2dsh) - DSH plugin — free OpenCode Zen models for DeepSeek Harness (DSH).
- [arcships/rutis](https://github.com/arcships/rutis) - Runtime plugin untuk perangkat lunak yang melakukan iterasi sendiri — lapisan…
- [kejixiaoliang/awesome-dsh-plugins](https://github.com/kejixiaoliang/awesome-dsh-plugins) - Direktori pilihan plugin DeepSeek Harness (DSH) — lebih dari 280 plugin…
- [Vncntvx/dsh-zotero](https://github.com/Vncntvx/dsh-zotero) - Toolkit Zotero untuk DeepSeek harness;
- [KannaKuron/dsh-gitbash-shell](https://github.com/KannaKuron/dsh-gitbash-shell) - Plugin DSH: shell Git Bash untuk semua mode agen di Windows.
- [ZhangFengshun/dsh-remote-ssh](https://github.com/ZhangFengshun/dsh-remote-ssh) - DSH web plugin: VSCode Remote-SSH-like remote development.
- [NekroAI/nekro-nxt](https://github.com/NekroAI/nekro-nxt) - NekroNXT: sistem agen obrolan grup multi-platform berbasis DeepSeek Harness…
- [omdsh-dev/dsh-office](https://github.com/omdsh-dev/dsh-office) - Paket tiga alat perkantoran! Alat dokumen Office untuk DeepSeek Harness (dsh)…
- [wingsky-1/dsh-plugin-hub](https://github.com/wingsky-1/dsh-plugin-hub) - DSH (DeepSeek Harness) web GUI plugin collection — task notifications, provider…
- [dphmoblie/deepseek-harness-android](https://github.com/dphmoblie/deepseek-harness-android) - dsh versi Android: mengintegrasikan DeepSeek Harness, lingkungan runtime…
- [gjj-star/dsh-conversation-navigator](https://github.com/gjj-star/dsh-conversation-navigator) - Navigasi sesi DSH.
- [lizhiyao/oh-my-knowledge](https://github.com/lizhiyao/oh-my-knowledge) - OMK — Evidence-backed evaluation and observability for prompts, RAG, skills…
- [weishao2/tizhuang-agent-skills](https://github.com/weishao2/tizhuang-agent-skills) - 2000万+中小学K12真题题库 Skill：免费注册、免费抽题、教材/章节/知识点检索、练习测验与AI智能组卷.
- [HaoyueQin/dsh-usage-statistics-panel](https://github.com/HaoyueQin/dsh-usage-statistics-panel) - Plugin web DSH: statistik penggunaan token per hari dengan heatmap aktivitas…
- [awesome-deepseekharness/awesome-deepseek-harness](https://github.com/awesome-deepseekharness/awesome-deepseek-harness) - Plugin, alat, skill, dan sumber belajar DeepSeek Harness (dsh) pilihan…
- [hyqhyq3/dsh-mcp-manager](https://github.com/hyqhyq3/dsh-mcp-manager) - Plugin pengelola server MCP untuk DeepSeek Harness: halaman Settings → MCP…
- [Wenaixi/dsh-superpower](https://github.com/Wenaixi/dsh-superpower) - Plugin DeepSeek Harness: 15 keterampilan rekayasa obra/superpowers, deskripsi…
- [harrylabsj/kiwi](https://github.com/harrylabsj/kiwi) - Runtime negosiasi perdagangan A2A + plugin DeepSeek Harness (dsh).
- [Imzl-zl/dsh-mcp-manager-ui](https://github.com/Imzl-zl/dsh-mcp-manager-ui) - UI manajemen server MCP untuk DeepSeek Harness Web — panel mengambang, impor…
- [liustack/pptwise](https://github.com/liustack/pptwise) - PowerPoint sungguhan, bukan HTML. Beri tahu AI Anda apa yang harus dibahas dan…
- [mistnest/dsh-cuigengji-plugin](https://github.com/mistnest/dsh-cuigengji-plugin) - 催更姬：给大肥鱼一个小说工作台。写正文、理设定、画情节，和 AI 一起讨论、续写与改稿.
- [Y1X1n/dsh-prompt-optimizer](https://github.com/Y1X1n/dsh-prompt-optimizer) - Plugin DeepSeek Harness · Tombol «optimalkan» sekali klik pada bilah pengiriman…
- [TecFancy/dsh-auth-gate](https://github.com/TecFancy/dsh-auth-gate) - Gerbang login untuk antarmuka web DeepSeek Harness (dsh): masuk dengan kata…
- [AmethystLuna/embedded-workbench](https://github.com/AmethystLuna/embedded-workbench) - Plugin rekayasa AI Embedded C/C++ — skill firmware.
- [Chael-Chael/dsh-reference-anything](https://github.com/Chael-Chael/dsh-reference-anything) - The best DeepSeek Harness plugin for referencing anything — enhanced @ menu for…
- [Sivan757/dsh-agent-plugins-market](https://github.com/Sivan757/dsh-agent-plugins-market) - Pengelola skills, subagen, MCP, dan LSP lengkap untuk DeepSeek Harness (DSH)…
- [dsh-plugin-lab/dsh-zhihu-search](https://github.com/dsh-plugin-lab/dsh-zhihu-search) - DSH 插件：基于知乎开放平台官方 API 创建的站内搜索、全网索引搜索与直答三个工具。搜索不幻觉，引用有出处。（原生嵌入“设置-插件-插件配置”）.
- [MicroMilo/upstream-radar](https://github.com/MicroMilo/upstream-radar) - Pengujian kompatibilitas yang selalu aktif untuk plugin DeepSeek Harness: rilis…
- [falling-ts/dsh-force-compact](https://github.com/falling-ts/dsh-force-compact) - Aggressive context compaction for local-first agents.
- [bonerush/dsh-obsidian-mem](https://github.com/bonerush/dsh-obsidian-mem) - Plugin host DeepSeek Harness yang menyimpan dokumen proyek dan memori jangka…
- [unStone/dsh-xray](https://github.com/unStone/dsh-xray) - X-ray untuk plugin DeepSeek Harness: kapabilitas yang dideklarasikan…
- [chnjames/dsh-plugin-market](https://github.com/chnjames/dsh-plugin-market) - DSH 插件市场 — DeepSeek Harness 设置内一键安装社区插件，并提供公开目录站（浏览 / 复制安装命令）.
- [cyanseek/dsh-landscape](https://github.com/cyanseek/dsh-landscape) - Agent-first DeepSeek Harness plugin intelligence: verify existing plugins…
- [dsh-plugin-lab/dsh-workbuddy-bridge](https://github.com/dsh-plugin-lab/dsh-workbuddy-bridge) - DSH 插件：把 WorkBuddy 桌面 App 里的模型接入 DeepSeek Harness，零配置直接用。（原生嵌入&quot;设置-插件-插件配置&quot;）.
- [lkhfrgc/scholar-llm-wiki](https://github.com/lkhfrgc/scholar-llm-wiki) - A knowledge base toolkit for research and literature review.
- [Mcd0LUO/dsh-guard-repeat-output](https://github.com/Mcd0LUO/dsh-guard-repeat-output) - Host-side degeneration guard for DSH: strips garbage code points, detects…
- [shenhuanageshei/dsh-team-link](https://github.com/shenhuanageshei/dsh-team-link) - Session deep links + full session export (markdown/JSON) + approved…
- [gulagala001/dsh-intelligent-ui](https://github.com/gulagala001/dsh-intelligent-ui) - Membuat jawaban DSH menjadi antarmuka yang dapat ditindaklanjuti: kalkulator…
- [AmethystLuna/logicprobe](https://github.com/AmethystLuna/logicprobe) - Verifikasi klaim desain dan kode: bandingkan klaim faktual dengan kode sumber…
- [cherrchen/dsh-plugin-multi-root-workspace](https://github.com/cherrchen/dsh-plugin-multi-root-workspace) - Workspace multi-folder: memungkinkan Agent DSH (DeepSeek Harness) tidak hanya…
- [godv61/dsh-task-engine](https://github.com/godv61/dsh-task-engine) - Plugin alur kerja engineering untuk DeepSeek Harness: tahap tugas, catatan…
- [Kr-ATG/dsh-chat-plus](https://github.com/Kr-ATG/dsh-chat-plus) - DSH 对话体验增强套件（零源码改动，纯插件注入）。Seeker 双栏执行大盘：右栏任务 / 操作面板 / 子智能体 / 产出物四张卡 +…
- [PerryLink/dsh-plugin-doctor](https://github.com/PerryLink/dsh-plugin-doctor) - Standar verifikasi tanpa dependensi untuk plugin DeepSeek Harness (dsh)…
- [viztor/dsh-opencode-patch](https://github.com/viztor/dsh-opencode-patch) - OpenCode di DeepSeek Harness — plugin DSH yang menjaga OpenCode Zen + model…
- [AI-Scarlett/DSH-Store](https://github.com/AI-Scarlett/DSH-Store) - DSH STORE — marketplace plugin pihak ketiga dan pengelola siklus hidup dengan…
- [Atelyx/Atelyx](https://github.com/Atelyx/Atelyx) - Atelyx adalah meja kerja desktop yang dapat diperluas dan berpusat pada…
- [dsh-cc/dsh-cc](https://github.com/dsh-cc/dsh-cc) - Agen coding lengkap untuk DeepSeek Harness — alur kerja bergaya Claude Code…
- [dsh-plugin-lab/dsh-ds-balance](https://github.com/dsh-plugin-lab/dsh-ds-balance) - DSH plugin: shows your DeepSeek account balance at the bottom of the left…
- [fangwen9527/dsh-composer-ux](https://github.com/fangwen9527/dsh-composer-ux) - Plugin pengalaman input DSH Web: pergantian tombol kirim/baris baru, menu klik…
- [Mzy123l/dsh-plugin-remote-access](https://github.com/Mzy123l/dsh-plugin-remote-access) - Menyediakan pintu masuk akses jarak jauh dengan 「segmen jaringan terbatas +…
- [sakanamaru/dsh-minato](https://github.com/sakanamaru/dsh-minato) - dsh-minato — rangkaian instalasi dan operasi pemeliharaan lokal versi komunitas…
- [tianyagk/dsh-tradewatcher](https://github.com/tianyagk/dsh-tradewatcher) - Plugin web DeepSeek Harness (DSH): tab sidebar market-dashboard untuk memantau…
- [xingzhen199186/dsh-mini-remote](https://github.com/xingzhen199186/dsh-mini-remote) - DSH 极简风远程移动端，提供「单帧」、「聊天」和「完整」三种模式，将注意力支配权交还给用户.
- [argszero/cordis-plugin-empty-response-retry](https://github.com/argszero/cordis-plugin-empty-response-retry) - Membuat upaya model kosong tanpa atribusi dapat dicoba ulang, untuk satu celah…
- [eovidiu/cordis-ios](https://github.com/eovidiu/cordis-ios) - Plugin yang membersihkan dirinya sendiri: port Code Swift 6 dari kerangka…
- [Magica-Chen/dsh-preset-codex-claude](https://github.com/Magica-Chen/dsh-preset-codex-claude) - Preset agen DeepSeek Harness: Codex dan Claude Code sebagai subagen delegasi…
- [validation-engineering/cordis-verus](https://github.com/validation-engineering/cordis-verus) - Runtime plugin Rust dengan kernel siklus hidup yang diverifikasi Verus dan…
- [YOU-SHOULD-KNOW-ME/antigrative-dashboard](https://github.com/YOU-SHOULD-KNOW-ME/antigrative-dashboard) - Inline Antigravity dashboard: tok/s, DSH-style cache hit rate, five-hour and…
- [Jecvay/paseo-dsh-direct](https://github.com/Jecvay/paseo-dsh-direct) - DeepSeek Harness 的 Paseo Provider Plugin (Direct Provider).
- [tellmewhattodo/dsh-serenity-plugin](https://github.com/tellmewhattodo/dsh-serenity-plugin) - dsh-serenity-plugin.
- [HaydenSmith1121/dsh-plugins](https://github.com/HaydenSmith1121/dsh-plugins) - DeepSeek Harness (dsh) 插件市场 —— 目录（一个插件一个配置文件）+ 可视化面板 + 一键安装；插件本体在…
- [SCP-008-1/dshop](https://github.com/SCP-008-1/dshop) - dsh 插件商城 - 基于 GitHub topic:dsh-plugin 自动发现与每小时定时同步.

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

| Bahasa     | Entri | Contoh                                                                                                             |
| ---------- | ----- | ------------------------------------------------------------------------------------------------------------------ |
| TypeScript | 322   | `anthropics/claude-code`, `anthropics/claude-code-action`, `karanb192/cache-tax`                                   |
| JavaScript | 69    | `karanb192/awesome-claude-code-mods`, `karanb192/claude-code-mods`, `augiefra/claude-mods`                         |
| Python     | 32    | `anthropics/claude-agent-sdk-python`, `anthropics/claude-code-security-review`, `alexgreensh/token-optimizer`      |
| Shell      | 19    | `anthropics/claude-agent-sdk-typescript`, `andrewbakercloudscale/claude-code-cost-sidebar`, `Gharib89/claude-mods` |
| HTML       | 12    | `awss1i/assay`, `omarcevi/claudemods`, `testy-cool/awesome-claude-code-mods`                                       |
| Go         | 6     | `backstabslash/goccc`, `kylesnowschwartz/tail-claude-hud`, `livlign/ccbit`                                         |
| Rust       | 5     | `persiyanov/herdr-reviewr`, `JairoTorregrosa/claude-statusline`, `OpenClawFarm/claude-statusline`                  |
| PowerShell | 2     | `GoSlowPoke168/claude-statusline`, `rainyfei/claude-statusline-win`                                                |
| C#         | 1     | `sakanamaru/dsh-minato`                                                                                            |
| Kotlin     | 1     | `dphmoblie/deepseek-harness-android`                                                                               |
| MDX        | 1     | `jkf87/mod-guide`                                                                                                  |
| Swift      | 1     | `eovidiu/cordis-ios`                                                                                               |

<sub>Hanya entri yang menyatakan bahasa yang dihitung. Entri dokumentasi dan diskusi tidak disertakan dalam tabel ini.</sub>

## Berkontribusi

Koreksi sangat diterima dan merupakan cara tercepat untuk meningkatkan daftar ini. Buka issue atau pull request jika suatu entri salah kategorisasi, salah tingkat, atau jika sebuah proyek keliru dikecualikan karena benturan nama — kategori terakhir itulah yang paling mungkin salah akibat filter otomatis.

---

<sub>Proyek komunitas independen. Tidak berafiliasi dengan, tidak didukung oleh, dan tidak ditinjau oleh Anthropic. Claude Code, Claude, dan Anthropic adalah merek dagang milik Anthropic. Perilaku produk dapat berubah tanpa pemberitahuan; verifikasi hal-hal penting terhadap dokumentasi resmi. Aset tetap menjadi milik proyek upstream masing-masing dan hanya direproduksi jika diizinkan oleh lisensinya.</sub>

<sub>Terakhir diperbarui · 2026-10-11T21:12:49+08:00</sub>
