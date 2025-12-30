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
    "versi": "1.0.0",
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

## 🧠 Arsitektur Knowledge Graph (KG)

### Pipeline Konstruksi KG

Framework mengimplementasikan sistem konstruksi Knowledge Graph yang canggih yang secara otomatis membangun hubungan semantik antara komponen proyek.

#### Algoritma KG Inti

**1. Ekstraksi Entitas Terstruktur**
```python
Algoritma: Ekstrak entitas dari basis kode
Input: Kode sumber, dokumentasi, file konfigurasi
Proses:
├── Tokenisasi dan penandaan POS
├── Pengenalan entitas bernama (NER)
├── Pencocokkan pola domain-spesifik
├── Validasi dan penilaian kepercayaan
Output: Entitas yang dikategorikan (fungsi, kelas, file, konsep)
```

**2. Penemuan Hubungan Berbasis Pola**
```python
Algoritma: Identifikasi hubungan antara entitas
Input: Daftar entitas, konteks kalimat
Proses:
├── Pencocokkan pola sintaks (subjek-kata kerja-objek)
├── Analisis dependensi (import, pemanggilan, pewarisan)
├── Penautan semantik (hubungan konsep)
├── Deteksi hubungan temporal
Output: Hubungan yang diketik dengan skor kepercayaan
```

**3. Pembangun Graph Inkremental**
```python
Algoritma: Konstruk dan pertahankan knowledge graph
Input: Entitas baru, hubungan, graph yang ada, sistem memori diaktifkan
Proses:
├── Inisialisasi graph dengan node dan edge yang ada
├── Deduplikasi dan penggabungan entitas
├── Validasi konsistensi hubungan
├── Optimasi dan pengindeksan graph
├── Persistensi status graph dengan metadata
Output: Graph KG yang diperbarui dengan interface query
```

### Komponen Arsitektur KG

#### **Lapisan Penyimpanan Graph**
```
Integrasi Sistem Memori:
├── Penyimpanan Utama: /lm/projects/{project}/kg/
├── Penyimpanan Cadangan: /lm/common/knowledge_graph/
├── Penyimpanan Metadata: Stempel waktu konstruksi graph, versi
├── Indeks Query: Dioptimalkan untuk traversal hubungan
```

#### **Mesin Pemrosesan Query**
```
Pemrosesan Query Semantik:
├── Bahasa Alami → Parsing Entitas/Intent
├── Algoritma Traversal Graph (BFS/DFS dengan batas kedalaman)
├── Pemfilteran dan Perangkingan Hubungan
├── Ekspansi Konteks dari Node yang Terhubung
├── Sintesis Respons dengan Penilaian Relevansi
```

#### **Arsitektur Pemrosesan Latar Belakang**
```
Konstruksi KG Asinkron:
├── Deteksi Pemicu: Analisis proyek, perubahan file, query pengguna
├── Pemrosesan Batch: Ekstraksi entitas dalam potongan yang dapat dikonfigurasi
├── Pembaruan Inkremental: Hanya proses komponen yang berubah
├── Manajemen Sumber Daya: Batas CPU/memori, kontrol timeout
├── Antrian Persistensi: Simpan hasil tanpa memblokir interaksi pengguna
```

### Integrasi KG dengan Sistem Aturan

#### **Aturan RAG ↔ Integrasi KG**
```
Peningkatan Pengambilan Informasi:
├── RAG Tradisional: Pengambilan dokumen berbasis kata kunci
├── RAG Berbasis KG: Traversal hubungan semantik
├── Penilaian Hibrid: Gabungkan relevansi kata kunci + centralitas graph
├── Ekspansi Konteks: Sertakan konsep dan dependensi terkait
```

#### **Aturan Memori ↔ Integrasi KG**
```
Penyimpanan Pengetahuan Persisten:
├── Struktur KG: Disimpan dalam kategori memori khusus
├── Pelestarian Hubungan: Pertahankan topologi graph di seluruh sesi
├── Riwayat Query: Pelajari dari query KG yang berhasil
├── Penautan Konteks: Hubungkan wawasan KG ke konteks percakapan
```

