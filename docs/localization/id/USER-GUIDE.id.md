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
Beritahu agen AI Anda: **`Initialize agentic rules system`** atau **`Setup agentic rules bootstrap`**

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

Copyright (c) 2025 Paulus Ery Wasito Adhi. Dilisensikan di bawah Lisensi MIT (lihat file LICENSE).

---

Diterjemahkan ke Bahasa Indonesia untuk kemudahan akses global.