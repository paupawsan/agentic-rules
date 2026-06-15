# 👥 Panduan Pengguna - Agentic Rules Framework (Bahasa Indonesia)

## Untuk Semua Orang (Tidak Perlu Pengetahuan Teknis!)

**Tidak perlu pengetahuan teknis sama sekali!** Panduan ini akan memandu Anda mengatur aturan agen AI dengan klik ganda sederhana.

## 🚀 Pengaturan Pertama Kali - Proses Lengkap

### ⚠️ **PENTING: Ikuti Urutan Ini!**

**Selesaikan setup.html TERLEBIH DAHULU, lalu inisialisasi bootstrap. Antarmuka web membuat file yang dibutuhkan bootstrap.**

---

### **Fase 1: Konfigurasi Web (WAJIB PERTAMA)**

#### **Langkah 1: Unduh dan Luncurkan Pengaturan**
1. **Unduh** file framework `agentic-rules` dari GitHub
2. **Ekstrak** file ke folder mana saja di komputer Anda
3. **Klik ganda** `setup.html` untuk membuka antarmuka web

#### **Langkah 2: Konfigurasi Aturan Anda**
1. **Pilih Bahasa** dari opsi yang didukung
2. **Pilih Aturan** yang ingin diaktifkan:
   - 🧠 **Aturan Memori**: AI mengingat konteks di seluruh percakapan
   - 📚 **Aturan RAG**: AI mencari dan menggunakan informasi yang relevan lebih baik
   - 🤔 **Aturan Berpikir Kritis**: AI lebih hati-hati dan akurat
3. **Klik "Hasilkan File Konfigurasi"**

> 💡 **Ini membuat file aturan dan konfigurasi yang dibutuhkan bootstrap!**

---

### **Fase 2: Inisialisasi Bootstrap (SETELAH setup.html)**

#### **Langkah 3: Inisialisasi Framework**
Beritahu agen AI Anda: **`Inisialisasi sistem aturan agentic di folder /path/to/your/agentic-rules. Saya sudah menyelesaikan setup.html, jadi lakukan saja inisialisasi bootstrap.`**

#### **Langkah 4: Berikan Izin Bootstrap**
Ketika diminta: *"Bootstrap configuration not found. Initialize Agentic Rules Framework? (y/n)"*
- Ketik: `y` dan tekan Enter

#### **Langkah 5: Konfirmasi Persetujuan Pengguna**
Ketika diminta: *"The Agentic Rules Framework enhances AI behavior... Do you want to enable this framework? (y/n)"*
- Ketik: `y` dan tekan Enter

#### **Langkah 6: Tinjau Pengaturan Framework**
Tinjau pengaturan untuk aturan yang Anda pilih. Ini harus cocok dengan pilihan setup.html Anda.

#### **Langkah 7: Framework Aktif!**
✅ **Pengaturan lengkap** - konfigurasi web dan inisialisasi bootstrap selesai
✅ **Aturan dikonfigurasi** - fitur yang dipilih aktif
✅ **Siap digunakan** - kemampuan AI yang ditingkatkan tersedia secara otomatis

---

## 🚀 Menggunakan Fitur Framework

## 🚀 Mulai Cepat (Metode Klik Ganda)

### Langkah 1: Unduh Framework
1. Unduh file framework `agentic-rules` dari GitHub
2. Ekstrak/unzip file yang diunduh ke folder mana saja di komputer Anda

### Langkah 2: Luncurkan Pengaturan
1. **Klik ganda** `setup.html` di folder yang diekstrak
2. Browser web default Anda akan terbuka secara otomatis

### Langkah 3: Konfigurasi Aturan Anda
1. **Pilih Bahasa**: Pilih dari bahasa yang didukung secara resmi
   - 🇺🇸 **English** (Bahasa utama)
   - 🇯🇵 **日本語** (Bahasa Jepang)
   - 🇮🇩 **Bahasa Indonesia**

   > 💡 **Untuk Pengembang Plugin**: Jika Anda ingin membuat plugin kustom dengan bahasa tambahan (🇩🇪 Deutsch, 🇫🇷 Français, 🇪🇸 Español, dll.), lihat [Manual Ekstensi](EXTENSION-MANUAL.id.md) untuk detail teknis penggunaan `generate_plugin_scaffold.py` dengan dukungan template multi-bahasa.
