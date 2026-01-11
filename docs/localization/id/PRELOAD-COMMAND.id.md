# 📥 Perintah Preload Agentic Rules

Perintah **Preload Agentic Rules** memungkinkan Anda untuk secara manual memuat aturan sistem dan konfigurasi dari direktori yang ditentukan ke dalam konteks operasional agen.

## 🎯 Tujuan

Perintah ini berguna ketika:
- Cursor tidak secara otomatis mendeteksi aturan agen bersarang
- Anda perlu memuat aturan dari lokasi direktori yang berbeda
- Anda ingin secara eksplisit memuat konfigurasi sistem tertentu
- Agen perlu memahami kerangka kerja atau set aturan dari proyek lain

## 📋 Sintaks Perintah

```
/agentic-rules/preload-agentic-rules [TARGET_DIRECTORY]
```

### Parameter

- **`TARGET_DIRECTORY`** (opsional): Path ke direktori yang berisi file aturan sistem
  - Dapat berupa path absolut: `/Users/username/Projects/my-agent-rules`
  - Dapat berupa path relatif: `../my-agent-rules` atau `./subfolder/rules`
  - Jika dihilangkan, perintah akan meminta Anda secara interaktif

## 💡 Contoh Penggunaan

### Contoh 1: Memuat dari Path Absolut
```bash
/agentic-rules/preload-agentic-rules /Users/paupawsan/Library/CloudStorage/GoogleDrive-paupawsan@gmail.com/My Drive/AI/local-as/agentic-rules
```

### Contoh 2: Memuat dari Path Relatif
```bash
# Relatif terhadap workspace saat ini
/agentic-rules/preload-agentic-rules ../my-agent-rules

# Relatif terhadap direktori saat ini
/agentic-rules/preload-agentic-rules ./config/rules
```

### Contoh 3: Mode Interaktif
```bash
# Jalankan tanpa argumen - akan meminta direktori
/agentic-rules/preload-agentic-rules
```

## 🔍 File Apa yang Dimuat?

Perintah ini secara otomatis mencari dan memuat file aturan sistem berikut:

- **`AGENTS.md`** - Aturan konfigurasi dan perilaku agen generik
- **`GEMINI.md`** - Konfigurasi sistem khusus Google Gemini
- **`CLAUDE.md`** - Konfigurasi sistem khusus Anthropic Claude

Perintah mencari secara rekursif melalui direktori target dan semua subdirektori, mengecualikan file backup (file yang berakhiran `.backup`).

## ✅ Output yang Diharapkan

Ketika file ditemukan:
```
Scanning for system files in: /path/to/directory
Found 3 system file(s):
  - AGENTS.md
  - modules/memory-rules/AGENTS.md
  - modules/rag-rules/AGENTS.md

Loading system files...

=== LOADING: AGENTS.md ===
[Konten file ditampilkan di sini]
--- END OF AGENTS.md ---

🎉 System loading complete!
System has been loaded from: /path/to/directory
```

Ketika tidak ada file ditemukan:
```
Scanning for system files in: /path/to/directory
No system files found in /path/to/directory

System directories typically contain:
- Agent configuration and behavior files
- Model-specific system configurations
- README.md or documentation files
- Configuration files (.json)
- Rule definition files (.md)
- System specification documents

🎉 System scan complete!
System has been scanned from: /path/to/directory
No system files were found to load.
```

## 🛡️ Fitur Keamanan

- **Tindakan Pengguna Eksplisit Diperlukan**: Hanya memuat ketika diminta secara eksplisit
- **Tidak Ada Auto-Loading**: Tidak pernah secara otomatis memuat atau memproses file
- **Perlindungan File Backup**: Secara otomatis mengecualikan file `.backup`
- **Validasi Direktori**: Memverifikasi direktori ada sebelum memindai
- **Operasi Hanya Baca**: Hanya membaca file, tidak pernah memodifikasinya

## 📝 Persyaratan

- Direktori target harus ada
- File sistem harus diberi nama persis: `AGENTS.md`, `GEMINI.md`, atau `CLAUDE.md`
- Agen harus memiliki akses baca ke direktori yang ditentukan
- Pengguna harus secara eksplisit menjalankan perintah

## 🔧 Pemecahan Masalah

### Masalah: "Directory does not exist"
**Solusi**: Verifikasi path benar. Gunakan path absolut jika path relatif tidak berfungsi.

### Masalah: "No system files found"
**Kemungkinan penyebab**:
- File tidak diberi nama dengan benar (harus `AGENTS.md`, `GEMINI.md`, atau `CLAUDE.md`)
- File berada di subdirektori yang tidak dipindai
- File memiliki ekstensi `.backup`

**Solusi**: 
- Periksa nama file cocok persis
- Verifikasi file ada di direktori target
- Hapus ekstensi `.backup` jika diperlukan

### Masalah: File ditemukan tetapi tidak dimuat
**Solusi**: 
- Periksa izin file (agen memerlukan akses baca)
- Verifikasi file berisi konten yang valid
- Coba jalankan perintah lagi

## 🔗 Dokumentasi Terkait

- **[Panduan Pemecahan Masalah](TROUBLESHOOTING.id.md)** - Masalah umum dan instruksi pemuatan manual
- **[Panduan Pengguna](USER-GUIDE.id.md)** - Setup dan penggunaan kerangka kerja lengkap
- **[Panduan Pengembang](DEVELOPER-GUIDE.id.md)** - Konfigurasi lanjutan dan otomatisasi

## 📚 Praktik Terbaik

1. **Gunakan Path Absolut**: Lebih andal daripada path relatif, terutama saat bekerja di berbagai direktori
2. **Organisir Aturan**: Simpan semua file aturan di direktori khusus untuk manajemen yang lebih mudah
3. **Kontrol Versi**: Lacak file aturan dalam kontrol versi untuk menjaga konsistensi
4. **Uji Setelah Memuat**: Verifikasi agen memahami aturan yang dimuat dengan mengajukan pertanyaan uji

---

**Catatan**: Perintah ini dirancang untuk bekerja dengan mulus dengan Agentic Rules Framework. Setelah memuat, agen akan memahami dan beroperasi sesuai dengan aturan sistem yang dimuat.

<!-- LICENSE: Copyright (c) 2025 Paulus Ery Wasito Adhi - Licensed under the MIT License. See LICENSE file for details. -->
