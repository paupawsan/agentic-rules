# 🔧 Panduan Pengembang - Agentic Rules Framework (Bahasa Indonesia)

## Untuk Insinyur & Pengembang (Pengaturan Lanjutan)

Panduan ini mencakup penggunaan lanjutan, otomasi, dan detail implementasi teknis.

## 🚀 Opsi Pengaturan Lanjutan

### Opsi A: Mode Server Enhanced (Direkomendasikan)

**Akses sistem file lengkap dengan otomasi:**

```bash
# Luncurkan server enhanced (direkomendasikan)
python setup-launcher.py

# Port kustom jika 8000 sedang digunakan
python setup-launcher.py --port 8080

# Mode dasar (dialog unduh)
python setup-launcher.py --web
```

**Manfaat Mode Enhanced:**
- ✅ **Empat opsi penyimpanan**: Salin, Simpan (dialog), Unduh, Buat Langsung
- ✅ **Pembuatan file langsung** - Tidak ada penempatan file manual
- ✅ **Pembersihan otomatis** - Menghapus jenis file yang bertentangan
- ✅ **Umpan balik real-time** - Operasi file segera
- ✅ **Kontrol server** - Penutupan bersih dari antarmuka web

### Opsi B: Antarmuka Baris Perintah

**Kontrol programatik lengkap:**

```bash
# Pengaturan interaktif
python setup.py

# Non-interaktif dengan argumen
python setup.py --lang id --rules memory,rag --file-type GEMINI.md
```

## 📋 Proses Pengaturan Lengkap

### 1. Luncurkan Antarmuka

**Mode Enhanced (Insinyur):**
```bash
python setup-launcher.py
```
Membuka http://localhost:8000/setup.html dengan akses sistem file lengkap.

**Mode Dasar (Siapa saja):**
```bash
open setup.html  # macOS
start setup.html  # Windows
xdg-open setup.html  # Linux
```
Membuka setup.html dengan dialog unduh/simpan.

### 2. Konfigurasi Pengaturan

- **Bahasa Agen**: Pilih bahasa untuk file yang dihasilkan (EN/JA/ID inti, 15+ diperluas untuk plugin)
- **Jenis File**: AGENTS.md (standar), GEMINI.md (Gemini), atau CLAUDE.md (Claude)
- **Pemilihan Aturan**: Aktifkan perilaku AI yang diinginkan

### 3. Hasilkan File

Klik "Hasilkan File Konfigurasi" untuk membuat:
- Root `AGENTS.md`/`GEMINI.md`/`CLAUDE.md`
- File khusus aturan di subdirektori
- File `settings.json` untuk setiap aturan yang diaktifkan

### 4. Metode Penyimpanan

#### 💾 Simpan (Direkomendasikan)
- Membuka dialog penyimpanan file asli
- Pilih lokasi penyimpanan yang tepat
- Dimulai di folder Dokumen
- Browser modern: API sistem file lengkap
- Browser lama: Fallback ke unduh

#### 📥 Unduh
- Mengunduh langsung ke folder Downloads
- Perilaku unduh browser tradisional
- Penempatan file manual diperlukan

#### 📋 Salin
- Menyalin konten ke clipboard
- Tempel dan simpan manual
- Kontrol penuh atas penamaan/lokasi file

#### 📁 Buat (Mode Enhanced Saja)
- Pembuatan file langsung di server
- Penempatan file otomatis
- Tidak ada dialog pengguna yang diperlukan
- Hanya tersedia di mode `python setup-launcher.py`

## 🔧 Arsitektur Teknis

### Struktur File
```
agentic-rules/
├── setup.html              # Antarmuka web utama
├── setup.py               # Skrip pengaturan CLI
├── setup-launcher.py      # Peluncur server enhanced
├── localization.json      # Terjemahan UI
├── bootstrap.json         # Konfigurasi framework
├── CORE-RULES.md         # Ikhtisar framework
└── [rule-name]/          # Direktori aturan
    ├── RULES.md.*        # Template aturan (bahasa inti EN/JA/ID)
    ├── settings.json     # Pengaturan default
    └── setup.json       # Konfigurasi aturan
```

### Proses Integrasi Aturan

1. **Pemuatan Bootstrap**: `bootstrap.json` mendefinisikan struktur framework
2. **Aktivasi Aturan**: Pengguna memilih aturan mana yang akan diaktifkan
3. **Pemrosesan Template**: Template aturan dilokalkan dan diproses
4. **Generasi File**: Membuat file konfigurasi khusus agen
5. **Integrasi Agen**: File ditempatkan di proyek untuk pemuatan agen

## 🛠️ Referensi API

### setup-launcher.py

**Opsi Baris Perintah:**
```bash
python setup-launcher.py [OPTIONS]

Options:
  --port PORT    Port untuk menjalankan server (default: 8000)
  --web         Luncurkan dalam mode dasar (dialog unduh)
  --help        Tampilkan pesan bantuan
```

**Endpoint Server (Mode Enhanced):**
- `GET /` - Sajikan file statis
- `POST /api/create-file` - Buat file langsung
- `POST /api/cleanup-files` - Hapus file yang bertentangan
- `POST /api/shutdown` - Matikan server dengan bersih

### setup.py

