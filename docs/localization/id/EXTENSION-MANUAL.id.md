# Manual Ekstensi Framework (Bahasa Indonesia)

Manual ini memberikan panduan komprehensif untuk memperluas framework aturan agentic dengan aturan baru. Framework sekarang menyertakan alat scaffolding plugin otomatis untuk pengembangan cepat.

## Mulai Cepat: Pembuatan Plugin Otomatis

**🎯 Pendekatan yang Direkomendasikan**: Gunakan generator scaffold otomatis untuk pembuatan plugin instan!

### Opsi 1: Pembuatan Plugin Interaktif
```bash
python generate_plugin_scaffold.py
```
**Fitur:**
- Antarmuka wizard terpandu
- Generasi file otomatis
- Dukungan multi-bahasa
- Pendaftaran plugin di `plugins.json`

### Opsi 2: Pembuatan Plugin Baris Perintah
```bash
# Buat dari nol
python generate_plugin_scaffold.py --name my-plugin --description "Plugin hebat saya"

# Buat dari template plugin yang ada (tidak perlu deskripsi)
python generate_plugin_scaffold.py --template memory-rules --name my-memory-plugin

# Plugin multi-bahasa (deskripsi diperlukan)
python generate_plugin_scaffold.py --name my-plugin --description "Contoh plugin multi-bahasa" --langs en,ja,id,zh

# Lanjutan: dinonaktifkan secara default
python generate_plugin_scaffold.py --name experimental-plugin --no-enable --description "Fitur eksperimental"
```

### Apa yang Dibuat Generator Scaffold
```
my-plugin/
├── README.md              # Dokumentasi plugin komprehensif
├── RULES.md.en           # Algoritma aturan Inggris dengan framework keamanan
├── RULES.md.ja           # Template pelokalan Jepang (jika diminta)
├── RULES.md.id           # Template pelokalan Indonesia (jika diminta)
├── RULES.md.zh           # Template pelokalan Cina (jika diminta)
├── settings.json         # Konfigurasi lengkap dengan default yang masuk akal
├── setup.json           # Konfigurasi antarmuka web dengan pelokalan
└── [Plugin secara otomatis terdaftar di plugins.json]
```

**✅ Manfaat:**
- ⚡ **Instan**: Plugin lengkap dalam hitungan detik
- 🎯 **Siap Framework**: Semua titik integrasi dikonfigurasi
- 🌍 **Multi-Bahasa**: Template dalam semua bahasa yang diminta
- 🔧 **Terintegrasi Web**: Muncul otomatis di setup.html
- 📚 **Terdokumentasi**: Termasuk contoh penggunaan dan pemecahan masalah
- 🛡️ **Aman**: Termasuk tindakan pencegahan keamanan dan validasi

**🔄 Untuk Pelokalan Lanjutan:**
Setelah generasi scaffold, jika Anda memerlukan string pelokalan kustom di luar template dasar:
```bash
# Edit localization.json dengan string kustom Anda
# Kemudian perbarui setup.html secara otomatis
python update_localization.py
```

---

## Pengembangan Plugin Manual (Lanjutan)

Untuk pengguna lanjutan yang membutuhkan kontrol penuh atau ingin memahami internal framework, ikuti langkah manual ini. Kami menggunakan penambahan aturan RAG sebagai contoh kasus penggunaan.

## Memahami Mekanisme Penemuan Plugin

### CLI vs Penemuan Antarmuka Web

Framework memiliki **dua mekanisme penemuan plugin yang berbeda**:

#### CLI (`setup.py`) - Penemuan Dinamis
- **Otomatis**: Memindai direktori yang diakhiri dengan `-rules`
- **Real-time**: Menemukan plugin dengan memeriksa file `RULES.md.*`
- **Fleksibel**: Bekerja dengan bahasa apa saja, mendukung fallback
- **Tidak diperlukan pendaftaran**: Cukup buat direktori dan file

#### Web (`setup.html`) - Manifes Statis
- **Berbasis manifes**: Membaca dari file `plugins.json`
- **Pra-kompilasi**: Menggunakan `generate_simple_setup.py` untuk menyematkan konfigurasi
- **Terstruktur**: Memerlukan file `setup.json` untuk setiap plugin
- **Diperlukan pendaftaran**: Harus ditambahkan ke `plugins.json` dan jalankan generator

### Mengapa Dua Sistem?
- **CLI**: Untuk pengembang dan pengguna daya yang menginginkan penemuan plugin segera
- **Web**: Untuk pengguna akhir yang membutuhkan pengalaman klik ganda sederhana
- **Keduanya**: Memastikan kompatibilitas lengkap di semua skenario penggunaan

## Memahami Struktur Bootstrap

Sebelum memperluas, pahami komponen bootstrap:

```json
{
  "entry_points": {
    "global_config": "settings/global-settings.json",
    "rag_config": "rag-rules/settings.json",        // Prioritas tinggi: dimuat pertama
    "memory_config": "memory-rules/settings.json",   // Prioritas sedang: dimuat kedua
    // Tambahkan konfigurasi aturan baru di sini
    "critical_thinking_config": "critical-thinking-rules/settings.json"  // Prioritas tinggi
  },
  "loading_sequence": [
    // Urutan pemuatan berbasis prioritas (angka langkah yang lebih rendah = prioritas lebih tinggi)
    // 1. Persetujuan pengguna dan konfigurasi global (selalu pertama)
    // 2. Aturan prioritas tinggi (RAG untuk optimasi konteks)
    // 3. Aturan prioritas sedang (Memori yang ditingkatkan oleh RAG)
    // 4. Aturan prioritas tinggi (Berpikir Kritis untuk validasi)
  ],
  "rule_interconnections": {
    // Bagaimana aturan berkomunikasi satu sama lain
  },
  "platform_adapters": {
    // Konfigurasi khusus platform
  },
  "framework_validation": {
    // Persyaratan validasi file
  }
}
```

## Langkah demi Langkah: Menambahkan Aturan RAG (Contoh Kasus Penggunaan)

### Langkah 1: Buat Struktur Direktori Aturan
```bash
mkdir -p rag-rules
```

### Langkah 2: Buat Spesifikasi Algoritma Aturan
Buat file algoritma aturan dalam semua bahasa yang didukung:

**File Algoritma Utama:** [`../rag-rules/RAG-RULES.md`](../rag-rules/RAG-RULES.md) (Inggris - referensi utama)

**File Aturan Pelokalan:**
- [`rag-rules/RULES.md.en`](../rag-rules/RULES.md.en) - Versi Inggris (identik dengan RAG-RULES.md)
- [`rag-rules/RULES.md.ja`](../rag-rules/RULES.md.ja) - Versi Jepang
- [`rag-rules/RULES.md.id`](../rag-rules/RULES.md.id) - Versi Indonesia

### Langkah 3: Buat File Konfigurasi

### Langkah 4: Perbarui Integrasi

### Langkah 5: Uji dan Validasi

## Topik Ekstensi Lanjutan

### Interkoneksi Aturan

### Adaptasi Platform

### Pengujian dan Validasi

---

**🔧 Pengembang ekstensi**: Framework ini memberikan fleksibilitas lengkap untuk meningkatkan sistem agen dengan perilaku AI baru.

---

Copyright (c) 2025 Paulus Ery Wasito Adhi. Dilisensikan di bawah Lisensi MIT (lihat file LICENSE).

---

Diterjemahkan ke Bahasa Indonesia untuk kemudahan akses global.