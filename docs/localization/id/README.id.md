# 🤖 Agentic Rules Framework (Bahasa Indonesia)

Framework plug-and-play yang menyediakan aturan terstruktur untuk perilaku agen AI cerdas di semua platform.

## 🌍 Pelokalan / Localization / 多言語対応

<details open>
<summary>📚 Dokumentasi tersedia dalam berbagai bahasa / Documentation available in multiple languages / 多言語ドキュメント</summary>

### English (Bahasa Inggris)
<details>
<summary>🇺🇸 English Documentation / Dokumentasi Bahasa Inggris</summary>

- **[Main Page / Halaman Utama](README.md)** - Framework overview and quick start
- **[Documentation Index / Indeks Dokumentasi](docs/INDEX.md)** - Complete documentation overview
- **[User Guide / Panduan Pengguna](docs/USER-GUIDE.md)** - Step-by-step setup for beginners
- **[Developer Guide / Panduan Pengembang](docs/DEVELOPER-GUIDE.md)** - Technical implementation details
- **[System Overview / Ikhtisar Sistem](docs/SYSTEM-OVERVIEW.md)** - Complete system architecture
- **[Extension Manual / Manual Ekstensi](docs/EXTENSION-MANUAL.md)** - Plugin development guide
- **[Troubleshooting / Panduan Pemecahan Masalah](docs/TROUBLESHOOTING.md)** - Problem solving guide

</details>

### Japanese (Bahasa Jepang)
<details>
<summary>🇯🇵 Japanese Documentation / Dokumentasi Bahasa Jepang</summary>

- **[メインページ / Halaman Utama](../ja/README.ja.md)** - フレームワークの概要とクイックスタート
- **[説明書の目次 / Indeks Dokumentasi](docs/localization/ja/INDEX.ja.md)** - 説明書の全体像
- **[ユーザーガイド / Panduan Pengguna](docs/localization/ja/USER-GUIDE.ja.md)** - 初心者向けガイド
- **[開発者ガイド / Panduan Pengembang](docs/localization/ja/DEVELOPER-GUIDE.ja.md)** - 技術者向け詳細
- **[システムの説明 / Ikhtisar Sistem](docs/localization/ja/SYSTEM-OVERVIEW.ja.md)** - システムの仕組み
- **[拡張マニュアル / Manual Ekstensi](docs/localization/ja/EXTENSION-MANUAL.ja.md)** - プラグイン開発
- **[トラブルシューティング / Panduan Pemecahan Masalah](docs/localization/ja/TROUBLESHOOTING.ja.md)** - 問題解決ガイド

</details>

</details>

## 🚀 Mulai Cepat - Pengaturan Pertama Kali

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

1. **Beritahu agen AI Anda**: `Initialize agentic rules system`
2. **Berikan izin** ketika diminta untuk mengaktifkan framework
3. **Tinjau pengaturan** untuk aturan Memori, RAG, dan Berpikir Kritis
4. **Framework aktif** - agen Anda sekarang memiliki kemampuan yang ditingkatkan!

> 💡 **Mengapa langkah ini?** Framework memerlukan konfigurasi bootstrap awal untuk memastikan integrasi yang tepat dengan lingkungan AI Anda. Pengaturan satu kali ini mengaktifkan semua fitur framework.

---

## 🎯 Ikhtisar Framework

**Agentic Rules Framework** meningkatkan kemampuan agen AI melalui 3 sistem aturan khusus:

### 🧠 **Aturan Memori** (Sistem Memori Lokal)
📖 **[Detail Plugin](modules/memory-rules/README.md)** - **Sistem memori lokal yang dapat dibaca manusia** dengan 10 kategori khusus untuk konteks persisten, pembelajaran, dan personalisasi di seluruh sesi. Visibilitas dan kontrol penuh atas data memori agen AI Anda.

### 📚 **Aturan RAG**
📖 **[Detail Plugin](modules/rag-rules/README.md)** - Pemrosesan informasi canggih dengan strategi membaca cerdas, optimasi konteks, dan penilaian relevansi untuk pemanfaatan pengetahuan yang efisien.

### 🤔 **Aturan Berpikir Kritis**
📖 **[Detail Plugin](modules/critical-thinking-rules/README.md)** - Peningkatan inferensi sistematis dengan pencegahan kesalahan, validasi asumsi, dan pengambilan keputusan berbasis bukti.