2. **Pilih Aturan**: Centang kotak untuk perilaku AI yang Anda inginkan:
   - 🧠 **Aturan Memori**: Membantu AI mengingat konteks di seluruh percakapan
   - 📚 **Aturan RAG**: Meningkatkan kemampuan AI untuk mencari dan menggunakan informasi yang relevan
   - 🤔 **Aturan Berpikir Kritis**: Membuat AI lebih hati-hati dan akurat

### Langkah 4: Hasilkan Konfigurasi
1. Klik **"Hasilkan File Konfigurasi"**
2. Antarmuka akan membuat aturan AI yang dipersonalisasi untuk Anda

### Langkah 5: Simpan File Anda
Pilih cara menyimpan file:

- **💾 Simpan**: Membuka browser file untuk memilih tempat penyimpanan yang tepat
- **📥 Unduh**: Mengunduh file langsung ke folder Downloads Anda
- **📋 Salin**: Menyalin konten ke clipboard untuk penyimpanan manual

### Langkah 6: Gunakan dengan Agen AI Anda
1. Salin file yang dihasilkan ke direktori root proyek AI Anda
2. Konfigurasi agen AI Anda untuk memuat file aturan
3. Agen AI Anda sekarang memiliki kemampuan yang ditingkatkan!

## 📂 Struktur File Setelah Pengaturan

Proyek AI Anda harus terlihat seperti ini:
```
your-ai-project/
├── AGENTS.md              # Konfigurasi agen utama
├── modules/               # Direktori modul plugin
│   ├── memory-rules/      # Aturan sistem memori
│   │   ├── AGENTS.md     # Aturan khusus memori
│   │   └── settings.json # Konfigurasi memori
│   ├── rag-rules/        # Aturan sistem RAG
│   │   ├── AGENTS.md     # Aturan khusus RAG
│   │   └── settings.json # Konfigurasi RAG
│   └── critical-thinking-rules/  # Aturan berpikir kritis
│       ├── AGENTS.md     # Aturan khusus berpikir
│       └── settings.json # Konfigurasi berpikir
```

## 🎯 Apa yang Dilakukan Setiap Aturan

### 🧠 Aturan Memori
- Mengingat informasi penting di seluruh percakapan
- Mempertahankan konteks antara sesi
- Membantu AI belajar dari interaksi sebelumnya

### 📚 Aturan RAG
- Mencari informasi relevan dari file Anda
- Mengoptimalkan cara AI membaca dan memproses informasi
- Meningkatkan akurasi respons dengan konteks yang lebih baik

### 🤔 Aturan Berpikir Kritis
- Membuat AI memeriksa ulang jawabannya
- Mengurangi kesalahan dan "halusinasi"
- Mendorong respons yang lebih hati-hati dan akurat

### 🧠 Kecerdasan Knowledge Graph (KG)
- **Pembelajaran Otomatis**: AI membangun peta pengetahuan dari proyek Anda
- **Koneksi Cerdas**: Menemukan hubungan antara kode, file, dan konsep
- **Pemahaman Ditingkatkan**: Memberikan wawasan yang lebih dalam tentang basis kode Anda
- **Memori Konteks**: Mengingat bagaimana berbagai bagian proyek Anda saling terkait

## 🧠 Bagaimana Knowledge Graphs Meningkatkan Pengalaman AI Anda

### Apa Itu Knowledge Graphs?

Knowledge Graphs (KG) adalah peta cerdas yang dibangun AI secara otomatis. KG menciptakan koneksi visual antara berbagai bagian proyek Anda, membuat AI "memahami" basis kode seperti ahli manusia.

```
🎯 Contoh: AI Anda menganalisis basis kode ini dan membuat koneksi:

File Kode ←→ Fungsi ←→ Dependensi ←→ Fitur
    ↓         ↓         ↓         ↓
"main.py" ←→ "process_data()" ←→ "pandas" ←→ "Pemrosesan Data"
"utils.py" ←→ "validate_input()" ←→ "None" ←→ "Validasi Input"
"config.py" ←→ "load_settings()" ←→ "json" ←→ "Konfigurasi"
```

