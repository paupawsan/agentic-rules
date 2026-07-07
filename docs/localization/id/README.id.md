# 🤖 Agentic Rules Framework (Bahasa Indonesia)

Framework plug-and-play yang menyediakan aturan terstruktur untuk perilaku agen AI cerdas di semua platform.

## 🌍 Pelokalan / Localization / 多言語対応

<details open>
<summary>📚 Dokumentasi tersedia dalam berbagai bahasa / Documentation available in multiple languages / 多言語ドキュメント</summary>

### English (Bahasa Inggris)
<details>
<summary>🇺🇸 English Documentation / Dokumentasi Bahasa Inggris</summary>

- **[Main Page / Halaman Utama](../../../README.md)** - Framework overview and quick start
- **[Documentation Index / Indeks Dokumentasi](../../INDEX.md)** - Complete documentation overview
- **[User Guide / Panduan Pengguna](../../USER-GUIDE.md)** - Step-by-step setup for beginners
- **[Developer Guide / Panduan Pengembang](../../DEVELOPER-GUIDE.md)** - Technical implementation details
- **[System Overview / Ikhtisar Sistem](../../SYSTEM-OVERVIEW.md)** - Complete system architecture
- **[Extension Manual / Manual Ekstensi](../../EXTENSION-MANUAL.md)** - Plugin development guide
- **[Troubleshooting / Panduan Pemecahan Masalah](../../TROUBLESHOOTING.md)** - Problem solving guide

</details>

### Japanese (Bahasa Jepang)
<details>
<summary>🇯🇵 Japanese Documentation / Dokumentasi Bahasa Jepang</summary>

- **[メインページ / Halaman Utama](../ja/README.ja.md)** - フレームワークの概要とクイックスタート
- **[説明書の目次 / Indeks Dokumentasi](../ja/INDEX.ja.md)** - 説明書の全体像
- **[ユーザーガイド / Panduan Pengguna](../ja/USER-GUIDE.ja.md)** - 初心者向けガイド
- **[開発者ガイド / Panduan Pengembang](../ja/DEVELOPER-GUIDE.ja.md)** - 技術者向け詳細
- **[システムの説明 / Ikhtisar Sistem](../ja/SYSTEM-OVERVIEW.ja.md)** - システムの仕組み
- **[拡張マニュアル / Manual Ekstensi](../ja/EXTENSION-MANUAL.ja.md)** - プラグイン開発
- **[トラブルシューティング / Panduan Pemecahan Masalah](../ja/TROUBLESHOOTING.ja.md)** - 問題解決ガイド

</details>

</details>

## 🧩 Gunakan dengan Claude Code (Plugin)

Jika Anda menggunakan **Claude Code**, framework ini terpasang sebagai plugin native — tanpa `setup.html`, tanpa langkah bootstrap. **Mengaktifkan plugin sudah merupakan aktivasinya.** Claude Code hanyalah satu dari banyak adapter: seluruh plugin berada di [claude-code/](../../../claude-code/), dan inti yang netral platform (`modules/`) tidak diubah sama sekali.

```bash
# 1. Tambahkan repo ini sebagai marketplace plugin
/plugin marketplace add paupawsan/agentic-rules

# 2. Pasang plugin dari marketplace tersebut
/plugin install agentic-rules@agentic-rules
```

Lalu kelola dari dalam Claude Code:

```bash
/plugin                 # aktif/nonaktif, edit opsi
/agentic-rules:status   # tampilkan modul yang aktif
/agentic-rules:help     # orientasi
```

**Yang Anda dapatkan**

- Empat modul aturan sebagai **skill** yang dimuat otomatis saat relevan: memori, RAG/konteks, berpikir kritis, dan unit test interaksi agen.
- Mode **always-on** opsional (`always_on_injection`) yang menyuntikkan aturan aktif ke setiap sesi — paling mirip dengan `CLAUDE.md`.
- Server MCP **Knowledge Graph** opsional — atur `kg_mcp_url` ke endpoint Anda (memori/RAG tetap berfungsi dengan baik tanpanya).
- **Tanpa duplikasi** — skill dan injektor membaca langsung file aturan `modules/` yang kanonik (semua bahasa yang disertakan framework, mis. `ja`/`id`); perubahan dari hulu mengalir tanpa sinkronisasi ulang.

**Konfigurasi** (atur via `/plugin`)

