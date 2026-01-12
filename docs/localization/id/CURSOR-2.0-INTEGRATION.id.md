# Panduan Integrasi Cursor 2.0 Multi-Agent

## Ikhtisar

Panduan ini menjelaskan cara menggunakan Agentic Rules Framework dengan sistem multi-agen Cursor 2.0, termasuk konfigurasi orchestrator dan sub-agen.

## Prasyarat

### Pengaturan Cursor 2.0

1. **Aktifkan Channel Nightly**:
   - Buka `Cursor Settings` > `Beta`
   - Setel Update Channel ke `Nightly`
   - Restart Cursor

2. **Aktifkan Mode Agent**:
   - Buka Composer (`Cmd + I` atau `Ctrl + I`)
   - Toggle ke mode **Agent** (bukan hanya "Chat")

3. **Inisialisasi Framework**:
   - Pastikan Agentic Rules Framework diinisialisasi
   - Verifikasi marker `.agentic_initialized` ada
   - Periksa `bootstrap.json` untuk konfigurasi framework

## Arsitektur

### Struktur Multi-Agent

```
Orchestrator Agent (Utama)
├── Memory Specialist Agent
├── RAG Specialist Agent
├── Critical Thinking Specialist Agent
├── Documentation Specialist Agent
└── Testing Specialist Agent
```

### Integrasi Framework

- **Orchestrator**: Mengkoordinasikan sub-agen menggunakan aturan framework
- **Sub-Agen**: Agen khusus menggunakan modul framework spesifik
- **Koordinasi Berbasis Aturan**: Menggunakan `bootstrap.json` untuk orkestrasi
- **Berbagi Memori**: Sub-agen berbagi konteks melalui Memory Rules
- **Jaminan Kualitas**: Critical Thinking Rules memvalidasi semua output

## Konfigurasi Agen

### Auto-Generasi via setup.html

**Semua konfigurasi agen dihasilkan secara otomatis oleh `setup.html`**. Pengguna tidak perlu membuat file ini secara manual.

#### Proses Setup

1. **Buka setup.html**: Buka `setup.html` di browser Anda
2. **Pilih Target Deployment**: Pilih "Cursor 2.0 Multi-Agent"
3. **Pilih Bahasa**: Pilih bahasa agen (Bahasa Inggris, Indonesia, atau Jepang)
4. **Pilih Aturan**: Pilih modul framework yang ingin diaktifkan
5. **Generate File**: Klik "Generate Configuration Files"
6. **Salin ke Proyek**: Salin file `.cursor/agents/*.md` yang dihasilkan ke direktori `.cursor/agents/` proyek Anda

#### File yang Dihasilkan

Setelah generasi, Anda akan memiliki:

```
.cursor/agents/
├── orchestrator.md              # Orchestrator utama
├── memory-agent.md              # Spesialis operasi memori
├── rag-agent.md                 # Spesialis pengambilan informasi
├── critical-thinking-agent.md   # Spesialis jaminan kualitas
├── docs-agent.md                # Spesialis dokumentasi
├── test-agent.md                # Spesialis pengujian
└── README.md                    # Panduan mulai cepat
```

**Catatan**: File-file ini **tidak di-commit ke git** (sudah ada di `.gitignore`). Setiap pengguna menghasilkan file mereka sendiri untuk proyek mereka.

### Peran Agen

#### Orchestrator Agent
- **Tujuan**: Dekomposisi tugas dan koordinasi sub-agen
- **Framework**: Menggunakan semua modul framework untuk koordinasi
- **Delegasi**: Menugaskan tugas ke sub-agen khusus
- **Sintesis**: Menggabungkan output sub-agen

#### Memory Specialist Agent
- **Tujuan**: Pengambilan konteks dan persistensi pengetahuan
- **Modul Framework**: Memory Rules
- **Kemampuan**: Penyimpanan memori, pengambilan, integrasi knowledge graph

#### RAG Specialist Agent
- **Tujuan**: Pengambilan informasi dan optimasi konteks
- **Modul Framework**: RAG Rules
- **Kemampuan**: Pencarian semantik, optimasi konteks, query knowledge graph

#### Critical Thinking Specialist Agent
- **Tujuan**: Jaminan kualitas dan validasi
- **Modul Framework**: Critical Thinking Rules
- **Kemampuan**: Deteksi error, tantangan asumsi, verifikasi

#### Documentation Specialist Agent
- **Tujuan**: Pembuatan dan pemeliharaan dokumentasi
- **Modul Framework**: Semua aturan (dokumentasi yang ditingkatkan)
- **Kemampuan**: Dokumentasi kode, dokumentasi arsitektur, panduan pengguna

#### Testing Specialist Agent
- **Tujuan**: Pembuatan tes dan verifikasi kualitas
- **Modul Framework**: Critical Thinking Rules, Memory Rules
- **Kemampuan**: Unit test, integration test, analisis coverage

## Pola Penggunaan

### Orkestrasi Dasar

1. **Buka Composer**: Tekan `Cmd + I` (Mac) atau `Ctrl + I` (Windows/Linux)
2. **Aktifkan Mode Agent**: Toggle ke mode Agent
3. **Gunakan Mode Rencana**: Tekan `Shift + Tab` untuk perencanaan teknis
4. **Konteks Global**: Gunakan `@Codebase` untuk pemahaman proyek lengkap
5. **Delegasikan Tugas**: Orchestrator secara otomatis mendelegasikan ke sub-agen

### Eksekusi Paralel

Cursor 2.0 menggunakan Git Worktrees untuk eksekusi agen paralel:

