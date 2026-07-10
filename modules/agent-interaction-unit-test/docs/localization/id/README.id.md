# Unit Test Interaksi Agen Modul

## Gambaran

Modul Unit Test Interaksi Agen menyediakan kerangka kerja validasi dan pengujian otomatis untuk percakapan agen dengan persyaratan transparansi maksimum dan ground check. Modul ini dapat dengan mudah diaktifkan/nonaktifkan untuk skenario unit testing.

### Hubungan dengan Aturan Berpikir Kritis / Relationship to Critical Thinking Rules

Modul ini dan `critical-thinking-rules` mencakup perilaku yang sama (menantang asumsi, ground-check klaim, mengakui kesalahan) tetapi memiliki **peran berbeda**, bukan duplikat:

- **`critical-thinking-rules`**: **Mendefinisikan** perilaku (heuristik yang harus diikuti agen). Aktifkan selama pekerjaan normal untuk membentuk respons agen.
- **Modul ini**: **Memverifikasi** bahwa perilaku tersebut benar-benar terjadi (test harness). Aktifkan saat pengujian untuk mengaudit kepatuhan percakapan dan menghasilkan laporan validasi.

Singkatnya, critical-thinking-rules adalah *standar*-nya; modul ini adalah *tes terhadap standar* tersebut. Heuristiknya sendiri berada di `modules/critical-thinking-rules/CRITICAL-THINKING-RULES.md` — modul ini merujuknya sebagai target validasi, bukan mendefinisikannya ulang.

## Fitur

- **Validasi Ground Check**: Verifikasi otomatis dari semua informasi terhadap data sumber
- **Tantangan Asumsi**: Identifikasi dan validasi dari semua asumsi yang dibuat
- **Pengakuan Kesalahan**: Deteksi segera dan koreksi dari halusinasi
- **Audit Pemanggilan Tool**: Logging lengkap dari semua eksekusi tool dengan validasi
- **Audit Proses Keputusan**: Dokumentasi dari semua titik keputusan dengan alternatif
- **Pemantauan Manajemen Konteks**: Pelacakan pemanfaatan jendela konteks dan optimasi
- **Analisis Debugging Agen**: Analisis sistematis dari proses penalaran agen, penggunaan tool, dan pemilihan parameter (lihat CORE-RULES.md untuk algoritma detail)
- **Validasi Kepatuhan**: Pemeriksaan otomatis terhadap persyaratan kerangka kerja

## Mulai Cepat

1. **Aktifkan modul** dengan mengatur `"agent_interaction_unit_test.enabled": true` di `settings.json`
2. **Eksekusi test case** dengan Agentic Rules Framework standar
3. **Tinjau laporan validasi** untuk metrik kepatuhan dan akurasi
4. **Nonaktifkan ketika selesai** dengan mengatur `"agent_interaction_unit_test.enabled": false`

## Konfigurasi

Edit `modules/agent-interaction-unit-test/settings.json` untuk mengkonfigurasi:

```json
{
  "agent_interaction_unit_test": {
    "enabled": false,  // Atur ke true untuk mengaktifkan unit testing
    "validation_level": "standard",
    "ground_check": {
      "enabled": true,
      "required_coverage": 100
    }
    // ... pengaturan tambahan
  }
}
```

## Format Test Case

Gunakan format ini untuk unit testing:

```markdown
# UNIT TEST: [Test_Name]
**Framework:** Agentic Rules v1.5.3
**Task:** [Specific_Test_Task]

[Eksekusi agen dengan validasi unit test...]
```

### Contoh Yang Terbukti Efektif

Pola prompt ini telah divalidasi dan terbukti efektif:

```markdown
UNIT TEST: Pengambilan Memori Agen
Framework: Agentic Rules v1.5.3
Task: Uji pengambilan Memori agen dasar.

Instruction:
Sinkronkan memori Anda untuk proyek saat ini.

Output:
Saya ingin laporan unit test dalam format markdown di folder ini [folder laporan Anda]
```

## Kriteria Validasi