| Opsi | Default | Tujuan |
|--------|---------|---------|
| `language` | `en` | Bahasa teks aturan yang disuntikkan (`en` / `ja` / `id`) |
| `memory_path` | — | Direktori root untuk penyimpanan memori |
| `enable_memory` / `enable_rag` / `enable_critical_thinking` | aktif | Aktifkan/nonaktifkan modul aturan |
| `enable_agent_unit_test` | nonaktif | Audit percakapan (panggil secara eksplisit) |
| `always_on_injection` | nonaktif | Suntik aturan tiap sesi vs skill sesuai permintaan |
| `kg_mcp_url` | — | Endpoint MCP Knowledge Graph (kosong = nonaktif) |

📖 **[Panduan Plugin Claude Code (Bahasa Inggris)](../../CLAUDE_CODE_PLUGIN.md)** — pemetaan komponen lengkap, cara aturan dikirim, dan perbedaannya dengan jalur `setup.html`.

> Bagian di bawah (`setup.html`, bootstrap) ditujukan untuk **platform lain** — Cursor, VSCode, dan sistem agentik kustom. Pengguna Claude Code dapat melewatinya.

---

## 🚀 Mulai Cepat - Pengaturan Pertama Kali (Platform Lain)

### ⚠️ **Langkah 1: Jalankan Antarmuka Pengaturan (PENTING!)**
**Jalankan `setup.html` terlebih dahulu untuk mengkonfigurasi aturan dan menghasilkan file yang diperlukan!**

1. **Unduh** file framework `agentic-rules` dari GitHub
2. **Klik ganda** `setup.html` untuk meluncurkan antarmuka web
3. **Konfigurasi** aturan yang diinginkan (Memori, RAG, Berpikir Kritis)
4. **Hasilkan** file konfigurasi

> 💡 **Mengapa setup.html terlebih dahulu?** Antarmuka web membuat file konfigurasi dan aturan yang dibutuhkan sistem bootstrap. Tanpa langkah ini, framework mungkin tidak menginisialisasi dengan benar.
>
> 🔧 **Untuk Insinyur/Pengembang**: Gunakan peluncur Python yang ditingkatkan untuk fungsionalitas yang lebih baik - menyediakan pembuatan file langsung dan kontrol server. Lihat [Panduan Pengembang](DEVELOPER-GUIDE.id.md) untuk opsi otomasi pengaturan.

---

### ⚡ **Langkah 2: Inisialisasi Sistem Agentic Rules**
**Setelah setup.html, selesaikan inisialisasi bootstrap SATU KALI ini!**

1. **Beritahu agen AI Anda**: `Inisialisasi sistem aturan agentic di folder /path/to/your/agentic-rules. Saya sudah menyelesaikan setup.html, jadi lakukan saja inisialisasi bootstrap.`
2. **Berikan izin** ketika diminta untuk mengaktifkan framework
3. **Tinjau pengaturan** untuk aturan Memori, RAG, dan Berpikir Kritis
4. **Framework aktif** - agen Anda sekarang memiliki kemampuan yang ditingkatkan!

> 💡 **Mengapa langkah ini?** Framework memerlukan konfigurasi bootstrap awal untuk memastikan integrasi yang tepat dengan lingkungan AI Anda. Pengaturan satu kali ini mengaktifkan semua fitur framework.

---

## 🎯 Ikhtisar Framework

**Agentic Rules Framework** meningkatkan kemampuan agen AI melalui 4 sistem aturan khusus:

### 🧠 **Aturan Memori** (Sistem Memori Lokal)
📖 **[Detail Plugin](../../../modules/memory-rules/docs/localization/id/README.id.md)** - **Sistem memori lokal yang dapat dibaca manusia** dengan 10 kategori khusus untuk konteks persisten, pembelajaran, dan personalisasi di seluruh sesi. Visibilitas dan kontrol penuh atas data memori agen AI Anda.

### 📚 **Aturan RAG**
📖 **[Detail Plugin](../../../modules/rag-rules/docs/localization/id/README.id.md)** - Pemrosesan informasi canggih dengan strategi membaca cerdas, optimasi konteks, penilaian relevansi, dan **konstruksi Knowledge Graph otomatis** untuk pemahaman proyek dan pemetaan hubungan.

