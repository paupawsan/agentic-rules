# 🤔 Plugin Aturan Berpikir Kritis (Bahasa Indonesia)

## Ikhtisar

**Plugin Aturan Berpikir Kritis** memberikan agen AI kemampuan penalaran sistematis dan pencegahan kesalahan. Plugin ini mengimplementasikan validasi asumsi, evaluasi bukti, dan jaminan konsistensi logis, memungkinkan pengambilan keputusan yang lebih dapat diandalkan.

## 🎯 Yang Dilakukan

Aturan Berpikir Kritis menyediakan kerangka kerja bagi agen untuk mengevaluasi informasi secara kritis dan membuat keputusan logis:

- **Validasi Asumsi**: Tantangan dan verifikasi asumsi otomatis
- **Evaluasi Bukti**: Mengevaluasi kekuatan dan keandalan informasi yang disajikan
- **Konsistensi Logis**: Mendeteksi dan menyelesaikan kontradiksi
- **Pencegahan Kesalahan**: Menghindari jebakan penalaran umum

## ✨ Kemampuan Utama

### Proses Evaluasi Kritis

#### 1. **Identifikasi dan Tantangan Asumsi**
- Mengenali asumsi implisit
- Verifikasi dengan bukti
- Mempertimbangkan penjelasan alternatif

#### 2. **Evaluasi Bukti**
- Mengevaluasi keandalan informasi
- Mendeteksi bias
- Menentukan kekuatan dan relevansi bukti

#### 3. **Analisis Logis**
- Menganalisis struktur argumen
- Mengidentifikasi kesalahan logis
- Memvalidasi validitas penalaran

#### 4. **Pertimbangan Probabilitas dan Ketidakpastian**
- Mengekspresikan keyakinan yang sesuai
- Mengenali batasan dan ketidakpastian
- Menerapkan penalaran probabilistik

### Mekanisme Jaminan Kualitas

#### 1. **Pemeriksaan Konsistensi**
- Mendeteksi kontradiksi internal
- Memvalidasi konsistensi dengan pernyataan sebelumnya
- Memastikan konsistensi cerita keseluruhan

#### 2. **Pertimbangan Penjelasan Alternatif**
- Mengeksplorasi beberapa interpretasi
- Memprioritaskan penjelasan paling sederhana
- Menghindari bias kognitif

#### 3. **Loop Umpan Balik**
- Belajar dari koreksi
- Meningkatkan pola penalaran
- Peningkatan akurasi yang berkelanjutan

## 🚫 Batasan dan Pertimbangan

### Kendala Kognitif
- **Kompleksitas Komputasi**: Analisis mendalam memiliki biaya komputasi tinggi
- **Dependensi Konteks**: Memerlukan pengetahuan khusus domain
- **Penanganan Ambiguitas**: Mengekspresikan ketidakpastian yang sesuai
- **Bias Budaya**: Pengaruh data pelatihan

### Pertimbangan Praktis
- **Trade-off Waktu Pemrosesan**: Kualitas vs kecepatan
- **Kepercayaan Berlebihan**: Menghindari kelumpuhan analisis
- **Keseimbangan Diperlukan**: Keseimbangan antara kreativitas dan kritik

## 🎯 Kasus Penggunaan

### Dukungan Pengambilan Keputusan
```
Kasus Penggunaan: Penasehat Strategis
Aturan berpikir kritis mengevaluasi strategi yang diusulkan
Mengidentifikasi risiko dan kelemahan potensial
Memberikan rekomendasi berbasis bukti
```

### Pemecahan Masalah
```
Kasus Penggunaan: Asisten Troubleshooting
Melakukan analisis akar penyebab
Mempertimbangkan hipotesis alternatif
Mengusulkan solusi sistematis
```

### Verifikasi Informasi
```
Kasus Penggunaan: Pemeriksa Fakta
Memverifikasi akurasi informasi yang disediakan
Mengevaluasi keandalan sumber
Mencegah penyebaran misinformasi
```

### Pertimbangan Etis
```
Kasus Penggunaan: Penasehat Etis
Mengevaluasi dampak etis dari keputusan
Mengidentifikasi bias potensial
Memberikan rekomendasi yang bertanggung jawab
```

## 📝 Setup dan Penggunaan