### Bagaimana Konstruksi KG Bekerja Secara Otomatis

**🤖 Arsitektur Agen Tunggal**: Agen AI Anda membangun KG menggunakan kecerdasan sendiri + algoritma framework

```
Pengguna Bekerja dengan Proyek → AI Menganalisis Kode → Pemicu Konstruksi KG → Peta Pengetahuan Dibuat
        ↓                              ↓                              ↓                    ↓
   "analisis file ini"           "ekstrak entitas"              "temukan hubungan"    "simpan koneksi"
```

**⚡ Pemrosesan Latar Belakang**: Konstruksi KG terjadi secara tersembunyi saat Anda bekerja:

```
Percakapan Utama: "bantu saya memahami proyek ini"
    ↓
AI merespons segera + memunculkan konstruksi KG di latar belakang:
├── 🔍 Penemuan Entitas (fungsi, kelas, file)
├── 🔗 Pemetaan Hubungan (dependensi, pemanggilan, import)
├── 🏗️ Konstruksi Graph (hubungkan komponen terkait)
├── 💾 Penyimpanan Memori (simpan untuk penggunaan di masa depan)
└── ⚡ Persiapan Query (siap untuk pertanyaan kompleks)
```

### Manfaat Praktis yang Anda Dapatkan

#### **1. Penjelasan Kode yang Lebih Cerdas**
```
❌ Tanpa KG: "Fungsi ini memproses input pengguna"
✅ Dengan KG: "validate_input() memproses data pengguna, terhubung dengan error_handler()
              untuk validasi, digunakan oleh process_user_request() di main.py, dan
              menangani sanitasi data"
```

#### **2. Navigasi Proyek Cerdas**
```
Pengguna: "Bagaimana sistem autentikasi bekerja?"
KG-Powered AI: Menunjukkan alur auth lengkap dengan semua komponen yang terhubung
```

#### **3. Pemahaman Dependensi**
```
Pengguna: "Apa yang terjadi jika saya mengubah config database ini?"
KG-Powered AI: "Mempengaruhi: user_auth() → db_connection() → data_validator() → api_response()"
```

#### **4. Pengenalan Pola**
```
Pengguna: "Mirip dengan sistem login saya?"
KG-Powered AI: "Pola auth Anda cocok dengan: login_flow() → validate_creds() → create_session()"
```

### Contoh Visualisasi KG

#### **Peta Arsitektur Proyek**
```
┌─────────────────────────────────────────────────────────────┐
│                      KG PROYEK ANDA                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐     │
│  │   Frontend  │◄───┤   Backend   │◄───┤  Database   │     │
│  │             │    │             │    │             │     │
│  │  • React    │    │  • API      │    │  • PostgreSQL│     │
│  │  • UI/UX    │    │  • Auth     │    │  • Users     │     │
│  │  • Forms    │    │  • Business │    │  • Sessions  │     │
│  └─────────────┘    └─────────────┘    └─────────────┘     │
│          ▲                   ▲                   ▲         │
│          │                   │                   │         │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐     │
│  │   Config    │◄───┤   Utils     │◄───┤   Models    │     │
│  │             │    │             │    │             │     │
│  │  • Settings │    │  • Helpers  │    │  • Schemas  │     │
│  │  • Env vars │    │  • Format   │    │  • Validation│     │
│  │  • Secrets  │    │  • Logging  │    │  • Types     │    │
│  └─────────────┘    └─────────────┘    └─────────────┘     │
└─────────────────────────────────────────────────────────────┘

Legenda: ◄─── Dependensi langsung    ···· Hubungan tidak langsung
```

#### **Jaringan Hubungan Komponen**
```
Alur Autentikasi Pengguna:
login_page.html → login_api.py → user_model.py → database.py
       ↓              ↓              ↓              ↓
   "submit form" → "validasi input" → "periksa user" → "query users"
```

### Kapan KG Paling Berguna

#### **🚀 Paling Baik Untuk:**
- **Basis Kode Besar**: Memahami struktur proyek kompleks
- **Kolaborasi Tim**: Onboarding developer baru
- **Keputusan Arsitektur**: Merencanakan penambahan fitur
- **Debugging**: Melacak masalah melalui komponen yang terhubung
- **Refactoring**: Memahami dampak perubahan kode