### 🤔 **Aturan Berpikir Kritis**
📖 **[Detail Plugin](../../../modules/critical-thinking-rules/docs/localization/id/README.id.md)** - Peningkatan penalaran sistematis dengan pencegahan kesalahan, validasi asumsi, dan pengambilan keputusan berbasis bukti.

### 🧪 **Unit Test Interaksi Agen** (nonaktif secara default)
📖 **[Detail Plugin](../../../modules/agent-interaction-unit-test/docs/localization/id/README.id.md)** - Kerangka kerja pengujian untuk percakapan agen, mencakup persyaratan ground check, pencatatan chain-of-thought, dan analisis debugging agen.

**Manfaat Utama:**
- **🔌 Plug-and-Play**: Aktifkan/nonaktifkan aturan tanpa memodifikasi perilaku agen
- **🖥️ Multi-Platform**: Bekerja dengan Cursor, VSCode, dan sistem agen kustom
- **📦 Mandiri**: File HTML tunggal dengan konfigurasi tersemat
- **🛠️ Tool Agnostic**: Agen menggunakan tool yang tersedia untuk mengimplementasikan persyaratan aturan
- **🌐 Generik**: Berlaku untuk agen AI apa pun yang dapat mengikuti pedoman terstruktur
- **🌍 Multi-Bahasa**: en/ja/id tersedia langsung di framework inti; sistem template plugin mendukung 18+ bahasa tambahan untuk ekstensi kustom

## 🧠 **Integrasi Knowledge Graph**
Aktif secara default — konstruksi dan penggunaan KG otomatis untuk pemahaman proyek.