### Setup Dasar
```bash
# Mengaktifkan aturan berpikir kritis
"Aktifkan aturan berpikir kritis untuk memastikan analisis yang ketat dan mencegah kesalahan."

# Mengatur standar keandalan
"Terapkan standar berpikir kritis yang memerlukan [tingkat keyakinan] untuk rekomendasi."
```

### Konfigurasi Lanjutan
```bash
# Mengatur kriteria evaluasi kustom
"Konfigurasikan berpikir kritis dengan evidence_threshold=0.8, bias_detection=enabled, dan alternative_hypotheses=3."
```

### Peningkatan Query
```bash
# Prompt yang mendorong berpikir kritis
"Sebelum memberikan rekomendasi apa pun, secara kritis evaluasi asumsi, bukti, dan bias potensial. Pertimbangkan penjelasan alternatif dan ekspresikan tingkat keyakinan yang sesuai."
```

## ⚙️ Opsi Konfigurasi

### Kriteria Evaluasi
```json
{
  "critical_thinking_rules": {
    "enabled": true,
    "evidence_threshold": 0.8,
    "bias_detection": true,
    "alternative_hypotheses": 3,
    "confidence_reporting": true
  }
}
```

### Pengaturan Khusus Domain
```json
{
  "domains": {
    "technical": {
      "rigor_level": "high",
      "evidence_types": ["empirical", "logical", "authoritative"]
    },
    "business": {
      "rigor_level": "medium",
      "evidence_types": ["data", "expert_opinion", "precedent"]
    }
  }
}
```

## 🔄 Integrasi dengan Aturan Lain

### Kolaborasi dengan Aturan RAG
- Evaluasi kritis terhadap informasi yang diambil
- Verifikasi keandalan sumber
- Evaluasi kekuatan bukti

### Integrasi dengan Aturan Memori
- Menyimpan koreksi kesalahan dan wawasan pembelajaran
- Meningkatkan pola penalaran
- Memperbaiki basis pengetahuan

### Kolaborasi dengan Framework Keseluruhan
- Terintegrasi dengan pengaturan bootstrap
- Berkolaborasi dengan aturan lain untuk jaminan kualitas
- Meningkatkan keandalan sistem keseluruhan

## 📊 Metrik Performa

### Metrik Kualitas
- **Akurasi**: Persentase keakuratan rekomendasi
- **Kelengkapan**: Jumlah alternatif yang dipertimbangkan
- **Konsistensi**: Persentase respons tanpa kontradiksi internal
- **Keandalan**: Akurasi tingkat keyakinan yang diekspresikan

### Metrik Efisiensi
- **Waktu Analisis**: Waktu yang dibutuhkan untuk evaluasi kritis
- **Kualitas Keputusan**: Pengukuran pengambilan keputusan yang ditingkatkan
- **Pengurangan Kesalahan**: Jumlah kesalahan yang dihindari
- **Kepuasan Pengguna**: Evaluasi kegunaan analisis

## 🔧 Pemecahan Masalah

### Analisis Terlalu Lambat
```
Masalah: Proses berpikir kritis memperlambat respons
Solusi: Sesuaikan kedalaman analisis atau terapkan secara kondisional
```

### Terlalu Skeptis
```
Masalah: Agen tidak membuat keputusan
Solusi: Sesuaikan threshold keyakinan atau gunakan mode seimbang
```

### Deteksi Bias Tidak Akurat
```
Masalah: Peringatan bias yang salah
Solusi: Perbarui data pelatihan atau sesuaikan sensitivitas deteksi
```

## 📚 Dokumentasi Terkait

- **[CRITICAL-THINKING-RULES.md](CRITICAL-THINKING-RULES.md)** - Spesifikasi teknis dan algoritma
- **[settings.json](settings.json)** - Opsi konfigurasi
- **[../../../../docs/CORE-RULES.id.md](../../../../docs/CORE-RULES.id.md)** - Ikhtisar framework

## 🤝 Berkontribusi

Ada saran untuk peningkatan fungsi berpikir kritis?

- **Laporan Bug**: [GitHub Issues](../../issues)
- **Permintaan Fitur**: [GitHub Discussions](../../discussions)
- **Kontribusi Kode**: Kirim pull request dengan peningkatan berpikir kritis

---

**🤔 Aturan Berpikir Kritis**: Memberikan agen kekuatan pengambilan keputusan yang bijak dan dapat diandalkan.

*Hak Cipta (c) 2025 Paulus Ery Wasito Adhi. Dilisensikan di bawah Lisensi MIT.*