**Manfaat Utama:**
- **🔌 Plug-and-Play**: Aktifkan/nonaktifkan aturan tanpa memodifikasi perilaku agen
- **🌍 Multi-Platform**: Bekerja dengan Cursor, VSCode, dan sistem agen kustom
- **📦 Mandiri**: File HTML tunggal dengan konfigurasi tersemat
- **🛠️ Tool Agnostic**: Agen menggunakan tool yang tersedia untuk mengimplementasikan persyaratan aturan
- **🌐 Generik**: Berlaku untuk agen AI apa pun yang dapat mengikuti pedoman terstruktur
- **🌍 Multi-Bahasa**: Template aturan dilokalkan dalam 18+ bahasa

## 🚀 Mulai Cepat

Pilih level pengalaman Anda:

### 👥 **Untuk Semua Orang** (Tidak Perlu Pengetahuan Teknis)
📖 **[Panduan Pengguna](USER-GUIDE.id.md)** - Setup langkah demi langkah dengan instruksi

### 🔧 **Untuk Insinyur & Pengembang**
📖 **[Panduan Pengembang](DEVELOPER-GUIDE.id.md)** - Setup server, otomasi, dan penggunaan API

### 🔌 **Untuk Pengembang Plugin**
📖 **[Manual Ekstensi](EXTENSION-MANUAL.id.md)** - Cara membuat plugin baru

## 📋 Persyaratan

- **Python 3.8+** (untuk mode server)
- **Web Browser** (untuk antarmuka HTML)
- **Platform AI yang Didukung**: Cursor, VSCode, Claude, Gemini, agen kustom

## 🛠️ Instalasi

### Opsi 1: Antarmuka HTML (Direkomendasikan)
```bash
# Kloning atau unduh repositori
git clone https://github.com/paupawsan/agentic-rules.git
cd agentic-rules

# Klik dua kali setup.html untuk memulai
# Jalankan setup interaktif di browser
```

### Opsi 2: Mode Server
```bash
# Siapkan lingkungan Python
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Instal dependensi
pip install flask  # jika diperlukan dependensi tambahan

# Jalankan server
python setup-launcher.py

# Akses http://localhost:8001 di browser
```

## 📚 Dokumentasi

### 🌍 Dokumentasi Multi-Bahasa
- **[English Documentation](../../../README.md)** - Dokumentasi versi Bahasa Inggris
- **[日本語ドキュメント](../ja/README.ja.md)** - Dokumentasi versi Bahasa Jepang

### 📖 Dokumentasi Utama
- **[Ikhtisar Sistem](SYSTEM-OVERVIEW.id.md)** - Arsitektur dan mekanisme lengkap
- **[Manual Ekstensi](EXTENSION-MANUAL.id.md)** - Panduan pengembangan plugin
- **[Panduan Pemecahan Masalah](TROUBLESHOOTING.id.md)** - Panduan penyelesaian masalah

### 🏗️ Untuk Pengembang
- **[Panduan Pengembang](DEVELOPER-GUIDE.id.md)** - Detail implementasi teknis
- **[Aturan Inti](CORE-RULES.id.md)** - Aturan dasar framework

## 🤝 Berkontribusi

Kontribusi sangat diterima!

### Cara Berkontribusi
1. Fork repositori ini
2. Buat branch fitur (`git checkout -b fitur/fitur-hebat`)
3. Komit perubahan (`git commit -m 'Tambah fitur hebat'`)
4. Push branch (`git push origin fitur/fitur-hebat`)
5. Buat Pull Request

### Partisipasi Pengembangan
- **Laporan Bug**: Gunakan [Issues](../../issues)
- **Permintaan Fitur**: Ajukan di [Issues](../../issues)
- **Kontribusi Kode**: Pull Request diterima
- **Terjemahan**: Perbaikan dokumentasi multi-bahasa

## 📄 Lisensi

Copyright (c) 2025 Paulus Ery Wasito Adhi

Dililis di bawah Lisensi MIT. Lihat file LICENSE untuk detailnya.

---

**🎉 Agentic Rules Framework v1.0.0 sekarang siap produksi!**

**Unduh dari:** [GitHub Releases](https://github.com/paupawsan/agentic-rules/releases/tag/v1.0.0)

**Mulai Cepat:** Jalankan `python setup.py` untuk memulai!

---

*Dibuat dengan ❤️ untuk komunitas agen AI*