### **Yang Dilakukannya**
- **🔍 Penemuan Otomatis**: Memindai percakapan dan codebase untuk membangun knowledge graph
- **🧷 Penautan Cerdas**: Menghubungkan konsep, file, dan ide yang terkait secara otomatis
- **💬 Penggunaan Proaktif**: Menggunakan insight KG dalam percakapan tanpa aktivasi manual
- **⏳ Pengetahuan Sadar-Waktu (Bi-Temporal)** *(v1.5.0)*: saat pengetahuan berubah,
  fakta lama digantikan (supersede) — bukan dihapus. Pengambilan default hanya
  mengembalikan pengetahuan terkini; riwayat tetap dapat dikueri ("apa yang kita
  ketahui pada tanggal X?"). Ini adalah adaptasi dari pemodelan basis data
  bi-temporal untuk memori agen, terinspirasi oleh
  [Graphiti dari Zep](https://github.com/getzep/graphiti) (hanya konsepnya —
  tidak ada kode yang digunakan ulang). Lihat [Panduan Implementasi KG](KG_IMPLEMENTATION_GUIDE.id.md)
  untuk model, implementasi berbasis basis data, dan kapan (tidak) menggunakannya,
  serta [perbandingan sebelum/sesudah](TEMPORAL_KG_COMPARISON.id.md) untuk
  perubahan yang terjadi dalam praktiknya.

### **Untuk Pengguna**
- **Zero Konfigurasi**: Bekerja langsung dengan setup standar
- **Percakapan yang Diperkaya**: Respons dapat menyertakan konteks historis yang relevan
- **Pemahaman Hubungan**: Sistem melacak bagaimana komponen proyek saling terhubung

### **Untuk Pengembang Agen**
📖 **[Panduan Implementasi KG](KG_IMPLEMENTATION_GUIDE.id.md)** - Algoritma logis dan pseudocode untuk fungsionalitas KG
📖 **[Integrasi KG untuk Pengguna](README_KG_INTEGRATION.id.md)** - Pengalaman dan manfaat KG dari sisi pengguna akhir

## 🧪 **Unit Test Interaksi Agen - Format yang Efektif**

Pencatatan chain-of-thought melalui file `CORE-RULES.md` dan `RULES.md`, digunakan untuk pengujian interaksi agen yang terstruktur.

### **Contoh Format Unit Test**
```
UNIT TEST: Agent Memory Retrieval
Framework: Agentic Rules v1.5.2
Task: Test basic agent Memory retrieval.

Instruction:
Sync your memory for current project.

Output:
I want unit test report in markdown format @debug
```

**Yang Disediakan Framework:**
- **🔍 Validasi Ground Check**: Verifikasi cakupan klaim informasi terhadap sumber
- **🛡️ Tantangan Asumsi**: Deteksi dan validasi asumsi implisit
- **⚡ Audit Tool Call**: Pencatatan eksekusi tool dengan skor relevansi
- **🎯 Dokumentasi Keputusan**: Jejak audit titik keputusan beserta alternatifnya
- **📊 Manajemen Konteks**: Pemantauan penggunaan konteks dan optimasi
- **🔧 Analisis Debugging Agen**: Analisis proses penalaran agen, penggunaan tool, dan pemilihan parameter
- **✅ Validasi Kepatuhan**: Pengecekan otomatis terhadap persyaratan framework

## 📋 Pelajari Lebih Lanjut

#### 👥 **Untuk Semua Orang** (Tidak Perlu Pengetahuan Teknis)
📖 **[Panduan Pengguna](USER-GUIDE.id.md)** - Setup langkah demi langkah dengan instruksi

#### 🔧 **Untuk Insinyur & Pengembang**
📖 **[Panduan Pengembang](DEVELOPER-GUIDE.id.md)** - Setup server, otomasi, dan penggunaan API

#### 🛠️ **Untuk Pengembang Plugin**
📖 **[Manual Ekstensi](EXTENSION-MANUAL.id.md)** - Pengembangan plugin dan ekstensi framework

#### 📚 **Arsitektur Sistem & Pendalaman Teknis**
📖 **[Ikhtisar Sistem](SYSTEM-OVERVIEW.id.md)** - Arsitektur teknis lengkap dan prinsip desain

#### 🐛 **Pemecahan Masalah & FAQ**
📖 **[Panduan Pemecahan Masalah](TROUBLESHOOTING.id.md)** - Solusi untuk masalah umum dan instruksi pemuatan manual
🛠️ **Scaffold Cepat**: `python generate_plugin_scaffold.py --help` - Hasilkan template plugin secara instan

### 🔄 **Siklus Hidup Framework**
- **Inisialisasi**: Setup satu kali dengan persetujuan pengguna
- **Aktivasi Otomatis**: Framework dimuat otomatis setelah setup pertama
- **Konfigurasi**: Ubah pengaturan di `settings/global-settings.json`
- **Reset**: Hapus file `.agentic_initialized` untuk memaksa inisialisasi ulang

## 🤝 Berkontribusi

**Kontribusi sangat kami sambut!** Proyek ini berkembang berkat masukan dan kolaborasi komunitas.

- 📝 **Laporkan Masalah**: Menemukan bug? Punya saran? [Buka issue](https://github.com/paupawsan/agentic-rules/issues)
- 🔧 **Kirim Pull Request**: Bantu tingkatkan framework
- 💬 **Diskusi**: Ikut serta dalam diskusi tentang sistem agentik dan perilaku AI
- 📖 **Dokumentasi**: Bantu tingkatkan panduan dan dokumentasi

## ⚠️ Disclaimer Penting

**Proyek Pribadi**: Framework ini dirancang dan dikembangkan menggunakan waktu dan sumber daya pribadi. Saya tidak berafiliasi dengan perusahaan mana pun, dan ini bukan produk atau layanan resmi.

**Catatan Pemeliharaan**: Saya tidak dapat menjamin pembaruan aktif atau pemeliharaan tepat waktu. Meski saya berupaya menjaga framework tetap berfungsi dan aman, pembaruan bergantung pada waktu dan sumber daya yang tersedia.

**Dukungan Komunitas**: Kontribusi, masukan, dan partisipasi Anda sangat berarti bagi pengembangan dan peningkatan framework ini secara berkelanjutan. Keterlibatan komunitas membantu menjaga proyek ini tetap berguna dan relevan.

**Perilaku Best-Effort**: Framework ini bekerja dengan cara memberi instruksi kepada agen AI, bukan dengan jaminan tingkat kode. Apakah aturan benar-benar diikuti (ground-check klaim, pemanggilan memori, penggunaan KG, dll.) bergantung pada kombinasi editor, agen, dan model spesifik yang digunakan — perilakunya bisa berbeda-beda dan tidak dijamin sama di semua setup.

**Gunakan dengan Risiko Anda Sendiri**: Framework ini disediakan apa adanya (as-is). Pengguna harus mengevaluasi kesesuaiannya dengan kasus penggunaan masing-masing dan menerapkan langkah keamanan yang sesuai.

---

Copyright (c) 2025-2026 Paulus Ery Wasito Adhi. Dilisensikan di bawah Lisensi MIT (lihat file LICENSE).