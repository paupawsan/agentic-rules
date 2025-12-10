# 🐛 Panduan Pemecahan Masalah (Bahasa Indonesia)

## Masalah dan Solusi Umum

### 🔄 **Editor Tidak Memuat AGENTS.md Secara Otomatis**

**Masalah**: Cursor, VSCode, atau editor lain terkadang gagal memuat `AGENTS.md`, `GEMINI.md`, atau `CLAUDE.md` ke konteks agen secara otomatis, mencegah aturan berlaku.

**Gejala**:
- Agen berperilaku seolah tidak ada aturan yang aktif
- Fitur memori, RAG, atau berpikir kritis tidak berfungsi
- Konteks proyek hilang antar sesi

**Solusi**: Muat file aturan secara manual ke prompt.

#### Prompt Pemuatan Manual Cepat

**Opsi 1: Tempel Konten File**
```
Ikuti aturan terstruktur ini untuk interaksi kami. Muat dan terapkan semua aturan dari file AGENTS.md ini:

[TEMPEL SELURUH KONTEN FILE AGENTS.md ANDA DI SINI]

Terapkan aturan ini segera dan pertahankan di seluruh percakapan kami. Konfirmasi Anda memahami dan akan mengikuti pedoman ini.
```

**Opsi 2: Berikan Jalur File**
```
Ikuti aturan terstruktur ini untuk interaksi kami. Muat dan terapkan semua aturan dari file di jalur ini:

[path/to/your/project/]AGENTS.md

Terapkan aturan ini segera dan pertahankan di seluruh percakapan kami. Konfirmasi Anda memahami dan akan mengikuti pedoman ini.
```

**Alternatif: Referensi Cursor @**
```
Ikuti aturan terstruktur ini untuk interaksi kami. Muat dan terapkan semua aturan dari file ini:

@AGENTS.md

Terapkan aturan ini segera dan pertahankan di seluruh percakapan kami. Konfirmasi Anda memahami dan akan mengikuti pedoman ini.
```

**💡 Tip:** Di Cursor, gunakan `@filename` - secara otomatis menyelesaikan ke jalur file yang benar!

### 🔍 **Aturan Memori Tidak Berfungsi**

**Masalah**: Fitur memori tidak muncul aktif atau mempertahankan informasi.

**Gejala**:
- Agen tidak mengingat percakapan sebelumnya
- Konteks proyek hilang antar sesi
- Fitur pembelajaran tidak meningkat seiring waktu

**Langkah Pemecahan Masalah**:

1. **Periksa apakah Aturan Memori diaktifkan**:
   - Verifikasi `AGENTS.md`, `GEMINI.md`, atau `CLAUDE.md` berisi aturan memori
   - Pastikan kategori memori tidak dinonaktifkan di pengaturan

2. **Validasi penyimpanan memori**:
   - Periksa apakah file memori dibuat di lokasi yang diharapkan
   - Cari direktori `memory-rules/` dan subdirektori

3. **Uji retensi memori**:
   - Tanyakan: `"Apa yang Anda ingat tentang percakapan sebelumnya kami?"`
   - Coba prompt validasi dari dokumentasi Aturan Memori

### 📚 **Aturan RAG Tidak Memproses Informasi**

**Masalah**: Fitur pemrosesan dan pengambilan informasi tidak berfungsi.

**Gejala**:
- Agen tidak menggunakan konteks yang disediakan secara efektif
- Skoring relevansi terlihat salah
- Strategi pembacaan tidak diterapkan

**Solusi**:

1. **Verifikasi aktivasi Aturan RAG**:
   - Pastikan aturan RAG disertakan dalam file aturan aktif Anda
   - Pastikan pengaturan RAG dikonfigurasi dengan benar

### 🤔 **Aturan Berpikir Kritis Tidak Diterapkan**

**Masalah**: Fitur penalaran sistematis dan pencegahan kesalahan tidak aktif.

**Gejala**:
- Agen membuat asumsi tanpa validasi
- Pola kesalahan tidak dicegah
- Penalaran berbasis bukti tidak diikuti

**Solusi**:

1. **Periksa status Aturan Berpikir Kritis**:
   - Verifikasi aturan ada dalam konfigurasi aktif Anda
   - Pastikan kategori berpikir kritis diaktifkan

