<p align="center">
  <img src="../assets/readme/hero.png" width="100%" alt="Mod Claude Keren">
</p>

<h1 align="center">Mod Claude Keren</h1>

<p align="center"><b>Indeks mod Claude Code, plugin, dan perubahan perilaku mendalam yang ditimbulkannya, dengan pemeringkatan berdasarkan bukti.</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-596-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="../LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
  <a href="https://wh000wh000.github.io/awesome-claude-mods/"><img src="https://img.shields.io/badge/site-searchable-1f6feb" alt="site"></a>
</p>

<p align="center"><sub><a href="../README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.pt-BR.md">Português</a> · <a href="README.ru.md">Русский</a> · <a href="README.it.md">Italiano</a> · <a href="README.ar.md">العربية</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.tr.md">Türkçe</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <b>Bahasa Indonesia</b> · <a href="README.pl.md">Polski</a> · <a href="README.nl.md">Nederlands</a> · <a href="README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **Indeks aktif** · Sinkronisasi terakhir: `2026-10-12T21:29:43+08:00` (UTC+8)
> · Entri: **596** · Ditambahkan pada pembaruan terbaru: **0** · Bahasa implementasi: **13**

<sub>Setiap entri di bawah dikumpulkan, difilter, dan diperiksa ulang secara otomatis. Tidak ada konten berbayar di sini.</sub>

<a id="featured"></a>

## Pilihan saat ini

<sub>Satu entri per kategori, diurutkan berdasarkan tingkat bukti dan jumlah bintang, lalu dihitung ulang setiap kali diperbarui. Ini adalah pemeringkatan, bukan dukungan; setiap pilihan tertaut ke kartu lengkapnya di bawah. Proyek yang memublikasikan tangkapan layar atau rekaman lebih diutamakan agar panel ini tetap visual.</sub>

