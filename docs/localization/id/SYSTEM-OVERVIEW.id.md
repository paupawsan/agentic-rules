# 🔧 Agentic Rules Framework - Penjelasan Sistem (Bahasa Indonesia)

## Cara Kerja Sistem

Dokumen ini menjelaskan bagaimana Agentic Rules Framework bekerja, prinsip dasar, dan detail implementasi.

## 🏗️ Struktur Utama

### Prinsip Dasar Framework

Agentic Rules Framework dibangun berdasarkan tiga prinsip utama:

#### 1. **Sistem Aturan Terpisah**
- **Tidak Ada Kontrol Pusat**: Setiap aturan bekerja sendiri di tugasnya masing-masing
- **Komunikasi Fleksibel**: Aturan saling berbagi data, bukan perintah langsung
- **Aman dari Kesalahan**: Jika satu aturan bermasalah, yang lain tidak terpengaruh
- **Mudah Ditambahkan**: Aturan baru bisa ditambahkan tanpa mengubah aturan yang ada

#### 2. **Panduan Perilaku Pintar**
- **Bukan Larangan Ketat**: Aturan memberikan cara berpikir, bukan batasan yang kaku
- **Alat Agnostik**: AI bisa menggunakan berbagai alat yang ada untuk mengikuti aturan
- **Fleksibilitas Pelaksanaan**: Ada banyak cara untuk mengikuti aturan
- **Peningkatan Bertahap**: Aturan menambahkan kemampuan tanpa mengganti yang sudah ada

#### 3. **Bekerja Mandiri**
- **Tidak Perlu Instalasi Tambahan**: Framework bekerja tanpa program tambahan
- **Bisa Offline**: Semua bagian sudah ada dalam satu file HTML
- **Pengaturan Portabel**: Konfigurasi berbasis JSON untuk mudah dipindahkan
- **Bekerja di Berbagai Platform**: Dapat disesuaikan dengan berbagai lingkungan AI

### Struktur Komponen

```
Bagian Framework
├── Pengaturan Awal (bootstrap.json)
├── Antarmuka Web (setup.html)
├── Alat Command Line (setup.py, setup-launcher.py)
└── Sistem Bahasa (localization.json)

Bagian Aturan
├── Aturan Memori (modules/memory-rules/)
├── Aturan RAG (modules/rag-rules/)
└── Aturan Berpikir Kritis (modules/critical-thinking-rules/)

Bagian Pelaksanaan
├── Template Aturan (RULES.md.*)
├── Skema Pengaturan (settings.json)
├── Info Pengaturan (setup.json)
└── File AI yang Dihasilkan (AGENTS.md)
```

## 🔄 Cara Kerja Framework

### 1. Tahap Persiapan Awal
```
Buka bootstrap.json → Periksa pengaturan → Siapkan urutan memuat aturan
```

**Langkah Utama:**
- Periksa dan pastikan semua pengaturan benar
- Atur urutan prioritas dan hubungan antar aturan
- Siapkan penyesuaian untuk platform tertentu
- Atur keamanan dan izin akses

### 2. Tahap Persiapan Aturan
```
Untuk setiap aturan yang aktif → Buka pengaturan → Periksa pengaturan → Siapkan cara kerja
```

**Proses Setiap Aturan:**
- Buka pengaturan khusus aturan dari `settings.json`
- Periksa pengaturan sesuai dengan aturan
- Siapkan struktur data dan penyimpanan sementara
- Hubungkan dengan aturan lain

### 3. Tahap Operasi Normal
```
Interaksi pengguna → Jalankan aturan → Gabungkan hasil → Buat respons
```

**Pelaksanaan Bersama:**
- Aturan bekerja bersamaan di tugas masing-masing
- Hasil dikumpulkan melalui pengaturan awal
- Pastikan konsistensi antar aturan
- Optimalkan dan selesaikan respons akhir

## 📋 Spesifikasi Teknis

### Format Pengaturan Awal

