# {{display_name}}

{{description}}

## Ikhtisar

Ini adalah plugin kustom untuk Agentic Rules Framework yang menyediakan fungsionalitas {{plugin_name_kebab}} untuk agen AI.

## Fitur

- **Implementasi Algoritma**: Menyediakan algoritma terstruktur untuk operasi {{plugin_name_kebab}}
- **Manajemen Konfigurasi**: Pengaturan fleksibel melalui `settings.json`
- **Dukungan Multi-bahasa**: Template tersedia dalam berbagai bahasa
- **Integrasi Framework**: Integrasi mulus dengan Agentic Rules Framework

## Instalasi

1. Salin direktori plugin ini ke framework agentic-rules Anda
2. Tambahkan nama plugin ke `plugins.json` (opsional, untuk antarmuka web)
3. Jalankan `python generate_simple_setup.py` untuk memperbarui konfigurasi web
4. Aktifkan plugin dengan `python setup.py`

## Konfigurasi

### Pengaturan Dasar (`settings.json`)

```json
{
  "{{plugin_key}}": {
    "enabled": true,
    "config": {
      "example_setting": "example_value",
      "max_entries": 100,
      "cleanup_days": 90
    },
    "advanced": {
      "debug_mode": false,
      "performance_mode": "balanced"
    }
  }
}
```

### Deskripsi Pengaturan

- `enabled`: Mengaktifkan/menonaktifkan plugin
- `config.max_entries`: Jumlah maksimum entri yang dikelola
- `config.cleanup_days`: Hari penyimpanan data sebelum pembersihan
- `advanced.debug_mode`: Mengaktifkan logging debug
- `advanced.performance_mode`: Mode optimasi performa

## Penggunaan

1. **Aktifkan Plugin**: Setel `enabled: true` di `settings.json`
2. **Aktifkan Aturan**: Gunakan `python setup.py` untuk menghasilkan data aturan
3. **Integrasi**: Salin data aturan yang dihasilkan (mis. `AGENTS.md`) ke proyek Anda
4. **Konfigurasi**: Sesuaikan pengaturan di `{{plugin_name}}/settings.json`

## Algoritma Aturan

Plugin ini mengimplementasikan algoritma berikut:

### Proses Inisialisasi {{pascal_case_name}}
- Menginisialisasi sistem {{plugin_name_kebab}}
- Memvalidasi konfigurasi
- Mengatur struktur data yang diperlukan

### Proses Utama {{pascal_case_name}}
- Memproses interaksi pengguna
- Menerapkan logika {{plugin_name_kebab}}
- Mengembalikan hasil yang diproses

### Proses Pembersihan {{pascal_case_name}}
- Melakukan pembersihan berkala
- Memerlukan persetujuan pengguna
- Mempertahankan integritas data

## Struktur File

```
{{plugin_name}}/
├── README.md              # Dokumentasi ini
├── RULES.md.en           # Template aturan bahasa Inggris
├── RULES.md.ja           # Template bahasa Jepang (jika diminta)
├── RULES.md.id           # Template bahasa Indonesia (jika diminta)
├── settings.json         # Pengaturan default
└── setup.json           # Konfigurasi antarmuka web
```

## Pengembangan

### Menambahkan Bahasa Baru

1. Buat `RULES.md.{{language_code}}` dengan template yang diterjemahkan
2. Tambahkan lokalisasi ke `setup.json`
3. Perbarui `settings.json` jika diperlukan

### Menyesuaikan Algoritma

Edit file `RULES.md.*` untuk mengubah algoritma dan perilaku.

### Pengujian

1. Aktifkan plugin di pengaturan
2. Jalankan setup.py untuk menghasilkan data aturan
3. Uji aturan yang dihasilkan di agen AI Anda

## Pemecahan Masalah

### Plugin Tidak Dikenali
- Pastikan direktori plugin ada
- Pastikan setidaknya ada satu file `RULES.md.*`
- Verifikasi bahwa `plugins.json` berisi nama plugin (untuk antarmuka web)

### Kesalahan Konfigurasi
- Periksa sintaks `settings.json`
- Verifikasi bahwa semua pengaturan yang diperlukan ada
- Pastikan izin file benar

### Aktivasi Aturan Gagal
- Pastikan plugin diaktifkan di pengaturan
- Verifikasi bahwa setup.py berhasil diselesaikan
- Pastikan data aturan yang dihasilkan disalin dengan benar

## Lisensi

Copyright (c) {{current_year}} {{author_name}}

Dilisensikan di bawah Lisensi MIT. Lihat file LICENSE untuk detail.

## Kontribusi

Kontribusi diterima dengan baik! Silakan:

1. Fork repositori
2. Buat branch fitur
3. Buat perubahan Anda
4. Uji secara menyeluruh
5. Ajukan pull request

Untuk perubahan besar, silakan buka issue terlebih dahulu untuk mendiskusikan perubahan yang diusulkan.