#### **Berpikir Kritis ↔ Integrasi KG**
```
Validasi Pengetahuan:
├── Verifikasi Sumber: Periksa hubungan KG terhadap fakta yang diketahui
├── Analisis Konsistensi: Validasi hubungan graph untuk konflik logis
├── Kuantifikasi Ketidakpastian: Tetapkan skor kepercayaan ke elemen graph
├── Deteksi Kesalahan: Identifikasi hubungan yang berpotensi salah
```

### Karakteristik Performa KG

#### **Metrik Skalabilitas**
```
Baseline Saat Ini (28 node, 47 hubungan):
├── Waktu Konstruksi: <30 detik untuk analisis proyek
├── Performa Query: <250ms waktu respons rata-rata
├── Penggunaan Memori: ~135KB untuk data KG proyek
├── Frekuensi Pembaruan: Inkremental, dipicu oleh perubahan

Proyeksi Pertumbuhan (50 node, 100 hubungan):
├── Waktu Konstruksi: <45 detik dengan pemrosesan batch
├── Performa Query: <500ms dengan pengindeksan yang dioptimalkan
├── Penggunaan Memori: ~250KB dengan kompresi
├── Pembaruan Real-time: Pemrosesan latar belakang mempertahankan performa
```

#### **Jaminan Kualitas**
```
Validasi Graph:
├── Akurasi Entitas: >95% identifikasi komponen yang benar
├── Presisi Hubungan: >90% pemetaan hubungan yang akurat
├── Konsistensi Graph: Resolusi konflik otomatis
├── Relevansi Query: Pencocokkan semantik dengan fallback ke pencarian kata kunci
```

### Visualisasi & Analisis KG

#### **Representasi ASCII Graph**
```
Graph Arsitektur Framework:
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Modul Aturan  │◄───┤   Sistem Setup  │◄───┤   Sistem Memori │
│                 │    │                 │    │                 │
│ • Aturan RAG    │    │ • setup.py      │    │ • penyimpanan   │
│ • Aturan Memori │    │ • setup.html    │    │ • /lm/          │
│ • Berpikir Kritis│    │ • web-config   │    │ • Kategori      │
└─────────────────┘    └─────────────────┘    └─────────────────┘
        ▲                        ▲                        ▲
        │                        │                        │
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│ Dokumentasi     │◄───┤   Lokalisasi    │◄───┤ Konfigurasi     │
│                 │    │                 │    │                 │
│ • README.md     │    │ • file JSON     │    │ • settings.json │
│ • Panduan       │    │ • multi-bahasa  │    │ • bootstrap.json│
│ • Dok API       │    │ • Terjemahan    │    │ • Lingkungan    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

#### **Legenda Tipe Hubungan**
- **───**: Dependensi langsung (kopling kuat)
- **◄───**: Hubungan aliran data
- **····**: Hubungan tidak langsung atau opsional
- **━━━━**: Jalur kritis atau alur kerja utama

### Interface Query KG

#### **Tipe Query yang Didukung**
```
1. Query Struktur: "Temukan semua komponen yang terhubung dengan X?"
2. Query Hubungan: "Bagaimana A dan B terhubung?"
3. Query Pola: "Temukan struktur serupa dengan Y"
4. Analisis Dampak: "Apa yang akan rusak jika saya mengubah Z?"
5. Query Navigasi: "Tunjukkan jalur dari A ke B"
```

#### **Pipeline Pemrosesan Query**
```
Query Bahasa Alami → Klasifikasi Intent → Resolusi Entitas → Traversal Graph → Perangkingan Hasil → Sintesis Respons
```

### Pemeliharaan & Evolusi KG

#### **Pembaruan Otomatis**
- **Deteksi Perubahan**: Pemantauan sistem file untuk modifikasi
- **Pembaruan Inkremental**: Hanya bangun kembali bagian graph yang terpengaruh
- **Kontrol Versi**: Lacak evolusi KG bersama kode
- **Pemantauan Performa**: Metrik performa dan akurasi query

#### **Pemeliharaan Kualitas**
- **Pemeriksaan Konsistensi**: Validasi reguler hubungan graph
- **Verifikasi Akurasi**: Cross-reference dengan kode sumber
- **Penyesuaian Performa**: Optimalkan pola query dan pengindeksan
- **Integrasi Umpan Balik Pengguna**: Pelajari dari pola keberhasilan/kegagalan query

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