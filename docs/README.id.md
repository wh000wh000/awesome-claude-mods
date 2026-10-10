<p align="center">
  <img src="../assets/readme/hero.png" width="100%" alt="Mod Claude Keren">
</p>

<h1 align="center">Mod Claude Keren</h1>

<p align="center"><b>Indeks mod Claude Code, plugin, dan perubahan perilaku mendalam yang ditimbulkannya, dengan pemeringkatan berdasarkan bukti.</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-617-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="../LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
  <a href="https://wh000wh000.github.io/awesome-claude-mods/"><img src="https://img.shields.io/badge/site-searchable-1f6feb" alt="site"></a>
</p>

<p align="center"><sub><a href="../README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.pt-BR.md">Português</a> · <a href="README.ru.md">Русский</a> · <a href="README.it.md">Italiano</a> · <a href="README.ar.md">العربية</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.tr.md">Türkçe</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <b>Bahasa Indonesia</b> · <a href="README.pl.md">Polski</a> · <a href="README.nl.md">Nederlands</a> · <a href="README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **Indeks aktif** · Sinkronisasi terakhir: `2026-10-11T05:58:46+08:00` (UTC+8)
> · Entri: **617** · Ditambahkan pada pembaruan terbaru: **0** · Bahasa implementasi: **10**

<sub>Setiap entri di bawah dikumpulkan, difilter, dan diperiksa ulang secara otomatis. Tidak ada konten berbayar di sini.</sub>

<a id="featured"></a>

## Pilihan saat ini

<sub>Satu entri per kategori, diurutkan berdasarkan tingkat bukti dan jumlah bintang, lalu dihitung ulang setiap kali diperbarui. Ini adalah pemeringkatan, bukan dukungan; setiap pilihan tertaut ke kartu lengkapnya di bawah. Proyek yang memublikasikan tangkapan layar atau rekaman lebih diutamakan agar panel ini tetap visual.</sub>

