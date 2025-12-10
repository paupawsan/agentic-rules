# 🤖 Agentic Rules Framework Aturan Inti (Bahasa Indonesia)

## Tujuan Dokumen

**🎯 Pembaca Utama**: Integrator Framework, Arsitek Sistem, dan Pengembang Agen

**📋 Tujuan**: Dokumen ini memberikan prinsip-prinsip dasar dan penjelasan umum untuk mengimplementasikan framework aturan agentic sebelum mempelajari detail aturan spesifik. Berfungsi sebagai panduan untuk memahami cara kerja, struktur, dan pendekatan framework.

---

## Ikhtisar

Agentic Rules Framework menyediakan sistem lengkap dan mandiri untuk meningkatkan kemampuan agen AI melalui aturan yang terstruktur. Framework ini dirancang untuk:

- **🔌 Plug-and-Play**: Aktifkan atau nonaktifkan aturan tanpa mengubah perilaku agen
- **📝 Berfokus pada Algoritma**: Aturan diberikan sebagai panduan perilaku, bukan batasan ketat
- **🌐 Multi-Platform**: Bekerja di Cursor, VSCode, sistem CI, dan implementasi khusus
- **🛠️ Independen Alat**: Agen menggunakan alat yang tersedia untuk mengikuti persyaratan aturan
- **📦 Mandiri**: Satu file HTML dengan konfigurasi tertanam (bekerja offline)
- **🌍 Multi-Bahasa**: Mendukung template aturan dalam lebih dari 18 bahasa
- **👀 Transparan**: Semua penerapan aturan dicatat dalam format yang mudah dibaca

## Arsitektur Framework

### Komponen Inti

#### 🎯 Antarmuka Web (`setup.html`)
- **Alat Utama**: Klik ganda untuk membuka, tidak perlu instalasi
- **Mandiri**: Konfigurasi tertanam, bekerja offline
- **Multi-Bahasa**: Pelokalan otomatis (EN/JA/ID)
- **Generasi Konfigurasi**: Antarmuka copy-paste untuk penerapan mudah
- **Auto-Re-lokalisasi**: Hasil diperbarui saat bahasa berubah

#### ⚙️ Sistem Bootstrap (`bootstrap.json`)
- **Mesin Orkestrasi**: Konfigurasi framework yang dapat dibaca mesin
- **Urutan Pemuatan**: Aktivasi aturan berdasarkan prioritas
- **Interkoneksi**: Alur data antar aturan
- **Adapter Platform**: Penyesuaian khusus lingkungan
- **Validasi**: Pemeriksaan integritas framework

#### 📚 Modul Aturan
- **Aturan Memori**: Penyimpanan konteks dan pengetahuan yang bertahan lama
- **Aturan RAG**: Pemrosesan informasi dan optimasi konteks
- **Aturan Berpikir Kritis**: Verifikasi penalaran dan pencegahan kesalahan

### Model Integrasi

#### Arsitektur Tersebar Per-Aturan
- **Konfigurasi Bootstrap**: `bootstrap.json` menyediakan orkestrasi
- **Algoritma Aturan**: File `AGENTS.md` individual berisi implementasi spesifik
- **Integrasi yang Dihasilkan**: Antarmuka web membuat file `AGENTS.md` untuk aturan yang diaktifkan
- **Adaptasi Platform**: Deteksi lingkungan otomatis dan konfigurasi

## Prinsip Framework

### 1. 🔌 Arsitektur Plug-and-Play
Aturan dapat diaktifkan/dinonaktifkan melalui antarmuka web tanpa memodifikasi perilaku agen inti. Framework mempertahankan netralitas dan tidak mengganggu operasi agen yang ada.

### 2. 📝 Fokus pada Algoritma
Aturan mendeskripsikan proses eksekusi dan algoritma perilaku, bukan detail implementasi spesifik. Agen memiliki kebebasan dalam bagaimana mereka mengeksekusi algoritma ini menggunakan alat yang tersedia.

### 3. 🛠️ Independensi Alat
Agen mengimplementasikan algoritma aturan menggunakan kemampuan mereka sendiri dan alat yang tersedia. Framework mendeskripsikan "apa yang harus dilakukan", bukan "bagaimana melakukannya dengan alat spesifik".

### 4. 👀 Transparansi
Semua penerapan aturan, keputusan, dan proses dicatat dalam format markdown yang dapat diakses. Pengguna dapat meninjau bagaimana aturan mempengaruhi perilaku agen.

### 5. 🏗️ Isolasi Framework
Framework tetap menjadi alat pengembangan saja. Jangan pernah menyertakan file framework dalam basis kode proyek pengguna. Semua integrasi terjadi melalui file `AGENTS.md` yang dihasilkan di direktori aturan.

## 🎯 Kategori Aturan AI