Modul memvalidasi respons terhadap:
- ✅ **100% Kepatuhan Kerangka Kerja** - Semua algoritma dieksekusi
- ✅ **100% Cakupan Ground Check** - Semua klaim diverifikasi
- ✅ **0% Halusinasi** - Semua informasi diverifikasi sumber
- ✅ **Transparansi Tool Lengkap** - Setiap pemanggilan dicatat
- ✅ **Dokumentasi Keputusan** - Semua pilihan dijelaskan
- ✅ **Analisis Debugging Agen** - Validasi penalaran sistematis dan penggunaan tool

## Integrasi

Modul ini terintegrasi dengan:
- **Aturan Memori**: Menyimpan hasil tes dan riwayat validasi
- **Aturan RAG**: Mengoptimalkan konteks untuk skenario testing
- **Aturan Berpikir Kritis**: Mendefinisikan heuristik (ground-check, menantang asumsi, mengakui kesalahan) yang divalidasi modul ini — lihat "Hubungan dengan Aturan Berpikir Kritis" di atas

## Analisis Debugging Agen

Modul ini mencakup kemampuan debugging lanjutan melalui algoritma `AgentDebuggingAnalysis_Process` untuk analisis sistematis perilaku agen:

### Fitur Debugging Utama
- **Analisis Chain of Thoughts**: Pemeriksaan detail dari proses penalaran dan pengambilan keputusan
- **Validasi Penggunaan Tool**: Analisis kesesuaian pemilihan tool dan pilihan parameter
- **Optimasi Parameter**: Evaluasi pengaturan parameter dan efektivitasnya
- **Penilaian Performa**: Identifikasi inefisiensi dan peluang optimasi
- **Pelaporan Terstruktur**: Laporan debugging komprehensif dalam format markdown

### Struktur Laporan Debugging
Analisis debugging menghasilkan laporan terstruktur dengan:
1. **Chain of Thought**: Dokumentasi proses penalaran langkah demi langkah mentah penuh
2. **Analisis Langkah demi Langkah**: Rincian tabular dari setiap langkah penalaran, keputusan, tool yang digunakan, dan temuan
3. **Masalah Utama & Peluang Perbaikan**: Masalah kritis dan saran perbaikan
4. **Rekomendasi**: Saran dapat ditindaklanjuti untuk peningkatan performa
5. **Ringkasan Langkah Utama**: 3-5 poin penting yang menyoroti temuan utama

### Kasus Penggunaan Debugging
- **Validasi Analisis Kode**: Verifikasi akurasi analisis kode dan rekomendasi
- **Tinjauan Pemilihan Tool**: Nilai kesesuaian pilihan tool dan pengaturan parameter
- **Audit Proses Penalaran**: Periksa alur logis dan kualitas pengambilan keputusan
- **Optimasi Performa**: Identifikasi bottleneck dan saran perbaikan

## Contoh Penggunaan

### Aktifkan untuk Testing
```json
{
  "agent_interaction_unit_test": {
    "enabled": true
  }
}
```

### Jalankan Test Case
```
UNIT TEST: Code Analysis Validation
Framework: Agentic Rules v1.5.3
Task: Analyze the function in setup.html that generates AGENTS.md files

[Agent executes with full validation...]
```

### Tinjau Hasil
Agen akan memberikan:
- Audit kepatuhan kerangka kerja
- Log validasi ground check
- Trail audit pemanggilan tool
- Dokumentasi proses keputusan
- Laporan unit test akhir

## Kasus Penggunaan Dunia Nyata: Validasi Tugas Pengembangan

Bagian ini mendemonstrasikan aplikasi praktis dari modul Agent Interaction Unit Test untuk tugas pengembangan spesifik, memastikan akurasi dan transparansi maksimum.

### Setup Initiation (Langkah Pertama yang Diperlukan)

**Penting:** Mulai dengan query inisiasi untuk menetapkan konteks pengujian unit:

```
Query Pengguna: "setup untuk merekam semua interaksi untuk unit test"
```