<table>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action">
<b>🏛️ <a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b>
<sub>⭐9482 · TypeScript · ✅ official</sub>
</td>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer">
<b>🧩 <a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b>
<sub>⭐2541 · Python · 👁️ observed</sub>
<sub>Temukan token hantu. Perbaiki. Bertahan dari kompaksi. Hindari penurunan kualitas konteks.</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo">
<b>🧵 <a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b>
<sub>⭐74398 · TypeScript · 👁️ observed</sub>
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
- [Mod: dibuat dengan kemampuan mod](#mod-dibuat-dengan-kemampuan-mod) — **482**
- [Ekosistem plugin DSH dan Cordis](#ekosistem-plugin-dsh-dan-cordis) — **86**
- [Tulisan, diskusi, dan video](#tulisan-diskusi-dan-video) — **11**
- [Proyek lainnya](#proyek-lainnya) — **1**
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
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></b> · ⭐150341 · TypeScript · ✅ official · 0 天</summary>

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
| Bintang                  | **150341** |
| Push terakhir            | 2026-10-11 |
| Pertama kali dicantumkan | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b> · ⭐9482 · TypeScript · ✅ official · 2 天</summary>

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
| Bintang                  | **9482**   |
| Push terakhir            | 2026-10-09 |
| Pertama kali dicantumkan | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-python">anthropics/claude-agent-sdk-python</a></b> · ⭐8253 · Python · ✅ official · 2 天</summary>

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
| Bintang                  | **8253**   |
| Push terakhir            | 2026-10-09 |
| Pertama kali dicantumkan | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-security-review">anthropics/claude-code-security-review</a></b> · ⭐6347 · Python · ✅ official · 242 天</summary>

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
| Bintang                  | **6347**   |
| Push terakhir            | 2026-02-11 |
| Pertama kali dicantumkan | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-typescript">anthropics/claude-agent-sdk-typescript</a></b> · ⭐1799 · Shell · ✅ official · 2 天</summary>

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
| Bintang                  | **1799**   |
| Push terakhir            | 2026-10-09 |
| Pertama kali dicantumkan | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/model-cards">anthropics/model-cards</a></b> · ⭐25 · ✅ official · 310 天</summary>

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
<summary>🏛️ <b><a href="https://github.com/see-stack/claude-code-mods">see-stack/claude-code-mods</a></b> · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Ringkasan

Mod Claude Code resmi dari See Stack: HUD jendela konteks langsung, dek narasi suara, dan alat terminal. Instal melalui: npx seestack

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Resmi: repositori dan catatan rilis milik Anthropic sendiri`     |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |
| Bahasa   | TypeScript                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **0**      |
| Push terakhir            | 2026-10-12 |
| Pertama kali dicantumkan | 2026-10-12 |

🏷 `anthropic` · `claude` · `claude-code` · `cli` · `context-window` · `developer-tools` · `plugins` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/see-stack--claude-code-mods/862872bae81c637c.gif" width="100%" alt="see-stack/claude-code-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/see-stack--claude-code-mods/862872bae81c637c.gif" width="100%" alt="see-stack/claude-code-mods animation"><br><sub>rekaman animasi</sub></td>
</tr></table>

</details>

<details>
<summary><b>Lainnya dalam kategori ini</b> <sub>· 3</sub></summary>

- [Claude Code 2.1.295 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Menambahkan `$.ui.notify` untuk mod: memunculkan notifikasi native melalui…
- [Claude Code 2.1.296 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Memperbaiki Esc atau interupsi selama hook `UserPromptSubmit` atau hook…
- [huaweicloud/huaweicloud-devkit](https://github.com/huaweicloud/huaweicloud-devkit) - Official Huawei Cloud plugin for AI agents — skills, MCP tools, safety…

</details>

<a id="mods"></a>

## Mod: dibuat dengan kemampuan mod

Setiap entri di sini menunjukkan bukti penggunaan kemampuan yang diperoleh Claude Code pada 2.1.287: kemampuan tersebut menggambar melalui `ui.render`, memiliki panel, pita, atau kartu, membaca `$.ui.selection()`, memunculkan rekan satu tim dengan `agent.spawn`, atau menyatakan dengan jelas bahwa itu adalah mod.

<details>
<summary>🧩 <b><a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b> · ⭐2541 · Python · 👁️ observed · 0 天</summary>

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
| Bintang                  | **2541**   |
| Push terakhir            | 2026-10-11 |
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
<summary>🧩 <b><a href="https://github.com/karanb192/awesome-claude-code-mods">karanb192/awesome-claude-code-mods</a></b> · ⭐514 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Ringkasan

Katalog komunitas mod Claude Code publik (function hooks), dipindai dari GitHub beserta informasi tentang apa yang dapat dibaca, ditulis, dijalankan, atau dikirim melalui jaringan oleh setiap mod. Jelajahi https://mods.aidojo.si/

<sub>🔧 Ditemukan digunakan dalam kode: `data/seeds.txt`, `data/duplicates.txt`, `tools/kind.mjs`, `README.md`</sub>

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Mod: dibuat dengan kemampuan mod`                                |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |
| Bahasa   | JavaScript                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **514**    |
| Push terakhir            | 2026-10-12 |
| Pertama kali dicantumkan | 2026-10-04 |

🏷 `anthropic` · `awesome` · `awesome-list` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hamzafer/claude-code-mods">hamzafer/claude-code-mods</a></b> · ⭐200 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Ringkasan

Mod Claude Code: plugin berbasis hook yang menambahkan baris langsung di atas prompt, penjaga, panel, dan permainan. Bilah konteks, pengukur penggunaan, pemantauan ulasan Codex, pratinjau Markdown, Spotify yang sedang diputar, dan lainnya.

<sub>🔧 Ditemukan digunakan dalam kode: `mods/next-steps/hooks/register.tsx`, `mods/agent-radar/hooks/register.tsx`, `mods/review-watch/hooks/register.tsx`</sub>

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Mod: dibuat dengan kemampuan mod`                                |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |
| Bahasa   | TypeScript                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **200**    |
| Push terakhir            | 2026-10-11 |
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugins` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/c683a5d95e78d920.png" width="100%" alt="hamzafer/claude-code-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/0b4dc7c7692bd024.gif" width="100%" alt="hamzafer/claude-code-mods animation"><br><sub>rekaman animasi</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/cache-tax">karanb192/cache-tax</a></b> · ⭐152 · TypeScript · 👁️ observed · 8 天</summary>

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
| Bintang                  | **152**    |
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
<summary>🧩 <b><a href="https://github.com/iamumeransari/claude-show-your-work">iamumeransari/claude-show-your-work</a></b> · ⭐135 · TypeScript · 👁️ observed · 0 天</summary>

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
| Bintang                  | **135**    |
| Push terakhir            | 2026-10-12 |
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/iamumeransari--claude-show-your-work/7a0af2143a7dfd15.jpg" width="100%" alt="iamumeransari/claude-show-your-work screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hellosverre/claude-skins">hellosverre/claude-skins</a></b> · ⭐108 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Ringkasan

Skin untuk Claude Code: baris alat dengan ikon, kartu diagram diff, tabel, dan Mermaid, pita penggunaan, serta lima belas tema. /skin menggantinya secara langsung.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Mod: dibuat dengan kemampuan mod`                                |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |
| Bahasa   | TypeScript                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **108**    |
| Push terakhir            | 2026-10-11 |
| Pertama kali dicantumkan | 2026-10-12 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hellosverre--claude-skins/e70c992c52ca2e70.gif" width="100%" alt="hellosverre/claude-skins animation"><br><sub>rekaman animasi</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NahumLitvin/prismantis">NahumLitvin/prismantis</a></b> · ⭐81 · TypeScript · 👁️ observed · 0 天</summary>

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
| Bintang                  | **81**     |
| Push terakhir            | 2026-10-12 |
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `markdown` · `mermaid` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/f6e44059e77434b4.png" width="100%" alt="NahumLitvin/prismantis screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/00e2cffa219a3511.gif" width="100%" alt="NahumLitvin/prismantis animation"><br><sub>rekaman animasi</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Tickloop/claude-mods">Tickloop/claude-mods</a></b> · ⭐79 · TypeScript · 👁️ observed · 3 天</summary>

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
| Bintang                  | **79**     |
| Push terakhir            | 2026-10-08 |
| Pertama kali dicantumkan | 2026-10-11 |

</details>

<details>
<summary>🧩 <b><a href="https://github.com/scasella/claude-flightdeck">scasella/claude-flightdeck</a></b> · ⭐72 · TypeScript · 👁️ observed · 0 天</summary>

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
| Bintang                  | **72**     |
| Push terakhir            | 2026-10-12 |
| Pertama kali dicantumkan | 2026-10-10 |

🏷 `agent-observability` · `agent-visualization` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/scasella--claude-flightdeck/8c83ca6b4347b2f9.gif" width="100%" alt="scasella/claude-flightdeck screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/scasella--claude-flightdeck/8c83ca6b4347b2f9.gif" width="100%" alt="scasella/claude-flightdeck animation"><br><sub>rekaman animasi</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/darrell-tw/darrelltw-mods">darrell-tw/darrelltw-mods</a></b> · ⭐65 · HTML · 👁️ observed · 6 天</summary>

##### 📝 Ringkasan

Mod Claude Code oleh Darrell Wang — pita di atas prompt, tanpa token model. Dasbor saham Taiwan／AS + akan hadir berikutnya.

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
<summary>🧩 <b><a href="https://github.com/0xDarkMatter/claude-mods">0xDarkMatter/claude-mods</a></b> · ⭐61 · Shell · 👁️ observed · 5 天</summary>

##### 📝 Ringkasan

Skills, agen, perintah, aturan, hook, dan gaya keluaran ahli untuk Claude Code — kesinambungan sesi + tooling CLI modern untuk alur kerja pengembangan dunia nyata

<sub>🔧 Ditemukan digunakan dalam kode: `justfile`, `skills/auto-skill/SKILL.md`, `skills/task-runner/SKILL.md`</sub>

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Mod: dibuat dengan kemampuan mod`                                |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |
| Bahasa   | Shell                                                             |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **61**     |
| Push terakhir            | 2026-10-07 |
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `agent-skills` · `ai-agents` · `ai-tools` · `anthropic` · `claude` · `claude-code` · `claude-skills` · `developer-tools`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/whyashthakker/awesome-claude-code-mods">whyashthakker/awesome-claude-code-mods</a></b> · ⭐50 · TypeScript · 👁️ observed · 9 天</summary>

##### 📝 Ringkasan

Kumpulan lebih dari 100 mod yang dapat digunakan dengan Claude Code.

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
| Bintang                  | **50**     |
| Push terakhir            | 2026-10-03 |
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/zycck/claude-mods">zycck/claude-mods</a></b> · ⭐46 · TypeScript · 👁️ observed · 3 天</summary>

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
| Pertama kali dicantumkan | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/49f09d1600b02c7a.gif" width="100%" alt="zycck/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/25f4230871cb30f6.gif" width="100%" alt="zycck/claude-mods animation"><br><sub>rekaman animasi · <a href="https://raw.githubusercontent.com/zycck/claude-mods/main/media/plan-progress.mp4">Buka video</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/henrik-thevibe/Claude-Fables">henrik-thevibe/Claude-Fables</a></b> · ⭐32 · TypeScript · 👁️ observed · 9 天</summary>

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
<summary>🧩 <b><a href="https://github.com/oikon48/prompt-rail">oikon48/prompt-rail</a></b> · ⭐28 · TypeScript · 👁️ observed · 9 天</summary>

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
| Bintang                  | **28**     |
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

Pokémon piksel yang hidup di atas prompt dalam Claude Code

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
| Push terakhir            | 2026-10-12 |
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
| Push terakhir            | 2026-10-12 |
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `developer-tools` · `eye-candy` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/52396333a085f3d5.gif" width="100%" alt="NovusEdge/glowup screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/4905ed24c2c755ad.gif" width="100%" alt="NovusEdge/glowup animation"><br><sub>rekaman animasi</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/artemnovichkov/xcode-mods">artemnovichkov/xcode-mods</a></b> · ⭐21 · TypeScript · 👁️ observed · 10 天</summary>

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
| Bintang                  | **21**     |
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
<summary>🧩 <b><a href="https://github.com/lemomo-ai/lemo-mod">lemomo-ai/lemo-mod</a></b> · ⭐20 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Ringkasan

Mod Claude Code: 21 gaya dan serangkaian fitur lengkap yang dapat Anda aktifkan saat diperlukan, untuk terminal dan aplikasi desktop. · Terapkan gaya baru ke Claude dengan sekali klik, serta sediakan serangkaian fitur yang dapat diaktifkan sesuai kebutuhan.

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
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-starter-kit">promptadvisers/claude-mods-starter-kit</a></b> · ⭐20 · JavaScript · 👁️ observed · 9 天</summary>

##### 📝 Ringkasan

Sepuluh mod Claude Code, panduan pemula, prompt pembuatan, demo aman, dan templat buat-sendiri.

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
<summary>🧩 <b><a href="https://github.com/Amorfx/claude-paste-view">Amorfx/claude-paste-view</a></b> · ⭐19 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Ringkasan

Mod kode Claude: pratinjau gambar yang ditempel dan teks panjang yang ditempel di atas prompt

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Mod: dibuat dengan kemampuan mod`                                |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |
| Bahasa   | TypeScript                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **19**     |
| Push terakhir            | 2026-10-12 |
| Pertama kali dicantumkan | 2026-10-12 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `clipboard` · `ghostty` · `image-preview` · `kitty` · `paste`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/amorfx--claude-paste-view/972d572d11675bb5.png" width="100%" alt="Amorfx/claude-paste-view screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/SavaSoftworks/BitFrost">SavaSoftworks/BitFrost</a></b> · ⭐16 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Ringkasan

Gunakan Codex, GLM, dan agen coding lainnya sebagai subagen Claude Code.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Mod: dibuat dengan kemampuan mod`                                |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |
| Bahasa   | TypeScript                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **16**     |
| Push terakhir            | 2026-10-12 |
| Pertama kali dicantumkan | 2026-10-12 |

🏷 `agent-orchestration` · `ai-agents` · `claude-code` · `claude-code-mods` · `claude-code-plugin` · `codex` · `developer-tools` · `glm`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/savasoftworks--bitfrost/247eb6d28062ba3b.png" width="100%" alt="SavaSoftworks/BitFrost screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/BrianHuang813/clawd-actor">BrianHuang813/clawd-actor</a></b> · ⭐15 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Ringkasan

Claude Code mod: Clawd acts out what Claude is doing, above the prompt

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Mod: dibuat dengan kemampuan mod`                                |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |
| Bahasa   | TypeScript                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **15**     |
| Push terakhir            | 2026-10-12 |
| Pertama kali dicantumkan | 2026-10-12 |

🏷 `animation` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-plugin` · `clawd` · `hooks` · `spinner`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/brianhuang813--clawd-actor/d6174db0110613e4.gif" width="100%" alt="BrianHuang813/clawd-actor screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/brianhuang813--clawd-actor/d6174db0110613e4.gif" width="100%" alt="BrianHuang813/clawd-actor animation"><br><sub>rekaman animasi</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-computer-use-threads">promptadvisers/claude-mods-computer-use-threads</a></b> · ⭐14 · JavaScript · 👁️ observed · 6 天</summary>

##### 📝 Ringkasan

Dua mod Claude Code: jembatan penggunaan komputer Codex dan sesi Claude terkoordinasi. Sumber, prompt build, penyiapan, dan pengujian.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Mod: dibuat dengan kemampuan mod`                                |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |
| Bahasa   | JavaScript                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **14**     |
| Push terakhir            | 2026-10-05 |
| Pertama kali dicantumkan | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/promptadvisers--claude-mods-computer-use-threads/c08dc292e500cd09.png" width="100%" alt="promptadvisers/claude-mods-computer-use-threads screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/JetsonChan/CC-Usage-Band">JetsonChan/CC-Usage-Band</a></b> · ⭐13 · TypeScript · 👁️ observed · 9 天</summary>

##### 📝 Ringkasan

Mod Claude Code: usage-band menampilkan batas 5 jam/7 hari, jendela konteks, dan tingkat cache hit di atas prompt

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
<summary>🧩 <b><a href="https://github.com/aieo-product/claude_qamods">aieo-product/claude_qamods</a></b> · ⭐12 · TypeScript · 👁️ observed · 5 天</summary>

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
| Bintang                  | **12**     |
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
<summary>🧩 <b><a href="https://github.com/augiefra/claude-mods">augiefra/claude-mods</a></b> · ⭐12 · JavaScript · 👁️ observed · 1 天</summary>

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
| Bintang                  | **12**     |
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
<summary>🧩 <b><a href="https://github.com/OneWave-AI/claude-code-mods">OneWave-AI/claude-code-mods</a></b> · ⭐12 · TypeScript · 👁️ observed · 9 天</summary>

##### 📝 Ringkasan

Sepuluh mod sumber terbuka untuk Claude Code: panel langsung, pita, statusline, dan penjaga pemanggilan alat. Pengukur penggunaan, kode peluncuran, sesi selesai, pertarungan bos, hewan peliharaan kode, dan lainnya.

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
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mods` · `claude-code-plugins`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/onewave-ai--claude-code-mods/763e0352f43b1cbc.png" width="100%" alt="OneWave-AI/claude-code-mods screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/furqan-khan07/pixelband">furqan-khan07/pixelband</a></b> · ⭐10 · TypeScript · 👁️ observed · 8 天</summary>

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
<summary>🧩 <b><a href="https://github.com/Arunjay4213/claude-mods">Arunjay4213/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 26 天</summary>

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
| Bintang                  | **9**      |
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
<summary>🧩 <b><a href="https://github.com/deepsteve/deepsteve">deepsteve/deepsteve</a></b> · ⭐9 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Ringkasan

Antarmuka untuk Claude Code dan terminal Codex milik Anda yang dibuat oleh agen Anda, sehingga satu-satunya model dalam pikiran Anda adalah milik Anda.

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
| Push terakhir            | 2026-10-11 |
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `ai-coding` · `ai-tools` · `browser-terminal` · `claude-code` · `codex` · `coding-agent` · `developer-tools` · `devtools`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/deepsteve--deepsteve/adee5ea71e2e3289.png" width="100%" alt="deepsteve/deepsteve screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/ersinkoc/claude-mods">ersinkoc/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 2 天</summary>

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
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `anthropic` · `claude-code` · `claude-code-mods` · `claude-code-plugin` · `tui`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ersinkoc--claude-mods/ece950c6b8ad049e.png" width="100%" alt="ersinkoc/claude-mods screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/az9713/claude-mod-pack">az9713/claude-mod-pack</a></b> · ⭐8 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Ringkasan

Enam mod Claude Code dalam satu plugin (Token Weather, Cache Keeper, Wait What, Prompt Queue, Snake, Blast Radius) dengan sakelar per mod, ditambah laporan mod-vs-hook.

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
<summary>🧩 <b><a href="https://github.com/devbrother2024/devbrothers-mods">devbrother2024/devbrothers-mods</a></b> · ⭐7 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Ringkasan

Kumpulan mod Claude Code milik Gaebaldongsaeng. Paket taksi: meteran, navigasi, kamera penindak pelanggaran kecepatan, dashcam

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
<summary><b>Lainnya dalam kategori ini</b> <sub>· 448</sub></summary>

- [karanb192/claude-code-mods](https://github.com/karanb192/claude-code-mods) - Mod Claude dan alat untuk membangunnya: skill builder, lalu mod.
- [ucsandman/claude-harness](https://github.com/ucsandman/claude-harness) - Harness Claude Code yang saya jalankan setiap hari, diterbitkan dengan nama ini…
- [kagamiurayama/claude-code-roof-mod](https://github.com/kagamiurayama/claude-code-roof-mod) - Ubah atap Claude Code dengan Claude Mods: tanpa mengubah biner, ganti prompt…
- [nateherkai/claude-code-mods](https://github.com/nateherkai/claude-code-mods) - Empat mod Claude Code: Cache Keeper, Recording Mode, Goal Meter, dan Collision…
- [HolyGrail/claude-mods](https://github.com/HolyGrail/claude-mods)
- [Hangghost/learning-hacker-claude-mod](https://github.com/Hangghost/learning-hacker-claude-mod) - Mod Claude Code milik Learning Hacker: membuat operasi agent menjadi sesuatu…
- [kakha13/claude](https://github.com/kakha13/claude) - Mod Claude Code yang memperbaiki dan menerjemahkan prompt Anda sebelum Claude…
- [nekyialabs/claude-code-toolkit](https://github.com/nekyialabs/claude-code-toolkit) - Mod dan skill Claude Code dari Nekyia Labs, dibuat dan digunakan setiap hari…
- [AgriciDaniel/claude-mods-brain](https://github.com/AgriciDaniel/claude-mods-brain) - Basis pengetahuan Obsidian dengan sumber yang dikutip tentang mod Claude Code…
- [nvr0x5/claude-deck](https://github.com/nvr0x5/claude-deck) - Kokpit untuk Claude Code: bilah rencana langsung, strip subagen, batas…
- [rashedInt32/glass](https://github.com/rashedInt32/glass) - Tampilan aplikasi desktop untuk transkrip terminal Claude Code, sebagai mod.
- [xuanji86/claude-agentpane](https://github.com/xuanji86/claude-agentpane) - Panel samping untuk Claude Code: subagen yang dijalankan sesi, apa yang sedang…
- [letswritetw/claude-mod-open-todos](https://github.com/letswritetw/claude-mod-open-todos) - Panel bilah samping Claude Desktop (tab Code): mencantumkan semua tugas…
- [letswritetw/claude-mod-token-usage](https://github.com/letswritetw/claude-mod-token-usage) - Bilah penggunaan di atas kotak input Claude Desktop (tab Code): kuota 5j / 7h…
- [BeLazy167/claude-mods-skill](https://github.com/BeLazy167/claude-mods-skill) - Skill yang mengajarkan agen Claude Code untuk membuat Claude Mod.
- [GoneTone/cc-askpass](https://github.com/GoneTone/cc-askpass) - Mod Claude Code yang memungkinkan Claude menjalankan perintah yang memerlukan…
- [omarcevi/claudemods](https://github.com/omarcevi/claudemods) - Mod, plugin &amp; skill Claude komunitas, dapat diinstal dari satu marketplace.
- [KilimcininKorOglu/claude-code-mods](https://github.com/KilimcininKorOglu/claude-code-mods) - Claude Mod (plugin function-hook) untuk Claude Code.
- [baselane-sh/mods-catalog](https://github.com/baselane-sh/mods-catalog) - Galeri mod Baselane: mod Claude Code yang telah diperiksa dan disematkan.
- [eighteyes/cactus](https://github.com/eighteyes/cactus) - Antrean keputusan CLI/TUI untuk manusia yang bekerja dengan agen percakapan.
- [jkf87/ide-mod](https://github.com/jkf87/ide-mod) - Mod panel IDE Claude Code: papan agen, pohon file dan penampil HWP/PDF, status…
- [natsukium/claude-code-figures-plugin](https://github.com/natsukium/claude-code-figures-plugin) - Gambar diagram, matematika LaTeX, dan citra hasil alat secara inline di…
- [neteye-platform/cc-split-diff-view](https://github.com/neteye-platform/cc-split-diff-view) - Mod Claude Code yang menggambar perbedaan Edit dan Write dalam dua kolom…
- [nogu66/md-prompt](https://github.com/nogu66/md-prompt) - Markdown, ditampilkan ke kotak prompt Claude Code saat Anda mengetik.
- [ray-amjad/claude-code-mods](https://github.com/ray-amjad/claude-code-mods) - Mod Claude Code milik Ray Amjad: panel, pita, penjaga prompt, penanganan…
- [ronanworks/claude-code-mods](https://github.com/ronanworks/claude-code-mods) - Mod Claude Code: panel penggunaan 像素螃蟹 usage-hud + tautan HTML yang dapat…
- [xuanji86/claude-statuspane](https://github.com/xuanji86/claude-statuspane) - Kartu status mengambang untuk Claude Code—model, konteks, batas laju, biaya…
- [arasovic/claude-code-mods](https://github.com/arasovic/claude-code-mods) - Mod untuk Claude Code: plugin hook fungsi yang menambahkan panel langsung dan…
- [danyuchn/claude-mods](https://github.com/danyuchn/claude-mods) - Mod Claude Code: screen-guard menyamarkan nama dan rahasia saat Anda berbagi…
- [magidandrew/cx](https://github.com/magidandrew/cx) - Ekstensi Claude Code. Buka seluruh kekuatan Claude.
- [markneonin/paneline](https://github.com/markneonin/paneline) - Mod (plugin) Claude Code yang menambahkan panel samping dengan tab Activity…
- [mishgoldenberg/claude-mods](https://github.com/mishgoldenberg/claude-mods) - Panel, pagar pengaman, dan mod peningkat kenyamanan untuk Claude Code: konteks…
- [ofeklevy11/claude-code-hud](https://github.com/ofeklevy11/claude-code-hud) - Dua mod Claude Code di atas kotak prompt: pengukur jendela konteks, batas 5…
- [VedantAndhale/claude-pro-kit](https://github.com/VedantAndhale/claude-pro-kit) - Buat paket Claude Pro bertahan lebih lama: mod Claude Code untuk HUD penggunaan…
- [xuanji86/claude-mdview](https://github.com/xuanji86/claude-mdview) - Baca file markdown yang diberi nama oleh Claude Code, tampilkan di samping…
- [hahmjuntae/claude-mods-image-preview](https://github.com/hahmjuntae/claude-mods-image-preview) - Mod Claude Code: thumbnail gambar yang ditempel di atas prompt, di terminal apa…
- [Jhonatan-de-Souza/ClaudeMods](https://github.com/Jhonatan-de-Souza/ClaudeMods) - Mod Claude Code: menu Tools Claude, mode Zen, tema terminal, kontrol upaya dan…
- [leopiney/wolfbud-claude-mod](https://github.com/leopiney/wolfbud-claude-mod) - Rekan kerja suara untuk Claude Code. Bicarakan berbagai hal dengan serigala 3D…
- [Boom-Vitt/boombignose-mods](https://github.com/Boom-Vitt/boombignose-mods) - Mod Claude Code: bilah konteks, panel agen, buram PDPA.
- [borabiricik/claude-mods](https://github.com/borabiricik/claude-mods) - Mod Claude Code: typing-speed, speedometer pengetikan langsung dengan statistik…
- [charimsma/dopa-mode](https://github.com/charimsma/dopa-mode) - Kembang api untuk Claude Code: setiap penekanan tombol, pemanggilan tool…
- [Danovich/turntype](https://github.com/Danovich/turntype) - Tes mengetik untuk mengisi waktu saat Claude bekerja. Mod Code Claude.
- [dougcunha/claude-mods](https://github.com/dougcunha/claude-mods) - Mod untuk Claude Code: panel, perintah, dan hook yang dibuat dengan plugin…
- [DrishtantKaushal/AwesomeClaudeCodeMods](https://github.com/DrishtantKaushal/AwesomeClaudeCodeMods) - Temukan mod, plugin, dan ekstensi Claude Code dengan demo animasi, daftar…
- [galElmalah/claude-mods](https://github.com/galElmalah/claude-mods) - Mod Claude Code: diagram mermaid yang digambar secara inline di transkrip.
- [GarvitNangru/claude-code-mods](https://github.com/GarvitNangru/claude-code-mods) - Mod dan skin untuk Claude Code: bilah kemajuan langsung untuk tugas Claude…
- [ha-ptt0601/cc-mods](https://github.com/ha-ptt0601/cc-mods) - Mod Claude Code kecil (plugin function-hook): session-switcher dan lainnya.
- [HMarzban/claude-mod](https://github.com/HMarzban/claude-mod) - Lihat biaya pesan Claude Code Anda berikutnya: pita langsung di atas prompt…
- [ice-lfernandes/claude-code-mods](https://github.com/ice-lfernandes/claude-code-mods) - Enam mod Claude Code: batas rencana dan konteks di atas prompt, pelatih daftar…
- [LeeHigma0201/claude-code-mods](https://github.com/LeeHigma0201/claude-code-mods) - Mod Claude Code: mod-scout (menemukan mod yang paling sering Anda gunakan)…
- [naicud/cc-vitals](https://github.com/naicud/cc-vitals) - Claude Code mod: a live vitals band above the prompt — tokens in/out, cache…
- [Nongfsq/frank-claude-cockpit](https://github.com/Nongfsq/frank-claude-cockpit) - Dua mod Claude Code untuk menjalankan banyak sesi sekaligus: kartu konteks di…
- [ayagmar/claude-modmgr](https://github.com/ayagmar/claude-modmgr) - modmgr: menemukan, memeriksa, mengaktifkan/nonaktifkan, dan memperbarui mod…
- [claude-code-mods/best-claude-code-mods](https://github.com/claude-code-mods/best-claude-code-mods) - Mod Claude Code terbaik: dipilih, divalidasi, dan disematkan secara khusus.
- [dominicrico/jev-router](https://github.com/dominicrico/jev-router) - Plugin Claude Code: perutean model Claude otomatis.
- [drkokorev/context-diet](https://github.com/drkokorev/context-diet) - Memangkas keluaran alat yang sangat besar sebelum memenuhi konteks Code Claude.
- [ElirazKed/claude-code-pr-watch](https://github.com/ElirazKed/claude-code-pr-watch) - Mod Claude Code: panel langsung berisi PR GitHub yang dibuka atau didorong oleh…
- [FynnXland/fynn-mods](https://github.com/FynnXland/fynn-mods) - Enam mod untuk Claude Code: maskot Clawd animasi, bar batas penggunaan dan…
- [Hula-Hoop-AI/supermods](https://github.com/Hula-Hoop-AI/supermods) - Marketplace mod untuk Claude Code: debugger langkah demi langkah untuk loop…
- [ibrahimkobeissy/claude-mods](https://github.com/ibrahimkobeissy/claude-mods) - Mod sumber terbuka untuk Claude Code: panel, baris status, toast, penjaga alat…
- [mertkayacs/ultramod](https://github.com/mertkayacs/ultramod) - Paket mod serba ada terbaik untuk Claude Code: batas penggunaan dan HUD…
- [mthli/cc-shorts](https://github.com/mthli/cc-shorts) - Putar YouTube Shorts di Claude Code Anda 💃.
- [NarenDawar/narens-claude-toolkit](https://github.com/NarenDawar/narens-claude-toolkit) - Toolkit Claude milik Naren: skills, mods, dan servers MCP untuk Claude Code.
- [raresmun/claude-mods](https://github.com/raresmun/claude-mods) - Mod untuk Claude Code: Clawd, maskot piksel kecil yang memerankan apa yang…
- [reporails/arcade](https://github.com/reporails/arcade) - Game desktop klasik sebagai mod Claude Code, dimainkan di panel saat Claude…
- [schreibse/claude-code-mods](https://github.com/schreibse/claude-code-mods) - code-mods untuk claude.
- [Szotasz/claude-mods](https://github.com/Szotasz/claude-mods) - Marketplace mod Claude Code milik saya sendiri.
- [testy-cool/awesome-claude-code-mods](https://github.com/testy-cool/awesome-claude-code-mods) - Daftar pilihan mod Claude Code yang dapat dipasang sebagai pasar plugin: tema…
- [timoncool/givememod](https://github.com/timoncool/givememod) - Mod Code Claude sesuai permintaan — keterampilan yang membaca percakapan Anda…
- [wdsewdser-bit/claude-code-mods](https://github.com/wdsewdser-bit/claude-code-mods) - Dua mod Claude Code: cache-keeper dan ctx-mod.
- [xsyetopz/dotclaude](https://github.com/xsyetopz/dotclaude) - Plugin Claude Code yang sangat berpendirian, dirancang oleh seorang Rustacean…
- [yash-gadodia/claude-mods](https://github.com/yash-gadodia/claude-mods) - Mod Claude Code yang menjaga kejujuran agen — function hook yang menjaga…
- [bostonaholic/claude-mods](https://github.com/bostonaholic/claude-mods) - Mod Code Claude yang saya gunakan.
- [chenyuxiaojin/cyxj-notch](https://github.com/chenyuxiaojin/cyxj-notch) - Dasbor notch macOS untuk Claude Code: batas penggunaan, sesi terbuka, progres…
- [chrisluo5311/squad-chat](https://github.com/chrisluo5311/squad-chat) - Claude sedang memasak. Chat dengan skuad Anda.
- [DarioFontanel/claude-code-mods](https://github.com/DarioFontanel/claude-code-mods) - Mod per Claude Code: bilah cache prompt, langkah berikutnya, tombol cepat, dan…
- [Elesiann/usagemeter](https://github.com/Elesiann/usagemeter) - Biaya, token, dan batas paket agen coding Anda.
- [estruyf/claude-stats-mod](https://github.com/estruyf/claude-stats-mod) - Mod Claude Code yang menggambar batas penggunaan dan pengeluaran Anda di bilah…
- [herman925/925-cc-plugins](https://github.com/herman925/925-cc-plugins) - Mod Claude Code milik Herman (marketplace herman-mods).
- [homieyangg/claude-code-mods](https://github.com/homieyangg/claude-code-mods) - Mod Claude Code: bilah kemajuan untuk rencana, catatan tentang apa yang masih…
- [lorenzh/rabe](https://github.com/lorenzh/rabe) - Lihat apa yang dijalankan Claude Code di latar belakang: subagen, pekerjaan…
- [macleodlabs-ai/claudeflow](https://github.com/macleodlabs-ai/claudeflow) - Mod Claude Code oleh MacLeod Labs: streams mengurai pekerjaan yang saling…
- [MankhongGarden/claude-code-mods-field-notes](https://github.com/MankhongGarden/claude-code-mods-field-notes) - Catatan lapangan hari pertama tentang mod Claude Code di Windows: bilah bahan…
- [NMenzel/claude-devtools-mod](https://github.com/NMenzel/claude-devtools-mod) - DevTools Claude: debugger untuk pemanggilan alat Code Claude.
- [oborchers/claude-gh-status](https://github.com/oborchers/claude-gh-status) - Mod Claude Code: status pull request GitHub langsung.
- [oMaN-Rod/claude-code-widgets](https://github.com/oMaN-Rod/claude-code-widgets) - Kartu-kartu kecil yang berada di bawah prompt Claude Code, atau dipasang di…
- [patitow/claude-mod-cost-visibility](https://github.com/patitow/claude-mod-cost-visibility) - Mod Claude Code: meter biaya langsung, konteks &amp; kuota paket di atas prompt.
- [rbartoli/agent-usage-guard](https://github.com/rbartoli/agent-usage-guard) - Mod Claude Code yang menahan fan-out subagent, prompt konteks berat, dan loop…
- [revenantworks/claude-skills](https://github.com/revenantworks/claude-skills) - 28 Agent Skills untuk Claude dalam lima paket.
- [ruslanshchuchkin/claude-techno-mod](https://github.com/ruslanshchuchkin/claude-techno-mod) - 😈 Kami sedang membuat TECHNO, sayang 😈.
- [Sennjen/claude-sdlc](https://github.com/Sennjen/claude-sdlc) - Plugin dan mod Claude Code: SDLC AI-native.
- [shimo4228/harness-scope](https://github.com/shimo4228/harness-scope) - Mod Claude Code yang mengaktifkan atau menonaktifkan skill, agen, aturan, dan…
- [simplecore-inc/claude-mods](https://github.com/simplecore-inc/claude-mods) - Plugin Claude Code (mod): beralih di antara beberapa akun Claude, memantau…
- [Singh-AP/awesome-claude-mods](https://github.com/Singh-AP/awesome-claude-mods) - 🧩 Mod Claude Code yang telah diuji dan dapat dipasang dengan satu perintah…
- [Sma1lboy/claude-mods](https://github.com/Sma1lboy/claude-mods) - Mod untuk Claude Code: plugin yang dibangun berdasarkan function hooks.
- [soulrocha/Claude-code-hero-journey](https://github.com/soulrocha/Claude-code-hero-journey) - 🦀 A cozy RPG HUD mod for Claude Code.
- [theonly1me/claude-code-mods](https://github.com/theonly1me/claude-code-mods) - Sekumpulan mod claude code yang dibuat oleh saya.
- [VladLeus/claude-mods](https://github.com/VladLeus/claude-mods) - Claude Code mods: agent-fleet dashboard and autopilot (local-mods marketplace).
- [y-hirakaw/claude-code-mods](https://github.com/y-hirakaw/claude-code-mods) - Mod Claude Code. touch-map: lihat berkas mana yang dicantumkan, dibaca, diedit…
- [yodakeisuke/claudelingo](https://github.com/yodakeisuke/claudelingo) - Pelajari bahasa asing sambil bekerja dengan Claude Code.
- [0xctx/sysop](https://github.com/0xctx/sysop) - Tell Claude what you want. Get it back built, tested, reviewed by another AI…
- [20alexl/windvane](https://github.com/20alexl/windvane) - Menjaga sesi Claude Code yang panjang agar Anda tidak perlu melakukannya…
- [404Mayank/cachebeat](https://github.com/404Mayank/cachebeat) - A Claude Code mod that keeps your prompt cache warm while you.
- [andrewbakercloudscale/claude-code-cost-sidebar](https://github.com/andrewbakercloudscale/claude-code-cost-sidebar) - Bilah samping penggunaan biaya, token, dan konteks secara langsung untuk Claude…
- [atharv6f/headway](https://github.com/atharv6f/headway) - Tujuan, tugas, dan agen di atas prompt Code Claude Anda — tanpa penyiapan.
- [comertial/comertial-mods](https://github.com/comertial/comertial-mods) - Mod Claude Code untuk Engineer sungguhan.
- [CrazyCoder/claude-desktop-recap](https://github.com/CrazyCoder/claude-desktop-recap) - Rekap sesi terminal Code Claude, di tab Code pada aplikasi desktop Claude.
- [crebot51/jack-mods](https://github.com/crebot51/jack-mods) - Koleksi mod Claude Code milik jack.
- [crockalet/claude-mods](https://github.com/crockalet/claude-mods) - Mod Claude Code: panel berisi tugas sesi, hal yang memerlukan Anda, prompt…
- [danielpg95/modster-hunter](https://github.com/danielpg95/modster-hunter) - Mod Claude Code: tangkap Modsters pixel-art dalam gim idle saat Claude bekerja.
- [Davron2004/slash-coverage](https://github.com/Davron2004/slash-coverage) - Lihat file mana yang ada dalam konteks setiap agen Claude Code, dan seberapa…
- [deejay-hub/sf-headless-band](https://github.com/deejay-hub/sf-headless-band) - Mod Claude Code yang menampilkan Orgs mana yang terhubung untuk Salesforce.
- [delexw/codyssey](https://github.com/delexw/codyssey) - Ubah setiap sesi Claude Code menjadi petualangan kecil: musik generatif yang…
- [enhki/claude-mods](https://github.com/enhki/claude-mods) - Mod kecil Claude Code untuk terminal dan aplikasi desktop.
- [Exdenta/ambient-spanish](https://github.com/Exdenta/ambient-spanish) - Skill + mod Claude CLI yang menambahkan kata-kata Spanyol ke balasan agen.
- [FrBmt-BIGetNouf/alarum-claude-mod](https://github.com/FrBmt-BIGetNouf/alarum-claude-mod) - Acara Alarum Anda di atas prompt Claude Code: apa yang baru saja tiba, dan satu…
- [FrBmt-BIGetNouf/floatee-claude-mod](https://github.com/FrBmt-BIGetNouf/floatee-claude-mod) - Backlog Floatee Anda di atas prompt Claude Code: jalankan, pandu, dan centang…
- [gaius-codius/ostrakon](https://github.com/gaius-codius/ostrakon) - Mod Claude Code untuk menangkap pemikiran saat bekerja, memilahnya di berbagai…
- [gonzalonicolasr/claude-code-nerv](https://github.com/gonzalonicolasr/claude-code-nerv) - Bilah samping bergaya Evangelion untuk Claude Code: konteks, kuota, aktivitas…
- [gregdotca/ccmod-the-machine](https://github.com/gregdotca/ccmod-the-machine) - Mod kode Claude yang menata ulang tampilannya menjadi The Machine dari Person…
- [herlonventura/claude-model-squad](https://github.com/herlonventura/claude-model-squad) - Mod Claude Code: regu seni piksel menyarankan model yang tepat.
- [HyunjunJeon/claude-workflow-mods](https://github.com/HyunjunJeon/claude-workflow-mods) - dag-workflow: mod Claude Code untuk alur kerja DAG subagen yang wajib dan…
- [jduerrmann/agent-crew](https://github.com/jduerrmann/agent-crew) - Mod kode Claude: satu panel untuk setiap subagen, file yang mereka sentuh…
- [JimmySadek/claude-code-tint-mod](https://github.com/JimmySadek/claude-code-tint-mod) - Mod Claude Code (mod CC tint): mewarnai setiap jendela berdasarkan…
- [joeldg/claude-mods](https://github.com/joeldg/claude-mods) - Berbagai mod yang saya buat untuk claude dan menurut saya bermanfaat.
- [jonyfs/astrolabe](https://github.com/jonyfs/astrolabe) - 🧭 Mod Claude Code: status sesi, kemajuan Spec Kit live, dan tata kelola jendela…
- [kongyo2/context-view](https://github.com/kongyo2/context-view) - Jendela konteks sebagai satu baris di atas prompt, digambar seperti meter milik…
- [kyledarling-io/claude-code-desktop-hud](https://github.com/kyledarling-io/claude-code-desktop-hud) - HUD tugas langsung untuk Claude Code Desktop: strip di atas prompt saat Claude…
- [KyongSik-Yoon/cc-desktop-mod](https://github.com/KyongSik-Yoon/cc-desktop-mod) - Plugin Claude Code (mod) yang membuat UI terminal Claude Code terlihat seperti…
- [leonidb/claude-code-mods](https://github.com/leonidb/claude-code-mods) - Jangan biarkan perhatian Anda teralihkan saat menunggu jawaban Code Claude.
- [LupusMalusDeviant/mod-box](https://github.com/LupusMalusDeviant/mod-box) - Empat belas mod Claude Code dalam satu plugin, masing-masing dapat diaktifkan…
- [m4cd4r4/clear-resume](https://github.com/m4cd4r4/clear-resume) - Plugin gratis dan open-source untuk Claude Code.
- [magiccreator-ai/awesome-claude-code-mods](https://github.com/magiccreator-ai/awesome-claude-code-mods) - Mod Claude Code pilihan, demo kreator asli, repositori publik, dan sumber daya…
- [mangow314/mango-mods](https://github.com/mangow314/mango-mods) - Mod Claude Code untuk sesi panjang: sitrep merangkum hasil dan pertanyaan…
- [modmyclaude/claude-code-mods](https://github.com/modmyclaude/claude-code-mods) - Mod Claude Code: dikurasi, diuji, dan setiap mod dilengkapi prompt yang…
- [muctebadikmen/claude-code-araclari](https://github.com/muctebadikmen/claude-code-araclari) - Mod Code Claude: serah terima otomatis dan bilah kemajuan.
- [NotRedFox/NotRedFoxs-Claude-skills](https://github.com/NotRedFox/NotRedFoxs-Claude-skills) - Keahlian Claude Code: pemeriksa fakta dokumen, auditor kode, log memori bug…
- [ondrhn/sharpprompt](https://github.com/ondrhn/sharpprompt) - Mod Claude Code yang menulis ulang prompt kasar menjadi jelas sebelum Anda…
- [pablodiazjorge/rea-casebook](https://github.com/pablodiazjorge/rea-casebook) - Mod Claude Code yang menyimpan casebook langsung berisi bukti yang diberikan…
- [PedroLaRosa/claude-code](https://github.com/PedroLaRosa/claude-code) - Mod Claude Code milik Pedro La Rosa, dalam satu marketplace plugin.
- [pepperonas/usage-bars](https://github.com/pepperonas/usage-bars) - Mod Claude Code: batas penggunaan 5 jam dan 7 hari Anda sebagai bilah animasi…
- [rezzminator/buddy](https://github.com/rezzminator/buddy) - Plugin teman Claude Code: pendamping ASCII di atas prompt Anda yang mengingat…
- [rezzminator/tool-visibility-controller](https://github.com/rezzminator/tool-visibility-controller) - Plugin Claude Code untuk visibilitas alat per agent — sembunyikan dan tolak…
- [samox73/claude-code-latex](https://github.com/samox73/claude-code-latex) - Render matematika tampilan LaTeX di terminal Claude Code: MathJax sudah…
- [shahsanket2107/clarvis](https://github.com/shahsanket2107/clarvis) - Clarvis: mod penggemar Avengers tidak resmi untuk Code Claude.
- [tanujarun/it-speaks](https://github.com/tanujarun/it-speaks) - It Speaks: mod Claude Code yang membacakan balasan Claude dan prompt Anda saat…
- [thangvofastboy/claude-mods](https://github.com/thangvofastboy/claude-mods)
- [timoncool/slapbox](https://github.com/timoncool/slapbox) - 🍑 Pukul Claude saat berbuat salah — mod pelepas stres untuk Claude Code: bokong…
- [TroyJLorents-GH/mod-squad](https://github.com/TroyJLorents-GH/mod-squad) - Mod Claude Code: plugin kecil untuk panel langsung, pengaturan perutean model…
- [valeryia-piatrova/token-hamster](https://github.com/valeryia-piatrova/token-hamster) - 🐹 Mod &amp; plugin Claude Code: monitor penggunaan, pelacak token &amp; baris status.
- [VictorGambarini/jev-mod](https://github.com/VictorGambarini/jev-mod) - Mod Claude Code yang menyerahkan keputusan-keputusan kecil kepada model…
- [0r0loo/claude-mods](https://github.com/0r0loo/claude-mods)
- [achiurizo/dreeft](https://github.com/achiurizo/dreeft) - Tangkap perubahan arah pemikiran sesi Claude Code-mu, tepat di atas prompt.
- [AgemameSutachi/claude-code-mods](https://github.com/AgemameSutachi/claude-code-mods)
- [agukov-dev/token-meter](https://github.com/agukov-dev/token-meter) - Claude Code mod: rate limits, context and spend under the prompt.
- [akaz01/claude-mods](https://github.com/akaz01/claude-mods) - Marketplace mod Claude Code: agent-board, auto-model, session-collab + mod…
- [akixi-maison/usage-mods](https://github.com/akixi-maison/usage-mods) - Mod Claude Code: bilah progres penggunaan (konteks, 5j, 7h) dan tombol ringkas…
- [alan-oliv/claude-mods](https://github.com/alan-oliv/claude-mods) - Mod Claude Code: kartu statistik sesi di atas prompt.
- [Aler1x/claude-cat](https://github.com/Aler1x/claude-cat) - Kucing braille animasi di atas prompt Claude Code.
- [alinaqi/mixture-of-models-claude-mod](https://github.com/alinaqi/mixture-of-models-claude-mod) - Mod Claude Code: mengarahkan pekerjaan ringan ke GLM/Kimi melalui Claude Code…
- [aloki-alok/omni-cat](https://github.com/aloki-alok/omni-cat) - Kucing piksel di atas prompt Code Claude Anda yang menjalankan panggilan uji…
- [ambervdberg/smartcompact](https://github.com/ambervdberg/smartcompact) - Mod Claude Code yang memilih waktu yang tepat untuk melakukan pemadatan agar…
- [an80sPWNstar/claude-mods](https://github.com/an80sPWNstar/claude-mods) - Mod Claude untuk Claude Code: token-meter.
- [andrej-kolic/claude-mods](https://github.com/andrej-kolic/claude-mods) - Mod serbaguna untuk Claude Code: band, panel, toast, dan hook.
- [arifamir/nukey](https://github.com/arifamir/nukey) - Nukey si microwave: pasar mod dan plugin Claude Code.
- [Ashley-Pettit/villager-hp](https://github.com/Ashley-Pettit/villager-hp) - Batas penggunaan Claude Anda sebagai kartu kesehatan penduduk desa animasi…
- [AskTinNguyen/ather-mods](https://github.com/AskTinNguyen/ather-mods) - Mod Claude Code untuk tim S2 (marketplace ather).
- [Atanur/deskfit](https://github.com/Atanur/deskfit) - Latihan singkat saat Claude bekerja: target harian, streak, badge, dan…
- [aycandv/claude-usage-meter](https://github.com/aycandv/claude-usage-meter) - Papan penggunaan untuk Claude Code: pengeluaran per model.
- [bastianfuchs/claude-code-cache-warm](https://github.com/bastianfuchs/claude-code-cache-warm) - Mod Claude Code yang menampilkan hitung mundur cache prompt di footer dan…
- [benjaminr/nowplaying](https://github.com/benjaminr/nowplaying) - Mod Now Playing untuk Claude Code: Apple Music dan Spotify di atas prompt…
- [broening/claude-mods](https://github.com/broening/claude-mods) - Mod untuk Claude Code: Cache-Uhr, Blast Radius, Vorschlaege, Arbeitsliste, Grill.
- [Broo37/claude-mods](https://github.com/Broo37/claude-mods) - Mod untuk Claude Code: Clean View menyembunyikan pemanggilan alat dan…
- [BuddyLim/claude-code-mod-ledger](https://github.com/BuddyLim/claude-code-mod-ledger) - Mod Claude Code: catatan pekerjaan terorkestrasi, dengan eksekusi, jalur…
- [C-M-Jones/suggestion-spotlight](https://github.com/C-M-Jones/suggestion-spotlight) - Mod Claude Code: Suggestion Spotlight menampilkan rujukan prompt berikutnya…
- [Carismarkus/clowl](https://github.com/Carismarkus/clowl) - Hanya seekor owl untuk Claude Code Anda.
- [cfelipemoreira/claude-code-mods](https://github.com/cfelipemoreira/claude-code-mods) - Mod Claude Code yang dibuat oleh saya (panel, perintah, dan hook).
- [ChaseWNorton/claude-doom](https://github.com/ChaseWNorton/claude-doom) - Engine Doom asli dengan Freedoom, dapat dimainkan di dalam Claude Code.
- [chittychat-studio/claude-code-mods](https://github.com/chittychat-studio/claude-code-mods) - Small, readable Claude Code mods from the CorporateChittyChat channel.
- [colorfield/claude-ci-watch](https://github.com/colorfield/claude-ci-watch) - Claude Code mod: Pane and status line for the current branch.
- [colorfield/claude-lagoon-watch](https://github.com/colorfield/claude-lagoon-watch) - Claude Code mod: Pane with the Lagoon project.
- [colorfield/claude-port-guard](https://github.com/colorfield/claude-port-guard) - Claude Code mod: Stops Claude from killing, or running E2E tests against…
- [colorfield/claude-session-line](https://github.com/colorfield/claude-session-line) - Claude Code mod: Status line with context fill, model, effort, git branch or…
- [comertial/claude-pending-changes](https://github.com/comertial/claude-pending-changes) - Tinjau setiap file yang disentuh Claude, seperti pull request, tanpa…
- [connectwithub/loopkeeper](https://github.com/connectwithub/loopkeeper) - Keep Claude Code on a plan: stages, approval gates and a file budget enforced…
- [CTeitzel/claude-code-cache-band](https://github.com/CTeitzel/claude-code-cache-band) - Mod Claude Code: pita di atas prompt dengan hitung mundur cache prompt, isi…
- [cybertron288/claude-mods](https://github.com/cybertron288/claude-mods) - My personal Claude Code mods, customised for my own setup.
- [d3nims/d3nim-claude-mods](https://github.com/d3nims/d3nim-claude-mods) - Mod Claude Code khusus tim d3nim.
- [dankelleher/claude-mod-pin-message](https://github.com/dankelleher/claude-mod-pin-message) - Mod Claude Code: sematkan balasan di atas prompt, dapat diciutkan menjadi…
- [davidcoulson/crab-workshop](https://github.com/davidcoulson/crab-workshop) - Sebelas mod Claude Code (plugin function-hook) untuk alur kerja homelab dengan…
- [davidcoulson/session-crew](https://github.com/davidcoulson/session-crew) - Mod Claude Code yang menampilkan sesi sampingan yang dimulai sesi desktop…
- [daviddecorso/claude-mods](https://github.com/daviddecorso/claude-mods)
- [davidho27941/cockpit](https://github.com/davidho27941/cockpit) - Claude Code mods: an OpenSpec and sub agent board, hand over before compacting…
- [davidurco/cc-tamagotchi](https://github.com/davidurco/cc-tamagotchi) - Tamagotchi yang hidup di dalam Claude Code: ia menetas, memakan kode yang…
- [DazzleML/claude-bookmarks](https://github.com/DazzleML/claude-bookmarks) - Bookmark dan mark bergaya vim di dalam percakapan terminal Claude Code: sorot…
- [DerpcatMusic/claude-context-controls](https://github.com/DerpcatMusic/claude-context-controls) - Claude Code mod: nested context / 5h / weekly rings, compaction threshold and…
- [devsomelife/somelife-claude-mods](https://github.com/devsomelife/somelife-claude-mods)
- [dgsantana/claude-mods](https://github.com/dgsantana/claude-mods) - Mod Claude Code: omp-port.
- [dhiroo-jpg/claude-mods](https://github.com/dhiroo-jpg/claude-mods) - クロードの使用量をチャット画面に表示.
- [diamondT/claude-mods](https://github.com/diamondT/claude-mods)
- [dieg666/claude-herald](https://github.com/dieg666/claude-herald) - Mod Code Claude: bilah di atas prompt dengan berita Claude serta rilis penting…
- [dim-owl/roll-call](https://github.com/dim-owl/roll-call) - Mod Claude Code: papan sesi Anda yang lain di atas prompt — siapa yang menunggu…
- [dot-agi/arrester](https://github.com/dot-agi/arrester) - Mod Claude Code: setelah guard memblokir pemanggilan alat, mod ini menghentikan…
- [dot-agi/downrange](https://github.com/dot-agi/downrange) - Mod Claude Code: pekerjaan latar belakang dalam satu tampilan, dengan kemajuan…
- [dot-agi/high-command](https://github.com/dot-agi/high-command) - Mod Claude Code: satu kotak masuk untuk pesan dari rekan tim, subagen bernama…
- [dot-agi/sandbox-tuner](https://github.com/dot-agi/sandbox-tuner) - Mod Claude Code: menjelaskan pemblokiran sandbox dan mengubah pemblokiran…
- [drolosoft/taskrail](https://github.com/drolosoft/taskrail) - A live wave board of your session.
- [duylinhdang1998/my-claude-mods](https://github.com/duylinhdang1998/my-claude-mods)
- [Eiyuo/Claude-Mods](https://github.com/Eiyuo/Claude-Mods)
- [elijah-rou/agent-kit](https://github.com/elijah-rou/agent-kit) - Instruksi, skill, ekstensi Pi, dan mod Claude Code untuk Pi, Codex, dan Claude…
- [feizaodemon/claude-mods](https://github.com/feizaodemon/claude-mods) - Mod Claude Code (plugin function-hook): session-meter dan lainnya.
- [fllag/claude-mods](https://github.com/fllag/claude-mods) - Mods em teste do time da Hospedin para o Claude Code.
- [freewisl/nunchi](https://github.com/freewisl/nunchi) - nunchi — a Claude Code mod: a mascot that reads the room above the prompt, with…
- [g761007/hudcade](https://github.com/g761007/hudcade) - HUD pixel art untuk Claude Code: konteks, biaya, cache, agen, dan batas laju…
- [gauravruhela07/claude-mods](https://github.com/gauravruhela07/claude-mods) - Tujuh mod Claude Code: savvy-progress, skins, filetree, cache-tax…
- [gggg5151/claude-desktop-links-to-vscode-mod](https://github.com/gggg5151/claude-desktop-links-to-vscode-mod) - A Claude Code mod for the desktop app: click a file reference in a reply and it…
- [gsporto226/claude-mods](https://github.com/gsporto226/claude-mods) - Mod claude code yang bermanfaat.
- [hal-9/claude-mods](https://github.com/hal-9/claude-mods) - Marketplace privat untuk mod Claude Code.
- [hb03/claude-mods](https://github.com/hb03/claude-mods) - Mod berbahasa Jerman untuk Claude Code: petunjuk konteks/cache, hal-hal yang…
- [HectorBailey/claude-mods](https://github.com/HectorBailey/claude-mods) - Mod Claude Code milik Hector Bailey (plugin marketplace: hectorbailey).
- [humvnpvrvdox777/NextSteps](https://github.com/humvnpvrvdox777/NextSteps) - Mod Code Claude: tiga langkah berikutnya setelah setiap jawaban, dalam bahasa…
- [Huuuuung/think-meter](https://github.com/Huuuuung/think-meter) - Mod Claude Code: berapa lama setiap jawaban berlangsung, berapa lama Claude…
- [hymleong/claude-mods](https://github.com/hymleong/claude-mods) - claude mods marketplace.
- [imsungbin/quackpit-mod](https://github.com/imsungbin/quackpit-mod) - Kokpit di atas perintah Code Claude Anda. Bebek membaca pengukur.
- [isandrel/redact-restore](https://github.com/isandrel/redact-restore) - Redaksi yang dapat dibatalkan untuk Claude Code: nilai privat diganti dengan…
- [jaeseongs95/claude-code-mods](https://github.com/jaeseongs95/claude-code-mods) - Bilah Status Claude.
- [jakerains/claudemods](https://github.com/jakerains/claudemods) - Mod Claude Code kecil: pengukur penggunaan konteks dan rencana, pengukur cache…
- [jalsarraf0/claudemod](https://github.com/jalsarraf0/claudemod) - Mod Claude Code: bilah konteks dan HUD cyberdeck.
- [jasonXiao422/drawing2sw](https://github.com/jasonXiao422/drawing2sw) - Membaca gambar teknik Anda secara otomatis, lalu membuat model di SolidWorks.
- [jeffyfung/claude-mods](https://github.com/jeffyfung/claude-mods) - Tempat untuk menampung mod claude saya.
- [jessetsai1024/claude-ctx-panel](https://github.com/jessetsai1024/claude-ctx-panel) - Panel penggunaan context di bilah samping: total, kategori, pertumbuhan tiap…
- [jessetsai1024/claude-files](https://github.com/jessetsai1024/claude-files) - Daftar file di bilah samping: file apa yang dibuat, diubah, atau dihapus dalam…
- [jessetsai1024/claude-maomao](https://github.com/jessetsai1024/claude-maomao) - 毛毛 bergaya 8-bit (kelinci lop Belanda hitam-putih) berlari dan melompat di atas…
- [jessetsai1024/claude-prompts](https://github.com/jessetsai1024/claude-prompts) - “Yang pernah saya tanyakan” di bilah samping: setiap kalimat yang diketik…
- [jessetsai1024/claude-timeline](https://github.com/jessetsai1024/claude-timeline) - Linimasa di bilah samping: ke mana waktu putaran ini digunakan.
- [jessetsai1024/claude-tokens](https://github.com/jessetsai1024/claude-tokens) - Pertukaran token di bilah samping: berapa token yang dikirim percakapan utama…
- [jessetsai1024/claude-whisper](https://github.com/jessetsai1024/claude-whisper) - Tas kacang jujur untuk claude code: setelah setiap putaran selesai menjawab…
- [Jh-jaehyuk/plan-checklist](https://github.com/Jh-jaehyuk/plan-checklist) - Daftar periksa rencana berbasis bukti untuk Claude Code: rencana yang disetujui…
- [jiangnanquan/claude-code-zh](https://github.com/jiangnanquan/claude-code-zh) - Claude Code CLI Terjemahan bahasa Tionghoa Sederhana (versi mandiri) — tabel…
- [jkf87/mod-guide](https://github.com/jkf87/mod-guide) - Panduan komunitas tidak resmi untuk mod Claude Code (hook fungsi) dalam 6…
- [jo-greco/johnny-mods](https://github.com/jo-greco/johnny-mods) - Dua mod Claude Code: serah-terima sesi dengan balasan, dan pengalihan giliran…
- [Joseph-Ayoub/claude-mods](https://github.com/Joseph-Ayoub/claude-mods) - Joseph Ayoub.
- [kad1r/claude-mods](https://github.com/kad1r/claude-mods)
- [KaiC5504/clawd-bar](https://github.com/KaiC5504/clawd-bar) - Clawd tinggal di pita di atas prompt Claude Code Anda: memeragakan sesi…
- [kartollikaa/claude-android-emulator](https://github.com/kartollikaa/claude-android-emulator) - Claude Code mod: Android emulator and device screens inside Claude Code.
- [kbrdn1/claude-crosstalk](https://github.com/kbrdn1/claude-crosstalk) - Mod Claude untuk membaca dan bergabung dalam percakapan antara sesi Claude Code…
- [ke11/claude-mods](https://github.com/ke11/claude-mods) - Mod Claude Code. PixBar: makhluk piksel di atas prompt Anda yang bergerak…
- [KiranPothana/session-board](https://github.com/KiranPothana/session-board) - Mod Claude Code: setiap sesi Claude Code dalam satu jendela mengambang, dengan…
- [klefix/claude-code-mods](https://github.com/klefix/claude-code-mods) - Beberapa bukti konsep untuk claude-code-mods.
- [krichardson/claude-mods](https://github.com/krichardson/claude-mods) - Mod Claude Code, diterbitkan sebagai marketplace.
- [kuehn-lars/cc-graph](https://github.com/kuehn-lars/cc-graph) - cc-graph: grafik langsung tentang apa yang diketahui Claude Code.
- [l4ckofsleep/ccdetails](https://github.com/l4ckofsleep/ccdetails) - Claude Code mod: context fill, prompt-cache hit %, rate limits and cost above…
- [lakmadev/claude-mods](https://github.com/lakmadev/claude-mods) - Ten Claude Code mods: an animated pixel pet, Code Wrapped, lo-fi beats, plus a…
- [linsanmufilm-svg/claude-mods](https://github.com/linsanmufilm-svg/claude-mods) - Mod Claude Code milik Sanmu — marketplace plugin (panel samping to-do).
- [lua-erissatallan/claude-mods](https://github.com/lua-erissatallan/claude-mods)
- [Lucas-CX/awesome-claude-mods](https://github.com/Lucas-CX/awesome-claude-mods) - Panduan Mod Claude Code yang dikurasi komunitas: kasus penggunaan, demo asli…
- [M-i-k-e-l/agent-state](https://github.com/M-i-k-e-l/agent-state) - Mod Claude Code yang menampilkan apa yang sedang dilakukan Claude di subtitel…
- [magiclin99/buddy-go](https://github.com/magiclin99/buddy-go) - Buddy, pendamping piksel tidak resmi buatan penggemar yang berada di atas…
- [makingaipractical/brain-drain-for-claude-code](https://github.com/makingaipractical/brain-drain-for-claude-code) - Seberapa penuh konteks Claude, kapan cache-nya menjadi dingin, dan berapa…
- [malinfossum/mango-buddy](https://github.com/malinfossum/mango-buddy) - Seekor kucing hitam berbulu di atas prompt Claude Code Anda.
- [Malkiz/claude-reply-comments](https://github.com/Malkiz/claude-reply-comments) - Mod Claude Code: jawab Claude poin demi poin, langsung pada teks.
- [MarkMerk/markmerk-mods](https://github.com/MarkMerk/markmerk-mods) - Mod kecil untuk Code Claude: runner-avatar, avatar kecil yang berlari di atas…
- [martin-macak/claude-code-mod-tracking](https://github.com/martin-macak/claude-code-mod-tracking) - Claude Code mod for tracking related artifacts and references.
- [mategog/mateai-mods](https://github.com/mategog/mateai-mods) - Mod kecil Claude Code dari kanal MateAI.
- [matrac/burnline](https://github.com/matrac/burnline) - Claude Code mod: usage limits and task progress in one status line.
- [mattbv/intent-ledger](https://github.com/mattbv/intent-ledger) - Mod Claude Code: panel langsung yang menampilkan sasaran, asumsi, rencana, dan…
- [max-gom/claude-session-remover](https://github.com/max-gom/claude-session-remover) - Mod Claude Code: panel /sessions untuk menelusuri dan menghapus sesi beserta…
- [michaelblaess/turbo-mod](https://github.com/michaelblaess/turbo-mod) - Panel samping untuk Claude Code: file yang ditulis Claude, pemisah terminal…
- [micke-dahlgren/token-range-monitor](https://github.com/micke-dahlgren/token-range-monitor) - Mod Claude Code: memproyeksikan sisa batas mingguan dan 5 jam Claude Anda saat…
- [Miriam2040/nugget](https://github.com/Miriam2040/nugget) - Select any part of Claude.
- [mmedum/glimt](https://github.com/mmedum/glimt) - Panel samping yang tenang untuk Claude Code: apa yang sedang dilakukan sesi…
- [mmedum/nuet](https://github.com/mmedum/nuet) - Waktu redup di atas setiap prompt dan setiap balasan dalam transkrip Code…
- [moinsen-dev/speckit-xref](https://github.com/moinsen-dev/speckit-xref) - Pertahankan kode sesuai spesifikasi: mod Claude Code dan ekstensi GitHub Spec…
- [Monte9/claude-mods](https://github.com/Monte9/claude-mods) - Plugin Claude Code untuk sesi dan memori: mod panel Memory dan skill…
- [muellerei/enable-todo-tools](https://github.com/muellerei/enable-todo-tools) - Mod Claude Code yang mengaktifkan kembali alat todo untuk model yang tidak…
- [muellerei/sweet-spot](https://github.com/muellerei/sweet-spot) - Mod Claude Code yang menunggu jeda aman, lalu menyerahkan sesi Anda atau…
- [muellerei/task-line](https://github.com/muellerei/task-line) - Mod Claude Code: satu baris per tugas di atas prompt dengan tugas saat ini…
- [mwmrs/claude-mods](https://github.com/mwmrs/claude-mods)
- [nachtgold/claude-code-connect-four](https://github.com/nachtgold/claude-code-connect-four) - Mainkan Connect Four melawan AI di dalam Claude Code (/connect-four).
- [naoanao/agent-cross-check](https://github.com/naoanao/agent-cross-check) - Mod Claude Code: ketika agen coding lain melakukan commit ke repo Anda, Claude…
- [naoanao/context-saver](https://github.com/naoanao/context-saver) - Mod Claude Code: menjaga sesi tetap ringan — bar penggunaan, peringatan, dan…
- [naoanao/shared-repo-guard](https://github.com/naoanao/shared-repo-guard) - Mod Claude Code untuk repo yang dibagikan oleh beberapa agen AI: menghentikan…
- [Nasrallah-Adel/claude-delegate-launcher](https://github.com/Nasrallah-Adel/claude-delegate-launcher) - Claude Code mod: one button per delegate-skills implementer.
- [ngxuanbminh/pr-watch](https://github.com/ngxuanbminh/pr-watch) - Claude Code mod: watch the GitHub PRs of the repo you.
- [nnemirovsky/cc-monitor-rearm](https://github.com/nnemirovsky/cc-monitor-rearm) - Mengaktifkan kembali pemantauan Monitor jangka panjang Claude Code saat…
- [nu0ma/query-guard](https://github.com/nu0ma/query-guard) - Pagar pengaman untuk SQL di Claude Code: meminta konfirmasi sebelum Claude…
- [OG-Matcha/tessera](https://github.com/OG-Matcha/tessera) - Satu mod untuk Claude Code, Windows dan CJK terlebih dahulu: pratinjau gambar…
- [osaki42/awesome-claude-mods](https://github.com/osaki42/awesome-claude-mods) - Mod Claude Code terbaik, diurutkan berdasarkan manfaatnya bagi Anda.
- [Para-FR/claude-code-mods-fr](https://github.com/Para-FR/claude-code-mods-fr) - Dua Mod Claude untuk Claude Code: garde-du-corps.
- [paragpandyareal/claude-code-timestamps](https://github.com/paragpandyareal/claude-code-timestamps) - Stempel waktu untuk Claude Code: waktu pada setiap pesan, balasan, dan…
- [paragpandyareal/claude-code-track-changes](https://github.com/paragpandyareal/claude-code-track-changes) - Lacak perubahan untuk Claude Code: lihat persis apa yang diubah Claude pada…
- [paweechinagarn/claude-code-mods](https://github.com/paweechinagarn/claude-code-mods) - Mod untuk Claude Code: plugin function hook yang bekerja di repositori apa pun.
- [pkkid/claude-mods](https://github.com/pkkid/claude-mods) - Berbagai mod dan skill untuk setup Claude Desktop saya.
- [poppydad/agent-efficiency](https://github.com/poppydad/agent-efficiency) - Mod Claude Code: melacak model, token, alat, dan waktu setiap subagen, menandai…
- [poppydad/agent-squad](https://github.com/poppydad/agent-squad) - Mod Claude Code: setiap subagen tampil sebagai figur tongkat kecil di panel…
- [pradyb/claude-mods](https://github.com/pradyb/claude-mods) - Mod untuk Code Claude: safety-guard memblokir perintah destruktif dan akses…
- [pvjbuilds/crab-buddy](https://github.com/pvjbuilds/crab-buddy) - Kepiting pixel-art Claude animasi untuk Claude Code: memeragakan apa yang…
- [qazwsx1121/Claude-Code-mods](https://github.com/qazwsx1121/Claude-Code-mods)
- [ramtinJ95/claude-mods](https://github.com/ramtinJ95/claude-mods) - Mod Claude Code, diterbitkan sebagai satu marketplace plugin.
- [ReDev1L/leanctx-colored](https://github.com/ReDev1L/leanctx-colored) - Claude Code mod: colored lean-ctx output.
- [Risdon8/push-ups](https://github.com/Risdon8/push-ups) - Mod Code Claude: push-up yang harus dilakukan saat Claude bekerja. Tanpa token.
- [robinade/claude-mods-ko](https://github.com/robinade/claude-mods-ko) - 6 mod Claude Code dalam bahasa Korea: catatan asumsi, bahasa sederhana, rak…
- [robinmarin/claude-mods](https://github.com/robinmarin/claude-mods) - hanya daftar mod yang saya gunakan.
- [rogod4rk/claude-code-mods](https://github.com/rogod4rk/claude-code-mods) - Tiga mod bebas dependensi untuk Claude Code: statusline responsif, path-guard…
- [Ron-Nefyodov/security-poc-mod](https://github.com/Ron-Nefyodov/security-poc-mod) - Mod Claude Code khusus POC untuk demonstrasi keamanan lokal yang eksplisit dan…
- [Ross-cripto/modshelf](https://github.com/Ross-cripto/modshelf) - An open-source marketplace for Claude Code mods, with repository skills for…
- [RuahTechSolutions/code-buddy](https://github.com/RuahTechSolutions/code-buddy) - Mod Claude Code: pengaman staging, radius dampak, pemutaran ulang edit, dan…
- [russellpope/claude-mods](https://github.com/russellpope/claude-mods) - Mod saya untuk Claude Code.
- [saadk408/stepline](https://github.com/saadk408/stepline) - Mod Claude Code: mengubah rencana yang Anda setujui dalam mode plan menjadi…
- [saksham10arora-dotcom/awesome-claude-mods](https://github.com/saksham10arora-dotcom/awesome-claude-mods) - Daftar pilihan mod Claude Code. Setiap entri dikloning dan diperiksa dengan…
- [saksham10arora-dotcom/claude-frugal](https://github.com/saksham10arora-dotcom/claude-frugal) - Mode tanpa biaya: agen pembantu berjalan di Haiku, dan file serta log besar…
- [saksham10arora-dotcom/claude-lofi](https://github.com/saksham10arora-dotcom/claude-lofi) - Soundtrack lofi yang mengikuti sesi: tenang, fokus, mengalir, plus isyarat…
- [saksham10arora-dotcom/claude-teach-me](https://github.com/saksham10arora-dotcom/claude-teach-me) - Belajar sambil Claude melakukan coding: setelah giliran yang mengubah kode…
- [saksham10arora-dotcom/claude-vhs](https://github.com/saksham10arora-dotcom/claude-vhs) - Rekaman setiap edit yang dibuat Claude: putar ulang setiap perubahan saat…
- [santosli/claude-mods](https://github.com/santosli/claude-mods) - Mod Claude Code: token-bar, jendela konteks dan batas penggunaan Anda di atas…
- [SeitaHigashi/claude-terminal-image](https://github.com/SeitaHigashi/claude-terminal-image) - Claude Code mod: show an image (PNG, JPEG, GIF, WebP, BMP) in the conversation…
- [Shashwat-19/Claude-cockpit](https://github.com/Shashwat-19/Claude-cockpit) - Pusat kendali untuk Claude Code: armada subagen langsung, penggunaan…
- [Showrin/claude-mods](https://github.com/Showrin/claude-mods) - Mod Claude Code milik Showrin untuk aktivitas harian yang lebih produktif.
- [sidhantunnithan/jindan-cc-marketplace](https://github.com/sidhantunnithan/jindan-cc-marketplace) - Mod Code Claude pribadi.
- [StanislavKozachenko/claude-mods](https://github.com/StanislavKozachenko/claude-mods) - A collection of Claude Code mods: TypeScript function hooks, shipped as a…
- [steven-ngle/blade-of-commits](https://github.com/steven-ngle/blade-of-commits) - Pesan commit sekali klik untuk Claude Code dengan Malenia pixel-art yang menari.
- [Subeen2/claude-mods](https://github.com/Subeen2/claude-mods) - Kumpulan mod Claude Code yang dibuat sendiri (marketplace plugin).
- [sunwu51/english-assistant](https://github.com/sunwu51/english-assistant) - Plugin Claude Code Mods untuk terjemahan bahasa Mandarin-Inggris yang…
- [takiguchi-yu/claude-mods](https://github.com/takiguchi-yu/claude-mods) - Tempat mod Claude Code untuk digunakan secara lokal.
- [talbarina/claude-editor-context](https://github.com/talbarina/claude-editor-context) - Mod Claude Code: lihat file dan pilihan Cursor / VS Code Anda di atas prompt…
- [Tanish-Dev/claude-usage-band](https://github.com/Tanish-Dev/claude-usage-band) - Clawd Meter — mod kode Claude yang menampilkan penggunaan paket Claude Anda…
- [TheBabaYaga/claude-session-flow](https://github.com/TheBabaYaga/claude-session-flow) - Mod Claude Code yang menampilkan sesi saat ini dalam sebuah panel: setiap…
- [theishandubey/claude-mods](https://github.com/theishandubey/claude-mods) - Marketplace plugin Claude Code untuk mod: plugin function-hooks yang menggambar…
- [Toptaab/token-garden](https://github.com/Toptaab/token-garden) - Mod Claude Code oleh Toptaab.
- [UsamaSadiq/claude-mods](https://github.com/UsamaSadiq/claude-mods) - Mod kecil, menyenangkan, dan berguna untuk Claude Code.
- [VAlux/claude-session-progress](https://github.com/VAlux/claude-session-progress) - Mod Claude Code: pita kemajuan animasi dan ringkasan penyelesaian untuk tugas…
- [Vansitha/clawd-watch](https://github.com/Vansitha/clawd-watch) - Tiga mod Claude Code kecil: lihat kapan subagen Anda selesai, antrekan pesan…
- [varunmoka7/layman](https://github.com/varunmoka7/layman) - Katakan &quot;Saya tersesat&quot; dan Claude akan menjelaskan kembali balasan terakhirnya…
- [varunmoka7/side-chat](https://github.com/varunmoka7/side-chat) - Ajukan pertanyaan sampingan kepada Claude di panel di sebelah pekerjaan Anda.
- [vmurin/cache-weather](https://github.com/vmurin/cache-weather) - Claude Code plugin: prompt-cache countdown, cache hit rate, context weather and…
- [wablevaibhav/claude-mods](https://github.com/wablevaibhav/claude-mods)
- [WeaponizedLego/claude-code-mods](https://github.com/WeaponizedLego/claude-code-mods) - Mod Claude Code saya.
- [wellavelino/mystique](https://github.com/wellavelino/mystique) - Mod Claude Code: pena penyorot untuk balasan, panel samping untuk hasil kueri…
- [wipeer/claude-mods](https://github.com/wipeer/claude-mods) - Small quality-of-life mods for Claude Code.
- [wirawansanusi/claude-mods-usage-meter](https://github.com/wirawansanusi/claude-mods-usage-meter) - Mod Claude Code ini menampilkan kartu di atas prompt.
- [wisbech/molt](https://github.com/wisbech/molt) - molt — when context outgrows its shell, shed it into the folder and keep going.
- [Wowbagger1994/claude-mods](https://github.com/Wowbagger1994/claude-mods) - Mod untuk Claude Code: secret yang disamarkan, daftar tugas, pemeriksaan dan…
- [wukonigcom/quanta-costa](https://github.com/wukonigcom/quanta-costa) - 🧾 Plugin Code Claude: batas penggunaan Claude Pro/Max Anda dengan perkiraan…
- [xinhuagu/oh-my-claude-mods](https://github.com/xinhuagu/oh-my-claude-mods) - Mod untuk Claude Code. agent-crew: lihat subagen Anda bekerja sebagai kru…
- [YeomYuJun/claude-mods](https://github.com/YeomYuJun/claude-mods) - Mod panel samping terminal untuk Claude Code — pelacakan agen, Tetris bertenaga…
- [YohanGarcia/agent-taskboard](https://github.com/YohanGarcia/agent-taskboard) - Papan tugas live untuk Claude Code: rencanakan sebelum membangun, ikuti setiap…
- [yuu1111/claude-agents-skills](https://github.com/yuu1111/claude-agents-skills) - Claude Code mod that loads Agent Skills from the shared .agents/skills…
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - Kumpulan pilihan sumber daya terbaik untuk agen-agen paling hebat, Claude Code…
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) - Plugin Claude Code yang menampilkan apa yang sedang terjadi — penggunaan…
- [sirmalloc/ccstatusline](https://github.com/sirmalloc/ccstatusline) - 🚀 Statusline yang indah dan sangat dapat disesuaikan untuk Claude Code CLI…
- [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) - Semua bagian system prompt Claude Code, 27 deskripsi alat bawaan, prompt…
- [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) - 45+ kiat untuk memaksimalkan Claude Code, dari dasar hingga tingkat lanjut…
- [op7418/guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill) - 🪧 Claude Code / Codex skill — buat carousel Xiaohongshu &amp; pasangan sampul…
- [persiyanov/herdr-reviewr](https://github.com/persiyanov/herdr-reviewr) - Tinjau diff agen pengodean Anda di panel terminal dan kirim komentar baris…
- [uppinote20/claude-dashboard](https://github.com/uppinote20/claude-dashboard) - Plugin baris status komprehensif untuk Claude Code dengan penggunaan konteks…
- [starbaser/ccproxy](https://github.com/starbaser/ccproxy) - Buat mod untuk Claude Code: kaitkan permintaan apa pun, ubah respons apa pun…
- [NYCU-Chung/cc-statusline](https://github.com/NYCU-Chung/cc-statusline) - Dasbor status komprehensif untuk Claude Code — info sesi, bilah kuota, pelacak…
- [gwittebolle/claude-carbon](https://github.com/gwittebolle/claude-carbon) - claude-carbon: lacak jejak karbon sesi Claude Code Anda.
- [AwesomeZun/CC-statusline](https://github.com/AwesomeZun/CC-statusline) - Statusline estetis untuk Claude Code oleh awesomejun.
- [JohnnyVizz/claude-kit](https://github.com/JohnnyVizz/claude-kit) - Skill dan mod Claude Code publik.
- [escapeboy/claude-code-kit](https://github.com/escapeboy/claude-code-kit) - Skills, mod, subagent, hook, perintah slash, dan panduan untuk Claude Code…
- [mvalentsev/awesome-free-ai-coding](https://github.com/mvalentsev/awesome-free-ai-coding) - 📡 LLM APIs legal gratis &amp; agen pengodean — diperbarui sendiri, diverifikasi…
- [backstabslash/goccc](https://github.com/backstabslash/goccc) - Kalkulator biaya cepat tanpa dependensi dan statusline yang dapat disesuaikan…
- [arturogarrido/claudinho](https://github.com/arturogarrido/claudinho) - ⚽ Skor langsung football(soccer), jadwal pertandingan, dan klasemen untuk…
- [johncattrall/keymap-ai](https://github.com/johncattrall/keymap-ai) - Agent Skill yang mengubah agen pengodean Anda menjadi ahli firmware keyboard.
- [Tripstack-Corp/spyc](https://github.com/Tripstack-Corp/spyc) - A Rust TUI file commander where the AI agent in the side pane can query the…
- [ashafizullah/claude-code-muslim-mods](https://github.com/ashafizullah/claude-code-muslim-mods) - Waktu salat, tanggal Hijriah, adhkar, ayat harian, puasa sunnah, Ramadan…
- [philoserf/claude-code-config](https://github.com/philoserf/claude-code-config) - Konfigurasi Claude Code pribadi yang diberi versi di dalam ~/.claude — agent…
- [benz-ai-x/dsh-research-graph](https://github.com/benz-ai-x/dsh-research-graph) - DSH Research Graph · Peta Riset — plugin DeepSeek Harness untuk topik riset…
- [chrisnguyen1211/pillrdotlol](https://github.com/chrisnguyen1211/pillrdotlol) - Every coding agent and every API key, in one pill at the edge of your Mac.
- [hoobnn/hoobnn-agent-mods](https://github.com/hoobnn/hoobnn-agent-mods) - Kumpulan plugin untuk Claude Code, pi, dan DeepSeek Harness: HUD bilah status…
- [luucas42/agent-flow](https://github.com/luucas42/agent-flow) - A live workflow panel for Claude Code: the main model, the advisor and every…
- [TurboKach/claude-code-statusline](https://github.com/TurboKach/claude-code-statusline) - Status line Claude Code yang ringan — satu skrip Bash sekitar 170 baris, tanpa…
- [mutlumehmet/claude-plugins](https://github.com/mutlumehmet/claude-plugins) - Plugin Claude Code yang saya gunakan setiap hari: skills dan mod, dirapikan…
- [cc-friend/ccost](https://github.com/cc-friend/ccost) - Analyze Claude Code token usage and costs from local conversation logs and…
- [manson341349-beep/claude-desktop-mods](https://github.com/manson341349-beep/claude-desktop-mods) - Mod tidak resmi untuk tab Code di Claude Desktop — usage-pet: pita penggunaan…
- [cmfok/dsh-feishucard](https://github.com/cmfok/dsh-feishucard) - Jembatan DSH &lt;-&gt; Feishu (Lark), dikembangkan sendiri (bukan fork): kartu…
- [darthmolen/hytale-claude-code-marketplace](https://github.com/darthmolen/hytale-claude-code-marketplace) - Marketplace untuk Plugin dan Skill Claude Code guna memfasilitasi mod game…
- [frsorrentino/fable-director](https://github.com/frsorrentino/fable-director) - Tata kelola token untuk Claude Code: model teratas mengarahkan, eksekusi…
- [hopp1395/cc-outline](https://github.com/hopp1395/cc-outline) - Penampil panel terpisah untuk Claude Code di Windows Terminal dan tmux: sesi…
- [romnycristopher/claude-am-mods](https://github.com/romnycristopher/claude-am-mods) - Repositori untuk mod Awesome Media Claude Code.
- [rootstudioyaml/sprag](https://github.com/rootstudioyaml/sprag) - Kurangi pengeluaran Claude Code &amp; Codex token: arahkan pencarian dan pengujian…
- [fbincon/claude-code-statusline](https://github.com/fbincon/claude-code-statusline) - Status line Claude Code yang dapat dikonfigurasi untuk Linux, WSL, Windows, dan…
- [crosscountryridinggirlwonder916/claude-statusline](https://github.com/crosscountryridinggirlwonder916/claude-statusline) - Menampilkan statusline Claude Code dengan batas laju, direktori saat ini, dan…
- [jv-k/claude-gauge](https://github.com/jv-k/claude-gauge) - Baris status dan baris token untuk Claude Code: konteks, penggunaan 5 jam dan…
- [Ma1achy/claude-statusline](https://github.com/Ma1achy/claude-statusline) - baris status Claude Code yang ramah dan bisa diutak-atik — bilah truecolor, ~80…
- [tc3oliver/claude-team-kit](https://github.com/tc3oliver/claude-team-kit) - Tim agen native. Di bawah kendali. Batas pekerja yang ketat, visibilitas tim…
- [yedidya-buildfy/claude-addons](https://github.com/yedidya-buildfy/claude-addons) - Add-on Claude Code: pemantau titik berwarna status tab + statusline GSD bawaan.
- [zach-source/claude-factory](https://github.com/zach-source/claude-factory) - Pabrik perangkat lunak yang dapat didefinisikan untuk Claude Code di herdr…
- [0xSerachu/claude-shortcuts](https://github.com/0xSerachu/claude-shortcuts) - Explore and quiz yourself on all Claude Code shortcuts with categorized…
- [akhilnalliboina/claude-usage-statusline](https://github.com/akhilnalliboina/claude-usage-statusline) - Baris status penggunaan Code Claude untuk macOS dan Linux, dikemas sebagai…
- [Alpinoo/claude-code-usage-statusline](https://github.com/Alpinoo/claude-code-usage-statusline) - Windows PowerShell status line for Claude Code: 5-hour and weekly limits with…
- [crafts69guy/claude-statusline.nvim](https://github.com/crafts69guy/claude-statusline.nvim) - Baris status Code Claude di Lua, dengan playground Neovim langsung.
- [ctfbio/claude-code-statusline](https://github.com/ctfbio/claude-code-statusline) - Statusline Claude Code tingkat profesional: durasi sesi, biaya multi-mata uang…
- [cvrt-gmbh/claude-statusline](https://github.com/cvrt-gmbh/claude-statusline) - Baris status yang memperhatikan langganan untuk Claude Code.
- [emmanuelbarturen/claude-code-statusline](https://github.com/emmanuelbarturen/claude-code-statusline) - Baris status untuk Claude Code dalam bahasa Spanyol: tugas, skill, konteks…
- [FukKwang/claude-statusline](https://github.com/FukKwang/claude-statusline) - Baris status Claude Code yang penuh warna: batas paket, konteks, biaya, dan…
- [Gabriel-Dalton/claude-statusline-tokens](https://github.com/Gabriel-Dalton/claude-statusline-tokens) - Baris status Claude Code untuk Windows: total token, biaya dengan tarif API…
- [gvart/claude-config](https://github.com/gvart/claude-config) - My Claude Code setup: agent-monitor mod, skills, agents and a one-command…
- [hanneshapke/claude-statusline](https://github.com/hanneshapke/claude-statusline) - Bilah status satu baris untuk Claude Code: model, git, konteks, token, biaya…
- [hieuvo/claude-imgview](https://github.com/hieuvo/claude-imgview) - Pratinjau gambar di dalam Code Claude: arahkan kursor ke chip di bawah balasan…
- [IdoSagiv/claude-config](https://github.com/IdoSagiv/claude-config) - Konfigurasi pribadi Claude Code: izin, statusline, server MCP.
- [ihororlovskyi/claude-statusline](https://github.com/ihororlovskyi/claude-statusline) - Baris status Claude Code dengan baris panel agen.
- [izahamyatim/claude-plugin-fizzy](https://github.com/izahamyatim/claude-plugin-fizzy) - 🚀 Sinkronkan todo Claude ke Fizzy.do untuk visibilitas tim secara langsung…
- [kgdemir/claude-agentic-os](https://github.com/kgdemir/claude-agentic-os) - Claude Agentic OS: pengaturan Claude Code portabel — aturan global, kumpulan…
- [Kimmihappy793/claude-status-line](https://github.com/Kimmihappy793/claude-status-line) - Menampilkan bilah status mendetail berkode warna untuk Claude Code yang…
- [Leechlike-intangibleasset343/claude-code-statusline](https://github.com/Leechlike-intangibleasset343/claude-code-statusline) - Lacak status Claude Code dengan dasbor ringkas yang menampilkan konteks, biaya…
- [LounisBou/claude-statusbar](https://github.com/LounisBou/claude-statusbar) - Bilah status dua baris untuk agen coding terminal: direktori, git, PR, model…
- [lucasmm96/claude-statusline](https://github.com/lucasmm96/claude-statusline) - Hook baris status Claude Code — melacak penggunaan token dan konteks di seluruh…
- [mesix971/mods-claude](https://github.com/mesix971/mods-claude) - Clawd, teman pixel art Claude Code, dan atelier, pengaman dev Android.
- [MSFSupply/claude-marketplace](https://github.com/MSFSupply/claude-marketplace) - Marketplace Claude Code de MSF Supply : mods sélectionnés et figés par commit.
- [msinclair-sudo/claude-code-setup](https://github.com/msinclair-sudo/claude-code-setup) - Penginstal lingkungan Claude Code: skills, statusline, hooks, permissions, dan…
- [munkgorn/usage-statusline-claude](https://github.com/munkgorn/usage-statusline-claude) - Rich multi-line status line for Claude Code — live usage limits (5h + weekly)…
- [Nachofranco5/claude-harness](https://github.com/Nachofranco5/claude-harness) - Harness Claude Code milik Nacho (aturan, papan, mod).
- [naughty00shortie/claude-statusline](https://github.com/naughty00shortie/claude-statusline) - Statusline Claude Code multibaris: bilah konteks, cabang git, bilah kuota…
- [OrihuelaConde/claude-plugins](https://github.com/OrihuelaConde/claude-plugins) - Plugin dan mod OrihuelaConde untuk Claude Code.
- [parisgroup-ai/claude-statusline](https://github.com/parisgroup-ai/claude-statusline) - @parisgroup-ai/claude-statusline — baris status Code Claude untuk macOS +…
- [peaceinitiativemenhadenoil263/claude-status-bar](https://github.com/peaceinitiativemenhadenoil263/claude-status-bar) - Memantau status Claude Code dari bilah menu macOS Anda dengan indikator waktu…
- [primelogiclabio/claude-tools](https://github.com/primelogiclabio/claude-tools) - Skill dan mod untuk Claude Code dan Cowork — pelacak proyek, dokumen referensi…
- [rainyfei/claude-statusline-win](https://github.com/rainyfei/claude-statusline-win) - Baris status Claude Code untuk Windows (PowerShell): bilah penggunaan, hitung…
- [robinalexandre/claude-code-kit](https://github.com/robinalexandre/claude-code-kit) - Skill, mod, hook, dan baris status untuk Claude Code, plus mesin sinkronisasi…
- [rotemx-10x/claude-code-statusline](https://github.com/rotemx-10x/claude-code-statusline) - Baris status dua baris untuk Code Claude.
- [Rubio-Enterprises/claude-statusline](https://github.com/Rubio-Enterprises/claude-statusline) - Statusline Claude Code kustom (upstream: kamranahmedse/claude-statusline).
- [Screddyice/claude-code-harness](https://github.com/Screddyice/claude-code-harness) - Harness awal untuk Claude Code: hooks, statusline, model lokal, dispatch swarm…
- [Sofia-D4L/claude-conf](https://github.com/Sofia-D4L/claude-conf) - Konfigurasi portabel Claude Code (statusline + penginstal).
- [SohamShirsat/claude-cockpit](https://github.com/SohamShirsat/claude-cockpit) - Dasbor kecil untuk Claude Code: konteks %, hitung mundur cache, penggunaan 5…
- [speti4/claude-statusline](https://github.com/speti4/claude-statusline) - Bilah status terminal khusus untuk Claude Code: model, direktori, status git…
- [Undone-drawknife974/claude-code-statusline](https://github.com/Undone-drawknife974/claude-code-statusline) - Melacak penggunaan konteks Claude Code, biaya sesi, dan reset batas laju dengan…
- [UtakataKyosui/utakata-cc-mod](https://github.com/UtakataKyosui/utakata-cc-mod) - Kumpulan mod untuk Claude Code.
- [vibe-coding-labs/claude-code-status-skills](https://github.com/vibe-coding-labs/claude-code-status-skills) - Baris status Code Claude: ID model saat ini, nama host, tautan repositori git…
- [warodan/vscode-claude-code-patch](https://github.com/warodan/vscode-claude-code-patch) - Skill Claude Code (VS Code, Windows): pratinjau gambar dan tombol buka di bawah…
- [whr819987540/claude-sync-settings](https://github.com/whr819987540/claude-sync-settings) - Sinkronisasi lintas mesin konfigurasi tingkat pengguna Claude Code…
- [Winn-Gaoti-Studio/claude-code-statusline](https://github.com/Winn-Gaoti-Studio/claude-code-statusline) - Statusline Claude Code dengan bilah kemajuan gradien, upaya sesi bergradasi…
- [ymoud/claude-code-statusline](https://github.com/ymoud/claude-code-statusline) - Baris status Code Claude: folder, cabang git, model, penggunaan jendela…
- [YoniYon00/claude-feedback-rings](https://github.com/YoniYon00/claude-feedback-rings) - Context Rot Detector 2026 - Monitor Memori AI &amp; Batas Laju Proaktif untuk Agen…
- [zhuyansen/awesome-claude-code-hooks](https://github.com/zhuyansen/awesome-claude-code-hooks) - Hook, subagen, dan statusline Claude Code: koleksi dan alat sumber terbuka…
- [Magnus-Gille/tokenatlas](https://github.com/Magnus-Gille/tokenatlas) - Statusline Claude Code yang menampilkan penggunaan token waktu nyata dan…
- [previsioncystolith584/ai-video-downloader](https://github.com/previsioncystolith584/ai-video-downloader) - Download videos from major platforms and automatically add translated…
- [babarot/c-c-statusline](https://github.com/babarot/c-c-statusline) - Baris status bertenaga Deno untuk Claude Code CLI.
- [ishuagrawal/clawdhouse](https://github.com/ishuagrawal/clawdhouse) - Mod untuk Claude Code: panel, pita, dan pendamping yang dibuat berdasarkan…
- [timvdhoorn/cc-my-pi](https://github.com/timvdhoorn/cc-my-pi) - Paket UI bergaya Claude Code untuk agen coding Pi — rendering alat, spinner…
- [ashishsk93/baton-mods](https://github.com/ashishsk93/baton-mods) - Teruskan tugas antar-sesi Claude Code Anda.
- [lahoramaker/mods-mcp](https://github.com/lahoramaker/mods-mcp) - Ini adalah MCP server untuk mengontrol MODS, alat modular lintas platform untuk…
- [Rimcat-JA/translate-ck3-mods](https://github.com/Rimcat-JA/translate-ck3-mods) - Skill Codex dan Claude Code untuk menerjemahkan mod CK3 dengan LLM lokal.
- [sTomerG/agent-kit](https://github.com/sTomerG/agent-kit) - Mod sumber terbuka dan ekstensi lainnya untuk Claude Code.
- [alan-oliv/team8](https://github.com/alan-oliv/team8) - A live browser console for Claude Code agent teams — every teammate.
- [Apparux/cc-fusion](https://github.com/Apparux/cc-fusion) - Statusline Claude Code: keindahan CCometixLine + fungsionalitas HUD Claude.
- [charlie947/mod-maker](https://github.com/charlie947/mod-maker) - Mod Maker: temukan hal yang berulang kali Anda minta kepada Claude Code, lalu…

</details>

<a id="dsh-cordis"></a>

## Ekosistem plugin DSH dan Cordis

DeepSeek Harness dan Cordis mencapai tempat yang sama dari arah yang berbeda: bagi keduanya, plugin adalah mekanisme mod, sehingga plugin di sana setara dengan mod di sini.

<details>
<summary>🧵 <b><a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b> · ⭐74398 · TypeScript · 👁️ observed · 0 天</summary>

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
| Bintang                  | **74398**  |
| Push terakhir            | 2026-10-12 |
| Pertama kali dicantumkan | 2026-10-04 |

🏷 `agentic-ai` · `agentic-framework` · `agentic-workflow` · `agents` · `ai-agents` · `ai-assistant` · `ai-skills` · `autonomous-agents`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/2ca82c9c9a7fca31.gif" width="100%" alt="ruvnet/ruflo animation"><br><sub>rekaman animasi</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/morluto/rea">morluto/rea</a></b> · ⭐134601 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Bintang                  | **134601** |
| Push terakhir            | 2026-10-12 |
| Pertama kali dicantumkan | 2026-10-05 |

🏷 `agent-skills` · `ai-agents` · `binary-analysis` · `claude-code` · `cli` · `codex` · `cordis` · `ctf`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--rea/f46ca8b1518ae39f.png" width="100%" alt="morluto/rea screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/nexu-io/open-design">nexu-io/open-design</a></b> · ⭐100691 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Bintang                  | **100691** |
| Push terakhir            | 2026-10-12 |
| Pertama kali dicantumkan | 2026-10-04 |

🏷 `agent-skills` · `ai-design` · `byok` · `claude-code-for-design` · `claude-design` · `codex-design` · `coding-agents` · `cursor-design`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nexu-io--open-design/a1049df34322d3ce.png" width="100%" alt="nexu-io/open-design screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/tt-a1i/archify">tt-a1i/archify</a></b> · ⭐82387 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Bintang                  | **82387**  |
| Push terakhir            | 2026-10-12 |
| Pertama kali dicantumkan | 2026-10-04 |

🏷 `agent-skills` · `ai-agents` · `architecture-diagram` · `claude-code` · `claude-skills` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tt-a1i--archify/71b7d4b2427db202.png" width="100%" alt="tt-a1i/archify screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/esengine/DeepSeek-Reasonix">esengine/DeepSeek-Reasonix</a></b> · ⭐35769 · Go · 🔎 inferred · 0 天</summary>

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
| Bintang                  | **35769**  |
| Push terakhir            | 2026-10-12 |
| Pertama kali dicantumkan | 2026-10-06 |

🏷 `agent` · `agent-framework` · `ai-agent` · `ai-coding` · `cli` · `coding-agent` · `deepseek` · `developer-tools`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/titanwings/distilly">titanwings/distilly</a></b> · ⭐25517 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

Distilly — Suling cara mereka berpikir menjadi Skills yang dapat digunakan kembali untuk Agent atau Bot apa pun. Sebelumnya Colleague Skill（原同事 Skill）.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | Python                                                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **25517**  |
| Push terakhir            | 2026-10-12 |
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `agent-skills` · `agentic-ai` · `ai-agent` · `ai-agents` · `ai-assistants` · `ai-persona` · `claude-code` · `claude-skills`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/titanwings--distilly/1e118bb52fdcbd1c.png" width="100%" alt="titanwings/distilly screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/zhu1090093659/dsh-web">zhu1090093659/dsh-web</a></b> · ⭐8659 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

Ekosistem Agregasi Plugin Web DeepSeek Harness (DSH) · Segala sesuatu adalah plugin, didistribusikan melalui Creative Workshop｜｜Ekosistem Agregasi Plugin Web DeepSeek Harness (DSH) · Segala sesuatu adalah plugin, didistribusikan melalui Creative Workshop

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | TypeScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **8659**   |
| Push terakhir            | 2026-10-12 |
| Pertama kali dicantumkan | 2026-10-12 |

🏷 `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-web` · `dsh-web-ui`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zhu1090093659--dsh-web/5153c3c61827ebb8.jpg" width="100%" alt="zhu1090093659/dsh-web screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ccch1mneyyy/dsh-TUI">ccch1mneyyy/dsh-TUI</a></b> · ⭐4385 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

Plugin TUI yang secara resmi paling direkomendasikan untuk DSH — performa tinggi, overhead rendah, paus piksel yang imut, interaksi mouse yang mulus. Instalasi satu perintah melalui npm. / Plugin TUI yang secara resmi paling direkomendasikan DSH, performa tinggi, penggunaan sumber daya rendah, paus piksel yang imut, interaksi mouse yang mulus, instalasi sekali klik melalui npm

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | TypeScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **4385**   |
| Push terakhir            | 2026-10-12 |
| Pertama kali dicantumkan | 2026-10-12 |

🏷 `claude-code` · `coding-agent` · `deepseek` · `deepseek-harness` · `dsh-plugin` · `ink` · `react` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ccch1mneyyy--dsh-tui/18fd45f8f1eaca04.png" width="100%" alt="ccch1mneyyy/dsh-TUI screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-tauri/deepseek-harness-desktop">dsh-tauri/deepseek-harness-desktop</a></b> · ⭐3060 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

DeepSeek Harness Edisi Desktop Tauri | Penginstal hanya 8 MB, tanpa penyiapan lingkungan, plugin prasetel, Windows / macOS / Linux.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | TypeScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **3060**   |
| Push terakhir            | 2026-10-12 |
| Pertama kali dicantumkan | 2026-10-12 |

🏷 `deepseek` · `deepseek-harness` · `desktop` · `dsh` · `dsh-desktop` · `dsh-plugin` · `tauri`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dsh-tauri--deepseek-harness-desktop/f281725e73da1059.png" width="100%" alt="dsh-tauri/deepseek-harness-desktop screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/kenryu42/cc-safety-net">kenryu42/cc-safety-net</a></b> · ⭐1601 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

Penjaga sebelum eksekusi untuk agen pengodean AI. Memblokir perintah Git dan sistem berkas yang merusak, serta upaya umum untuk mengakses berkas sensitif, sebelum pemanggilan alat dijalankan. Mendukung Amp Code, Antigravity CLI, Claude Code, Codex, Cursor, DeepSeek Harness, Devin CLI, GitHub Copilot CLI, Grok Build, Hermes Agent, Kimi Code, OpenClaw, OpenCode, dan Pi.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | TypeScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **1601**   |
| Push terakhir            | 2026-10-12 |
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `ai-agents` · `ai-safety` · `antigravity` · `claude` · `claude-code` · `claude-code-plugin` · `cli` · `codex`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/GanyuanRan/Aegis">GanyuanRan/Aegis</a></b> · ⭐1343 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

Make AI coding agents architecture-aware: baseline-first, evidence-verified, drift-checked, and safe across long tasks.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | Python                                                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **1343**   |
| Push terakhir            | 2026-10-12 |
| Pertama kali dicantumkan | 2026-10-12 |

🏷 `agent-skills` · `ai-agents` · `ai-coding` · `architecture-driven-development` · `awsome-coding-plugin` · `baseline-first` · `claude-code` · `codex`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ganyuanran--aegis/4581f8f71af5092d.png" width="100%" alt="GanyuanRan/Aegis screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/vshulcz/deja-vu">vshulcz/deja-vu</a></b> · ⭐1179 · Go · 🔎 inferred · 0 天</summary>

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
| Bintang                  | **1179**   |
| Push terakhir            | 2026-10-12 |
| Pertama kali dicantumkan | 2026-10-04 |

🏷 `agent-memory` · `ai-memory` · `claude-code` · `claude-code-hooks` · `claude-code-plugins` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/8033ba54a9424c88.png" width="100%" alt="vshulcz/deja-vu screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/5fb930f1983f270b.gif" width="100%" alt="vshulcz/deja-vu animation"><br><sub>rekaman animasi</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/omdsh-dev/dsh-genui">omdsh-dev/dsh-genui</a></b> · ⭐552 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

GenUI for DeepSeek Harness: interactive UI components rendered inline in assistant replies via the dsh-ui fence — layout, charts, plots, forms, quizzes, mermaid, 3D scenes, and an action event loop back to the model. Ships the fence-teaching host plugin, the browser renderer (client half), and the genui skill.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | TypeScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **552**    |
| Push terakhir            | 2026-10-12 |
| Pertama kali dicantumkan | 2026-10-12 |

🏷 `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/omdsh-dev--dsh-genui/cf8bd9040af17cab.png" width="100%" alt="omdsh-dev/dsh-genui screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/omdsh-dev--dsh-genui/1f990c9a328356e9.gif" width="100%" alt="omdsh-dev/dsh-genui animation"><br><sub>rekaman animasi · <a href="https://raw.githubusercontent.com/omdsh-dev/dsh-genui/main/assets/demo.mp4">Buka video</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/text2future/flowix">text2future/flowix</a></b> · ⭐459 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

Notes for you, Memory for your agents. / 内置 Deepseek harness Agent / 适用 办公 & 写作 & Coding

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | TypeScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **459**    |
| Push terakhir            | 2026-10-12 |
| Pertama kali dicantumkan | 2026-10-12 |

🏷 `agent-memory` · `claude-code` · `codex-cli` · `desktop` · `dsh` · `dsh-plugin` · `dsh-plugin-desktop` · `hermes-agent`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/text2future--flowix/9fc65a8848fe78ee.png" width="100%" alt="text2future/flowix screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/text2future--flowix/ea3f84c8693d4236.gif" width="100%" alt="text2future/flowix animation"><br><sub>rekaman animasi</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/DDDMUC/dsh-free-search">DDDMUC/dsh-free-search</a></b> · ⭐374 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

Penyedia pencarian web gratis untuk DeepSeek Harness - backend DuckDuckGo, tidak memerlukan kunci API

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | JavaScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **374**    |
| Push terakhir            | 2026-10-12 |
| Pertama kali dicantumkan | 2026-10-12 |

🏷 `bing` · `deepseek-harness` · `dsh` · `dsh-plugin` · `duckduckgo` · `web-search`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dddmuc--dsh-free-search/ec034e713544ead5.png" width="100%" alt="DDDMUC/dsh-free-search screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/tingly-dev/tingly-box">tingly-dev/tingly-box</a></b> · ⭐351 · Go · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

Your Intelligence, Orchestrated. Every builder. Every team. Every agent. For Everyone.

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
| Push terakhir            | 2026-10-12 |
| Pertama kali dicantumkan | 2026-10-12 |

🏷 `claude-code` · `dsh` · `dsh-plugin` · `gateway` · `golang` · `harness` · `llm` · `open-source`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tingly-dev--tingly-box/54666b3bdc5c6195.png" width="100%" alt="tingly-dev/tingly-box screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tingly-dev--tingly-box/0ef2aa2f5bc4239d.gif" width="100%" alt="tingly-dev/tingly-box animation"><br><sub>rekaman animasi</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/RevolutionLA/dsh-dream-skin">RevolutionLA/dsh-dream-skin</a></b> · ⭐230 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

Plugin ganti tampilan / wallpaper / paket tema DeepSeek Harness (dsh-plugin) — 8 tema Mirage, warna aksen per pengguna, Wallpaper 2.0, impor-ekspor paket tema / tautan berbagi, favorit dan acak, seluruhnya diimplementasikan dengan sistem token native.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | JavaScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **230**    |
| Push terakhir            | 2026-10-12 |
| Pertama kali dicantumkan | 2026-10-12 |

🏷 `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-plugin-theme` · `skin` · `theme` · `wallpaper`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/revolutionla--dsh-dream-skin/9ae1ef97a89d3ff0.png" width="100%" alt="RevolutionLA/dsh-dream-skin screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/luobosibing2/dsh-jev-plugin">luobosibing2/dsh-jev-plugin</a></b> · ⭐204 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Bintang                  | **204**    |
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
<summary>🧵 <b><a href="https://github.com/xiajiajun516/dsh-config-manager">xiajiajun516/dsh-config-manager</a></b> · ⭐181 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

Plugin pencadangan & pemulihan DeepSeek Harness (DSH) — ekspor, impor, migrasikan, dan sinkronkan konfigurasi DSH lengkap, plugin, server MCP, keahlian, dan ruang kerja Anda. Migrasi sekali klik ke mesin lain.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | TypeScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **181**    |
| Push terakhir            | 2026-10-11 |
| Pertama kali dicantumkan | 2026-10-12 |

🏷 `backup` · `cli` · `config-manager` · `configuration` · `cordis` · `deepseek` · `deepseek-harness` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xiajiajun516--dsh-config-manager/52a2f3587f8e40b4.png" width="100%" alt="xiajiajun516/dsh-config-manager screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/morluto/flameox">morluto/flameox</a></b> · ⭐180 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

Bukti runtime yang membantu agen melacak, membuat profil, dan mengatasi hotspot dalam kode aplikasi dan native, kernel GPU, serta tumpukan inferensi.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | Python                                                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **180**    |
| Push terakhir            | 2026-10-12 |
| Pertama kali dicantumkan | 2026-10-12 |

🏷 `benchmarking` · `coding-agents` · `cordis` · `debugging` · `developer-tools` · `dsh` · `dsh-plugin` · `gpu-profiling`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--flameox/2914b7977590380e.png" width="100%" alt="morluto/flameox screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Totoro-qaq/dsh-plugin-bridge">Totoro-qaq/dsh-plugin-bridge</a></b> · ⭐165 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

Plugin DeepSeek Harness untuk migrasi sesi lintas preset yang dapat dipratinjau. Serah-terima dengan skema tetap mempertahankan status, maksud model sumber, dan gambar yang belum terselesaikan; sesi asli tetap tidak tersentuh.

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
| Push terakhir            | 2026-10-12 |
| Pertama kali dicantumkan | 2026-10-12 |

🏷 `context-migration` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `preset-migration` · `session-migration`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/totoro-qaq--dsh-plugin-bridge/568de849cd2e9608.png" width="100%" alt="Totoro-qaq/dsh-plugin-bridge screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/totoro-qaq--dsh-plugin-bridge/b4a12cab0ba15f06.gif" width="100%" alt="Totoro-qaq/dsh-plugin-bridge animation"><br><sub>rekaman animasi</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Nwflower/dsh-claude-style">Nwflower/dsh-claude-style</a></b> · ⭐142 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

Claude Code Desktop theme for DeepSeek Harness｜ 为 DeepSeek Harness 网页 GUI 打造的 Claude Code 桌面主题

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | TypeScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **142**    |
| Push terakhir            | 2026-10-12 |
| Pertama kali dicantumkan | 2026-10-12 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-desktop` · `cordis` · `dark-mode` · `deepseek-harness` · `desktop-theme`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Nwflower/dsh-claude-style/master/docs/screenshots/claude-home-dark.png" width="100%" alt="Nwflower/dsh-claude-style screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Nwflower/dsh-claude-style/master/docs/gifs/idle.gif" width="100%" alt="Nwflower/dsh-claude-style animation"><br><sub>rekaman animasi</sub></td>
</tr></table>

<sub>Aset ditautkan langsung dari repositori upstream karena tidak ada lisensi yang mengizinkan redistribusi yang dinyatakan.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/FeatherHunter/dsh-mattpocock-skills-deck">FeatherHunter/dsh-mattpocock-skills-deck</a></b> · ⭐137 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

Dilengkapi 27 keahlian rekayasa dan produktivitas mattpocock/skills v1.3.1 sejak instalasi, tanpa perlu memasang keahlian secara manual. Dibangun dengan 40 miliar token, plugin ini memberikan efisiensi pengembangan 10 kali lipat di atas keahlian asli, serta membantu pemula memulai dengan paket keahlian ini lebih cepat. Dukungan penuh untuk issue GitHub; Markdown masih dalam versi pratinjau; GitLab belum didukung. Terima kasih atas penggunaan dan dukungan Anda 💗

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | JavaScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **137**    |
| Push terakhir            | 2026-10-12 |
| Pertama kali dicantumkan | 2026-10-12 |

🏷 `agent` · `ai` · `claude` · `deepseek-harness` · `dsh` · `dsh-better-sidebar` · `dsh-plugin` · `github-issues`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/featherhunter--dsh-mattpocock-skills-deck/c4bd78003446c161.png" width="100%" alt="FeatherHunter/dsh-mattpocock-skills-deck screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Sutera-Diffusus/dsh-whale-musume">Sutera-Diffusus/dsh-whale-musume</a></b> · ⭐121 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

Plugin hewan peliharaan desktop DeepSeek Harness: paus betina yang penuh energi menemani Anda menulis kode 🐋 Mendukung DSH desktop 0.2.0-rc.2 dan Web versi lama (hewan peliharaan desktop / maskot, local-first)

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | JavaScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **121**    |
| Push terakhir            | 2026-10-12 |
| Pertama kali dicantumkan | 2026-10-12 |

🏷 `ai-assistant` · `ai-companion` · `cordis` · `cute` · `deepseek` · `deepseek-harness` · `desktop-app` · `desktop-mascot`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/sutera-diffusus--dsh-whale-musume/cb85aa05cce65f77.png" width="100%" alt="Sutera-Diffusus/dsh-whale-musume screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Aik358/dsh-auto-memory">Aik358/dsh-auto-memory</a></b> · ⭐111 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

Proactive associative memory for DSH: system-prompt recall before the model speaks, three-layer auto-consolidation, skill crystallization, and Astra-style context management - handoff ledgers, PLAN whiteboard, water-level sensing. Local-first, model-agnostic, zero deps. 主动联想记忆+Astra 式上下文管理：自动唤回/自动沉淀/技能固化/交接账本与白板跨窗口续命/水位感知。

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | JavaScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **111**    |
| Push terakhir            | 2026-10-12 |
| Pertama kali dicantumkan | 2026-10-12 |

🏷 `context` · `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-plugins` · `memory` · `npm` · `plugin`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aik358--dsh-auto-memory/ba11cddac1ec16d1.png" width="100%" alt="Aik358/dsh-auto-memory screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aik358--dsh-auto-memory/a44325f737275ef4.gif" width="100%" alt="Aik358/dsh-auto-memory animation"><br><sub>rekaman animasi</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/kukucaiCndy/Corum-Harness">kukucaiCndy/Corum-Harness</a></b> · ⭐69 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Bintang                  | **69**     |
| Push terakhir            | 2026-10-12 |
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `agent` · `agent-os` · `ai-agent` · `cordis` · `desktop-app` · `dsh` · `electron` · `harness`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/kukucaicndy--corum-harness/b8971b2831acec9e.png" width="100%" alt="kukucaiCndy/Corum-Harness screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/morluto/leantoken">morluto/leantoken</a></b> · ⭐64 · Rust · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

Code intelligence for agents: find the code that matters and keep your context window and tokens lean.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | Rust                                                                                          |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **64**     |
| Push terakhir            | 2026-10-12 |
| Pertama kali dicantumkan | 2026-10-12 |

🏷 `ai-coding` · `code-intelligence` · `code-navigation` · `code-retrieval` · `code-search` · `codebase-indexing` · `coding-agents` · `context-engineering`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--leantoken/38b3e8f4a7b20aea.jpg" width="100%" alt="morluto/leantoken screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/cloader/dsh-taskboard">cloader/dsh-taskboard</a></b> · ⭐59 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

deepseekharness 任务看板插件

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | TypeScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **59**     |
| Push terakhir            | 2026-10-12 |
| Pertama kali dicantumkan | 2026-10-12 |

🏷 `agent` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `kanban` · `task-board`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/cloader--dsh-taskboard/cfd9efd4514a0b8f.png" width="100%" alt="cloader/dsh-taskboard screenshot"></td>
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
| Push terakhir            | 2026-10-12 |
| Pertama kali dicantumkan | 2026-10-06 |

🏷 `agent-framework` · `awesome-list` · `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/whyihaveyou--dsh-suite/e9daf3bb6313ff1b.png" width="100%" alt="whyihaveyou/dsh-suite screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/PolinniZhong/dsh-knit">PolinniZhong/dsh-knit</a></b> · ⭐54 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

Pengambilan konteks ruang kerja yang sadar tugas dan pelacakan siklus hidup untuk AI coding agent: menemukan, mengatur, dan terus melacak dokumen, kode, serta media yang paling relevan dengan tugas saat ini. Sepenuhnya lokal, tanpa pemanggilan model, tanpa jaringan. Pengambilan konteks ruang kerja yang sadar tugas dan pelacakan siklus hidup untuk AI coding agent. Temukan, atur, dan lacak konteks ruang kerja yang paling relevan dengan tugas yang sedang dikerjakan — secara lokal, deterministik, tanpa pemanggilan model, tanpa jaringan.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | JavaScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **54**     |
| Push terakhir            | 2026-10-12 |
| Pertama kali dicantumkan | 2026-10-12 |

🏷 `agent-tools` · `ai-agent` · `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-better-sidebar`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/polinnizhong--dsh-knit/e98f690af54d1e8d.png" width="100%" alt="PolinniZhong/dsh-knit screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/polinnizhong--dsh-knit/338cb6ef3e90368c.gif" width="100%" alt="PolinniZhong/dsh-knit animation"><br><sub>rekaman animasi</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/NekroAI/nekro-nxt">NekroAI/nekro-nxt</a></b> · ⭐35 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

NekroNXT: sistem agen obrolan grup multi-platform berbasis DeepSeek Harness (DSH)｜Sistem agen obrolan grup multi-platform yang didukung DSH

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | TypeScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **35**     |
| Push terakhir            | 2026-10-12 |
| Pertama kali dicantumkan | 2026-10-10 |

🏷 `ai-agents` · `cordis` · `deepseek-harness` · `desktop-app` · `docker` · `dsh` · `dsh-plugin` · `electron`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nekroai--nekro-nxt/7c9f9f2e5bc195f1.png" width="100%" alt="NekroAI/nekro-nxt screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/HOWILLMAKEIT/dsh-model-context-catalog">HOWILLMAKEIT/dsh-model-context-catalog</a></b> · ⭐34 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

Plugin DeepSeek Harness: mencocokkan jendela konteks model dengan sekali klik, menampilkan sumber kapasitas, mendukung konfigurasi batch melalui pilihan, pengelolaan jendela yang sudah ada, dan pengeditan manual.

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
| Push terakhir            | 2026-10-12 |
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `context-window` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `javascript` · `llm` · `model-metadata`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/howillmakeit--dsh-model-context-catalog/3b6ba492f13cdcbf.png" width="100%" alt="HOWILLMAKEIT/dsh-model-context-catalog screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/gjj-star/dsh-conversation-navigator">gjj-star/dsh-conversation-navigator</a></b> · ⭐23 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

Navigasi sesi DSH

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | JavaScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **23**     |
| Push terakhir            | 2026-10-12 |
| Pertama kali dicantumkan | 2026-10-12 |

🏷 `cordis` · `dsh` · `dsh-plugin` · `dsh-plugins` · `ui`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/gjj-star--dsh-conversation-navigator/4aef8cb83b546a1c.png" width="100%" alt="gjj-star/dsh-conversation-navigator screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Imzl-zl/dsh-toolbox-ui">Imzl-zl/dsh-toolbox-ui</a></b> · ⭐20 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

Panel Toolbox untuk DeepSeek Harness Web: pengelola MCP (alat & JSON Schema, market, impor, penyalinan ruang kerja) dan pengelola skills (cakupan & shadowing, aktifkan/nonaktifkan, pemanggilan otomatis model, market skillhub.cn).

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | JavaScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **20**     |
| Push terakhir            | 2026-10-12 |
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `agent-skills` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `mcp` · `skill-manager` · `skills`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/imzl-zl--dsh-toolbox-ui/bab6fdf6979d2501.png" width="100%" alt="Imzl-zl/dsh-toolbox-ui screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary><b>Lainnya dalam kategori ini</b> <sub>· 52</sub></summary>

- [hashgraph-online/awesome-ai-plugins](https://github.com/hashgraph-online/awesome-ai-plugins) - Daftar pilihan plugin AI terbaik yang luar biasa untuk asisten AI termasuk…
- [imsai-sh/awesome-deepseek-harness-plugins](https://github.com/imsai-sh/awesome-deepseek-harness-plugins) - DeepSeek Harness plugin store, marketplace and hub — 11,000+ dsh plugins with…
- [FishBottle7/opencode2dsh](https://github.com/FishBottle7/opencode2dsh) - Plugin DSH — model OpenCode Zen gratis untuk DeepSeek Harness (DSH).
- [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) - Pasar plugin DSH / DSH Plugin Marketplace: jelajahi, instal, dan perbarui semua…
- [arcships/rutis](https://github.com/arcships/rutis) - Runtime plugin untuk perangkat lunak yang melakukan iterasi sendiri — lapisan…
- [hanelalo/browser-bridge](https://github.com/hanelalo/browser-bridge) - 让你的agent真的像你一样操控你的浏览器窗口.
- [kejixiaoliang/awesome-dsh-plugins](https://github.com/kejixiaoliang/awesome-dsh-plugins) - Direktori pilihan plugin DeepSeek Harness (DSH) — lebih dari 280 plugin…
- [KannaKuron/dsh-gitbash-shell](https://github.com/KannaKuron/dsh-gitbash-shell) - Plugin DSH: shell Git Bash untuk semua mode agen di Windows.
- [wingsky-1/dsh-plugin-hub](https://github.com/wingsky-1/dsh-plugin-hub) - Kumpulan plugin GUI web DSH (DeepSeek Harness) — notifikasi tugas, penggunaan…
- [awesome-deepseekharness/awesome-deepseek-harness](https://github.com/awesome-deepseekharness/awesome-deepseek-harness) - Plugin, alat, skill, dan sumber belajar DeepSeek Harness (dsh) pilihan…
- [Airmetro/dsh-update-checker](https://github.com/Airmetro/dsh-update-checker) - Pengelolaan pembaruan program utama dan plugin DeepSeek Harness: perbandingan…
- [liustack/pptwise](https://github.com/liustack/pptwise) - PowerPoint sungguhan, bukan HTML. Beri tahu AI Anda apa yang harus dibahas dan…
- [Roarpeng/GraphFlow](https://github.com/Roarpeng/GraphFlow) - Graf pengetahuan kode dan harness konteks yang mengutamakan lokal untuk agen…
- [Ianzhyh/workbuddy-to-dsh](https://github.com/Ianzhyh/workbuddy-to-dsh) - Ubah model yang telah login di aplikasi desktop WorkBuddy lokal.
- [ouli-1242/dsh-plugin-tool-management](https://github.com/ouli-1242/dsh-plugin-tool-management) - DSH 插件：一个设置面板，统一管理 MCP 服务器、技能、场景、记忆、子智能体人格、AGENTS.md…
- [dsh-plugin-lab/dsh-zhihu-search](https://github.com/dsh-plugin-lab/dsh-zhihu-search) - Plugin DSH: tiga alat berupa pencarian internal, pencarian indeks seluruh web…
- [MichaelShii/dsh-plugin-teamflow](https://github.com/MichaelShii/dsh-plugin-teamflow) - plugin dsh teamflow.
- [MicroMilo/upstream-radar](https://github.com/MicroMilo/upstream-radar) - Pengujian kompatibilitas yang selalu aktif untuk plugin DeepSeek Harness: rilis…
- [chipweaver/veripower](https://github.com/chipweaver/veripower) - An open-source agent flow from natural language spec through Verilog RTL and…
- [bonerush/dsh-obsidian-mem](https://github.com/bonerush/dsh-obsidian-mem) - Plugin host DeepSeek Harness yang menyimpan dokumen proyek dan memori jangka…
- [PianoPrince/dsh-workspace-mover](https://github.com/PianoPrince/dsh-workspace-mover) - 拖拽真迁移 DSH 会话跨工作区：批量移动、分组合并、挂错归位、回收站、备份恢复 + 对话内 agent 工具；步步备份可回滚，零 token / True…
- [unStone/dsh-xray](https://github.com/unStone/dsh-xray) - X-ray untuk plugin DeepSeek Harness: kapabilitas yang dideklarasikan…
- [cherrchen/dsh-plugin-multi-root-workspace](https://github.com/cherrchen/dsh-plugin-multi-root-workspace) - Workspace multi-folder: memungkinkan Agent DSH (DeepSeek Harness) tidak hanya…
- [dsh-plugin-lab/dsh-workbuddy-bridge](https://github.com/dsh-plugin-lab/dsh-workbuddy-bridge) - Plugin DSH: menghubungkan model dari aplikasi desktop WorkBuddy ke DeepSeek…
- [Noob-stupid/dsh-github-login](https://github.com/Noob-stupid/dsh-github-login) - DeepSeek Harness 生态的 GitHub 可视化登录工具（零终端）：设备码流程，令牌同步 gh CLI | Visual GitHub…
- [shenhuanageshei/dsh-team-link](https://github.com/shenhuanageshei/dsh-team-link) - Deep link sesi + ekspor sesi lengkap (markdown/JSON) + pengiriman pesan lintas…
- [KannaKuron/dsh-ide-git](https://github.com/KannaKuron/dsh-ide-git) - Plugin DSH: jendela alat Git setara IDE sebagai tab dsh-better-sidebar native…
- [ItQianChen/dsh-github-flow](https://github.com/ItQianChen/dsh-github-flow) - Membuat DeepSeek Harness Agent memiliki tangan dan kaki native untuk…
- [laoduu/DeepSeek-Harness-yizi-themes](https://github.com/laoduu/DeepSeek-Harness-yizi-themes) - 19 tema gaya pilihan untuk DeepSeek Harness（dsh）Web UI, sepenuhnya diadaptasi…
- [PerryLink/dsh-plugin-doctor](https://github.com/PerryLink/dsh-plugin-doctor) - Standar verifikasi tanpa dependensi untuk plugin DeepSeek Harness (dsh)…
- [PerryLink/perrylink](https://github.com/PerryLink/perrylink) - DeepSeek Harness plugin ecosystem: 86 open-source plugins in a 101-repo family…
- [possible055/agentshim](https://github.com/possible055/agentshim) - High-performance, capability-aware repository tools and process execution for…
- [viztor/dsh-opencode-patch](https://github.com/viztor/dsh-opencode-patch) - OpenCode di DeepSeek Harness — plugin DSH yang menjaga OpenCode Zen + model…
- [YeqingTang/dsh-session-flow](https://github.com/YeqingTang/dsh-session-flow) - DSH 会话信息流重设计插件：跨会话档案柜，折叠时间线 / 血缘树 / 检索 / 双模式摘要 / ZIP 导出 / 实时跟踪.
- [AI-Scarlett/DSH-Store](https://github.com/AI-Scarlett/DSH-Store) - DSH STORE — marketplace plugin pihak ketiga dan pengelola siklus hidup dengan…
- [Atelyx/Atelyx](https://github.com/Atelyx/Atelyx) - Atelyx adalah meja kerja desktop yang dapat diperluas dan berpusat pada…
- [Djokovical5294/DeepSeek-Harness-Token-Free](https://github.com/Djokovical5294/DeepSeek-Harness-Token-Free) - Jalankan DeepSeek Harness di desktop tanpa biaya token—GUI gratis dan sumber…
- [dsh-cc/dsh-cc](https://github.com/dsh-cc/dsh-cc) - Agen pengodean lengkap untuk DeepSeek Harness — workflow bergaya Claude Code…
- [dsh-plugin-lab/dsh-ds-balance](https://github.com/dsh-plugin-lab/dsh-ds-balance) - Plugin DSH: menampilkan saldo akun DeepSeek Anda di bagian bawah bilah samping…
- [dushaobindoudou/dsh-bots](https://github.com/dushaobindoudou/dsh-bots) - Meja kerja dsh Bots: plugin Cordis yang menjembatani gateway orkestrasi…
- [sakanamaru/dsh-minato](https://github.com/sakanamaru/dsh-minato) - dsh-minato — perangkat instalasi dan operasional deployment lokal versi…
- [tianyagk/dsh-tradewatcher](https://github.com/tianyagk/dsh-tradewatcher) - Plugin web DeepSeek Harness (DSH): tab sidebar market-dashboard untuk memantau…
- [Wanbinyu/wanbinyu-harness-toolbox](https://github.com/Wanbinyu/wanbinyu-harness-toolbox) - Plugin dan alat pihak ketiga independen untuk DeepSeek Harness, dikelola oleh…
- [x5427876/dsh-opencode-free](https://github.com/x5427876/dsh-opencode-free) - Gunakan model gratis OpenCode Zen di DeepSeek Harness dengan akses anonim atau…
- [Asukayanamii/learn-cordis4py](https://github.com/Asukayanamii/learn-cordis4py) - Cordis 插件框架的 Python 复刻：上下文与作用域、fiber 生命周期、五种事件分发、服务依赖注入、配置校验、YAML 装载器.
- [argszero/cordis-plugin-sandbox-grant-advisor](https://github.com/argszero/cordis-plugin-sandbox-grant-advisor) - Plugin DeepSeek Harness: mengubah kegagalan penyediaan ACL sandbox Windows…
- [argszero/cordis-plugin-goal-progress-guard](https://github.com/argszero/cordis-plugin-goal-progress-guard) - Penilaian kemajuan untuk putaran tujuan otonom dsh: tunda loop saat tugas latar…
- [argszero/cordis-plugin-length-stop-overflow](https://github.com/argszero/cordis-plugin-length-stop-overflow) - plugin dsh: mengubah penghentian panjang yang terpotong menjadi pemulihan…
- [eovidiu/cordis-ios](https://github.com/eovidiu/cordis-ios) - Plugin yang membersihkan dirinya sendiri: port Code Swift 6 dari kerangka…
- [validation-engineering/cordis-verus](https://github.com/validation-engineering/cordis-verus) - Runtime plugin Rust dengan kernel siklus hidup yang diverifikasi Verus dan…
- [tellmewhattodo/dsh-serenity-plugin](https://github.com/tellmewhattodo/dsh-serenity-plugin) - dsh-serenity-plugin.
- [arkme-senx/arkme-dsh-plugin](https://github.com/arkme-senx/arkme-dsh-plugin) - Integrasi akun, catatan, obrolan, dan momen yang saling terjalin Arkme untuk…

</details>

<a id="writing"></a>

## Tulisan, diskusi, dan video

Tulisan, diskusi, dan video tentang kemampuan mod.

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925102">Claude Code Mods</a></b> · ⭐6 · 👁️ observed · 10 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50003222">What the Hell Are Claude Mods? [video]</a></b> · ⭐4 · 👁️ observed · 4 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49999983">A Claude Code mod plays MIDI music when it works</a></b> · ⭐3 · 👁️ observed · 4 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925800">Claude Code Mods: plugins may now modify deeper behavior</a></b> · ⭐3 · 👁️ observed · 10 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49926243">Getting started with Claude Code mods</a></b> · ⭐3 · 👁️ observed · 10 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49945600">Show HN: Terminal Gym – a Claude mod that makes you do pushups between prompts</a></b> · ⭐3 · 👁️ observed · 8 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49971594">Terminal Steps: A Claude mod for a daily step goal, synced from Apple Health</a></b> · ⭐3 · 👁️ observed · 6 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50024345">Agent-config&amp;Claude Code mods</a></b> · ⭐2 · 👁️ observed · 2 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49940121">Getting started with Claude Code mods</a></b> · ⭐2 · 👁️ observed · 9 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49927599">Pi-autoresearch ported to Claude Code 1:1 using the new mods API</a></b> · ⭐2 · 👁️ observed · 10 天</summary>

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

<a id="other"></a>

## Proyek lainnya

Entri yang menyentuh permukaan mod tetapi bukan mod itu sendiri, tetap ditampilkan alih-alih disembunyikan.

<details>
<summary>📦 <b><a href="https://github.com/rajmand/claude_mods">rajmand/claude_mods</a></b> · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Ringkasan

Tidak ada deskripsi upstream yang dipublikasikan.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Proyek lainnya`                                                  |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |
| Bahasa   | TypeScript                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **0**      |
| Push terakhir            | 2026-10-12 |
| Pertama kali dicantumkan | 2026-10-12 |

</details>

<a id="projects-by-implementation-language"></a>

## Proyek berdasarkan bahasa implementasi

Ekosistem ini terkonsentrasi pada Python dan TypeScript, tetapi client bertipe terus bermunculan dalam bahasa lain. Tabel ini dibuat dari entri-entri itu sendiri.

| Bahasa     | Entri | Contoh                                                                                                        |
| ---------- | ----- | ------------------------------------------------------------------------------------------------------------- |
| TypeScript | 386   | `anthropics/claude-code`, `anthropics/claude-code-action`, `see-stack/claude-code-mods`                       |
| JavaScript | 76    | `huaweicloud/huaweicloud-devkit`, `karanb192/awesome-claude-code-mods`, `karanb192/claude-code-mods`          |
| Python     | 39    | `anthropics/claude-agent-sdk-python`, `anthropics/claude-code-security-review`, `alexgreensh/token-optimizer` |
| Shell      | 30    | `anthropics/claude-agent-sdk-typescript`, `0xDarkMatter/claude-mods`, `BeLazy167/claude-mods-skill`           |
| HTML       | 10    | `darrell-tw/darrelltw-mods`, `omarcevi/claudemods`, `testy-cool/awesome-claude-code-mods`                     |
| Rust       | 9     | `persiyanov/herdr-reviewr`, `Tripstack-Corp/spyc`, `cc-friend/ccost`                                          |
| Go         | 5     | `kartollikaa/claude-android-emulator`, `backstabslash/goccc`, `esengine/DeepSeek-Reasonix`                    |
| Swift      | 3     | `chrisnguyen1211/pillrdotlol`, `peaceinitiativemenhadenoil263/claude-status-bar`, `eovidiu/cordis-ios`        |
| PowerShell | 2     | `Gabriel-Dalton/claude-statusline-tokens`, `rainyfei/claude-statusline-win`                                   |
| C          | 1     | `reporails/arcade`                                                                                            |
| C#         | 1     | `sakanamaru/dsh-minato`                                                                                       |
| Lua        | 1     | `crafts69guy/claude-statusline.nvim`                                                                          |
| MDX        | 1     | `jkf87/mod-guide`                                                                                             |

<sub>Hanya entri yang menyatakan bahasa yang dihitung. Entri dokumentasi dan diskusi tidak disertakan dalam tabel ini.</sub>

## Berkontribusi

Koreksi sangat diterima dan merupakan cara tercepat untuk meningkatkan daftar ini. Buka issue atau pull request jika suatu entri salah kategorisasi, salah tingkat, atau jika sebuah proyek keliru dikecualikan karena benturan nama — kategori terakhir itulah yang paling mungkin salah akibat filter otomatis.

---

<sub>Proyek komunitas independen. Tidak berafiliasi dengan, tidak didukung oleh, dan tidak ditinjau oleh Anthropic. Claude Code, Claude, dan Anthropic adalah merek dagang milik Anthropic. Perilaku produk dapat berubah tanpa pemberitahuan; verifikasi hal-hal penting terhadap dokumentasi resmi. Aset tetap menjadi milik proyek upstream masing-masing dan hanya direproduksi jika diizinkan oleh lisensinya.</sub>

<sub>Terakhir diperbarui · 2026-10-12T21:29:43+08:00</sub>