### 🧠 Aturan Memori (Prioritas: Sedang)
**File Algoritma**: [`memory-rules/MEMORY-RULES.md`](memory-rules/MEMORY-RULES.md)
**Pengaturan**: [`memory-rules/settings.json`](memory-rules/settings.json)
**Integrasi yang Dihasilkan**: [`memory-rules/AGENTS.md`](memory-rules/AGENTS.md) (dihasilkan oleh antarmuka web)

**Kemampuan**:
- Penyimpanan pengetahuan terstruktur berbasis markdown
- Sistem tangkap dan cari yang sadar konteks
- Pengenalan pola dan kategorisasi
- Kebijakan retensi adaptif
- Memori persisten antar sesi

**Persyaratan Integrasi**:
- Memerlukan konfigurasi jalur penyimpanan yang valid
- Harus mengimplementasikan semua algoritma memori saat aktif
- Harus terintegrasi dengan aturan RAG untuk konteks yang ditingkatkan

### 🔍 Aturan RAG (Prioritas: Tinggi)
**File Algoritma**: [`rag-rules/RAG-RULES.md`](rag-rules/RAG-RULES.md)
**Pengaturan**: [`rag-rules/settings.json`](rag-rules/settings.json)
**Integrasi yang Dihasilkan**: [`rag-rules/AGENTS.md`](rag-rules/AGENTS.md) (dihasilkan oleh antarmuka web)

**Kemampuan**:
- Pembacaan dan analisis dokumen hierarkis
- Optimasi konteks berbasis relevansi
- Pemrosesan konten multi-bahasa
- Manajemen jendela konteks untuk efisiensi LLM
- Pengenalan pola di seluruh basis kode

**Persyaratan Integrasi**:
- Kritis untuk penggunaan konteks optimal
- Harus mempengaruhi prioritas konstruksi memori
- Harus mengimplementasikan algoritma penilaian relevansi

### 🤔 Aturan Berpikir Kritis (Prioritas: Tinggi)
**File Algoritma**: [`critical-thinking-rules/CRITICAL-THINKING-RULES.md`](critical-thinking-rules/CRITICAL-THINKING-RULES.md)
**Pengaturan**: [`critical-thinking-rules/settings.json`](critical-thinking-rules/settings.json)
**Integrasi yang Dihasilkan**: [`critical-thinking-rules/AGENTS.md`](critical-thinking-rules/AGENTS.md) (dihasilkan oleh antarmuka web)

**Kemampuan**:
- Tantangan asumsi sistematis
- Protokol verifikasi multi-sumber
- Mekanisme penerimaan dan koreksi kesalahan
- Validasi konsistensi logis
- Pelindung penalaran berbasis bukti

**Persyaratan Integrasi**:
- **WAJIB** untuk perilaku AI yang bertanggung jawab
- Harus mengimplementasikan algoritma penerimaan kesalahan
- Kritis untuk mencegah halusinasi

## ⚙️ Sistem Konfigurasi

### Pengaturan Global
**File**: [`settings/global-settings.json`](settings/global-settings.json)
**Tujuan**: Kontrol master untuk komponen framework dan adaptasi platform
**Metode Konfigurasi**: Edit manual atau gunakan antarmuka web

### Pengaturan Khusus Aturan
**Lokasi**: `{rule-name}-rules/settings.json`
**Tujuan**: Konfigurasi perilaku detail untuk aturan individual
**Metode Konfigurasi**: Dimodifikasi oleh antarmuka web saat aturan diaktifkan

### Konfigurasi Bootstrap
**File**: [`bootstrap.json`](bootstrap.json)
**Tujuan**: Orkestrasi yang dapat dibaca mesin dan interkoneksi aturan
**Pembaca**: Sistem agen yang mengimplementasikan framework
**Modifikasi**: Hanya pengguna lanjutan - mendefinisikan urutan pemuatan dan adapter platform

### Konfigurasi Antarmuka Web
**File**: [`setup.html`](setup.html) (tertanam)
**Tujuan**: Antarmuka konfigurasi yang ramah pengguna
**Kemampuan**: Pemilihan bahasa, aktivasi aturan, generasi pengaturan
**Output**: Menghasilkan file `AGENTS.md` untuk aturan yang diaktifkan

## 🚀 Alur Kerja Implementasi

### Untuk Pengguna Non-Teknis (Setup Cepat)
1. **Unduh** file framework ke komputer Anda
2. **Klik ganda** `setup.html` untuk membuka antarmuka web
3. **Pilih** bahasa pilihan Anda (🇺🇸 English / 🇯🇵 日本語 / 🇮🇩 Bahasa Indonesia)
4. **Pilih** aturan AI yang ingin Anda aktifkan
5. **Konfigurasi** pengaturan khusus aturan
6. **Hasilkan** file konfigurasi menggunakan antarmuka bawaan
7. **Copy-paste** file yang dihasilkan ke proyek AI Anda
8. **Selesai!** Agen AI Anda sekarang akan menggunakan perilaku yang ditingkatkan