Ini memberitahu agen untuk mempersiapkan validasi komprehensif dalam percakapan saat ini. Setelah diinisiasi, semua query berikutnya dalam percakapan yang sama akan secara otomatis menerima validasi pengujian unit.

### Kasus Penggunaan 1: Analisis Kode & Debugging
```
UNIT TEST: code_analysis_debugging
Framework: Agentic Rules v1.5.3
Task: Analyze authentication module for security vulnerabilities

Query Pengguna: "Analisis kode autentikasi di auth.js untuk masalah keamanan potensial"
```

**Fokus Validasi:**
- Verifikasi ground check dari klaim analisis kode
- Validasi asumsi untuk penilaian keamanan
- Audit pemanggilan tool untuk pembacaan kode yang akurat
- Dokumentasi keputusan untuk prioritas kerentanan

### Kasus Penggunaan 2: Identifikasi Masalah
```
UNIT TEST: problem_identification
Framework: Agentic Rules v1.5.3
Task: Identify root cause of database connection failures

Query Pengguna: "Debug masalah koneksi database di production - periksa log dan identifikasi akar penyebabnya"
```

**Fokus Validasi:**
- Verifikasi sumber dari klaim analisis log
- Cross-reference dari pola kesalahan
- Tantangan asumsi untuk kesimpulan diagnostik
- Identifikasi akar penyebab berbasis bukti

### Kasus Penggunaan 3: Analisis Arsitektur Kodebase
```
UNIT TEST: architecture_analysis
Framework: Agentic Rules v1.5.3
Task: Analyze codebase structure and recommend improvements

Query Pengguna: "Analisis seluruh struktur codebase dan sarankan perbaikan arsitektur"
```

**Fokus Validasi:**
- Verifikasi struktur file yang komprehensif
- Validasi analisis dependensi
- Akurasi pengenalan pola arsitektur
- Justifikasi rekomendasi dengan bukti

### Kasus Penggunaan 4: Validasi Refactoring
```
UNIT TEST: refactoring_validation
Framework: Agentic Rules v1.5.3
Task: Validate refactoring changes maintain functionality

Query Pengguna: "Review perubahan refactoring terbaru untuk memastikan tidak merusak fungsionalitas yang ada"
```

**Fokus Validasi:**
- Akurasi penilaian dampak perubahan kode
- Validasi deteksi regresi
- Verifikasi kompatibilitas
- Dokumentasi penilaian risiko

### Kasus Penggunaan 5: Pengujian Sistem Komprehensif
```
UNIT TEST: comprehensive_agent_interaction_testing
Framework: Agentic Rules v1.5.3
Task: Complete interaction validation and compliance testing

Query Pengguna: "buat log urutan interaksi agen yang detail termasuk pemanggilan tools dan parameter"
```

### Kasus Penggunaan 6: Analisis Debugging Agen
```
UNIT TEST: agent_debugging_analysis
Framework: Agentic Rules v1.5.3
Task: Systematic debugging and validation of agent reasoning processes

Query Pengguna: "debug proses penalaran agen untuk tugas analisis kode sebelumnya"
```

**Fokus Analisis Debugging:**
- Pemeriksaan chain of thoughts dan validasi alur logis
- Kesesuaian pemilihan tool dan optimasi parameter
- Penilaian efisiensi proses penalaran dan kualitas keputusan
- Identifikasi bottleneck performa dan rekomendasi perbaikan

### Contoh Interaksi Detail

**Contoh: Selama Validasi Analisis Kode**

Ketika pengguna meminta analisis kode, kerangka kerja pengujian unit menangkap detail komprehensif:

#### Log Audit Pemanggilan Tool
```
🔍 Pemanggilan Tool #1: run_terminal_cmd
├── Fungsi: run_terminal_cmd
├── Parameter: {"command": "find /project -name '*.js' -type f | head -10", "is_background": false}
├── Waktu Eksekusi: 0.245 detik
├── Skor Relevansi: 95% (justifikasi: Penting untuk penemuan codebase)
├── Hasil: Ditemukan 8 file JavaScript di root project

🔍 Pemanggilan Tool #2: read_file
├── Fungsi: read_file
├── Parameter: {"target_file": "auth.js", "offset": 1, "limit": 50}
├── Waktu Eksekusi: 0.089 detik
├── Skor Relevansi: 98% (justifikasi: Respons langsung terhadap permintaan pengguna)
├── Hasil: Berhasil membaca modul autentikasi (50 baris)

🔍 Pemanggilan Tool #3: grep
├── Fungsi: grep
├── Parameter: {"pattern": "password|secret|key", "path": "auth.js", "output_mode": "content", "case_insensitive": true}
├── Waktu Eksekusi: 0.156 detik
├── Skor Relevansi: 97% (justifikasi: Persyaratan analisis keamanan)
├── Hasil: Ditemukan 3 pola keamanan potensial
```

#### Trail Audit Keputusan
```
🎯 Titik Keputusan: Pendekatan Analisis Keamanan
├── Opsi yang Dipertimbangkan:
│   ├── Opsi 1: Pencocokan pola level permukaan saja
│   ├── Opsi 2: Analisis kode mendalam dengan konteks
│   ├── Opsi 3: Pengujian keamanan black-box
├── Dipilih: Opsi 2 (Analisis kode mendalam dengan konteks)
├── Rationale: Menyediakan validasi keamanan komprehensif
├── Penilaian Risiko: Akurasi lebih tinggi mengimbangi waktu pemrosesan
├── Validasi: Ground truth - praktik terbaik keamanan industri
├── Hasil: Pendekatan analisis mendalam dipilih
```

#### Metrik Manajemen Konteks
```
📊 Pemanfaatan Jendela Konteks: 78%
├── Kategori Memori Diakses: 4
│   ├── Memori Teknis: 3 entri direferensikan
│   ├── Memori Perilaku: 2 entri direferensikan
│   ├── Memori Kontekstual: 1 entri direferensikan
│   ├── Memori Sesi: Pelacakan sesi saat ini
├── Prioritas Informasi: Pola kritis keamanan diprioritaskan
├── Integrasi Memori: 5 cross-reference ditetapkan
├── Tindakan Optimasi: Kompresi konteks diterapkan (pengurangan 15%)
```

#### Hasil Validasi Ground Check
```
✅ Ground Check #1: Keberadaan File
├── Klaim: "auth.js ada di project"
├── Verifikasi: Pemindaian filesystem dikonfirmasi
├── Sumber: hasil run_terminal_cmd
├── Status: DIVERIFIKASI

✅ Ground Check #2: Akurasi Konten Kode
├── Klaim: "File berisi logika autentikasi"
├── Verifikasi: Analisis pola mengonfirmasi 12 fungsi terkait auth
├── Sumber: hasil grep dan read_file
├── Status: DIVERIFIKASI

✅ Ground Check #3: Validasi Temuan Keamanan
├── Klaim: "Kerentanan SQL injection potensial"
├── Verifikasi: Cross-reference terhadap pedoman OWASP
├── Sumber: Beberapa database pola keamanan
├── Status: DIVERIFIKASI
```

### Alur Eksekusi dengan Validasi

#### 1. Fase Inisialisasi
- **Algoritma**: AgentInteractionUnitTestValidation_Initialization_Process
- **Validasi**: Pengaturan diverifikasi, kerangka kerja diaktifkan
- **Hasil**: Memori sesi unit test dibuat

#### 2. Validasi Ground Check
- **Algoritma**: GroundCheckValidation_Process
- **Validasi**: Semua klaim informasi diverifikasi terhadap sumber
- **Hasil**: 100% akurasi dikonfirmasi untuk semua pernyataan

#### 3. Tantangan Asumsi
- **Algoritma**: AssumptionChallenge_Process
- **Validasi**: Asumsi respons diidentifikasi dan ditantang
- **Hasil**: Semua asumsi divalidasi dengan bukti

#### 4. Audit Pemanggilan Tool
- **Algoritma**: ToolCallAudit_Process
- **Validasi**: Setiap pemanggilan tool dicatat dengan parameter dan hasil
- **Hasil**: Trail audit lengkap dengan skor relevansi