#### **📈 Query Tingkat Lanjut yang Dapat Anda Ajukan:**
```
"Perlihatkan semua fungsi yang menangani data pengguna"
"Komponen apa yang bergantung pada sistem pembayaran?"
"Bagaimana alur penanganan error melalui aplikasi?"
"Temukan pola serupa dengan fitur baru saya"
"Apa yang akan rusak jika saya mengubah skema database ini?"
```

### Pengaturan Konstruksi KG

**Untuk Pengguna Tingkat Lanjut**: Anda dapat mengontrol perilaku KG di `modules/rag-rules/settings.json`:

```json
{
  "kg_background_processing": {
    "enabled": true,              // Aktifkan konstruksi KG otomatis
    "separate_conversation": true, // Jangan pernah mengganggu pekerjaan Anda
    "minimal_construction": true,  // Hanya bangun apa yang diperlukan
    "project_analysis_only": true, // Cakup ke proyek saat ini
    "batch_processing": true,      // Proses secara efisien
    "no_user_waiting": true        // Respons instan selalu
  }
}
```

### Privasi & Performa

**🛡️ Data Anda Tetap Privat:**
- KG dibangun dari file lokal Anda saja
- Tidak ada data yang dikirim ke server eksternal
- Pengetahuan tetap dalam lingkungan proyek Anda

**⚡ Dioptimalkan Performa:**
- Pemrosesan latar belakang mencegah perlambatan
- Pembaruan inkremental (hanya perubahan yang diproses)
- Cache cerdas untuk komponen yang sering diakses
- Jejak memori minimal

### Memulai dengan Kecerdasan KG

**🎯 Mulai Sederhana:**
1. **Aktifkan RAG Rules** di setup.html (termasuk kemampuan KG)
2. **Bekerja secara normal** - KG dibangun otomatis di latar belakang
3. **Ajukan pertanyaan yang lebih dalam** - AI sekarang memahami hubungan proyek
4. **Rasakan respons yang ditingkatkan** - Jawaban yang lebih akurat dan kontekstual

**Itu saja!** AI Anda menjadi jauh lebih cerdas tentang basis kode melalui konstruksi KG otomatis. 🧠✨

## 🔧 Pemecahan Masalah

### Pengaturan Tidak Terbuka
- Coba klik kanan `setup.html` dan pilih "Buka dengan" browser web Anda
- Pastikan Anda membuka file dari folder yang diekstrak, bukan dari dalam arsip ZIP

### File Tidak Dapat Disimpan
- Periksa apakah browser Anda memiliki izin untuk menyimpan file
- Coba gunakan opsi **📥 Unduh** terlebih dahulu, lalu pindahkan file secara manual

### Bahasa Tidak Berubah
- Segarkan halaman setelah mengubah bahasa
- Jika terjemahan tidak muncul, hapus cache browser

## 💡 Tips

- **Mulai Sederhana**: Mulai dengan 1-2 aturan untuk memahami cara kerjanya
- **Uji Secara Bertahap**: Coba agen AI Anda dengan aturan baru pada tugas sederhana terlebih dahulu
- **Cadangkan Dulu**: Simpan konfigurasi AI yang ada sebelum menambahkan aturan baru
- **Eksperimen**: Kombinasi aturan yang berbeda bekerja lebih baik untuk jenis tugas yang berbeda

## 📞 Butuh Bantuan?

- Periksa bagian [pemecahan masalah](#-pemecahan-masalah) di atas
- Tinjau [panduan pengembang](DEVELOPER-GUIDE.md) untuk opsi lanjutan
- Buka issue di GitHub untuk masalah teknis

---

**🎉 Selamat!** Agen AI Anda sekarang memiliki kemampuan yang ditingkatkan melalui Agentic Rules Framework.

---

Copyright (c) 2025-2026 Paulus Ery Wasito Adhi. Dilisensikan di bawah Lisensi MIT (lihat file LICENSE).

---

Diterjemahkan ke Bahasa Indonesia untuk kemudahan akses global.