### Untuk Integrator Framework
1. **Antarmuka Web**: Gunakan `setup.html` untuk konfigurasi terpandu
2. **Tinjau Prinsip**: Baca dokumen ini untuk filosofi framework
3. **Setup Platform**: Konfigurasi [`settings/global-settings.json`](settings/global-settings.json) untuk lingkungan Anda
4. **Integrasi Aturan**: Muat file `AGENTS.md` yang dihasilkan untuk setiap aturan yang diaktifkan
5. **Pemuatan Bootstrap**: Baca [`bootstrap.json`](bootstrap.json) untuk logika orkestrasi
6. **Pantau Operasi**: Tinjau log yang dihasilkan untuk pelacakan penerapan aturan

### Untuk Pengembang Agen
1. **Studi Algoritma**: Baca dokumen aturan spesifik (MEMORY-RULES.md, dll.) untuk detail implementasi
2. **File Integrasi**: Muat `AGENTS.md` dari direktori aturan yang diaktifkan
3. **Implementasi Algoritma**: Eksekusi algoritma aturan menggunakan alat yang tersedia
4. **Log Transparansi**: Catat semua penerapan aturan dan proses keputusan
5. **Kepatuhan Bootstrap**: Hormati persyaratan orkestrasi [`bootstrap.json`](bootstrap.json)
6. **Adaptasi Platform**: Gunakan adapter platform untuk perilaku khusus lingkungan

### Untuk Arsitek Sistem
1. **Desain Framework**: Pahami model integrasi tersebar per-aturan
2. **Perencanaan Platform**: Konfigurasi adapter platform di `bootstrap.json`
3. **Orkestrasi Aturan**: Desain pola interaksi aturan optimal
4. **Penyesuaian Performa**: Sesuaikan pengaturan untuk kasus penggunaan dan skala spesifik
5. **Setup Pemantauan**: Tetapkan prosedur log dan pemantauan kepatuhan

## 🌍 Dukungan Multi-Bahasa

Framework menyediakan dukungan pelokalan lengkap:

- **🇺🇸 English**: Antarmuka dan dokumentasi lengkap
- **🇯🇵 日本語**: Terjemahan Jepang lengkap
- **🇮🇩 Bahasa Indonesia**: Pelokalan Indonesia lengkap

**Pengalihan bahasa** terjadi secara otomatis di antarmuka web dan memengaruhi semua konten yang dihasilkan.

## 📚 Sumber Dokumentasi

### Dokumentasi Pengguna
- **[`README.md`](README.md)**: Panduan setup lengkap dan instruksi penggunaan
- **[`docs/INDEX.md`](docs/INDEX.md)**: Indeks dokumentasi dan navigasi

### Dokumentasi Pengembang
- **[`docs/EXTENSION-MANUAL.md`](docs/EXTENSION-MANUAL.md)**: Panduan langkah demi langkah untuk menambahkan aturan baru
- **[`CORE-RULES.md`](CORE-RULES.md)**: File ini - prinsip dan arsitektur framework

### Referensi Teknis
- **[`bootstrap.json`](bootstrap.json)**: Konfigurasi orkestrasi yang dapat dibaca mesin
- **[`Bootstrap.md`](Bootstrap.md)**: Spesifikasi algoritma detail untuk agen
- **File Algoritma Aturan**: `{rule-name}-rules/{RULE-NAME}-RULES.md` - algoritma implementasi spesifik

## 🔧 Alat Pengembangan

### Antarmuka Web (`setup.html`)
- **Alat Utama**: Antarmuka konfigurasi mandiri
- **Operasi Offline**: Tidak ada ketergantungan jaringan
- **Multi-bahasa**: Pelokalan otomatis
- **Generasi File**: Alur kerja penerapan copy-paste

### Skrip Python
- **`generate_simple_setup.py`**: Alat pengembangan plugin untuk pembaruan antarmuka web
- **`update_localization.py`**: Manajemen pelokalan dan penyematan HTML
- **`setup.py`**: Antarmuka baris perintah untuk pengguna lanjutan

## ⚠️ Catatan Integrasi Kritis

### Isolasi Framework
**WAJIB**: Framework agentic-rules adalah alat pengembangan saja. Jangan pernah menyertakan file framework dalam basis kode proyek pengguna.

### Integrasi Tersebar
**DIWAJIBKAN**: Agen harus memuat file `AGENTS.md` dari direktori aturan individual (dihasilkan oleh antarmuka web) daripada file framework secara langsung.

### Kepatuhan Bootstrap
**KRITIS**: Agen harus menghormati konfigurasi [`bootstrap.json`](bootstrap.json) dan hanya mengeksekusi aturan yang diaktifkan.

### Implementasi Aktif
**WAJIB**: Konfigurasi saja tidak cukup. Agen harus benar-benar mengimplementasikan dan mengeksekusi semua algoritma aturan di lingkungan runtime mereka.

---

<!-- METADATA: Aturan inti dan pedoman integrasi untuk pengembang -->
<!-- LICENSE: Copyright (c) 2025 Paulus Ery Wasito Adhi - Dilisensikan di bawah Lisensi MIT. Lihat file LICENSE. -->