#### 5. Audit Proses Keputusan
- **Algoritma**: DecisionAudit_Process
- **Validasi**: Semua titik keputusan didokumentasikan dengan alternatif
- **Hasil**: Transparansi penuh dalam pengambilan keputusan

#### 6. Manajemen Konteks
- **Algoritma**: ContextManagementAudit_Process
- **Validasi**: Pemanfaatan konteks dipantau dan dioptimalkan
- **Hasil**: Manajemen konteks yang efisien dikonfirmasi

#### 7. Validasi Kepatuhan
- **Algoritma**: AgentInteractionUnitTestCompliance_Process
- **Validasi**: 100% kepatuhan kerangka kerja diverifikasi
- **Hasil**: ✅ LULUS - Validasi lengkap dicapai

### Ringkasan Hasil Tes
```
✅ Kepatuhan Kerangka Kerja: 100%
✅ Cakupan Ground Check: 100%
✅ Deteksi Halusinasi: 0%
✅ Transparansi Tool: Lengkap
✅ Dokumentasi Keputusan: Trail audit penuh
✅ Analisis Debugging Agen: Validasi penalaran komprehensif
```

### Dampak Sistem Memori
Sesi pengujian unit menghasilkan:
- **8 file memori** dibuat (7 konten + 1 indeks)
- **40KB penyimpanan** digunakan
- **100% cakupan validasi** dipertahankan
- **Trail audit lengkap** dipertahankan

### Pembelajaran Utama
1. **Kekuatan Kerangka Kerja**: Semua algoritma dieksekusi dengan sukses
2. **Integrasi Memori**: Integrasi seamless dengan sistem memori yang ada
3. **Manfaat Transparansi**: Visibilitas lengkap ke semua operasi
4. **Efektivitas Validasi**: 100% akurasi dicapai dengan validasi ground check

### Instruksi Replikasi
Untuk menerapkan pengujian unit pada tugas pengembangan Anda:

1. Aktifkan pengujian unit: Atur `"agent_interaction_unit_test.enabled": true` di settings.json
2. **Inisiasi konteks pengujian unit** (query pertama dalam percakapan):
   - Query: `"setup to record all interaction for unit test"`
   - Ini menetapkan validasi komprehensif untuk seluruh percakapan
3. **Eksekusi tugas pengembangan** (query berikutnya secara otomatis divalidasi):
   - **Analisis Kode**: `"Analisis kode autentikasi di auth.js untuk masalah keamanan"`
   - **Debugging**: `"Debug masalah koneksi database dan identifikasi akar penyebabnya"`
   - **Review Arsitektur**: `"Analisis struktur codebase dan sarankan perbaikan"`
   - **Refactoring**: `"Review perubahan refactoring untuk memastikan tidak merusak fungsionalitas"`
4. Tinjau laporan validasi: Periksa kepatuhan kerangka kerja, cakupan ground check, dan dokumentasi keputusan
5. Analisis metrik: Evaluasi skor akurasi, validasi asumsi, dan transparansi pemanggilan tool
6. Nonaktifkan ketika selesai: Atur `"agent_interaction_unit_test.enabled": false`

## Langkah Keamanan

- **Perlindungan Template**: AGENTS.md ditandai sebagai template-only
- **Persetujuan Pengguna**: Membutuhkan pengaktifan eksplisit di pengaturan
- **Isolasi Kerangka Kerja**: Tidak pernah disertakan dalam codebase project pengguna
- **Transparansi Kesalahan**: Semua kegagalan segera dilaporkan dan dikoreksi

## Berkontribusi

Ikuti panduan kontribusi Agentic Rules Framework standar. Semua perubahan harus mempertahankan kepatuhan kerangka kerja dan persyaratan validasi ground check.

---

**Integrasi Kerangka Kerja:** Kompatibel dengan Agentic Rules v1.4.0+
**Lisensi:** Lisensi MIT
**Maintenance:** Dipertahankan secara aktif