```json
{
  "_info": {
    "versi": "0.1.0",
    "kompatibilitas": ["cursor", "vscode", "custom"],
    "lisensi": "MIT"
  },
  "urutan_memuat": [
    "memory-rules",
    "rag-rules",
    "critical-thinking-rules"
  ],
  "hubungan_antar_aturan": {
    "memory_rag_sharing": true,
    "critical_memory_learning": true,
    "rag_critical_validation": true
  },
  "penyesuaian_platform": {
    "cursor": { /* Pengaturan khusus Cursor */ },
    "vscode": { /* Pengaturan khusus VSCode */ }
  }
}
```

## 🔗 Interkoneksi Aturan

### Kerja Sama Memori ↔ RAG

**Alur Kerja:**
```
Pertanyaan Pengguna → Cari Konteks RAG → Personalisasi Memori → Konteks yang Lebih Baik → Buat Jawaban
```

**Hal yang Dibagikan:**
- Cara memahami konteks dan seberapa relevan
- Kebiasaan pengguna dari memori
- Perbaikan cara mencari berdasarkan pengalaman sebelumnya

### Kerja Sama Berpikir Kritis ↔ Memori

**Siklus Perbaikan:**
```
Buat Jawaban → Analisis Kritis → Temukan Kesalahan → Simpan di Memori → Perbaikan di Masa Depan
```

**Jaminan Kualitas:**
- Periksa keakuratan informasi yang disimpan
- Belajar dari koreksi dan pola yang ditemukan
- Sesuaikan kepercayaan berdasarkan kinerja sebelumnya

### Kerja Sama RAG ↔ Berpikir Kritis

**Proses Validasi:**
```
Cari Informasi → Periksa Secara Kritis → Validasi Sumber → Nilai Kepercayaan → Kualifikasi Jawaban
```

**Pintu Kualitas:**
- Nilai kredibilitas sumber informasi
- Periksa konsistensi logis
- Uji dan validasi asumsi

## 🌍 Dukungan Berbagai Platform

### Sistem Penyesuaian Platform

```json
{
  "penyesuaian_platform": {
    "cursor": {
      "sistem_file": "cursor_workspace",
      "integrasi_alat": "cursor_tools",
      "penyimpanan_memori": "cursor_storage"
    },
    "vscode": {
      "sistem_file": "workspace_folders",
      "integrasi_alat": "vscode_extensions",
      "penyimpanan_memori": "workspace_settings"
    }
  }
}
```

### Pendeteksian Lingkungan

**Pengenalan Platform Otomatis:**
- Analisis struktur sistem file
- Deteksi alat yang tersedia
- Kehadiran file konfigurasi
- Variabel lingkungan saat berjalan

## 🔒 Sistem Keamanan & Keselamatan

### Mekanisme Keselamatan

#### Keselamatan Aktivasi Template
- **Tidak Ada Pemuatan Otomatis**: Aturan harus diaktifkan secara eksplisit oleh pengguna
- **Penanda Template**: Tanda yang jelas mencegah aktivasi yang tidak disengaja
- **Persetujuan Pengguna**: Konfirmasi eksplisit diperlukan untuk aktivasi aturan

#### Keselamatan Runtime
- **Isolasi Kesalahan**: Kegagalan aturan diisolasi dari operasi sistem
- **Batas Sumber Daya**: Batas waktu dan batas sumber daya yang dapat dikonfigurasi
- **Logging Audit**: Semua operasi aturan dicatat untuk ditinjau

### Perlindungan Data

#### Keamanan Memori
- **Opsi Enkripsi**: Data sensitif dapat dienkripsi
- **Kontrol Akses**: Tingkat izin berbeda untuk kategori memori
- **Kebijakan Retensi**: Pembersihan otomatis data yang kedaluwarsa

#### Keamanan Konfigurasi
- **Validasi**: Semua konfigurasi divalidasi terhadap skema
- **Sanitisasi**: Validasi input dan sanitasi
- **Backup**: Backup otomatis sebelum perubahan konfigurasi

## 📊 Arsitektur Performa

### Strategi Optimasi

#### Manajemen Memori
- **Pemuatan Lambat**: Komponen dimuat sesuai permintaan
- **Lapisan Cache**: Cache multi-level untuk performa
- **Kompresi**: Kompresi otomatis untuk dataset besar
- **Pengindeksan**: Indeks yang dioptimalkan untuk pencarian cepat