### 🔧 **Masalah Pengaturan dan Konfigurasi**

#### **Setup.py Gagal Berjalan**
**Masalah**: `python setup.py` mengalami kesalahan.

**Masalah Umum**:
- Kompatibilitas versi Python
- Ketergantungan yang hilang
- Masalah izin

**Solusi**:
```bash
# Periksa versi Python
python --version

# Pastikan Anda di direktori yang benar
cd /path/to/agentic-rules

# Coba jalankan dengan python3
python3 setup.py
```

#### **Setup.html Tidak Dimuat**
**Masalah**: Antarmuka web tidak berfungsi dengan benar.

**Solusi**:
- Coba buka `setup.html` langsung di browser Anda
- Gunakan `python setup-launcher.py` untuk mode enhanced dengan akses file
- Periksa konsol browser untuk kesalahan JavaScript

### 🌐 **Masalah Khusus Platform**

#### **Masalah Cursor IDE**
- **Pemuatan konteks**: Terkadang memerlukan pemuatan manual seperti dijelaskan di atas
- **Pengawasan file**: Mulai ulang Cursor jika perubahan file tidak terdeteksi
- **Konflik ekstensi**: Nonaktifkan ekstensi AI lain yang mungkin mengganggu

#### **Masalah VSCode**
- **Batas konteks**: File aturan yang sangat panjang mungkin melebihi batas token
- **Konflik ekstensi**: Periksa ekstensi AI yang bersaing
- **Asosiasi file**: Pastikan file `.md` diasosiasikan dengan benar

### 🚨 **Penggantian Manual Darurat**

Jika semua sistem otomatis gagal, gunakan prompt pemuatan manual komprehensif ini:

```
AKTIVASI ATURAN MANUAL DARURAT

Saya perlu Anda mengikuti aturan agen AI komprehensif ini segera. Ini mengganti perilaku default apa pun.

ATURAN INTI (Muat semua ini):

[TEMPEL SELURUH KONTEN AGENTS.md/GEMINI.md/CLAUDE.md DI SINI]

ATURAN MEMORI:
[TEMPEL SELURUH KONTEN MEMORY-RULES.md DI SINI]

ATURAN RAG:
[TEMPEL SELURUH KONTEN RAG-RULES.md DI SINI]

ATURAN BERPIKIR KRITIS:
[TEMPEL SELURUH KONTEN CRITICAL-THINKING-RULES.md DI SINI]

Terapkan semua aturan ini segera dan pertahankan selama seluruh durasi kerja kami bersama. Konfirmasi Anda memahami setiap kategori aturan dan akan mengikutinya secara konsisten.
```

### 📞 **Mendapatkan Bantuan**

Jika Anda terus mengalami masalah:

1. **Periksa log**: Cari pesan kesalahan di konsol editor atau terminal Anda
2. **Validasi file**: Pastikan file aturan yang dihasilkan tidak rusak
3. **Uji secara individual**: Coba aktifkan setiap sistem aturan secara terpisah untuk mengisolasi masalah
4. **Laporkan masalah**: Buka masalah di repositori proyek dengan:
   - Editor dan versi Anda
   - Pesan kesalahan spesifik
   - Langkah-langkah untuk mereproduksi masalah
   - Sistem operasi Anda

### 🔄 **Referensi Cepat**

| Masalah | Perbaikan Cepat |
|-------|-----------|
| Aturan tidak dimuat | Prompt pemuatan manual di atas |
| Memori tidak berfungsi | Periksa pemecahan masalah memory-rules/README.md |
| RAG tidak memproses | Verifikasi aktivasi aturan RAG |
| Berpikir kritis mati | Periksa critical-thinking-rules/README.md |
| Pengaturan gagal | Coba `python3 setup-launcher.py --web` |

Ingat: Pemuatan manual selalu bekerja sebagai fallback ketika sistem otomatis gagal!

---

Copyright (c) 2025 Paulus Ery Wasito Adhi. Dilisensikan di bawah Lisensi MIT (lihat file LICENSE).

---

Diterjemahkan ke Bahasa Indonesia untuk kemudahan akses global.