**Opsi Baris Perintah:**
```bash
python setup.py [OPTIONS]

Options:
  --ui-lang {en,ja,id}        Bahasa antarmuka (en, ja, id)
  --agent-lang {en,ja,id}     Bahasa template agen (en, ja, id)
  --agent-file-type {AGENTS.md,GEMINI.md,CLAUDE.md}
                               Jenis file agen untuk dihasilkan
  --lang {en,ja,id}           Tetapkan bahasa UI dan agen (en, ja, id)
  --rules RULES               Daftar aturan yang dipisahkan koma, atau "all"
  --help                      Tampilkan pesan bantuan
```

**Catatan:** `setup.py` saat ini mendukung 3 bahasa inti. Untuk dukungan bahasa 18+ lengkap, gunakan antarmuka web (`setup.html`) atau generator scaffold (`generate_plugin_scaffold.py`).

## 🔌 Contoh Integrasi

### Integrasi Cursor
```javascript
// Di konfigurasi Cursor
{
  "agentic-rules": {
    "enabled": true,
    "rules": ["memory", "rag"],
    "language": "en"
  }
}
```

### Ekstensi VSCode
```json
// settings.json
{
  "agenticRules.enabled": true,
  "agenticRules.rules": ["memory", "critical-thinking"],
  "agenticRules.fileType": "AGENTS.md"
}
```

### Integrasi Agen Kustom
```python
# Muat aturan agentic
import json

# Muat konfigurasi bootstrap
with open('bootstrap.json', 'r') as f:
    bootstrap = json.load(f)

# Muat aturan yang diaktifkan
enabled_rules = ['memory-rules', 'rag-rules']
for rule in enabled_rules:
    rule_file = f"{rule}/AGENTS.md"
    settings_file = f"{rule}/settings.json"

    # Muat dan terapkan konfigurasi aturan
    with open(rule_file, 'r') as f:
        rule_content = f.read()

    with open(settings_file, 'r') as f:
        rule_settings = json.load(f)
```

## 🔍 Debug & Pemecahan Masalah

### Server Tidak Dapat Dimulai
```bash
# Periksa apakah port tersedia
lsof -i :8000

# Coba port berbeda
python setup-launcher.py --port 8081
```

### File Tidak Dihasilkan
```bash
# Periksa izin file
ls -la setup.html setup.py

# Verifikasi instalasi Python
python --version
python -c "import json; print('JSON working')"
```

### Masalah Browser
```bash
# Hapus cache browser
# Coba mode pribadi/incognito
# Periksa konsol browser untuk kesalahan
```

### Konflik Aturan
- Setiap jenis file agen (AGENTS.md/GEMINI.md/CLAUDE.md) bersifat mutual exclusive
- Mode enhanced membersihkan file yang bertentangan secara otomatis
- Pembersihan manual mungkin diperlukan dalam mode dasar

## 🚀 Penggunaan Lanjutan

### Pengembangan Aturan Kustom
- Lihat [Manual Ekstensi](EXTENSION-MANUAL.md)
- Buat direktori aturan baru
- Tentukan settings.json dan file template
- Tambahkan ke konfigurasi bootstrap.json

### Penerapan Otomatis
```bash
#!/bin/bash
# Skrip pengaturan otomatis
python setup-launcher.py --port 9000 &
sleep 2
curl -X POST http://localhost:9000/api/shutdown
```

### Integrasi CI/CD
```yaml
# Contoh GitHub Actions
- name: Setup Agentic Rules
  run: |
    python setup.py --lang en --rules memory,rag --file-type AGENTS.md
    cp -r generated-files/* ./ai-project/
```

## 📊 Pertimbangan Performa

### Penggunaan Memori
- Template aturan dimuat ke memori selama generasi
- Set aturan besar mungkin memerlukan lebih banyak RAM
- Pertimbangkan pemilihan aturan berdasarkan kasus penggunaan

### Operasi Sistem File
- Mode enhanced melakukan penulisan file langsung
- Pastikan izin yang tepat untuk direktori target
- File backup dibuat secara otomatis

### Kompatibilitas Browser
- Browser modern: Dukungan API Sistem File lengkap
- Browser lama: Fallback ke dialog unduh
- Browser seluler: Fungsionalitas terbatas

## 🔐 Catatan Keamanan

- Framework berjalan sisi klien saat menggunakan `setup.html`
- Mode enhanced memerlukan server lokal (kepercayaan pengguna diperlukan)
- Tidak ada data yang dikirim secara eksternal
- Semua operasi file bersifat lokal ke sistem pengguna

## 📞 Dukungan & Kontribusi

- **Issues**: [GitHub Issues](https://github.com/your-repo/issues)
- **Diskusi**: Desain dan implementasi framework
- **Kontribusi**: Lihat README utama untuk panduan kontribusi

---

**🔧 Pengguna lanjutan**: Framework ini memberikan fleksibilitas maksimal untuk mengintegrasikan perilaku AI terstruktur ke dalam sistem agentic apa pun.

---

Copyright (c) 2025 Paulus Ery Wasito Adhi. Dilisensikan di bawah Lisensi MIT (lihat file LICENSE).

---

Diterjemahkan ke Bahasa Indonesia untuk kemudahan akses global.