<table>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action">
<b>🏛️ <a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b>
<sub>⭐9466 · TypeScript · ✅ official</sub>
</td>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer">
<b>🧩 <a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b>
<sub>⭐2532 · Python · 👁️ observed</sub>
<sub>Find the ghost tokens. Fix them. Survive compaction. Avoid context quality decay.</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo">
<b>🧵 <a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b>
<sub>⭐74280 · TypeScript · 👁️ observed</sub>
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
- [Mod: dibuat dengan kemampuan mod](#mod-dibuat-dengan-kemampuan-mod) — **493**
- [Ekosistem plugin DSH dan Cordis](#ekosistem-plugin-dsh-dan-cordis) — **97**
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
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></b> · ⭐150059 · TypeScript · ✅ official · 1 天</summary>

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
| Bintang                  | **150059** |
| Push terakhir            | 2026-10-09 |
| Pertama kali dicantumkan | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b> · ⭐9466 · TypeScript · ✅ official · 1 天</summary>

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
| Bintang                  | **9466**   |
| Push terakhir            | 2026-10-09 |
| Pertama kali dicantumkan | 2026-10-04 |

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-python">anthropics/claude-agent-sdk-python</a></b> · ⭐8244 · Python · ✅ official · 1 天</summary>

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
| Bintang                  | **8244**   |
| Push terakhir            | 2026-10-09 |
| Pertama kali dicantumkan | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-security-review">anthropics/claude-code-security-review</a></b> · ⭐6335 · Python · ✅ official · 241 天</summary>

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
| Bintang                  | **6335**   |
| Push terakhir            | 2026-02-11 |
| Pertama kali dicantumkan | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-typescript">anthropics/claude-agent-sdk-typescript</a></b> · ⭐1799 · Shell · ✅ official · 1 天</summary>

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
<summary>🏛️ <b><a href="https://github.com/PerryLink/dsh-mcp-panel">PerryLink/dsh-mcp-panel</a></b> · ⭐74 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

Konsol manajemen MCP untuk klien MCP resmi DeepSeek Harness: perintah /mcp dengan diagnostik kesehatan dan panggilan uji pipeline, tab Settings MCP dengan CRUD server (penulisan yang memerlukan persetujuan, pencadangan otomatis), serta konsol uji alat melalui pipeline alat resmi (Apache-2.0, dsh-plugin).

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Resmi: repositori dan catatan rilis milik Anthropic sendiri`                                 |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | TypeScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **74**     |
| Push terakhir            | 2026-10-10 |
| Pertama kali dicantumkan | 2026-10-10 |

🏷 `ai-agent` · `ai-agents` · `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-mcp-panel/f435adadbab44c9f.png" width="100%" alt="PerryLink/dsh-mcp-panel screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-mcp-panel/79405ad96d2dc69e.gif" width="100%" alt="PerryLink/dsh-mcp-panel animation"><br><sub>rekaman animasi</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/MIHassan3/DSH-Launcher">MIHassan3/DSH-Launcher</a></b> · ⭐3 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

ini adalah launcher untuk DeepSeek Harness resmi. tanpa modifikasi, hanya menjalankan apa yang dikembangkan DeepSeek.

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
| Push terakhir            | 2026-10-10 |
| Pertama kali dicantumkan | 2026-10-10 |

🏷 `ai-agent` · `ai-agents` · `ai-tools` · `cordis` · `deepseek` · `deepseek-harness` · `dsh` · `dsh-desktop`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/mihassan3--dsh-launcher/2d777b77102fa60f.png" width="100%" alt="MIHassan3/DSH-Launcher screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

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
<summary>🧩 <b><a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b> · ⭐2532 · Python · 👁️ observed · 0 天</summary>

##### 📝 Ringkasan

Find the ghost tokens. Fix them. Survive compaction. Avoid context quality decay.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Mod: dibuat dengan kemampuan mod`                                |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |
| Bahasa   | Python                                                            |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **2532**   |
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
<summary>🧩 <b><a href="https://github.com/karanb192/awesome-claude-code-mods">karanb192/awesome-claude-code-mods</a></b> · ⭐467 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Ringkasan

Katalog komunitas mod Claude Code publik (function hooks), dipindai dari GitHub beserta informasi tentang apa yang dapat dibaca, ditulis, dijalankan, atau dikirim melalui jaringan oleh setiap mod. Jelajahi https://mods.aidojo.si/

<sub>🔧 Ditemukan digunakan dalam kode: `data/seeds.txt`, `data/duplicates.txt`, `data/repos.txt`</sub>

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Mod: dibuat dengan kemampuan mod`                                |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |
| Bahasa   | JavaScript                                                        |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **467**    |
| Push terakhir            | 2026-10-10 |
| Pertama kali dicantumkan | 2026-10-04 |

🏷 `anthropic` · `awesome` · `awesome-list` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hamzafer/claude-code-mods">hamzafer/claude-code-mods</a></b> · ⭐181 · TypeScript · 👁️ observed · 1 天</summary>

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
| Bintang                  | **181**    |
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
<summary>🧩 <b><a href="https://github.com/karanb192/cache-tax">karanb192/cache-tax</a></b> · ⭐115 · TypeScript · 👁️ observed · 6 天</summary>

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
| Bintang                  | **115**    |
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
<summary>🧩 <b><a href="https://github.com/HeyCubit/effortless">HeyCubit/effortless</a></b> · ⭐106 · HTML · 👁️ observed · 0 天</summary>

##### 📝 Ringkasan

Claude Code mod: picks the reasoning effort for every prompt, shows the prompt cache and context, and hands off or compacts in one click

<sub>🔧 Ditemukan digunakan dalam kode: `docs/agent-panel/PLAN.md`, `hooks/register.tsx`</sub>

##### 📌 Fakta dasar

| Bidang   | Nilai                                                             |
| -------- | ----------------------------------------------------------------- |
| Kategori | `Mod: dibuat dengan kemampuan mod`                                |
| Bukti    | `teksnya sendiri menyebut mod API, atau menyatakan kemampuan mod` |
| Bahasa   | HTML                                                              |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **106**    |
| Push terakhir            | 2026-10-10 |
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `ai-tools` · `anthropic` · `claude` · `claude-code` · `claude-code-plugin` · `developer-tools` · `prompt-caching`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/heycubit--effortless/ad0a6472f7a34cd7.png" width="100%" alt="HeyCubit/effortless screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/heycubit--effortless/fcef2f9593961020.gif" width="100%" alt="HeyCubit/effortless animation"><br><sub>rekaman animasi</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/awss1i/assay">awss1i/assay</a></b> · ⭐104 · HTML · 👁️ observed · 0 天</summary>

##### 📝 Ringkasan

An agent-native QA CLI for web pages. Deterministic, no tests to write, no LLM.

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
<summary>🧩 <b><a href="https://github.com/hellosverre/claude-skins">hellosverre/claude-skins</a></b> · ⭐88 · TypeScript · 👁️ observed · 0 天</summary>

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
| Bintang                  | **88**     |
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

Colorful, themeable Claude Code replies: tables, code, diagrams, charts and tool rows in 15 themes, with copy buttons. A Claude Code mod.

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
<summary>🧩 <b><a href="https://github.com/scasella/claude-flightdeck">scasella/claude-flightdeck</a></b> · ⭐59 · TypeScript · 👁️ observed · 8 天</summary>

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
| Bintang                  | **59**     |
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
<summary>🧩 <b><a href="https://github.com/0xDarkMatter/claude-mods">0xDarkMatter/claude-mods</a></b> · ⭐57 · Shell · 👁️ observed · 3 天</summary>

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
| Bintang                  | **57**     |
| Push terakhir            | 2026-10-07 |
| Pertama kali dicantumkan | 2026-10-04 |

🏷 `agent-skills` · `ai-agents` · `ai-tools` · `anthropic` · `claude` · `claude-code` · `claude-skills` · `developer-tools`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/zycck/claude-mods">zycck/claude-mods</a></b> · ⭐45 · TypeScript · 👁️ observed · 2 天</summary>

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
| Bintang                  | **45**     |
| Push terakhir            | 2026-10-08 |
| Pertama kali dicantumkan | 2026-10-04 |

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/49f09d1600b02c7a.gif" width="100%" alt="zycck/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/25f4230871cb30f6.gif" width="100%" alt="zycck/claude-mods animation"><br><sub>rekaman animasi · <a href="https://raw.githubusercontent.com/zycck/claude-mods/main/media/plan-progress.mp4">Buka video</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/henrik-thevibe/Claude-Fables">henrik-thevibe/Claude-Fables</a></b> · ⭐32 · TypeScript · 👁️ observed · 7 天</summary>

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
<summary>🧩 <b><a href="https://github.com/oikon48/prompt-rail">oikon48/prompt-rail</a></b> · ⭐27 · TypeScript · 👁️ observed · 7 天</summary>

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

A glow-up for Claude Code: a live cockpit pane, shareable themes, and a pixel pet that acts out what Claude is doing

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
<summary>🧩 <b><a href="https://github.com/lemomo-ai/lemo-mod">lemomo-ai/lemo-mod</a></b> · ⭐20 · TypeScript · 👁️ observed · 6 天</summary>

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
<summary>🧩 <b><a href="https://github.com/aieo-product/claude_qamods">aieo-product/claude_qamods</a></b> · ⭐11 · TypeScript · 👁️ observed · 3 天</summary>

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
<summary>🧩 <b><a href="https://github.com/OneWave-AI/claude-code-mods">OneWave-AI/claude-code-mods</a></b> · ⭐11 · TypeScript · 👁️ observed · 7 天</summary>

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
<summary>🧩 <b><a href="https://github.com/furqan-khan07/pixelband">furqan-khan07/pixelband</a></b> · ⭐10 · TypeScript · 👁️ observed · 6 天</summary>

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
<summary>🧩 <b><a href="https://github.com/az9713/claude-mod-pack">az9713/claude-mod-pack</a></b> · ⭐8 · TypeScript · 👁️ observed · 6 天</summary>

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
<summary>🧩 <b><a href="https://github.com/Arunjay4213/claude-mods">Arunjay4213/claude-mods</a></b> · ⭐7 · TypeScript · 👁️ observed · 25 天</summary>

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
| Bintang                  | **7**      |
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
<summary>🧩 <b><a href="https://github.com/nogu66/md-prompt">nogu66/md-prompt</a></b> · ⭐7 · TypeScript · 👁️ observed · 7 天</summary>

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
<summary>🧩 <b><a href="https://github.com/ronanworks/claude-code-mods">ronanworks/claude-code-mods</a></b> · ⭐7 · TypeScript · 👁️ observed · 2 天</summary>

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
<summary><b>Lainnya dalam kategori ini</b> <sub>· 459</sub></summary>

- [whyashthakker/awesome-claude-code-mods](https://github.com/whyashthakker/awesome-claude-code-mods) - Koleksi lebih dari 100 mod yang dapat Anda gunakan dengan Claude Code.
- [karanb192/claude-code-mods](https://github.com/karanb192/claude-code-mods) - Mod Claude dan alat untuk membangunnya: skill builder, lalu mod.
- [ucsandman/claude-harness](https://github.com/ucsandman/claude-harness) - Harness Claude Code yang saya jalankan setiap hari, diterbitkan dengan nama ini…
- [kagamiurayama/claude-code-roof-mod](https://github.com/kagamiurayama/claude-code-roof-mod) - Ubah atap Claude Code dengan Claude Mods: tanpa mengubah biner, ganti prompt…
- [nateherkai/claude-code-mods](https://github.com/nateherkai/claude-code-mods) - Empat mod Claude Code: Cache Keeper, Recording Mode, Goal Meter, dan Collision…
- [Hangghost/learning-hacker-claude-mod](https://github.com/Hangghost/learning-hacker-claude-mod) - Mod Claude Code dari Learning Hacker: menggambarkan operasi agen agar mudah…
- [kakha13/claude](https://github.com/kakha13/claude) - Mod Claude Code yang memperbaiki dan menerjemahkan prompt Anda sebelum Claude…
- [xuanji86/claude-agentpane](https://github.com/xuanji86/claude-agentpane) - Panel samping untuk Claude Code: subagen yang dijalankan sesi, apa yang sedang…
- [nvr0x5/claude-deck](https://github.com/nvr0x5/claude-deck) - Kokpit untuk Claude Code: bilah rencana live, strip subagent, batas penggunaan…
- [AgriciDaniel/claude-mods-brain](https://github.com/AgriciDaniel/claude-mods-brain) - Basis pengetahuan Obsidian dengan sumber kutipan tentang mod Claude Code: cara…
- [BeLazy167/claude-mods-skill](https://github.com/BeLazy167/claude-mods-skill) - Skill yang mengajarkan agen Claude Code untuk membuat Mod Claude.
- [letswritetw/claude-mod-open-todos](https://github.com/letswritetw/claude-mod-open-todos) - Panel bilah samping Claude Desktop (tab Code): mencantumkan semua tugas…
- [nekyialabs/claude-code-toolkit](https://github.com/nekyialabs/claude-code-toolkit) - Mod dan skill Claude Code dari Nekyia Labs, dibuat dan digunakan setiap hari…
- [KilimcininKorOglu/claude-code-mods](https://github.com/KilimcininKorOglu/claude-code-mods) - Mod Claude (plugin function-hooks) untuk Claude Code.
- [letswritetw/claude-mod-token-usage](https://github.com/letswritetw/claude-mod-token-usage) - Bilah penggunaan di atas kotak input Claude Desktop (tab Code): kuota 5j / 7h…
- [omarcevi/claudemods](https://github.com/omarcevi/claudemods) - Mod, plugin &amp; skill Claude komunitas, dapat diinstal dari satu marketplace.
- [baselane-sh/mods-catalog](https://github.com/baselane-sh/mods-catalog) - Galeri mod Baselane: mod Claude Code yang telah diperiksa dan disematkan.
- [eighteyes/cactus](https://github.com/eighteyes/cactus) - Antrean keputusan CLI/TUI untuk manusia yang bekerja dengan agen percakapan.
- [jkf87/ide-mod](https://github.com/jkf87/ide-mod) - Mod panel IDE Claude Code: papan agent, pohon file dan penampil HWP/PDF, status…
- [xuanji86/claude-statuspane](https://github.com/xuanji86/claude-statuspane) - Kartu status mengambang untuk Claude Code—model, konteks, batas laju, biaya…
- [danyuchn/claude-mods](https://github.com/danyuchn/claude-mods) - Mod Claude Code: screen-guard menyamarkan nama dan rahasia saat Anda berbagi…
- [magidandrew/cx](https://github.com/magidandrew/cx) - Ekstensi Claude Code. Buka seluruh kekuatan Claude.
- [mishgoldenberg/claude-mods](https://github.com/mishgoldenberg/claude-mods) - Panel, pagar pengaman, dan mod peningkat kenyamanan untuk Claude Code: konteks…
- [ofeklevy11/claude-code-hud](https://github.com/ofeklevy11/claude-code-hud) - Dua mod Claude Code di atas kotak prompt: pengukur jendela konteks, batas 5…
- [Shuffzord/RoadRaven](https://github.com/Shuffzord/RoadRaven) - Your plan, watching itself. Local desktop roadmap tree that Claude Code and any…
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
- [yash-gadodia/claude-mods](https://github.com/yash-gadodia/claude-mods) - Mod Claude Code yang menjaga agent tetap jujur — function hooks yang menjaga…
- [alexcz-a11y/claude-mods](https://github.com/alexcz-a11y/claude-mods) - Koleksi mod Claude Code saya, satu mod per direktori.
- [Ankitrai97/rai-claude-mods](https://github.com/Ankitrai97/rai-claude-mods) - Lima mod Claude Code gratis: Simple Mode, Usage Tally, Context Handoff, Inbox…
- [arviaja/token-watch](https://github.com/arviaja/token-watch) - Mod Claude Code: menampilkan penggunaan token, batas plan, dan suhu cache sesi…
- [Boom-Vitt/boombignose-mods](https://github.com/Boom-Vitt/boombignose-mods) - Claude Code mods: context bar, agents panel, PDPA blur.
- [CodyAMaughan/meme-factory](https://github.com/CodyAMaughan/meme-factory) - Baru keluar dari pabrik. Mod Claude Code: minta meme, lalu terus bekerja.
- [DarioFontanel/claude-code-mods](https://github.com/DarioFontanel/claude-code-mods) - Mod untuk Claude Code: bilah prompt cache, langkah berikutnya, tombol cepat…
- [estruyf/claude-stats-mod](https://github.com/estruyf/claude-stats-mod) - Mod Claude Code yang menggambar batas penggunaan dan pengeluaran Anda di bilah…
- [gecm0/skill-router-mod](https://github.com/gecm0/skill-router-mod) - Mod skill-router: Jev memilih dan memuat keterampilan yang dibutuhkan setiap…
- [hellosverre/mod-store](https://github.com/hellosverre/mod-store) - App store untuk mod Claude Code, di dalam Claude Code: /mods untuk menjelajah…
- [herman925/925-cc-plugins](https://github.com/herman925/925-cc-plugins) - Mod Claude Code milik Herman (marketplace herman-mods).
- [homieyangg/claude-code-mods](https://github.com/homieyangg/claude-code-mods) - Mod Claude Code: bilah kemajuan untuk rencana, buku besar tentang apa yang…
- [ice-lfernandes/claude-code-mods](https://github.com/ice-lfernandes/claude-code-mods) - Mod Claude Code untuk UX sehari-hari: batas rencana, konteks, dan apa yang…
- [macleodlabs-ai/claudeflow](https://github.com/macleodlabs-ai/claudeflow) - Mod Claude Code oleh MacLeod Labs: streams mengurai pekerjaan sesi yang saling…
- [MankhongGarden/claude-code-mods-field-notes](https://github.com/MankhongGarden/claude-code-mods-field-notes) - Catatan lapangan hari pertama tentang mod Claude Code di Windows: bilah bahan…
- [MichaelP17/claude-mods](https://github.com/MichaelP17/claude-mods) - Mod yang saya buat dan gunakan sendiri dalam penyiapan Claude Code saya.
- [patitow/claude-mod-cost-visibility](https://github.com/patitow/claude-mod-cost-visibility) - Mod Claude Code: meter biaya langsung, konteks &amp; kuota paket di atas prompt.
- [rbartoli/agent-usage-guard](https://github.com/rbartoli/agent-usage-guard) - Mod Claude Code yang menahan fan-out subagent, prompt konteks berat, dan loop…
- [schreibse/claude-code-mods](https://github.com/schreibse/claude-code-mods) - code-mods untuk claude.
- [shimo4228/harness-scope](https://github.com/shimo4228/harness-scope) - Mod Claude Code yang mengaktifkan atau menonaktifkan skill, agen, aturan, dan…
- [Sma1lboy/claude-mods](https://github.com/Sma1lboy/claude-mods) - Mod untuk Claude Code: plugin yang dibangun berdasarkan hook fungsi.
- [smukh/roll-credits](https://github.com/smukh/roll-credits) - Kredit bergaya film untuk sesi coding Anda.
- [theonly1me/claude-code-mods](https://github.com/theonly1me/claude-code-mods) - Sekumpulan mod claude code yang saya buat.
- [Unayung/cc-mods-youtube](https://github.com/Unayung/cc-mods-youtube) - Pemutar YouTube berbasis cliamp di dalam Claude Code (mod Claude Code).
- [VladLeus/claude-mods](https://github.com/VladLeus/claude-mods) - Mod Claude Code: dasbor agent-fleet dan autopilot (marketplace local-mods).
- [vynnlee/mods](https://github.com/vynnlee/mods) - Mod Claude Code oleh vynnlee. Satu folder per mod, dapat dipasang dari satu…
- [yodakeisuke/claudelingo](https://github.com/yodakeisuke/claudelingo) - Pelajari bahasa asing sambil bekerja dengan Claude Code.
- [20alexl/windvane](https://github.com/20alexl/windvane) - Menjaga sesi Claude Code yang panjang agar Anda tidak perlu melakukannya…
- [akerskuuug/claude-mods](https://github.com/akerskuuug/claude-mods) - Claude Code mod: usage, limits, branch and model around the prompt.
- [AlexeyHRDesign/colorwheel](https://github.com/AlexeyHRDesign/colorwheel) - Balasan bertema, diagram lebar penuh, serta konteks dan batas Anda dalam sekali…
- [alexlifexyz/p3c-guard](https://github.com/alexlifexyz/p3c-guard) - Saat Agen menulis Java, kode yang melanggar aturan Alibaba Java (p3c) tidak…
- [andrewbakercloudscale/claude-code-cost-sidebar](https://github.com/andrewbakercloudscale/claude-code-cost-sidebar) - Sidebar biaya, token, dan penggunaan konteks live untuk Claude Code: mod yang…
- [ben-rogerson/claude-counter-strike](https://github.com/ben-rogerson/claude-counter-strike) - Panggilan radio Counter-Strike 1.6 untuk Claude Code - &quot;Fire in the hole&quot; saat…
- [burnrate-ai/burnrate](https://github.com/burnrate-ai/burnrate) - Lihat dan perlambat seberapa cepat Claude Code menghabiskan batas Claude.ai…
- [CalvoSeko/claude-factory-mod](https://github.com/CalvoSeko/claude-factory-mod) - agent-graph: a Claude Code mod for designing and running graphs of agents…
- [cephalofoil/kitt](https://github.com/cephalofoil/kitt) - Herdr setup + Claude Code mods for product dev work.
- [chenyuxiaojin/cyxj-notch](https://github.com/chenyuxiaojin/cyxj-notch) - Dasbor notch macOS untuk Claude Code: batas penggunaan, sesi terbuka, progres…
- [chrisluo5311/squad-chat](https://github.com/chrisluo5311/squad-chat) - Claude sedang memasak. Chat dengan skuad Anda.
- [danielpg95/modster-hunter](https://github.com/danielpg95/modster-hunter) - Mod Claude Code: tangkap Modsters pixel-art dalam game idle saat Claude bekerja.
- [DarkVelours/claude-code-galactic-battle](https://github.com/DarkVelours/claude-code-galactic-battle) - Pertempuran luar angkasa di atas prompt Claude Code saat ia bekerja.
- [davidbalzan/status-band](https://github.com/davidbalzan/status-band) - Mod Claude Code oleh David Balzan: status-band, pita status di atas prompt…
- [Davron2004/slash-coverage](https://github.com/Davron2004/slash-coverage) - Lihat file mana yang ada dalam konteks setiap agen Claude Code, dan seberapa…
- [drakulavich/cogload](https://github.com/drakulavich/cogload) - Tetap tenang. Termometer untuk hari-hari Claude Code Anda: setiap jam diberi…
- [drkokorev/context-diet](https://github.com/drkokorev/context-diet) - Memangkas output alat yang sangat besar sebelum memenuhi konteks Claude Code.
- [enhki/claude-mods](https://github.com/enhki/claude-mods) - Mod kecil Claude Code untuk terminal dan aplikasi desktop.
- [Exdenta/ambient-spanish](https://github.com/Exdenta/ambient-spanish) - Skill + mod Claude CLI yang menambahkan kata-kata Spanyol ke balasan agen.
- [Fazzani/claude-mods](https://github.com/Fazzani/claude-mods) - Mod Claude.
- [gregdotca/ccmod-the-machine](https://github.com/gregdotca/ccmod-the-machine) - A Claude Code mod that restyles it as The Machine from Person of Interest.
- [hellosverre/smart-compact](https://github.com/hellosverre/smart-compact) - Mod Claude Code: melakukan compact pada saat yang tepat.
- [HyunjunJeon/claude-workflow-mods](https://github.com/HyunjunJeon/claude-workflow-mods) - dag-workflow: mod Code Claude untuk alur kerja DAG subagen yang wajib dan…
- [i-harsha-reddy/naruto-mod](https://github.com/i-harsha-reddy/naruto-mod) - A pixel-art Naruto companion for Claude Code: 20 ninja, 60 jutsu, performed…
- [ibrahimkobeissy/claude-mods](https://github.com/ibrahimkobeissy/claude-mods) - Open-source mods for Claude Code: panes, status lines, toasts, tool guards and…
- [joeVenner/claude-code-mods](https://github.com/joeVenner/claude-code-mods) - Direktori komunitas untuk mod, plugin, skills, agents, hooks, dan server MCP…
- [jonyfs/astrolabe](https://github.com/jonyfs/astrolabe) - 🧭 Mod Claude Code: status sesi, kemajuan Spec Kit live, dan tata kelola jendela…
- [kongyo2/context-view](https://github.com/kongyo2/context-view) - Jendela konteks sebagai satu baris di atas prompt, digambar seperti meter milik…
- [koslowskyj/tdd-mod](https://github.com/koslowskyj/tdd-mod) - Experimental Claude Code mod that enforces test-driven development: on coding…
- [KyongSik-Yoon/cc-desktop-mod](https://github.com/KyongSik-Yoon/cc-desktop-mod) - Plugin Code Claude (mod) yang membuat UI terminal Code Claude tampak seperti…
- [lorenzh/rabe](https://github.com/lorenzh/rabe) - Lihat apa yang dijalankan Claude Code di latar belakang: subagen, pekerjaan…
- [m4cd4r4/clear-resume](https://github.com/m4cd4r4/clear-resume) - Hapus chat, pertahankan pekerjaan. Plugin Code Claude + mod relay: Claude…
- [manuacl/claude-mods](https://github.com/manuacl/claude-mods) - Personal Claude Code mods: otto-hud, Otto the octopus with context weather and…
- [meganemura/pull-request-pane](https://github.com/meganemura/pull-request-pane) - Mod Claude yang menampilkan pull request GitHub milik sesi dalam panel di…
- [NMenzel/claude-devtools-mod](https://github.com/NMenzel/claude-devtools-mod) - Claude DevTools: debugger untuk tool call Claude Code.
- [NotRedFox/NotRedFoxs-Claude-skills](https://github.com/NotRedFox/NotRedFoxs-Claude-skills) - Keahlian Claude Code: pemeriksa fakta dokumen, auditor kode, log memori bug…
- [ondrhn/sharpprompt](https://github.com/ondrhn/sharpprompt) - Mod Claude Code yang menulis ulang prompt kasar menjadi jelas sebelum Anda…
- [rezzminator/buddy](https://github.com/rezzminator/buddy) - Plugin teman Claude Code: pendamping ASCII di atas prompt Anda yang mengingat…
- [rezzminator/tool-visibility-controller](https://github.com/rezzminator/tool-visibility-controller) - Plugin Claude Code untuk visibilitas alat per agen — sembunyikan dan tolak…
- [roma-vibe/jev-governor](https://github.com/roma-vibe/jev-governor) - Mod Claude Code: perutean model/usaha yang dipandu Jev, pemadatan konteks…
- [samfrmr/barmkin-mod](https://github.com/samfrmr/barmkin-mod) - Claude Code mods: security layer for Claude Code - secret redaction…
- [seanrobertwright/claude-mods](https://github.com/seanrobertwright/claude-mods) - Kumpulan mod Claude Code.
- [Sennjen/claude-sdlc](https://github.com/Sennjen/claude-sdlc) - Plugin dan mod Claude Code: SDLC AI-native.
- [SeongGwangJu/k-mods](https://github.com/SeongGwangJu/k-mods) - Koleksi mod Claude Code yang luar biasa | Koleksi mod Claude Code.
- [simplecore-inc/claude-mods](https://github.com/simplecore-inc/claude-mods) - Plugin Claude Code (mod): beralih di antara beberapa akun Claude, memantau…
- [Singh-AP/awesome-claude-mods](https://github.com/Singh-AP/awesome-claude-mods) - 🧩 Mod Claude Code yang telah diuji dan dapat dipasang dengan satu perintah…
- [Spardutti/claude-mods](https://github.com/Spardutti/claude-mods) - Mod Code Claude: panel langsung dan hook untuk pekerjaan sehari-hari.
- [tanujarun/it-speaks](https://github.com/tanujarun/it-speaks) - It Speaks: mod Claude Code yang membacakan balasan Claude dan prompt Anda saat…
- [TroyJLorents-GH/mod-squad](https://github.com/TroyJLorents-GH/mod-squad) - Mod Claude Code: plugin kecil untuk panel langsung, pengaturan perutean model…
- [valeryia-piatrova/token-hamster](https://github.com/valeryia-piatrova/token-hamster) - 🐹 Mod &amp; plugin Claude Code: monitor penggunaan, pelacak token &amp; baris status.
- [Verinoda-Labs/verinoda-symbiosis](https://github.com/Verinoda-Labs/verinoda-symbiosis) - Verinoda + Code Claude, bersama: Verinoda dengan verinoda-live, mod Code Claude…
- [VictorGambarini/jev-mod](https://github.com/VictorGambarini/jev-mod) - A Claude Code mod that hands the small decisions to a cheap decision model…
- [y-hirakaw/claude-code-mods](https://github.com/y-hirakaw/claude-code-mods) - Mod Claude Code. touch-map: lihat berkas mana yang dicantumkan, dibaca, diedit…
- [Yanir-R/catchup](https://github.com/Yanir-R/catchup) - Mod Claude Code yang merangkum pesan agen yang belum Anda baca, dalam bahasa…
- [zchee/claude-code-mods](https://github.com/zchee/claude-code-mods)
- [AbyssCN/claude-lead-harness](https://github.com/AbyssCN/claude-lead-harness) - Claude Code mods + cheap-executor driver: one Claude session as lead, MiniMax…
- [afterever/claude-mods](https://github.com/afterever/claude-mods) - Claude Code mods by afterever (plugin marketplace).
- [ajkatom/claude-mods](https://github.com/ajkatom/claude-mods)
- [Aler1x/claude-cat](https://github.com/Aler1x/claude-cat) - Kucing braille animasi di atas prompt Claude Code.
- [alinaqi/mixture-of-models-claude-mod](https://github.com/alinaqi/mixture-of-models-claude-mod) - Mod Claude Code: mengarahkan pekerjaan ringan ke GLM/Kimi melalui Claude Code…
- [aloki-alok/omni-cat](https://github.com/aloki-alok/omni-cat) - Kucing piksel di atas prompt Code Claude Anda yang menjalankan panggilan uji…
- [ambervdberg/smartcompact](https://github.com/ambervdberg/smartcompact) - Mod Claude Code yang memilih waktu yang tepat untuk melakukan pemadatan agar…
- [an80sPWNstar/claude-mods](https://github.com/an80sPWNstar/claude-mods) - Mod Claude untuk Claude Code: token-meter.
- [anderson-spider/claude-mods](https://github.com/anderson-spider/claude-mods) - Marketplace plugin Claude Code oleh anderson-spider.
- [ankits3a/cache-keeper](https://github.com/ankits3a/cache-keeper) - Claude Code mod: prompt-cache band, keep-warm, handoff judge trial.
- [antonisPanos/claude-mods](https://github.com/antonisPanos/claude-mods)
- [aott33/model-router](https://github.com/aott33/model-router) - Mod Claude Code yang memilih model untuk setiap subagen sebelum dimulai, dan…
- [arthurglaizal/quiet-token-bar](https://github.com/arthurglaizal/quiet-token-bar) - Mod Claude Code: jendela konteks Anda dalam satu baris yang tenang, berwarna…
- [Ashley-Pettit/lgtm-flash](https://github.com/Ashley-Pettit/lgtm-flash) - Kapal LGTM Lines berlayar melewati setelah setiap perubahan kode — mod Code…
- [Ashley-Pettit/villager-hp](https://github.com/Ashley-Pettit/villager-hp) - Batas penggunaan Claude Anda sebagai kartu kesehatan penduduk desa animasi…
- [AskTinNguyen/ather-mods](https://github.com/AskTinNguyen/ather-mods) - Mod Claude Code untuk tim S2 (marketplace ather).
- [astrosteveo/plain-english](https://github.com/astrosteveo/plain-english) - A Claude Code mod that makes Claude write plain English and flags its usual…
- [Atanur/deskfit](https://github.com/Atanur/deskfit) - Latihan singkat saat Claude bekerja: target harian, streak, badge, dan…
- [aycandv/claude-usage-meter](https://github.com/aycandv/claude-usage-meter) - Papan penggunaan untuk Claude Code: pengeluaran per model.
- [bastianfuchs/claude-code-cache-warm](https://github.com/bastianfuchs/claude-code-cache-warm) - Claude Code mod that shows the prompt-cache countdown in the footer and keeps…
- [benjaminr/nowplaying](https://github.com/benjaminr/nowplaying) - Mod Now Playing untuk Claude Code: Apple Music dan Spotify di atas prompt…
- [bennewton999/claude-code-mods](https://github.com/bennewton999/claude-code-mods) - Lima mod Claude Code untuk menjalankan banyak sesi sekaligus: papan armada…
- [Berkay2002/berkays-mods](https://github.com/Berkay2002/berkays-mods) - Mod Code Claude untuk sesi orkestrator dan pekerja.
- [bhargava-gumpula/claude-mods](https://github.com/bhargava-gumpula/claude-mods) - Mod Code Claude: pita penggunaan, daftar obrolan, /cube, /handoff, pembersihan…
- [broening/claude-mods](https://github.com/broening/claude-mods) - Mod untuk Claude Code: Cache-Uhr, Blast Radius, Vorschlaege, Arbeitsliste, Grill.
- [C-M-Jones/suggestion-spotlight](https://github.com/C-M-Jones/suggestion-spotlight) - Mod Claude Code: Suggestion Spotlight menampilkan hal yang dirujuk oleh prompt…
- [Carismarkus/clowl](https://github.com/Carismarkus/clowl) - Hanya seekor owl untuk Claude Code Anda.
- [cdeust/claude-mods](https://github.com/cdeust/claude-mods) - Mod Claude Code untuk harness ai-architect.tools: satu perhatian per mod…
- [cGradying/claude-code-cockpit](https://github.com/cGradying/claude-code-cockpit) - Pita Claude Code satu baris.
- [ChaseWNorton/claude-doom](https://github.com/ChaseWNorton/claude-doom) - Engine Doom asli dengan Freedoom, dapat dimainkan di dalam Claude Code.
- [cmorss/claude-mods](https://github.com/cmorss/claude-mods) - Mod Claude Code untuk git worktrees: /terminal dan /worktree-files membuka…
- [comertial/comertial-mods](https://github.com/comertial/comertial-mods) - Mod Claude Code untuk Engineer sejati.
- [d3nims/d3nim-claude-mods](https://github.com/d3nims/d3nim-claude-mods) - Mod Code Claude khusus tim d3nim.
- [David-AP-TON618/claude-explain](https://github.com/David-AP-TON618/claude-explain) - Claude Code mod: /explain re-renders an answer as controlled language (STE), a…
- [davidurco/cc-tamagotchi](https://github.com/davidurco/cc-tamagotchi) - Tamagotchi yang hidup di dalam Claude Code: ia menetas, memakan kode yang…
- [DazzleML/claude-bookmarks](https://github.com/DazzleML/claude-bookmarks) - Bookmark dan mark bergaya vim di dalam percakapan terminal Claude Code: sorot…
- [degterev/swiftui-preview-mod](https://github.com/degterev/swiftui-preview-mod) - Claude Code mod: SwiftUI previews rendered by Xcode, shown in a terminal pane.
- [delexw/codyssey](https://github.com/delexw/codyssey) - Ubah setiap sesi Claude Code menjadi petualangan kecil: musik generatif yang…
- [derekwden-droid/message-timestamps](https://github.com/derekwden-droid/message-timestamps) - Claude Code mod: shows the time on each prompt and reply in the terminal and…
- [devohmycode/ccmods](https://github.com/devohmycode/ccmods) - Mod Claude Code yang ditulis sebagai hook fungsi, serta marketplace yang…
- [DiegoCarrillo32/claude-plugins](https://github.com/DiegoCarrillo32/claude-plugins) - Claude Code mods and design systems: crab-crew and the Crab Crew design system.
- [divramod/divramod-claude-code-mods](https://github.com/divramod/divramod-claude-code-mods) - Mod Claude Code dari divramod: panel langsung dan penyesuaian untuk antarmuka…
- [DominikSch004/claude-mods](https://github.com/DominikSch004/claude-mods) - Mod Code Claude yang saya gunakan di setiap mesin: savvy-progress, filetree…
- [drprofi114-star/claude-mods](https://github.com/drprofi114-star/claude-mods)
- [duylinhdang1998/my-claude-mods](https://github.com/duylinhdang1998/my-claude-mods)
- [EggmanPDX/claude-mods](https://github.com/EggmanPDX/claude-mods) - mods.
- [Egrn/claude-code-mutedit](https://github.com/Egrn/claude-code-mutedit) - Hei, dibisukan! Buang diff, pangkas riff, tak ada lagi edit, kurangi kredit.
- [elkinaguas/claude-mods](https://github.com/elkinaguas/claude-mods)
- [eric1hua/claudemods-desktop-statusline](https://github.com/eric1hua/claudemods-desktop-statusline) - Mod Claude Code: penggunaan langganan (5h / 7d) sebagai pita di atas prompt di…
- [fabiopbarbieri/claude-test-progress](https://github.com/fabiopbarbieri/claude-test-progress) - Claude Code Mod for background test progress: JUnit, Karma, pytest and unittest.
- [fanoisme/claude-mods](https://github.com/fanoisme/claude-mods) - Mod dengan desain gerak untuk Code Claude: monitor langsung dan responsif untuk…
- [Flo0806/fh-claude-mods](https://github.com/Flo0806/fh-claude-mods) - Claude Mod Marketplace.
- [floheissler/cc-worktree-radar](https://github.com/floheissler/cc-worktree-radar) - A live radar of your parallel branches and worktrees above the prompt: which…
- [Gabrielmtvp/claude-code-mods](https://github.com/Gabrielmtvp/claude-code-mods) - Mod Claude Code saya.
- [GarvitNangru/claude-code-mods](https://github.com/GarvitNangru/claude-code-mods) - Mods and skins for Claude Code: a live progress bar for Claude.
- [GeckoKing9/claude-code-copy-button](https://github.com/GeckoKing9/claude-code-copy-button) - Ctrl+click copy link on every code block in Claude Code replies.
- [gecm0/jev-mod](https://github.com/gecm0/jev-mod) - Mod jev: $.jev untuk Code Claude, penilaian bertipe dari TypeSafe Jev.
- [Gersom/claude-mod-cache-watch](https://github.com/Gersom/claude-mod-cache-watch) - Mod de Claude Code: panel que muestra si el caché de prompts está caliente o…
- [Gersom/claude-mod-usage-meter](https://github.com/Gersom/claude-mod-usage-meter) - Mod de Claude Code: recuadro con el % de contexto y de los límites de 5 horas y…
- [Gersom/gersom-claude-mods](https://github.com/Gersom/gersom-claude-mods) - Mod untuk Claude Code: plugin hook, seperti usage-meter.
- [Gharib89/claude-mods](https://github.com/Gharib89/claude-mods) - Mod Claude Code (plugin function-hook), diinstal melalui satu marketplace.
- [gonzalonicolasr/claude-code-nerv](https://github.com/gonzalonicolasr/claude-code-nerv) - Bilah samping bergaya Evangelion untuk Claude Code: konteks, kuota, aktivitas…
- [gsporto226/claude-mods](https://github.com/gsporto226/claude-mods) - Useful claude code mods.
- [Gxrco/Screen-peek](https://github.com/Gxrco/Screen-peek) - Claude-Code Plugin (Mod) lets you see what the model is doing while it works.
- [hellosverre/redgreen](https://github.com/hellosverre/redgreen) - Hasil pengujian di panel Claude Code: kegagalan, detailnya, dan riwayat proses…
- [hfknight/claude-mod-said](https://github.com/hfknight/claude-mod-said) - Mod Claude Code: /said membuka panel samping berisi pesan yang Anda kirim…
- [Huuuuung/think-meter](https://github.com/Huuuuung/think-meter) - Mod Claude Code: berapa lama setiap jawaban berlangsung, berapa lama Claude…
- [icedevil2001/session-sidebar](https://github.com/icedevil2001/session-sidebar) - Mod Claude Code: tautan, hal-hal yang perlu diketahui, dan item tindakan untuk…
- [iddhi-sulakshana/claude-mods](https://github.com/iddhi-sulakshana/claude-mods) - Mod untuk Code Claude: tombol langkah berikutnya, pesan lintas sesi, dan…
- [jagp/xray-mod](https://github.com/jagp/xray-mod) - ⋐∿⋑ Tatap dalam-dalam konteks Anda: mod Claude Code live yang menampilkan apa…
- [jakerains/claudemods](https://github.com/jakerains/claudemods) - Small Claude Code mods: context and plan-usage gauges, a prompt-cache meter…
- [jduerrmann/agent-crew](https://github.com/jduerrmann/agent-crew) - A Claude Code mod: one pane for every subagent, the files they touch, and your…
- [jeffyfung/claude-mods](https://github.com/jeffyfung/claude-mods) - A place to house my claude mods.
- [jessetsai1024/claude-ctx-panel](https://github.com/jessetsai1024/claude-ctx-panel) - Panel penggunaan context di bilah samping: total, kategori, pertumbuhan tiap…
- [jessetsai1024/claude-files](https://github.com/jessetsai1024/claude-files) - Daftar file di bilah samping: file apa yang dibuat, diubah, atau dihapus dalam…
- [jessetsai1024/claude-maomao](https://github.com/jessetsai1024/claude-maomao) - 毛毛 bergaya 8-bit (kelinci lop Belanda hitam-putih) berlari dan melompat di atas…
- [jessetsai1024/claude-prompts](https://github.com/jessetsai1024/claude-prompts) - “Yang pernah saya tanyakan” di bilah samping: setiap kalimat yang diketik…
- [jessetsai1024/claude-timeline](https://github.com/jessetsai1024/claude-timeline) - Linimasa di bilah samping: ke mana waktu putaran ini digunakan.
- [jessetsai1024/claude-tokens](https://github.com/jessetsai1024/claude-tokens) - Pertukaran token di bilah samping: berapa token yang dikirim percakapan utama…
- [jessetsai1024/claude-whisper](https://github.com/jessetsai1024/claude-whisper) - Tas kacang jujur untuk claude code: setelah setiap putaran selesai menjawab…
- [jgilb17/claude-mods](https://github.com/jgilb17/claude-mods)
- [Jh-jaehyuk/plan-checklist](https://github.com/Jh-jaehyuk/plan-checklist) - Daftar periksa rencana untuk Code Claude yang terikat bukti: rencana yang…
- [jimmysteinmetz/b-sides](https://github.com/jimmysteinmetz/b-sides) - Mod kecil untuk Claude Code, seperti perintah slash baru dan panel samping.
- [jorgehsy/claude-mods](https://github.com/jorgehsy/claude-mods) - Catálogo de mods para Claude Code.
- [jpo-oss/claude-games](https://github.com/jpo-oss/claude-games) - Game multiplayer untuk dimainkan di dalam Claude Code saat bekerja.
- [juliomyitbrain/claude-code-git-graph](https://github.com/juliomyitbrain/claude-code-git-graph) - Claude Code mod: a pane that draws the repository.
- [justmytwospence/claude-cache-guard](https://github.com/justmytwospence/claude-cache-guard) - Mod Claude Code: menjaga cache prompt tetap hangat saat Anda pergi dan bertanya…
- [KaiC5504/clawd-bar](https://github.com/KaiC5504/clawd-bar) - Clawd tinggal di pita di atas prompt Claude Code Anda: memeragakan sesi…
- [kaicodedocument/claude-code-usage-bar](https://github.com/kaicodedocument/claude-code-usage-bar) - Mod Claude Code yang menampilkan alokasi batas laju, token sesi, dan biaya di…
- [kajidog/cc-mods-tts](https://github.com/kajidog/cc-mods-tts) - Mod yang membacakan respons dan notifikasi Claude Code menggunakan VOICEVOX /…
- [kbrdn1/claude-crosstalk](https://github.com/kbrdn1/claude-crosstalk) - Mod Claude untuk membaca dan bergabung dalam percakapan antara sesi Claude Code…
- [kikostefanov-lab/claude-code-mods](https://github.com/kikostefanov-lab/claude-code-mods) - Mod Claude Code: panel Whiteboard tempat Claude menggambar diagram Mermaid/UML…
- [KingP1197/claude-mods](https://github.com/KingP1197/claude-mods) - Niceties/quality of life improvement Claude mods.
- [kjhq/haiku-compact](https://github.com/kjhq/haiku-compact) - memadatkan sesi claude code dingin dengan haiku — pita cache satu baris yang…
- [kk5190/claude-code-mods](https://github.com/kk5190/claude-code-mods) - Mod untuk Code Claude: pengukur konteks dan panel server pengembangan.
- [krishna-goutham-tls/cc-mods](https://github.com/krishna-goutham-tls/cc-mods) - Two Claude Code mods: folio, a file pane beside the chat, and tint, a restyle…
- [kyledarling-io/claude-code-desktop-hud](https://github.com/kyledarling-io/claude-code-desktop-hud) - A live task HUD for Claude Code Desktop: a strip above the prompt while Claude…
- [KytioisaCat/playpen](https://github.com/KytioisaCat/playpen) - Siapa yang perlu perhatian? Sesi Claude Code Anda yang lain sebagai kartu di…
- [lua-erissatallan/claude-mods](https://github.com/lua-erissatallan/claude-mods)
- [Lucas-CX/awesome-claude-mods](https://github.com/Lucas-CX/awesome-claude-mods) - Panduan Mod Claude Code yang dikurasi komunitas: kasus penggunaan, demo asli…
- [lucasram20/claude-mods](https://github.com/lucasram20/claude-mods)
- [M-i-k-e-l/agent-state](https://github.com/M-i-k-e-l/agent-state) - Mod Claude Code yang menampilkan apa yang sedang dilakukan Claude di subtitel…
- [m-tababi/delegation-guard](https://github.com/m-tababi/delegation-guard) - Mod Claude Code: mendorong sesi utama untuk mendelegasikan ke subagent dan…
- [MahadSalim/claude-mods](https://github.com/MahadSalim/claude-mods) - My personal collection of claude mod plugins.
- [marcelmatula/claude-mods](https://github.com/marcelmatula/claude-mods) - Marcel.
- [MarcusJellinghaus/claude-mode-gate](https://github.com/MarcusJellinghaus/claude-mode-gate) - Mod Claude Code dengan profil izin yang dapat diganti: dasar yang aman, profil…
- [martin-macak/claude-code-mod-tracking](https://github.com/martin-macak/claude-code-mod-tracking) - Claude Code mod for tracking related artifacts and references.
- [MDmubarak786/claude-mods](https://github.com/MDmubarak786/claude-mods) - Community mods for Claude Code: guards, panes, and commands that run inside…
- [michaelblaess/turbo-mod](https://github.com/michaelblaess/turbo-mod) - Panel samping untuk Claude Code: berkas yang ditulis Claude, split terminal…
- [micke-dahlgren/token-range-monitor](https://github.com/micke-dahlgren/token-range-monitor) - Claude Code mod: projects what will be left of your weekly and 5-hour Claude…
- [mikejhill/claude-usage-status](https://github.com/mikejhill/claude-usage-status) - Claude Code mod: always-on band showing 5h/weekly limits, context fill, and…
- [mmedum/glimt](https://github.com/mmedum/glimt) - Panel samping yang tenang untuk Claude Code: apa yang sedang dilakukan sesi…
- [mmedum/spor](https://github.com/mmedum/spor) - Mengembalikan apa yang disembunyikan Claude Code: file yang dibaca Claude…
- [moonteek/claude-mods](https://github.com/moonteek/claude-mods) - Mod Claude Code: bilah memori dan daftar periksa tugas langsung di atas prompt.
- [muctebadikmen/claude-code-araclari](https://github.com/muctebadikmen/claude-code-araclari) - Mod Claude Code: serah-terima otomatis dan bilah kemajuan.
- [muellerei/enable-todo-tools](https://github.com/muellerei/enable-todo-tools) - Mod Claude Code yang mengaktifkan kembali alat todo untuk model yang tidak…
- [muellerei/task-line](https://github.com/muellerei/task-line) - Mod Claude Code: satu baris per tugas di atas prompt dengan tugas saat ini…
- [nachtgold/claude-code-connect-four](https://github.com/nachtgold/claude-code-connect-four) - Mainkan Connect Four melawan AI di dalam Claude Code (/connect-four).
- [Nachx639/context-canary](https://github.com/Nachx639/context-canary) - Canary pixel-art untuk Claude Code: ia mati ketika Claude berhenti mengikuti…
- [naoanao/agent-cross-check](https://github.com/naoanao/agent-cross-check) - Mod Claude Code: ketika agen coding lain melakukan commit ke repo Anda, Claude…
- [naoanao/shared-repo-guard](https://github.com/naoanao/shared-repo-guard) - Mod Claude Code untuk repo yang dibagikan oleh beberapa agen AI: menghentikan…
- [narley/sessions-sidebar](https://github.com/narley/sessions-sidebar) - Claude Code mod: a sidebar listing every Claude Code session, for Warp.
- [Nexus-nimdA/null-radio](https://github.com/Nexus-nimdA/null-radio) - Panel radio internet cyber-neon untuk Code Claude - dial synthwave…
- [niksavis/handily](https://github.com/niksavis/handily) - Mod Claude Code yang menampilkan item kerja, tugas, dan sesi Anda, untuk…
- [nnemirovsky/cc-monitor-rearm](https://github.com/nnemirovsky/cc-monitor-rearm) - Mengaktifkan kembali watch Monitor panjang Claude Code saat kedaluwarsa, tanpa…
- [nu0ma/query-guard](https://github.com/nu0ma/query-guard) - Pagar pengaman untuk SQL di Claude Code: meminta konfirmasi sebelum Claude…
- [OctopiAI/claude-code-statusline](https://github.com/OctopiAI/claude-code-statusline) - Mod Claude Code ringan.
- [OG-Matcha/tessera](https://github.com/OG-Matcha/tessera) - Satu mod untuk Claude Code, Windows dan CJK terlebih dahulu: pratinjau gambar…
- [oguz-hd/claude-code-chime](https://github.com/oguz-hd/claude-code-chime) - Chime untuk Claude Code: suara saat Claude selesai, membutuhkan input Anda…
- [ohade/claude-mods](https://github.com/ohade/claude-mods) - Mod Claude Code: gambar mini dan baris status.
- [onk3sh/fix-on-edit](https://github.com/onk3sh/fix-on-edit)
- [osaki42/awesome-claude-mods](https://github.com/osaki42/awesome-claude-mods) - Mod Claude Code terbaik, diurutkan berdasarkan manfaatnya bagi Anda.
- [oscarcosmedev/claude-mods](https://github.com/oscarcosmedev/claude-mods)
- [ozdeger/claude-looked-at-mod](https://github.com/ozdeger/claude-looked-at-mod) - Mod Claude Code: lihat setiap gambar dan berkas yang dilihat agen Anda…
- [pablodiazjorge/impact-radius](https://github.com/pablodiazjorge/impact-radius) - A Claude Code mod that holds risky shell commands.
- [Para-FR/claude-code-mods-fr](https://github.com/Para-FR/claude-code-mods-fr) - Dua Mod Claude untuk Claude Code: garde-du-corps.
- [paragpandyareal/lazy-panda-panel](https://github.com/paragpandyareal/lazy-panda-panel) - Lazy Panda Panel untuk Claude Code: tinjau dokumen tanpa mengangkat satu kaki…
- [philarete173/claude_mods](https://github.com/philarete173/claude_mods) - Panel samping statistik sesi langsung untuk tab Code aplikasi desktop Claude…
- [pkkid/claude-mods](https://github.com/pkkid/claude-mods) - Berbagai mod dan skill untuk pengaturan Claude Desktop saya.
- [pradyb/claude-mods](https://github.com/pradyb/claude-mods) - Mod untuk Code Claude: safety-guard memblokir perintah destruktif dan akses…
- [prompteafacil-hub/mods-claude-code](https://github.com/prompteafacil-hub/mods-claude-code) - Mods de Claude Code de la comunidad prompteafacil.
- [ptpmediabr/ideas-shelf](https://github.com/ptpmediabr/ideas-shelf) - Rak ide per proyek: catat ide di panel dan tandai sebagai selesai;
- [ptpmediabr/mods-manager](https://github.com/ptpmediabr/mods-manager) - Panel untuk melihat, mengaktifkan, menonaktifkan, memasang, dan mengelompokkan…
- [ptpmediabr/side-chat](https://github.com/ptpmediabr/side-chat) - Panel obrolan samping di dalam sesi yang menjawab pertanyaan atau menjalankan…
- [ptpmediabr/usage-weather](https://github.com/ptpmediabr/usage-weather) - Satu baris tenang di atas prompt: konteks, penggunaan 5 jam dan mingguan…
- [qarge/claude-mods](https://github.com/qarge/claude-mods)
- [rajib2k5/claude-market-watch](https://github.com/rajib2k5/claude-market-watch) - Mod Claude Code: ticker saham langsung, panel /quote, peringatan harga, pita…
- [ramtinJ95/claude-mods](https://github.com/ramtinJ95/claude-mods) - Mod Code Claude, diterbitkan sebagai satu marketplace plugin.
- [RedRoosterKey/claude-code-ssh-usage-band](https://github.com/RedRoosterKey/claude-code-ssh-usage-band) - Mod Claude Code: host SSH, RAM, dan batas penggunaan 5j/7h dalam satu baris di…
- [Risdon8/push-ups](https://github.com/Risdon8/push-ups) - Mod Code Claude: push-up yang harus dilakukan saat Claude bekerja. Tanpa token.
- [risen372/claude-mods](https://github.com/risen372/claude-mods)
- [ryx2/slopshopper](https://github.com/ryx2/slopshopper) - Toko mod untuk Claude Code: mengambil mod dari GitHub, menampilkannya dalam…
- [saadk408/stepline](https://github.com/saadk408/stepline) - Mod Claude Code: mengubah rencana yang Anda setujui dalam mode plan menjadi…
- [sadhirr1/claude-mods](https://github.com/sadhirr1/claude-mods) - Just a repo with different claude mods.
- [saksham10arora-dotcom/awesome-claude-mods](https://github.com/saksham10arora-dotcom/awesome-claude-mods) - Daftar pilihan mod Claude Code. Setiap entri dikloning dan diperiksa dengan…
- [saksham10arora-dotcom/claude-frugal](https://github.com/saksham10arora-dotcom/claude-frugal) - Mode tanpa biaya: agen pembantu berjalan di Haiku, dan file serta log besar…
- [saksham10arora-dotcom/claude-lofi](https://github.com/saksham10arora-dotcom/claude-lofi) - Soundtrack lofi yang mengikuti sesi: tenang, fokus, mengalir, plus isyarat…
- [saksham10arora-dotcom/claude-teach-me](https://github.com/saksham10arora-dotcom/claude-teach-me) - Belajar sambil Claude melakukan coding: setelah giliran yang mengubah kode…
- [saksham10arora-dotcom/claude-vhs](https://github.com/saksham10arora-dotcom/claude-vhs) - Rekaman setiap edit yang dibuat Claude: putar ulang setiap perubahan saat…
- [samaphp/session-links](https://github.com/samaphp/session-links) - Setiap tautan yang disebutkan sesi Anda, dalam satu baris di atas prompt.
- [SanjayPG/claude-code-usage-tracker](https://github.com/SanjayPG/claude-code-usage-tracker) - Claude Code mod: live usage-quota progress bars above your prompt.
- [SanjayPG/claude-quota-band.](https://github.com/SanjayPG/claude-quota-band.) - Claude Code mod: live usage-quota progress bars above your prompt.
- [sawzhang/hello-mod](https://github.com/sawzhang/hello-mod) - Demo minimal fungsi hook Claude Code: panel token/biaya real-time di atas…
- [servaes/cockpit](https://github.com/servaes/cockpit) - Cockpit Board dan mod Claude Code lainnya oleh André Servaes.
- [shaheershoaib/agent-warehouse](https://github.com/shaheershoaib/agent-warehouse) - agent-warehouse: a Claude Code mod by Shaheer Shoaib.
- [shaheershoaib/usage-meter](https://github.com/shaheershoaib/usage-meter) - usage-meter: a Claude Code mod by Shaheer Shoaib.
- [shelltime/claude-code-mods](https://github.com/shelltime/claude-code-mods) - Mod Claude Code (plugin hook fungsi) oleh ShellTime.
- [siller/supermod](https://github.com/siller/supermod) - Claude Code mod: Superpowers progress, context window and agents above the…
- [simplybychris/claude-code-mods](https://github.com/simplybychris/claude-code-mods) - Mod untuk Claude Code: Rec Mode, Cache Bar, Snake dan panel agen.
- [skryvets/claude-code-session-mod](https://github.com/skryvets/claude-code-session-mod) - Claude Code mod: coloured session info under the prompt - context, model…
- [soulrocha/Claude-code-hero-journey](https://github.com/soulrocha/Claude-code-hero-journey) - 🦀 Mod HUD RPG yang nyaman untuk Claude Code.
- [sstani-bgv/claude-crew](https://github.com/sstani-bgv/claude-crew) - Mod Claude Code: sidebar kepiting piksel untuk subagen.
- [StalicJi/my-mods](https://github.com/StalicJi/my-mods) - Marketplace mod Claude Code pribadi: clean-view, where-am-i, next-steps…
- [steven-ngle/blade-of-commits](https://github.com/steven-ngle/blade-of-commits) - Pesan commit sekali klik untuk Claude Code dengan Malenia pixel-art yang menari.
- [StevenGFX/claude-gh-actions](https://github.com/StevenGFX/claude-gh-actions) - Claude Code mod: GitHub Actions runs in a /ci pane, the status line and toasts.
- [stillgbx/still-mods](https://github.com/stillgbx/still-mods) - Claude code mods.
- [stylusnexus/claude-mods](https://github.com/stylusnexus/claude-mods)
- [Sunkanxx/Mods](https://github.com/Sunkanxx/Mods) - Claude Code mods — marketplace sunkanxx-mods.
- [Suyeo2025/claude-mods](https://github.com/Suyeo2025/claude-mods) - Claude Code mods: mini-bar HUD.
- [SyntacticFlow/claude-mods](https://github.com/SyntacticFlow/claude-mods) - Plugins for Claude Code.
- [systemNEO/claude-code-mods](https://github.com/systemNEO/claude-code-mods) - Mods for Claude Code: delete-guard.
- [Tanish-Dev/claude-usage-band](https://github.com/Tanish-Dev/claude-usage-band) - Mod Claude Code: lihat penggunaan paket Claude Anda.
- [tanwar-harsh/luff-crew-monitor](https://github.com/tanwar-harsh/luff-crew-monitor) - Mod Claude Code: panel kru langsung untuk setiap subagen.
- [tartinerlabs/claude-code-mods](https://github.com/tartinerlabs/claude-code-mods)
- [teambrilliant/claude-code-mods](https://github.com/teambrilliant/claude-code-mods)
- [TFoxik/claude-model-router](https://github.com/TFoxik/claude-model-router) - A Claude Code mod that picks the model and effort for each kind of work, and…
- [TheBabaYaga/claude-session-flow](https://github.com/TheBabaYaga/claude-session-flow) - Mod Claude Code yang menampilkan sesi saat ini dalam sebuah panel: setiap…
- [theishandubey/claude-mods](https://github.com/theishandubey/claude-mods) - Marketplace plugin Claude Code untuk mod: plugin function-hooks yang menggambar…
- [thickiran/claude-coaster-tycoon](https://github.com/thickiran/claude-coaster-tycoon) - 🎢 Claude builds you a RollerCoaster Tycoon-style theme park while it works.
- [tjanuki/claude-mod-agent-board](https://github.com/tjanuki/claude-mod-agent-board) - Claude Code mod: a docked pane showing the session.
- [tjanuki/claude-mod-context-meter](https://github.com/tjanuki/claude-mod-context-meter) - Claude Code mod: context-window fill in the status line and a hand-off reminder…
- [tommy5dollar/effort-router](https://github.com/tommy5dollar/effort-router) - Buat penggunaan Claude Code Anda bertahan hingga dua kali lebih lama.
- [Toptaab/token-garden](https://github.com/Toptaab/token-garden) - Mod Claude Code oleh Toptaab.
- [Tum4s/sprout](https://github.com/Tum4s/sprout) - Mod Claude Code: sebuah band dan panel yang melacak subagen Anda, beserta file…
- [tusharck/mods-for-claude](https://github.com/tusharck/mods-for-claude) - A curated catalogue of Claude Code mods, each with a copy-paste prompt that…
- [tyree88/tempered_plugins](https://github.com/tyree88/tempered_plugins) - Claude Code mods from Tempered Works: ship-state, timeline, limit-resume — plus…
- [VAlux/claude-session-progress](https://github.com/VAlux/claude-session-progress) - Mod Claude Code: pita kemajuan animasi dan ringkasan penyelesaian untuk tugas…
- [Vansitha/clawd-watch](https://github.com/Vansitha/clawd-watch) - Three small Claude Code mods: see when your subagents will finish, queue…
- [varunmoka7/layman](https://github.com/varunmoka7/layman) - Katakan &quot;Saya tersesat&quot; dan Claude akan menjelaskan kembali balasan terakhirnya…
- [varunmoka7/side-chat](https://github.com/varunmoka7/side-chat) - Ajukan pertanyaan sampingan kepada Claude di panel di sebelah pekerjaan Anda.
- [Victormartinsilva/MODS-CLAUDECODE](https://github.com/Victormartinsilva/MODS-CLAUDECODE) - Marketplace de mods do Claude Code com instalação em um passo e guia em vídeo…
- [vihrea1337/headroom](https://github.com/vihrea1337/headroom) - Rate-limit countdowns and a burn-rate forecast for Claude Code.
- [vinkdc/roclaude](https://github.com/vinkdc/roclaude) - Lapisan keamanan Roblox Studio untuk Claude Code: audit RemoteEvent, undo…
- [was865/usage-band](https://github.com/was865/usage-band) - Claude Code mod: context window, prompt cache hit rate and countdown, rate…
- [wipeer/claude-mods](https://github.com/wipeer/claude-mods) - Small quality-of-life mods for Claude Code.
- [wmaq/wmaq-claude-mods](https://github.com/wmaq/wmaq-claude-mods) - Claude Code mods: stage-toons, a workflow progress bar above the prompt with…
- [wolves/usage-line](https://github.com/wolves/usage-line) - Claude Code mod: usage, model, effort and advisor readout above the prompt.
- [wszaq/claude-mods](https://github.com/wszaq/claude-mods) - Plugin Claude Code kecil untuk alur kerja lokal yang lebih aman dan jelas.
- [xinhuagu/oh-my-claude-mods](https://github.com/xinhuagu/oh-my-claude-mods) - Mod untuk Claude Code. agent-crew: lihat subagen Anda bekerja sebagai kru…
- [YeonwooSung/my-claude-code-mods](https://github.com/YeonwooSung/my-claude-code-mods)
- [youngOman/pill-mods](https://github.com/youngOman/pill-mods) - Mod Claude Code: kapsul langkah berikutnya Tionghoa Tradisional, salin blok…
- [zexion7873/usage-band](https://github.com/zexion7873/usage-band) - Pita selalu aktif di atas prompt Claude Code: pengisian konteks dan jendela…
- [zh10only1/claude-code-mods](https://github.com/zh10only1/claude-code-mods) - Personal Claude Code mods (plugin marketplace).
- [zhuzhu0710/claude-mods](https://github.com/zhuzhu0710/claude-mods)
- [ziedgithub/claude-code-mods](https://github.com/ziedgithub/claude-code-mods)
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - Kumpulan pilihan sumber daya terbaik untuk agen-agen paling hebat, Claude Code…
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) - Plugin Claude Code yang menampilkan apa yang sedang terjadi — penggunaan…
- [sirmalloc/ccstatusline](https://github.com/sirmalloc/ccstatusline) - 🚀 Statusline yang indah dan sangat dapat disesuaikan untuk Claude Code CLI…
- [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) - Semua bagian system prompt Claude Code, 27 deskripsi alat bawaan, prompt…
- [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) - 45+ kiat untuk memaksimalkan Claude Code, dari dasar hingga tingkat lanjut…
- [op7418/guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill) - 🪧 Claude Code / skill Codex — buat carousel Xiaohongshu &amp; pasangan sampul…
- [Owloops/claude-powerline](https://github.com/Owloops/claude-powerline) - Beautiful vim-style powerline for Claude Code.
- [persiyanov/herdr-reviewr](https://github.com/persiyanov/herdr-reviewr) - Tinjau diff agen pengodean Anda di panel terminal dan kirim komentar baris…
- [uppinote20/claude-dashboard](https://github.com/uppinote20/claude-dashboard) - Plugin baris status komprehensif untuk Claude Code dengan penggunaan konteks…
- [stormzhang/token-tracker](https://github.com/stormzhang/token-tracker) - Pelacakan token lokal Claude Code &amp; Codex — bilah status.
- [starbaser/ccproxy](https://github.com/starbaser/ccproxy) - Buat mod untuk Claude Code: kaitkan permintaan apa pun, ubah respons apa pun…
- [NYCU-Chung/cc-statusline](https://github.com/NYCU-Chung/cc-statusline) - Dasbor baris status komprehensif untuk Claude Code — info sesi, bilah kuota…
- [gwittebolle/claude-carbon](https://github.com/gwittebolle/claude-carbon) - claude-carbon: lacak jejak karbon sesi Claude Code Anda.
- [AwesomeZun/CC-statusline](https://github.com/AwesomeZun/CC-statusline) - Statusline estetis untuk Claude Code oleh awesomejun.
- [fatihaydost/brand-identity-skill](https://github.com/fatihaydost/brand-identity-skill) - A Claude Code skill that designs a brand identity as one system: logo…
- [JohnnyVizz/claude-kit](https://github.com/JohnnyVizz/claude-kit) - Skill dan mod Claude Code publik.
- [escapeboy/claude-code-kit](https://github.com/escapeboy/claude-code-kit) - Skills, mod, subagen, hook, perintah garis miring, dan panduan untuk Claude…
- [mvalentsev/awesome-free-ai-coding](https://github.com/mvalentsev/awesome-free-ai-coding) - 📡 LLM APIs legal gratis &amp; agent coding — diperbarui sendiri, diverifikasi…
- [kylesnowschwartz/tail-claude-hud](https://github.com/kylesnowschwartz/tail-claude-hud) - Statusline terminal untuk sesi Claude Code.
- [arturogarrido/claudinho](https://github.com/arturogarrido/claudinho) - ⚽ Skor langsung football(soccer), jadwal pertandingan, dan klasemen untuk…
- [johncattrall/keymap-ai](https://github.com/johncattrall/keymap-ai) - Agent Skill yang mengubah agen coding Anda menjadi ahli firmware keyboard.
- [philoserf/claude-code-config](https://github.com/philoserf/claude-code-config) - Konfigurasi Claude Code pribadi yang diberi versi di dalam ~/.claude — agent…
- [ashafizullah/claude-code-muslim-mods](https://github.com/ashafizullah/claude-code-muslim-mods) - Waktu salat, tanggal Hijriah, adhkar, ayat harian, puasa sunnah, Ramadan…
- [moguiyu/dsh-tavily](https://github.com/moguiyu/dsh-tavily) - Tavily-powered optional search tool for DeepSeek Harness.
- [livlign/ccbit](https://github.com/livlign/ccbit) - Baris status yang menyadari sesi untuk Claude Code.
- [benz-ai-x/dsh-research-graph](https://github.com/benz-ai-x/dsh-research-graph) - DSH Research Graph · 研图 — plugin DeepSeek Harness untuk topik riset, kartu…
- [igdigitallab/cardloop](https://github.com/igdigitallab/cardloop) - Your AI dev team on your own server, steered from your phone.
- [pierrebelin/claude-code-toolkit](https://github.com/pierrebelin/claude-code-toolkit) - Perangkat Claude Code portabel untuk .NET DDD/Clean Architecture: agen TDD…
- [hoobnn/hoobnn-agent-mods](https://github.com/hoobnn/hoobnn-agent-mods) - Kumpulan plugin untuk Claude Code, pi, dan DeepSeek Harness: HUD bilah status…
- [jcdendrite/claude-config](https://github.com/jcdendrite/claude-config) - Konfigurasi global Claude Code yang portabel: skill khusus, hook PreToolUse…
- [mutlumehmet/claude-plugins](https://github.com/mutlumehmet/claude-plugins) - Plugin Claude Code yang saya gunakan setiap hari: skills dan mod, dirapikan…
- [34823/tg-pane](https://github.com/34823/tg-pane) - Telegram di dalam Claude Code: baca chat dan channel dalam sebuah pane…
- [cmfok/dsh-feishucard](https://github.com/cmfok/dsh-feishucard) - Jembatan DSH &lt;-&gt; Feishu (Lark), dikembangkan sendiri (bukan fork): kartu…
- [Dakaric/claude-code-statusline](https://github.com/Dakaric/claude-code-statusline) - Status line siap pakai untuk Claude Code: bilah jendela konteks, TTL cache…
- [darthmolen/hytale-claude-code-marketplace](https://github.com/darthmolen/hytale-claude-code-marketplace) - Marketplace untuk Plugin dan Skill Claude Code guna memfasilitasi mod game…
- [frsorrentino/fable-director](https://github.com/frsorrentino/fable-director) - Tata kelola token untuk Claude Code: model teratas mengarahkan, eksekusi…
- [hopp1395/cc-outline](https://github.com/hopp1395/cc-outline) - Penampil panel terpisah untuk Claude Code di Windows Terminal dan tmux: sesi…
- [jeancarlo-javier/claude-status-bar](https://github.com/jeancarlo-javier/claude-status-bar) - Live workflow-phase status line for Claude Code (Plan → Exec → Verify → Done)…
- [manson341349-beep/claude-desktop-mods](https://github.com/manson341349-beep/claude-desktop-mods) - Mod tidak resmi untuk tab Code Claude Desktop — usage-pet: pita penggunaan…
- [romnycristopher/claude-am-mods](https://github.com/romnycristopher/claude-am-mods) - Repositori untuk mod Awesome Media Claude Code.
- [rootstudioyaml/sprag](https://github.com/rootstudioyaml/sprag) - Pangkas pengeluaran token Claude Code &amp; Codex: merutekan lookup dan test run ke…
- [aquahitt/claude-code-limit-alerts](https://github.com/aquahitt/claude-code-limit-alerts) - Peringatan batas penggunaan untuk Claude Code: notifikasi macOS, peringatan…
- [fbincon/claude-code-statusline](https://github.com/fbincon/claude-code-statusline) - Status line Claude Code yang dapat dikonfigurasi untuk Linux, WSL, Windows, dan…
- [JairoTorregrosa/claude-statusline](https://github.com/JairoTorregrosa/claude-statusline) - Fast Rust statusline for Claude Code — payload-first, cached git, ~10ms renders.
- [JohnnyTh/claude-status-bar](https://github.com/JohnnyTh/claude-status-bar) - Statusline Code Claude dengan bilah konteks, sparkline token &amp; pelacak biaya.
- [jsh135790/claude-code-capsule-panel](https://github.com/jsh135790/claude-code-capsule-panel) - Dashboard penggunaan live untuk Claude Code — rincian konteks, hit cache…
- [kyllian330/claude-statusline](https://github.com/kyllian330/claude-statusline) - Menampilkan detail status utama Code Claude termasuk model, konteks, batas…
- [Ma1achy/claude-statusline](https://github.com/Ma1achy/claude-statusline) - status line Code Claude yang ramah dan dapat diutak-atik — bilah truecolor…
- [Obednal97/claude-statusline-kit](https://github.com/Obednal97/claude-statusline-kit) - Multi-row Claude Code status line: spend, context %, git, and active account…
- [QingqiShi/claude](https://github.com/QingqiShi/claude) - Personal ~/.claude for Claude Code: settings, global CLAUDE.md, hooks, status…
- [salvanya/claude_code_statusline](https://github.com/salvanya/claude_code_statusline) - Statusline dengan informasi berguna untuk claude code.
- [Screddyice/claude-code-harness](https://github.com/Screddyice/claude-code-harness) - Templat awal untuk mengatur ruang kerja Claude Code multi-perusahaan: templat…
- [tc3oliver/claude-team-kit](https://github.com/tc3oliver/claude-team-kit) - Tim agen native. Di bawah kendali. Batas pekerja yang ketat, visibilitas tim…
- [zach-source/claude-factory](https://github.com/zach-source/claude-factory) - Definable software factories for Claude Code on herdr: xstate station graphs, a…
- [andkirby/claude-statusline](https://github.com/andkirby/claude-statusline) - Statusline kustom untuk Claude Code — bilah konteks dengan persentase…
- [bunderlog/claude-plugins](https://github.com/bunderlog/claude-plugins) - Marketplace plugin Claude Code dengan baloo: keahlian, agen yang memverifikasi…
- [chrisns/claude-image-cli-mod](https://github.com/chrisns/claude-image-cli-mod) - Lihat gambar yang dicetak perintah (imgcat, gambar inline iTerm2) dalam…
- [ChristianVerghis/claude-statusline](https://github.com/ChristianVerghis/claude-statusline) - Baris status Claude Code: penggunaan konteks, bilah kuota 5 jam/7 hari, waktu…
- [ctfbio/claude-code-statusline](https://github.com/ctfbio/claude-code-statusline) - Statusline Claude Code tingkat profesional: durasi sesi, biaya multi-mata uang…
- [cvrt-gmbh/claude-statusline](https://github.com/cvrt-gmbh/claude-statusline) - Baris status yang memperhatikan langganan untuk Claude Code.
- [d3r3nic/claude-live-sessions](https://github.com/d3r3nic/claude-live-sessions) - A Claude Code plugin: a pane of the live Claude Code and Codex sessions on your…
- [diegorv/koko.claude-statusline](https://github.com/diegorv/koko.claude-statusline) - A rich terminal statusline for Claude Code — Bun + TypeScript, zero runtime…
- [duplonicus/claude-statusline](https://github.com/duplonicus/claude-statusline) - Baris status dua baris untuk Claude Code: konteks, batas laju dengan penanda…
- [ejklock/claude-mermaid-render](https://github.com/ejklock/claude-mermaid-render) - Plugin Claude Code yang menampilkan diagram Mermaid dengan indah dalam…
- [filtercoffeeway/claude-kit](https://github.com/filtercoffeeway/claude-kit) - Tools, skill, dan agent untuk Claude Code — dimulai dengan baris status yang…
- [Furkan-rgb/claude-config](https://github.com/Furkan-rgb/claude-config) - Claude Code global config: agents, skills, mods, settings.
- [Guidin9/claude-usage-footer](https://github.com/Guidin9/claude-usage-footer) - Plugin Claude Code: selalu lihat sisa batas penggunaan Claude 5 jam Anda di…
- [hardtomakeanadress/claude-code-deepseek-cost](https://github.com/hardtomakeanadress/claude-code-deepseek-cost) - Pengeluaran DeepSeek API yang sebenarnya untuk Claude Code: menetapkan ulang…
- [ihororlovskyi/claude-statusline](https://github.com/ihororlovskyi/claude-statusline) - Baris status Claude Code dengan baris panel agen.
- [izahamyatim/claude-plugin-fizzy](https://github.com/izahamyatim/claude-plugin-fizzy) - 🚀 Sinkronkan todo Claude ke Fizzy.do untuk visibilitas tim secara langsung…
- [izzatum/claude-code-cockpit](https://github.com/izzatum/claude-code-cockpit) - Plugin baris status Claude Code (cockpit): persentase konteks, biaya sesi, dan…
- [jv-k/claude-gauge](https://github.com/jv-k/claude-gauge) - A status line and token line for Claude Code: context, 5-hour and weekly usage…
- [Kimmihappy793/claude-status-line](https://github.com/Kimmihappy793/claude-status-line) - Tampilkan bilah status terperinci berkode warna untuk Claude Code yang…
- [konnichiwab/claude-code-config](https://github.com/konnichiwab/claude-code-config) - Menu pengaturan, baris status, dan konfigurasi Claude Code.
- [Larg0Winch/claude-label](https://github.com/Larg0Winch/claude-label) - Label per jendela yang dapat diedit di baris status Claude Code.
- [ldk00315-jpg/claude-code-voice-mod](https://github.com/ldk00315-jpg/claude-code-voice-mod) - Bicara dengan Claude Code melalui suara di Windows: Mod + pembantu menggunakan…
- [lucasmm96/claude-statusline](https://github.com/lucasmm96/claude-statusline) - Hook statusline Claude Code — melacak penggunaan token dan konteks di berbagai…
- [matthewjschultz/claude-statusline](https://github.com/matthewjschultz/claude-statusline) - Baris status Claude Code kustom dengan jendela konteks, pelacakan penggunaan…
- [melderan/claude-statusline-rust](https://github.com/melderan/claude-statusline-rust) - Baris status Rust yang cepat untuk Claude Code.
- [mgstegmaier/claude-plugins](https://github.com/mgstegmaier/claude-plugins) - home-grown, cage-free claude plugins, skills, mods, and more.
- [msinclair-sudo/claude-code-setup](https://github.com/msinclair-sudo/claude-code-setup) - Penginstal lingkungan Claude Code: skills, statusline, hooks, permissions, dan…
- [oshnilia/claude-plugins](https://github.com/oshnilia/claude-plugins) - Plugin dan mod Claude Code untuk memahami apa yang dilakukan Claude: format…
- [peaceinitiativemenhadenoil263/claude-status-bar](https://github.com/peaceinitiativemenhadenoil263/claude-status-bar) - Pantau status Claude Code dari bilah menu macOS dengan indikator waktu nyata…
- [pirncedark/afu-claude-statusline](https://github.com/pirncedark/afu-claude-statusline) - Bilah status multi-baris berwarna-warni untuk Claude Code.
- [rainyfei/claude-statusline-win](https://github.com/rainyfei/claude-statusline-win) - Baris status Claude Code untuk Windows (PowerShell): bilah penggunaan, hitung…
- [realkewal/claude-kit](https://github.com/realkewal/claude-kit) - Plugin Claude Code. Usage Bars menampilkan batas laju sesi dan mingguan Anda…
- [roy651/cc-plugins](https://github.com/roy651/cc-plugins) - Mod Bearings dan Glossary untuk Claude Code.
- [Rubio-Enterprises/claude-statusline](https://github.com/Rubio-Enterprises/claude-statusline) - Statusline Claude Code khusus (upstream: kamranahmedse/claude-statusline).
- [satoramoto/awesome-claude](https://github.com/satoramoto/awesome-claude) - Konfigurasi dan mod Claude Code, dengan kit komponen bersama, playground, dan…
- [SohamShirsat/claude-cockpit](https://github.com/SohamShirsat/claude-cockpit) - Dasbor kecil untuk Claude Code: persentase konteks, hitung mundur cache…
- [thaiquangquy/claude.me](https://github.com/thaiquangquy/claude.me) - Konfigurasi Claude Code portabel: CLAUDE.md, settings, statusline, skills.
- [thurtado1993/claude-cabina](https://github.com/thurtado1993/claude-cabina) - Cabina: a live session dashboard for the Claude Code Desktop side panel.
- [tichara1/ai.claude-status-panel](https://github.com/tichara1/ai.claude-status-panel) - Mod pro Claude Code: panel nad promptem s kontextem, limity, cenou, stavem…
- [Undone-drawknife974/claude-code-statusline](https://github.com/Undone-drawknife974/claude-code-statusline) - Lacak penggunaan konteks Claude Code, biaya sesi, dan reset batas laju dengan…
- [UtakataKyosui/utakata-cc-mod](https://github.com/UtakataKyosui/utakata-cc-mod) - Claude Code 用の mod 集 (goal-orchestrator: /goal をタスク分解して SubAgent に委譲させる).
- [vladimir-ks/ai-agile-claude-code-statusline](https://github.com/vladimir-ks/ai-agile-claude-code-statusline) - Real-time cost tracking and session monitoring statusline for Claude Code.
- [xinvxueyuan/cordis-plugin-secret](https://github.com/xinvxueyuan/cordis-plugin-secret) - Plugin Cordis / DeepSeek Harness — agen meminta rahasia kepada manusia dalam…
- [yacb2/claude-statusline](https://github.com/yacb2/claude-statusline) - Baris status Claude Code tiga baris: kedalaman konteks, batas laju lintas sesi…
- [YoniYon00/claude-feedback-rings](https://github.com/YoniYon00/claude-feedback-rings) - Context Rot Detector 2026 - Monitor Memori AI &amp; Batas Laju Proaktif untuk Agen…
- [zerofaultlabs/claude-statusline](https://github.com/zerofaultlabs/claude-statusline) - Baris status Claude Code: penggunaan konteks, batas laju, biaya, dan cache hit…
- [zhuyansen/awesome-claude-code-hooks](https://github.com/zhuyansen/awesome-claude-code-hooks) - Hook, subagen, dan statusline Claude Code: koleksi dan alat sumber terbuka…
- [zoo3323/claude-statusline](https://github.com/zoo3323/claude-statusline) - Baris status Claude Code — pengukur penggunaan Claude/Codex yang tetap aktif…
- [tronschell/statusline.sh](https://github.com/tronschell/statusline.sh) - A visual builder for Claude Code statuslines.
- [Magnus-Gille/tokenatlas](https://github.com/Magnus-Gille/tokenatlas) - Claude Code statusline showing real-time token usage and estimated energy…
- [ishuagrawal/clawdhouse](https://github.com/ishuagrawal/clawdhouse) - Mod untuk Claude Code: panel, pita, dan buddy yang dibangun di atas hook fungsi.
- [ashishsk93/baton-mods](https://github.com/ashishsk93/baton-mods) - Oper tugas antar sesi Claude Code Anda.
- [lahoramaker/mods-mcp](https://github.com/lahoramaker/mods-mcp) - Gunakan ini di server MCP untuk mengendalikan MODS, alat lintas platform…
- [pedrotspinola/lps-statusline](https://github.com/pedrotspinola/lps-statusline) - Statusline Claude Code kustom: model + tingkat usaha, kuota penggunaan native…
- [Rimcat-JA/translate-ck3-mods](https://github.com/Rimcat-JA/translate-ck3-mods) - Skill Codex dan Claude Code untuk menerjemahkan mod CK3 dengan LLM lokal.
- [sTomerG/agent-kit](https://github.com/sTomerG/agent-kit) - Mod open-source dan ekstensi lainnya untuk Claude Code.
- [charlie947/mod-maker](https://github.com/charlie947/mod-maker) - Mod Maker: temukan apa yang Anda minta kepada Claude Code berulang kali, dan…

</details>

<a id="dsh-cordis"></a>

## Ekosistem plugin DSH dan Cordis

DeepSeek Harness dan Cordis mencapai tempat yang sama dari arah yang berbeda: bagi keduanya, plugin adalah mekanisme mod, sehingga plugin di sana setara dengan mod di sini.

<details>
<summary>🧵 <b><a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b> · ⭐74280 · TypeScript · 👁️ observed · 0 天</summary>

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
| Bintang                  | **74280**  |
| Push terakhir            | 2026-10-10 |
| Pertama kali dicantumkan | 2026-10-04 |

🏷 `agentic-ai` · `agentic-framework` · `agentic-workflow` · `agents` · `ai-agents` · `ai-assistant` · `ai-skills` · `autonomous-agents`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/2ca82c9c9a7fca31.gif" width="100%" alt="ruvnet/ruflo animation"><br><sub>rekaman animasi</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/nexu-io/open-design">nexu-io/open-design</a></b> · ⭐100394 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Bintang                  | **100394** |
| Push terakhir            | 2026-10-10 |
| Pertama kali dicantumkan | 2026-10-04 |

🏷 `agent-skills` · `ai-design` · `byok` · `claude-code-for-design` · `claude-design` · `codex-design` · `coding-agents` · `cursor-design`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nexu-io--open-design/a1049df34322d3ce.png" width="100%" alt="nexu-io/open-design screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/tt-a1i/archify">tt-a1i/archify</a></b> · ⭐81639 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Bintang                  | **81639**  |
| Push terakhir            | 2026-10-10 |
| Pertama kali dicantumkan | 2026-10-04 |

🏷 `agent-skills` · `ai-agents` · `architecture-diagram` · `claude-code` · `claude-skills` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tt-a1i--archify/71b7d4b2427db202.png" width="100%" alt="tt-a1i/archify screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/morluto/rea">morluto/rea</a></b> · ⭐70094 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Bintang                  | **70094**  |
| Push terakhir            | 2026-10-10 |
| Pertama kali dicantumkan | 2026-10-05 |

🏷 `agent-skills` · `ai-agents` · `binary-analysis` · `claude-code` · `cli` · `codex` · `cordis` · `ctf`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--rea/f46ca8b1518ae39f.png" width="100%" alt="morluto/rea screenshot"></td>
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
| Push terakhir            | 2026-10-10 |
| Pertama kali dicantumkan | 2026-10-06 |

🏷 `agent` · `agent-framework` · `ai-agent` · `ai-coding` · `cli` · `coding-agent` · `deepseek` · `developer-tools`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/anywhere-labs/dsh-desktop">anywhere-labs/dsh-desktop</a></b> · ⭐30358 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Bintang                  | **30358**  |
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
<summary>🧵 <b><a href="https://github.com/titanwings/distilly">titanwings/distilly</a></b> · ⭐25470 · Python · 🔎 inferred · 18 天</summary>

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
| Bintang                  | **25470**  |
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
<summary>🧵 <b><a href="https://github.com/cordiverse/cordis">cordiverse/cordis</a></b> · ⭐9112 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

Meta-Framework Komposabilitas Spasiotemporal

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | TypeScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **9112**   |
| Push terakhir            | 2026-10-10 |
| Pertama kali dicantumkan | 2026-10-09 |

🏷 `effect` · `framework` · `nodejs` · `plugin`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/zhu1090093659/dsh-web">zhu1090093659/dsh-web</a></b> · ⭐8594 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Bintang                  | **8594**   |
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
<summary>🧵 <b><a href="https://github.com/ccch1mneyyy/dsh-TUI">ccch1mneyyy/dsh-TUI</a></b> · ⭐4266 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Bintang                  | **4266**   |
| Push terakhir            | 2026-10-10 |
| Pertama kali dicantumkan | 2026-10-10 |

🏷 `claude-code` · `coding-agent` · `deepseek` · `deepseek-harness` · `dsh-plugin` · `ink` · `react` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ccch1mneyyy--dsh-tui/18fd45f8f1eaca04.png" width="100%" alt="ccch1mneyyy/dsh-TUI screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-tauri/deepseek-harness-desktop">dsh-tauri/deepseek-harness-desktop</a></b> · ⭐3162 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

DeepSeek Harness Tauri versi desktop | Installer hanya 8mb, tanpa penyiapan lingkungan, plugin preset, Windows / macOS / Linux.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | TypeScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **3162**   |
| Push terakhir            | 2026-10-10 |
| Pertama kali dicantumkan | 2026-10-10 |

🏷 `deepseek` · `deepseek-harness` · `desktop` · `dsh` · `dsh-desktop` · `dsh-plugin` · `tauri`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dsh-tauri--deepseek-harness-desktop/f281725e73da1059.png" width="100%" alt="dsh-tauri/deepseek-harness-desktop screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/kenryu42/cc-safety-net">kenryu42/cc-safety-net</a></b> · ⭐1583 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

Pelindung sebelum eksekusi untuk agen pengodean AI. Memblokir perintah Git dan sistem berkas yang merusak, serta upaya umum untuk mengakses berkas sensitif, sebelum panggilan alat dijalankan. Mendukung Amp Code, Antigravity CLI, Claude Code, Codex, Cursor, DeepSeek Harness, Devin CLI, GitHub Copilot CLI, Grok Build, Hermes Agent, Kimi Code, OpenClaw, OpenCode, dan Pi.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | TypeScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **1583**   |
| Push terakhir            | 2026-10-10 |
| Pertama kali dicantumkan | 2026-10-04 |

🏷 `ai-agents` · `ai-safety` · `antigravity` · `claude` · `claude-code` · `claude-code-plugin` · `cli` · `codex`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/vshulcz/deja-vu">vshulcz/deja-vu</a></b> · ⭐1167 · Go · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

Memory for Claude Code, Codex, Cursor and 38 more coding agents, built from the session history already on your disk. Local search, MCP and hooks, no LLM, one Go binary.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | Go                                                                                            |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **1167**   |
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
<summary>🧵 <b><a href="https://github.com/agentrq/agentrq">agentrq/agentrq</a></b> · ⭐1139 · Go · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

AgentRQ: Human-in-loop realtime conversational task manager for AI Agents. Self-hosted! Control your own agents from wherever you want Mobile, Web, Desktop. Designed to work well with your own Claude subscriptions and any harness with ACP support.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | Go                                                                                            |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **1139**   |
| Push terakhir            | 2026-10-10 |
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `acp-client` · `acp-gateway` · `agentic-ai` · `agentic-workflow` · `agents` · `ai-memory` · `claude-code` · `claude-plugin`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/agentrq--agentrq/71791429350e448f.png" width="100%" alt="agentrq/agentrq screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/agentrq--agentrq/e4115ab2a9de3317.gif" width="100%" alt="agentrq/agentrq animation"><br><sub>rekaman animasi</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/LivXue/dsh-plugin-shop">LivXue/dsh-plugin-shop</a></b> · ⭐1007 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Bintang                  | **1007**   |
| Push terakhir            | 2026-10-10 |
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `agent` · `deepseek` · `deepseek-harness` · `deepseek-harness-plugin` · `dsh` · `dsh-plugin` · `harness`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/livxue--dsh-plugin-shop/0cd59c71bcc6f86e.png" width="100%" alt="LivXue/dsh-plugin-shop screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/myYangyunfan/dsh_desktop">myYangyunfan/dsh_desktop</a></b> · ⭐702 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Bintang                  | **702**    |
| Push terakhir            | 2026-10-10 |
| Pertama kali dicantumkan | 2026-10-10 |

🏷 `ai-agent` · `cordis` · `deepseek` · `deepseek-harness` · `desktop` · `desktop-app` · `dsh` · `dsh-desktop`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/myyangyunfan--dsh_desktop/822cff4e94634530.png" width="100%" alt="myYangyunfan/dsh_desktop screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/vibeinging/dsh-desktop">vibeinging/dsh-desktop</a></b> · ⭐593 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

DeepSeek Harness Desktop App: a local AI desktop workspace for DSH Sessions, projects, files, web research, plugins, and Office artifacts.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | JavaScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **593**    |
| Push terakhir            | 2026-10-10 |
| Pertama kali dicantumkan | 2026-10-11 |

🏷 `agentic-workflows` · `ai-agent` · `ai-workbench` · `data-analysis` · `deepseek-harness` · `desktop-app` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vibeinging--dsh-desktop/ccbf15d3a2c42437.png" width="100%" alt="vibeinging/dsh-desktop screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/cv-superding/dsh-deepseek-web-login">cv-superding/dsh-deepseek-web-login</a></b> · ⭐247 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

Plugin DSH (DeepSeek Harness) tidak resmi: gunakan model web chat.deepseek.com sebagai penyedia LLM—pengambilan login browser, pemecahan PoW, streaming SSE, dan panggilan alat berbasis prompting.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | JavaScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **247**    |
| Push terakhir            | 2026-10-10 |
| Pertama kali dicantumkan | 2026-10-09 |

🏷 `browser-automation` · `cordis` · `cordis-plugin` · `deepseek` · `deepseek-harness` · `dsh` · `llm-provider`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/cv-superding--dsh-deepseek-web-login/b95392c45786ce03.png" width="100%" alt="cv-superding/dsh-deepseek-web-login screenshot"></td>
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
| Push terakhir            | 2026-10-10 |
| Pertama kali dicantumkan | 2026-10-10 |

🏷 `context-migration` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `preset-migration` · `session-migration`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/totoro-qaq--dsh-plugin-bridge/568de849cd2e9608.png" width="100%" alt="Totoro-qaq/dsh-plugin-bridge screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/totoro-qaq--dsh-plugin-bridge/b4a12cab0ba15f06.gif" width="100%" alt="Totoro-qaq/dsh-plugin-bridge animation"><br><sub>rekaman animasi</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/FeatherHunter/dsh-mattpocock-skills-deck">FeatherHunter/dsh-mattpocock-skills-deck</a></b> · ⭐130 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

Instalasi sudah menyertakan 27 keterampilan rekayasa dan produktivitas dari mattpocock/skills v1.3.1, tanpa perlu memasang keterampilan secara manual. Plugin ini dibuat dengan 40 miliar token, memberikan efisiensi pengembangan 10 kali lipat di atas keterampilan asli, serta membantu pemula menguasai rangkaian keterampilan ini lebih cepat. Dukungan penuh untuk issue GitHub; Markdown masih dalam versi pratinjau; GitLab belum didukung. Terima kasih atas penggunaan dan dukungan Anda 💗

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | JavaScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **130**    |
| Push terakhir            | 2026-10-10 |
| Pertama kali dicantumkan | 2026-10-10 |

🏷 `agent` · `ai` · `claude` · `deepseek-harness` · `dsh` · `dsh-better-sidebar` · `dsh-plugin` · `github-issues`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/featherhunter--dsh-mattpocock-skills-deck/c4bd78003446c161.png" width="100%" alt="FeatherHunter/dsh-mattpocock-skills-deck screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Nwflower/dsh-claude-style">Nwflower/dsh-claude-style</a></b> · ⭐127 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Bintang                  | **127**    |
| Push terakhir            | 2026-10-10 |
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
<summary>🧵 <b><a href="https://github.com/youdotcom-oss/agent-skills">youdotcom-oss/agent-skills</a></b> · ⭐87 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

Skill dan plugin You.com untuk penelusuran web, ekstraksi konten, riset, keuangan, dan penemuan integrasi, yang membantu agen AI membangun dengan konteks web terkini.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | TypeScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **87**     |
| Push terakhir            | 2026-10-10 |
| Pertama kali dicantumkan | 2026-10-10 |

🏷 `agent-plugins` · `agent-skills` · `ai-agents` · `claude-code` · `codex` · `cordis` · `cursor` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/youdotcom-oss--agent-skills/894c769a60cbc23c.png" width="100%" alt="youdotcom-oss/agent-skills screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/EricWang1358/dsh-web-studyhub">EricWang1358/dsh-web-studyhub</a></b> · ⭐85 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

StudyHub: plugin DeepSeek Harness (DSH) yang mengubah materi Anda sendiri menjadi pertanyaan dan tinjauan berjarak · Plugin belajar DSH yang mengubah materi sendiri menjadi soal dan pengulangan berjarak

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | JavaScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **85**     |
| Push terakhir            | 2026-10-10 |
| Pertama kali dicantumkan | 2026-10-10 |

🏷 `dsh` · `dsh-plugin` · `education` · `flashcards` · `spaced-repetition` · `study`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ericwang1358--dsh-web-studyhub/1e4a97948bc59f9d.jpg" width="100%" alt="EricWang1358/dsh-web-studyhub screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Sev7eEn7/dsh-sieve">Sev7eEn7/dsh-sieve</a></b> · ⭐72 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

dsh-sieve: plugin rekayasa konteks dan optimasi token untuk DeepSeek Harness (DSH) — penyaringan keluaran alat, pemangkasan konteks, pengungkapan keterampilan progresif. Payload 36% lebih kecil dalam pemutaran ulang offline. Plugin pengelolaan konteks dan pengoptimalan token DSH untuk menghemat penggunaan.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | TypeScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **72**     |
| Push terakhir            | 2026-10-10 |
| Pertama kali dicantumkan | 2026-10-10 |

🏷 `agent-tools` · `ai-agent` · `ai-coding` · `coding-agent` · `context-engineering` · `context-management` · `context-pruning` · `context-window`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/sev7een7--dsh-sieve/eab2b3c8b1588637.webp" width="100%" alt="Sev7eEn7/dsh-sieve screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ZASENJC/dsh-plugins-store">ZASENJC/dsh-plugins-store</a></b> · ⭐69 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

Marketplace yang secara otomatis mengklasifikasikan, mengkurasi, dan memvalidasi plugin komunitas DeepSeek-Harness. Secara otomatis mengategorikan, mengkurasi, dan memvalidasi marketplace plugin komunitas DeepSeek-Harness.

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
| Push terakhir            | 2026-10-10 |
| Pertama kali dicantumkan | 2026-10-10 |

🏷 `agent-tools` · `awesome-list` · `community-project` · `deepseek-harness` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zasenjc--dsh-plugins-store/e83b24d43eca5912.png" width="100%" alt="ZASENJC/dsh-plugins-store screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/whyihaveyou/dsh-suite">whyihaveyou/dsh-suite</a></b> · ⭐57 · HTML · 🔎 inferred · 0 天</summary>

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
| Bintang                  | **57**     |
| Push terakhir            | 2026-10-10 |
| Pertama kali dicantumkan | 2026-10-06 |

🏷 `agent-framework` · `awesome-list` · `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/whyihaveyou--dsh-suite/e9daf3bb6313ff1b.png" width="100%" alt="whyihaveyou/dsh-suite screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/NekroAI/nekro-nxt">NekroAI/nekro-nxt</a></b> · ⭐27 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Bintang                  | **27**     |
| Push terakhir            | 2026-10-10 |
| Pertama kali dicantumkan | 2026-10-10 |

🏷 `ai-agents` · `cordis` · `deepseek-harness` · `desktop-app` · `docker` · `dsh` · `dsh-plugin` · `electron`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nekroai--nekro-nxt/7c9f9f2e5bc195f1.png" width="100%" alt="NekroAI/nekro-nxt screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/zp-home/dsh-recommend">zp-home/dsh-recommend</a></b> · ⭐22 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

Peringkat dan rekomendasi transparan ekosistem plugin DSH: secara otomatis mengambil topik dsh-plugin setiap hari + model penilaian publik + plugin peringkat/rekomendasi dan situs statis

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | JavaScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **22**     |
| Push terakhir            | 2026-10-10 |
| Pertama kali dicantumkan | 2026-10-10 |

🏷 `deepseek-harness` · `dsh-plugin` · `plugin` · `rankings` · `recommendations`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zp-home--dsh-recommend/fbc10141cf0df5b3.png" width="100%" alt="zp-home/dsh-recommend screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Wenaixi/dsh-superpower">Wenaixi/dsh-superpower</a></b> · ⭐21 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

Plugin DeepSeek Harness: 15 keterampilan rekayasa obra/superpowers, deskripsi dwibahasa, dan sakelar per keterampilan | Plugin DeepSeek Harness: 15 keterampilan disiplin rekayasa obra/superpowers, deskripsi keterampilan dapat dialihkan bebas antara bahasa Mandarin dan Inggris, serta setiap keterampilan dapat diaktifkan atau dinonaktifkan secara bebas

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | JavaScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **21**     |
| Push terakhir            | 2026-10-10 |
| Pertama kali dicantumkan | 2026-10-10 |

🏷 `ai-agent` · `brainstorming` · `chinese` · `code-review` · `cordis` · `debugging` · `deepseek` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/wenaixi--dsh-superpower/72fd369dacf071c0.png" width="100%" alt="Wenaixi/dsh-superpower screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Imzl-zl/dsh-mcp-manager-ui">Imzl-zl/dsh-mcp-manager-ui</a></b> · ⭐20 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

UI manajemen server MCP untuk DeepSeek Harness Web — panel mengambang, impor JSON, dan persistensi berbasis profil.

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
| Push terakhir            | 2026-10-10 |
| Pertama kali dicantumkan | 2026-10-10 |

🏷 `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `mcp`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/imzl-zl--dsh-mcp-manager-ui/344d069db6cf421d.png" width="100%" alt="Imzl-zl/dsh-mcp-manager-ui screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/liustack/pptwise">liustack/pptwise</a></b> · ⭐19 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

PowerPoint sungguhan, bukan HTML. Beri tahu AI Anda apa yang harus dibahas dan pptwise akan membuat deck yang dapat diedit di komputer Anda sendiri. Agent skill + plugin DSH, tanpa akun dan tanpa kunci API untuk merender. | PPT sungguhan, bukan HTML. Beri tahu AI apa yang ingin dibahas, dan pptwise akan membuat PPT yang dapat diedit di komputer Anda sendiri. Agent skill + plugin DSH, tanpa pendaftaran, rendering tanpa API key.

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | TypeScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **19**     |
| Push terakhir            | 2026-10-10 |
| Pertama kali dicantumkan | 2026-10-04 |

🏷 `agent-skill` · `agent-skills` · `ai-agent` · `claude-code` · `claude-skills` · `codex` · `cordis` · `deck-generation`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/liustack--pptwise/e6f193d6fc2ea355.png" width="100%" alt="liustack/pptwise screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Wenaixi/dsh-ponytail">Wenaixi/dsh-ponytail</a></b> · ⭐18 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

Plugin DeepSeek Harness: mode senior malas DietrichGebert/ponytail dan port tangga 7 tingkat, 6 keterampilan dengan deskripsi dwibahasa dan sakelar per keterampilan, tanpa alat, tanpa cache miss | Plugin DeepSeek Harness: port sempurna mode senior malas dan tangga tujuh tingkat DietrichGebert/ponytail, deskripsi 6 keterampilan dapat dialihkan bebas antara dua bahasa, setiap keterampilan memiliki sakelar sendiri, tanpa registrasi alat, dan tanpa kerusakan cache di semua skenario

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | JavaScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **18**     |
| Push terakhir            | 2026-10-10 |
| Pertama kali dicantumkan | 2026-10-10 |

🏷 `agent-skills` · `ai-agents` · `claude-code` · `code-review` · `cordis` · `cursor` · `deepseek` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/wenaixi--dsh-ponytail/ffd031e53f39269a.png" width="100%" alt="Wenaixi/dsh-ponytail screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/KannaKuron/dsh-better-workspace">KannaKuron/dsh-better-workspace</a></b> · ⭐17 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Ringkasan

Plugin web DSH: pohon workspace hierarkis untuk sidebar — judul yang berisi / dikelompokkan ke folder virtual; alur tambah-workspace mendapat popup grup induk

##### 📌 Fakta dasar

| Bidang   | Nilai                                                                                         |
| -------- | --------------------------------------------------------------------------------------------- |
| Kategori | `Ekosistem plugin DSH dan Cordis`                                                             |
| Bukti    | `menyatakan adanya mod, plugin, atau hook, tetapi tidak menyebut mod surface secara spesifik` |
| Bahasa   | JavaScript                                                                                    |

##### 📊 Data

| Metrik                   | Nilai      |
| ------------------------ | ---------- |
| Bintang                  | **17**     |
| Push terakhir            | 2026-10-10 |
| Pertama kali dicantumkan | 2026-10-10 |

🏷 `cordis` · `deepseek` · `deepseek-harness` · `dsh` · `dsh-plugin` · `sidebar` · `tree` · `workspace`

---

<table><tr><th align="center" width="50%">🖼 Gambar</th><th align="center" width="50%">🎬 Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/kannakuron--dsh-better-workspace/83cddff440dfe49a.png" width="100%" alt="KannaKuron/dsh-better-workspace screenshot"></td>
<td align="center" valign="top"><sub>tidak ada media yang dipublikasikan</sub></td>
</tr></table>

</details>

<details>
<summary><b>Lainnya dalam kategori ini</b> <sub>· 63</sub></summary>

- [hashgraph-online/awesome-ai-plugins](https://github.com/hashgraph-online/awesome-ai-plugins) - Daftar pilihan plugin AI terbaik yang luar biasa untuk asisten AI termasuk…
- [bruc3van/awesome-dsh-plugin](https://github.com/bruc3van/awesome-dsh-plugin) - 30 秒找到真正适合你的 DeepSeek Harness插件。每天自动抓取 GitHub 上的 `dsh-plugin`…
- [imsai-sh/awesome-deepseek-harness-plugins](https://github.com/imsai-sh/awesome-deepseek-harness-plugins) - DeepSeek Harness plugin store, marketplace and hub — 11,000+ dsh plugins with…
- [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) - Pasar plugin DSH / DSH Plugin Marketplace: jelajahi, instal, dan perbarui semua…
- [flymysql/dsh-remote](https://github.com/flymysql/dsh-remote) - Remote-work assistant for DeepSeek Harness (DSH): connect SSH.
- [morluto/flameox](https://github.com/morluto/flameox) - Runtime evidence that helps agents trace, profile, and burn down hotspots in…
- [Noob-stupid/dsh-plugin-gating-hub](https://github.com/Noob-stupid/dsh-plugin-gating-hub) - DSH plugin - framework upgrade safety &amp; plugin gating: contract pre-check…
- [arcships/rutis](https://github.com/arcships/rutis) - Runtime plugin untuk program yang terus berjalan — inti Rust, plugin TypeScript…
- [like-study1/Oh-My-DSH](https://github.com/like-study1/Oh-My-DSH) - 🐳 Komunitas agregasi plugin DeepSeek Harness — sinkronisasi otomatis ekosistem…
- [mrRisega/dsh-remote](https://github.com/mrRisega/dsh-remote) - 公网远程控制 DeepSeek Harness.
- [adamkhalile/luau-docs-oracle](https://github.com/adamkhalile/luau-docs-oracle) - Best Roblox Luau Bug Checker and API Verifier 2026 DevForum MCP Tool.
- [kejixiaoliang/awesome-dsh-plugins](https://github.com/kejixiaoliang/awesome-dsh-plugins) - Direktori pilihan plugin DeepSeek Harness (DSH) — lebih dari 280 plugin…
- [Cerbur/clutch-dsh](https://github.com/Cerbur/clutch-dsh) - Open-source DSH plugins for DeepSeek Harness：Git Worktree session…
- [KannaKuron/dsh-gitbash-shell](https://github.com/KannaKuron/dsh-gitbash-shell) - DSH plugin: Git Bash shell for all agent modes on Windows.
- [Vncntvx/dsh-zotero](https://github.com/Vncntvx/dsh-zotero) - Toolkit Zotero untuk DeepSeek harness;
- [maxwell-feng/dsh-tinyfish-search](https://github.com/maxwell-feng/dsh-tinyfish-search) - TinyFish-backed web search provider for DeepSeek Harness (ctx.web) — 将内置…
- [Lixiaoyiao/deepseek-harness-action](https://github.com/Lixiaoyiao/deepseek-harness-action) - Action GitHub komunitas untuk DeepSeek Harness — AI Code Review · Diagnosis CI…
- [StvLi/dsh-ros2](https://github.com/StvLi/dsh-ros2) - The Deepseek Harness ROS 2 plugin can be used to efficiently diagnose issues…
- [siweina/dsh-novel-writer](https://github.com/siweina/dsh-novel-writer) - Workbench penulisan lokal untuk penulis web novel berbahasa Mandarin (19 alat)…
- [awesome-deepseekharness/awesome-deepseek-harness](https://github.com/awesome-deepseekharness/awesome-deepseek-harness) - Plugin, alat, skill, dan sumber belajar DeepSeek Harness (dsh) yang dikurasi…
- [YELEBAI/dsh-plugin-marketplace](https://github.com/YELEBAI/dsh-plugin-marketplace) - Verified plugin marketplace and autonomous registry for DeepSeek Harness.
- [dshworks/awesome-dsh-plugins](https://github.com/dshworks/awesome-dsh-plugins) - Spam-filtered, open-data registry of DeepSeek Harness (dsh) plugins, bundles…
- [miuzel/dsh-graph](https://github.com/miuzel/dsh-graph) - 把工作组织成目标看板的 DeepSeek Harness (dsh) 插件：目标 / 判据 / 上下文卡片 / 执行 attempt…
- [Ianzhyh/workbuddy-to-dsh](https://github.com/Ianzhyh/workbuddy-to-dsh) - Mengubah model yang sudah login di desktop WorkBuddy lokal.
- [PerryLink/dsh-test-drive](https://github.com/PerryLink/dsh-test-drive) - Penggerak pengujian instalasi dan smoke test terisolasi untuk plugin DeepSeek…
- [wycto/dsh-dock](https://github.com/wycto/dsh-dock) - dsh-dock · Plugin dock fungsi DeepSeek Harness: satu panel untuk…
- [YangShen-SWE/dsh-plugin-simple-pet](https://github.com/YangShen-SWE/dsh-plugin-simple-pet) - Windows desktop pet with DeepSeek billing, Codex subscription quotas, opt-in…
- [MicroMilo/upstream-radar](https://github.com/MicroMilo/upstream-radar) - Pengujian kompatibilitas yang selalu aktif untuk plugin DeepSeek Harness: rilis…
- [gezi-wen/sage-mem](https://github.com/gezi-wen/sage-mem) - File-based cross-session memory for DeepSeek Harness (DSH) — every memory is a…
- [BotHarness/DeepSeekBot](https://github.com/BotHarness/DeepSeekBot) - DeepSeekBot: alternatif GrokBot open-source, dibangun di atas DeepSeek Harness…
- [dsh-pub/dsh-pub](https://github.com/dsh-pub/dsh-pub) - The bilingual, source-backed registry and installer for the DeepSeek Harness…
- [Icather/dsh-clean-desktop-shell](https://github.com/Icather/dsh-clean-desktop-shell) - DSH 纯净桌面壳：双击像普通软件一样一键启动，后端活性实时监测 + 托盘快捷启停，零视觉改造.
- [unStone/dsh-xray](https://github.com/unStone/dsh-xray) - X-ray untuk plugin DeepSeek Harness: kapabilitas yang dideklarasikan…
- [bonerush/dsh-obsidian-mem](https://github.com/bonerush/dsh-obsidian-mem) - Plugin host DeepSeek Harness yang menyimpan dokumen proyek dan memori jangka…
- [chnjames/dsh-plugin-market](https://github.com/chnjames/dsh-plugin-market) - DSH 插件市场 — DeepSeek Harness 设置内一键安装社区插件，并提供公开目录站（浏览 / 复制安装命令）.
- [cyanseek/dsh-landscape](https://github.com/cyanseek/dsh-landscape) - Agent-first DeepSeek Harness plugin intelligence: verify existing plugins…
- [Exagone313/dsh-podman](https://github.com/Exagone313/dsh-podman) - Podman-backed execution for DeepSeek Harness (dsh).
- [victorwads/dsh-live-voice](https://github.com/victorwads/dsh-live-voice) - Local-first voice conversations for DSH.
- [KannaKuron/dsh-ide-git](https://github.com/KannaKuron/dsh-ide-git) - Plugin DSH: jendela tool Git setara IDE sebagai tab native dsh-better-sidebar…
- [KannaKuron/dsh-ptc-cordis-preset](https://github.com/KannaKuron/dsh-ptc-cordis-preset) - PTC 模式基础上的创造模式:DSH 插件,合成 Code Mode 工具编排 + 自引用 Cordis 工具与 preset 创作指导,物化为…
- [xbzbing/dsh-git-panel](https://github.com/xbzbing/dsh-git-panel) - DSH 插件：Web GUI 里的 IDE 风格 Git 面板——分支/提交历史总览、变更提交与 amend、文件浏览、代码与图片新旧差异对照、输入框分支标记…
- [ywsldxk/dsh-plugin-stars](https://github.com/ywsldxk/dsh-plugin-stars) - DeepSeek Harness (DSH) plugin leaderboard &amp; directory｜DeepSeek…
- [cherrchen/dsh-plugin-multi-root-workspace](https://github.com/cherrchen/dsh-plugin-multi-root-workspace) - 多文件夹 workspace：让 DSH（DeepSeek Harness）的 Agent 不只能读写主目录，还能同时读写你添加的其他文件夹.
- [godv61/dsh-task-engine](https://github.com/godv61/dsh-task-engine) - Plugin alur kerja engineering untuk DeepSeek Harness: tahap tugas, catatan…
- [liceses/dsh-cosplay](https://github.com/liceses/dsh-cosplay) - DSH 角色扮演插件：角色卡（系统提示词注入 + 用户提示词改写）、可分享的单文件卡包、复刻原版 UI 的角色页签与首轮选角 chip.
- [majiayu000/dsh-plugin-registry](https://github.com/majiayu000/dsh-plugin-registry) - Searchable DeepSeek Harness plugin registry with curated listings and…
- [PerryLink/dsh-plugin-doctor](https://github.com/PerryLink/dsh-plugin-doctor) - Standar verifikasi tanpa dependensi untuk plugin DeepSeek Harness (dsh)…
- [TheYoungChen/dsh-plugin-market](https://github.com/TheYoungChen/dsh-plugin-market) - Marketplace plugin DeepSeek Harness - jelajahi, cari &amp; instal plugin topik…
- [viztor/dsh-opencode-patch](https://github.com/viztor/dsh-opencode-patch) - OpenCode di DeepSeek Harness — plugin DSH yang menjaga OpenCode Zen + model…
- [AI-Scarlett/DSH-Store](https://github.com/AI-Scarlett/DSH-Store) - DSH STORE — marketplace plugin pihak ketiga dan pengelola siklus hidup dengan…
- [Atelyx/Atelyx](https://github.com/Atelyx/Atelyx) - Atelyx adalah meja kerja desktop yang dapat diperluas dan berpusat pada…
- [chenkai2/dsh-daemon](https://github.com/chenkai2/dsh-daemon) - Daemon dsh: mendaftarkan server web DeepSeek Harness (dsh web) sebagai layanan…
- [fangwen9527/dsh-composer-ux](https://github.com/fangwen9527/dsh-composer-ux) - Plugin pengalaman input DSH Web: pergantian tombol kirim/baris baru, menu klik…
- [grloper/dsh-claude-oauth](https://github.com/grloper/dsh-claude-oauth) - Claude Pro/Max OAuth model provider for DeepSeek Harness with Google/Gmail…
- [iasiv5/dsh-skip-browser-auth](https://github.com/iasiv5/dsh-skip-browser-auth) - DSH 插件：（Web Profile 专用）自动跳过 BrowserAuth，访问 Web 地址即可直接使用，无需每次复制启动 URL 中的随机 Token…
- [Mzy123l/dsh-plugin-remote-access](https://github.com/Mzy123l/dsh-plugin-remote-access) - Menyediakan pintu masuk akses jarak jauh dengan 「segmen jaringan terbatas +…
- [tianyagk/dsh-tradewatcher](https://github.com/tianyagk/dsh-tradewatcher) - DeepSeek Harness (DSH) web plugin: 盯盘 market-dashboard sidebar tab — three…
- [argszero/cordis-plugin-sandbox-grant-advisor](https://github.com/argszero/cordis-plugin-sandbox-grant-advisor) - Plugin Harness DeepSeek: mengubah kegagalan penyediaan ACL sandbox Windows…
- [argszero/cordis-plugin-empty-response-retry](https://github.com/argszero/cordis-plugin-empty-response-retry) - Membuat upaya model kosong tanpa atribusi dapat dicoba ulang, untuk satu celah…
- [validation-engineering/cordis-verus](https://github.com/validation-engineering/cordis-verus) - Runtime plugin Rust dengan kernel siklus hidup yang diverifikasi Verus dan…
- [helloHupc/dsh-plugin-hub](https://github.com/helloHupc/dsh-plugin-hub) - DSH 插件聚合站:全网 DeepSeek Harness 插件聚合检索,多源自动去重分类,每小时刷新 |…
- [HaydenSmith1121/dsh-plugins](https://github.com/HaydenSmith1121/dsh-plugins) - DeepSeek Harness (dsh) 插件市场 —— 目录（一个插件一个配置文件）+ 可视化面板 + 一键安装；插件本体在…
- [SCP-008-1/dshop](https://github.com/SCP-008-1/dshop) - Toko plugin dsh - penemuan otomatis dan sinkronisasi terjadwal setiap jam…

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50003222">What the Hell Are Claude Mods? [video]</a></b> · ⭐4 · 👁️ observed · 2 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49999983">A Claude Code mod plays MIDI music when it works</a></b> · ⭐3 · 👁️ observed · 2 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49971594">Terminal Steps: A Claude mod for a daily step goal, synced from Apple Health</a></b> · ⭐3 · 👁️ observed · 4 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49940121">Getting started with Claude Code mods</a></b> · ⭐2 · 👁️ observed · 7 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49927599">Pi-autoresearch ported to Claude Code 1:1 using the new mods API</a></b> · ⭐2 · 👁️ observed · 8 天</summary>

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
| TypeScript | 396   | `anthropics/claude-code`, `anthropics/claude-code-action`, `PerryLink/dsh-mcp-panel`                          |
| JavaScript | 87    | `MIHassan3/DSH-Launcher`, `karanb192/awesome-claude-code-mods`, `karanb192/claude-code-mods`                  |
| Python     | 43    | `anthropics/claude-agent-sdk-python`, `anthropics/claude-code-security-review`, `alexgreensh/token-optimizer` |
| Shell      | 30    | `anthropics/claude-agent-sdk-typescript`, `0xDarkMatter/claude-mods`, `BeLazy167/claude-mods-skill`           |
| HTML       | 16    | `HeyCubit/effortless`, `awss1i/assay`, `darrell-tw/darrelltw-mods`                                            |
| Go         | 7     | `cephalofoil/kitt`, `kylesnowschwartz/tail-claude-hud`, `livlign/ccbit`                                       |
| Rust       | 5     | `persiyanov/herdr-reviewr`, `JairoTorregrosa/claude-statusline`, `melderan/claude-statusline-rust`            |
| PowerShell | 2     | `rainyfei/claude-statusline-win`, `YangShen-SWE/dsh-plugin-simple-pet`                                        |
| Swift      | 2     | `bhargava-gumpula/claude-mods`, `peaceinitiativemenhadenoil263/claude-status-bar`                             |
| C          | 1     | `reporails/arcade`                                                                                            |

<sub>Hanya entri yang menyatakan bahasa yang dihitung. Entri dokumentasi dan diskusi tidak disertakan dalam tabel ini.</sub>

## Berkontribusi

Koreksi sangat diterima dan merupakan cara tercepat untuk meningkatkan daftar ini. Buka issue atau pull request jika suatu entri salah kategorisasi, salah tingkat, atau jika sebuah proyek keliru dikecualikan karena benturan nama — kategori terakhir itulah yang paling mungkin salah akibat filter otomatis.

---

<sub>Proyek komunitas independen. Tidak berafiliasi dengan, tidak didukung oleh, dan tidak ditinjau oleh Anthropic. Claude Code, Claude, dan Anthropic adalah merek dagang milik Anthropic. Perilaku produk dapat berubah tanpa pemberitahuan; verifikasi hal-hal penting terhadap dokumentasi resmi. Aset tetap menjadi milik proyek upstream masing-masing dan hanya direproduksi jika diizinkan oleh lisensinya.</sub>

<sub>Terakhir diperbarui · 2026-10-11T05:58:46+08:00</sub>