1. **Luncurkan Tugas Paralel**: Orchestrator mendelegasikan tugas independen
2. **Pembuatan Worktree**: Cursor secara otomatis membuat worktrees
3. **Pantau Kemajuan**: Periksa worktrees dengan `git worktree list`
4. **Terapkan Perubahan**: Gunakan tombol "Apply" di UI untuk menggabungkan hasil

### Strategi Best-of-N

Untuk tugas kritis, gunakan beberapa model:

1. **Pilih Beberapa Model**: Pilih 2-3 model di pemilih model
2. **Kirim Prompt**: Satu prompt meluncurkan agen paralel
3. **Bandingkan Hasil**: Toggle antar "tab" agen
4. **Pilih Terbaik**: Pilih solusi paling elegan
5. **Terapkan**: Gabungkan solusi yang dipilih

## Koordinasi Framework

### Delegasi Berbasis Aturan

Orchestrator menggunakan aturan framework untuk delegasi:

- **Tugas Memori**: Didelegasikan ke Memory Specialist saat pengambilan konteks diperlukan
- **Tugas Informasi**: Didelegasikan ke RAG Specialist untuk pencarian kompleks
- **Tugas Kualitas**: Didelegasikan ke Critical Thinking Specialist untuk validasi
- **Tugas Dokumentasi**: Didelegasikan ke Documentation Specialist
- **Tugas Pengujian**: Didelegasikan ke Testing Specialist

### Interkoneksi Aturan

Interkoneksi aturan framework memandu koordinasi agen:

- **Error → Memory**: Koreksi error disimpan dalam memori
- **RAG → Memory**: Konteks yang dioptimasi meningkatkan memori
- **Memory → RAG**: Konteks sesi meningkatkan query RAG
- **Critical Thinking → RAG**: Validasi kualitas untuk informasi yang diambil
- **Memory → Critical Thinking**: Pola pengguna menginformasikan tantangan asumsi

### Eksekusi Berbasis Prioritas

Prioritas framework menentukan aktivasi agen:

- **Prioritas Tinggi**: RAG Rules, Critical Thinking Rules (selalu aktif)
- **Prioritas Sedang**: Memory Rules, Documentation, Testing (tergantung konteks)
- **Prioritas Rendah**: Agent Interaction Unit Test (opsional)

## Contoh Alur Kerja

### Contoh 1: Implementasi Fitur

```
Pengguna: "Implementasikan autentikasi pengguna dengan tes dan dokumentasi"

Alur Kerja Orchestrator:
1. Mode Rencana: Buat rencana teknis (Shift + Tab)
2. Delegasikan ke RAG Specialist: Analisis pola autentikasi
3. Delegasikan ke Memory Specialist: Ambil pekerjaan auth sebelumnya
4. Delegasikan ke Implementation: Buat kode auth (parallel worktree)
5. Delegasikan ke Testing Specialist: Buat tes (parallel worktree)
6. Delegasikan ke Critical Thinking Specialist: Validasi implementasi
7. Delegasikan ke Documentation Specialist: Hasilkan dokumentasi
8. Sintesis: Gabungkan semua hasil
9. Terapkan: Gabungkan worktrees
```

### Contoh 2: Review Kode

```
Pengguna: "Tinjau PR ini untuk kualitas dan masalah potensial"

Alur Kerja Orchestrator:
1. Delegasikan ke RAG Specialist: Kumpulkan konteks PR
2. Delegasikan ke Memory Specialist: Ambil pola PR serupa
3. Delegasikan ke Critical Thinking Specialist: Validasi kualitas kode
4. Delegasikan ke Testing Specialist: Verifikasi coverage tes
5. Sintesis: Laporan review komprehensif
```

## Konfigurasi

### Pengaturan Framework

Konfigurasikan framework di `settings/global-settings.json`:

```json
{
  "agentic_rules_framework": {
    "rule_categories": {
      "memory_rules": { "enabled": true, "priority": "medium" },
      "critical_thinking_rules": { "enabled": true, "priority": "high" },
      "rag_rules": { "enabled": true, "priority": "high" }
    }
  }
}
```

## Praktik Terbaik

### Penggunaan Orchestrator

1. **Selalu Rencanakan Dulu**: Gunakan Mode Rencana (`Shift + Tab`) untuk tugas kompleks
2. **Konteks Global Pertama**: Gunakan `@Codebase` sebelum mendelegasikan
3. **Delegasi Jelas**: Berikan tugas spesifik dan dapat ditindaklanjuti
4. **Pantau Kemajuan**: Periksa status worktree secara teratur
5. **Tinjau Kualitas**: Selalu validasi dengan Critical Thinking Specialist

## Referensi

- **Dokumentasi Framework**: `docs/CORE-RULES.md`
- **Panduan Bootstrap**: `Bootstrap.md`
- **Generator Konfigurasi Agen**: `setup.html` (menghasilkan file `.cursor/agents/*.md`)
- **Konfigurasi Adapter**: `settings/cursor-2.0-multi-agent-adapter.json`
- **Konfigurasi Bootstrap**: `bootstrap.json`

**Catatan**: File konfigurasi agen (`.cursor/agents/*.md`) dihasilkan secara otomatis oleh `setup.html`. Pengguna harus menghasilkan file tersebut menggunakan installer daripada membuatnya secara manual.

---

**Versi Framework**: 1.3.0  
**Versi Cursor**: 2.0+  
**Model Integrasi**: distributed_per_rule  
**Terakhir Diperbarui**: 2026-01-12