#### Optimasi Pemrosesan
- **Eksekusi Paralel**: Aturan dieksekusi secara paralel jika memungkinkan
- **Pemrosesan Batch**: Kelompokkan operasi untuk efisiensi
- **Pemuatan Progresif**: Muat komponen kritis terlebih dahulu
- **Tugas Latar Belakang**: Operasi latar belakang yang tidak memblokir

### Pertimbangan Skalabilitas

#### Penskalaan Sumber Daya
- **Batas Memori**: Batas penggunaan memori yang dapat dikonfigurasi
- **Batas Waktu Pemrosesan**: Batas waktu operasi yang dapat dikonfigurasi
- **Kuota Penyimpanan**: Batas ukuran penyimpanan yang dapat dikonfigurasi
- **Operasi Bersamaan**: Batas operasi simultan

## 🔧 Pengembangan & Ekstensi

### Menambahkan Aturan Baru

**Proses Langkah demi Langkah:**

1. **Pembuatan Direktori**: `mkdir new-rule-rules/`
2. **Pengembangan Template**: Buat `RULES.md.en` dengan algoritma
3. **Skema Konfigurasi**: Tentukan `settings.json` dan `setup.json`
4. **Pelokalan**: Tambahkan string ke `localization.json`
5. **Integrasi Bootstrap**: Tambahkan ke urutan pemuatan `bootstrap.json`
6. **Antarmuka Web**: Jalankan `generate_simple_setup.py` untuk memperbarui UI
7. **Pengujian**: Validasi di semua platform yang didukung

### Pedoman Pengembangan Aturan

#### Desain Algoritma
- **Tujuan Jelas**: Setiap algoritma memiliki tujuan spesifik dan terukur
- **Fleksibilitas Implementasi**: Beberapa pendekatan implementasi diperbolehkan
- **Penanganan Kesalahan**: Deteksi dan pemulihan kesalahan yang komprehensif
- **Kesadaran Performa**: Pertimbangan penggunaan sumber daya yang efisien

#### Desain Konfigurasi
- **Pengungkapan Progresif**: Default sederhana dengan opsi lanjutan
- **Validasi**: Validasi input komprehensif dan pesan kesalahan
- **Dokumentasi**: Penjelasan yang jelas tentang setiap opsi konfigurasi
- **Kompatibilitas**: Kompatibilitas mundur dengan konfigurasi yang ada

## 📈 Evolusi & Pemeliharaan

### Kompatibilitas Versi

**Pembuatan Versi Semantik:**
- **MAJOR**: Perubahan yang melanggar antarmuka aturan atau format bootstrap
- **MINOR**: Fitur baru dan penambahan aturan
- **PATCH**: Perbaikan bug dan peningkatan performa

### Kompatibilitas Mundur

**Strategi Migrasi:**
- **Migrasi Konfigurasi**: Migrasi otomatis pengaturan pengguna
- **Kompatibilitas Aturan**: Aturan baru tidak merusak integrasi yang ada
- **Dukungan Platform**: Pertahankan kompatibilitas di seluruh versi platform

---

## 📚 Sumber Tambahan

- **[../../README.id.md](../../README.id.md)** - Mulai cepat dan ikhtisar
- **[../../CORE-RULES.id.md](../../CORE-RULES.id.md)** - Prinsip framework
- **[USER-GUIDE.id.md](USER-GUIDE.id.md)** - Panduan pengaturan pengguna akhir
- **[DEVELOPER-GUIDE.id.md](DEVELOPER-GUIDE.id.md)** - Panduan implementasi teknis
- **[EXTENSION-MANUAL.id.md](EXTENSION-MANUAL.id.md)** - Panduan ekstensi framework

---

**🔧 Ikhtisar Sistem**: Arsitektur teknis komprehensif dan prinsip desain Agentic Rules Framework.

*Copyright (c) 2025 Paulus Ery Wasito Adhi. Dilisensikan di bawah Lisensi MIT.*

---

Diterjemahkan ke Bahasa Indonesia untuk kemudahan akses global.