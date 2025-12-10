# 📚 Plugin Aturan RAG (Bahasa Indonesia)

## Ikhtisar

**Plugin Aturan RAG** memberikan agen AI kemampuan pemrosesan informasi canggih dan optimasi konteks. Plugin ini mengimplementasikan sistem Retrieval-Augmented Generation (RAG), memungkinkan agen menghasilkan respons yang lebih akurat dan kontekstual dari informasi yang tersedia.

## 🎯 Yang Dilakukan

Aturan RAG menyediakan sistem bagi agen untuk memproses informasi secara efektif dan mengoptimalkan konteks:

- **Pencarian Cerdas**: Mencari dan mengambil informasi terkait secara efisien
- **Optimasi Konteks**: Memaksimalkan jendela konteks LLM
- **Integrasi Informasi**: Mengintegrasikan wawasan dari beberapa sumber informasi
- **Penilaian Relevansi**: Memprioritaskan informasi yang paling relevan

## ✨ Kemampuan Utama

### Strategi Pencarian

#### 1. **Pemrosesan Dokumen Hierarkis**
- Memahami dan menavigasi struktur dokumen
- Mengidentifikasi bagian dan sub-bagian
- Mengevaluasi hierarki kepentingan

#### 2. **Chunking Cerdas**
- Mengidentifikasi segmen teks yang bermakna secara otomatis
- Mempertahankan kelengkapan konteks
- Meminimalkan duplikasi

#### 3. **Integrasi Multi-Sumber**
- Mengintegrasikan informasi dari beberapa dokumen
- Mendeteksi dan menyelesaikan kontradiksi
- Membangun perspektif komprehensif

#### 4. **Manajemen Konteks Dinamis**
- Memilih informasi optimal dalam batasan token LLM
- Memprioritaskan konten yang paling relevan
- Menghindari redundansi

### Fitur Optimasi

#### 1. **Evaluasi Relevansi**
- Memahami intensi query
- Memberi skor relevansi konten
- Meranking kepentingan

#### 2. **Kompresi Konteks**
- Mengkondensasikan informasi penting
- Menghapus detail yang tidak perlu
- Mempertahankan densitas informasi yang efisien

#### 3. **Pencarian Adaptif**
- Menyesuaikan strategi berdasarkan tipe query
- Belajar dari kesuksesan masa lalu
- Peningkatan performa yang berkelanjutan

## 🚫 Batasan dan Pertimbangan

### Kendala Teknis
- **Batasan Token**: Kendala jendela konteks LLM
- **Akurasi Pencarian**: Bergantung pada kualitas informasi yang tersedia
- **Waktu Pemrosesan**: Latensi pada set dokumen berskala besar
- **Dukungan Bahasa**: Dioptimalkan terutama untuk konten bahasa Inggris

### Ketergantungan Kualitas Data
- **Akurasi Informasi**: Bergantung pada kualitas materi sumber
- **Frekuensi Pembaruan**: Menangani informasi yang kedaluwarsa
- **Propagasi Bias**: Mewarisi bias dari materi sumber

## 🎯 Kasus Penggunaan

### Sistem Q&A Dokumen
```
Kasus Penggunaan: Asisten Dokumentasi Produk
Aturan RAG mencari informasi terkait dari manual produk
Mengidentifikasi bagian yang paling relevan dengan query pengguna
Memberikan konteks untuk jawaban yang akurat
```

### Pemahaman Basis Kode
```
Kasus Penggunaan: Pembantu Review Kode
Mencari kode terkait dari seluruh repositori
Memahami hubungan fungsi dan kelas
Memberikan praktik terbaik implementasi
```

### Dukungan Penelitian
```
Kasus Penggunaan: Asisten Penelitian
Mengambil informasi terkait dari makalah akademik dan materi penelitian
Mengintegrasikan kutipan dan bukti yang tepat
Membangun jawaban komprehensif
```

## 📝 Setup dan Penggunaan

### Setup Dasar
```bash
# Mengaktifkan aturan RAG
"Aktifkan aturan RAG untuk pemrosesan informasi optimal di proyek ini."

# Menentukan basis dokumen
"Proyek ini menggunakan dokumentasi di [lokasi]. Ingat untuk mencari sumber ini untuk informasi terkait."
```

### Konfigurasi Lanjutan
```bash
# Mengatur parameter pencarian kustom
"Konfigurasikan RAG dengan chunk_size=1000, overlap=200, dan prioritaskan [tipe dokumen]."
```

### Optimasi Query
```bash
# Query RAG yang efektif
"Saat menjawab pertanyaan, pertama cari informasi terkait di [sumber], lalu berikan respons berbasis bukti."
```

## ⚙️ Opsi Konfigurasi

### Konfigurasi Pencarian
```json
{
  "rag_rules": {
    "enabled": true,
    "chunk_size": 1000,
    "overlap": 200,
    "max_results": 5,
    "similarity_threshold": 0.7
  }
}
```

### Konfigurasi Sumber
```json
{
  "sources": [
    {
      "path": "./docs",
      "type": "markdown",
      "priority": "high"
    },
    {
      "path": "./src",
      "type": "code",
      "priority": "medium"
    }
  ]
}
```

## 🔄 Integrasi dengan Aturan Lain

### Koordinasi dengan Aturan Memori
- Memori menyimpan informasi yang disediakan RAG
- Belajar dan mengoptimalkan pola pencarian
- Pencarian informasi yang dipersonalisasi

### Integrasi dengan Aturan Berpikir Kritis
- Memvalidasi informasi yang diambil
- Mendeteksi dan menyelesaikan kontradiksi
- Memastikan informasi yang dapat dipercaya

### Kolaborasi dengan Framework Keseluruhan
- Terintegrasi dengan pengaturan bootstrap
- Berbagi informasi dengan aturan lain
- Optimasi sistem keseluruhan

## 📊 Metrik Performa

### Metrik Efisiensi
- **Akurasi Pencarian**: Persentase hasil yang relevan
- **Waktu Respons**: Waktu dari query ke jawaban
- **Utilisasi Konteks**: Persentase konteks yang tersedia yang digunakan
- **Kepuasan Pengguna**: Skor kegunaan jawaban

### Metrik Kualitas
- **Akurasi**: Akurasi informasi yang disediakan
- **Kelengkapan**: Jawaban komprehensif terhadap query
- **Relevansi**: Kesesuaian jawaban dengan query
- **Kebaruan**: Penyediaan wawasan baru

## 🔧 Pemecahan Masalah

### Hasil Pencarian Tidak Akurat
```
Masalah: Informasi yang kurang relevan dikembalikan
Solusi: Sesuaikan threshold kesamaan, perbaiki query
```

### Waktu Pemrosesan Lama
```
Masalah: Query RAG lambat
Solusi: Kurangi ukuran chunk, batasi jumlah hasil
```

### Konteks Tidak Memadai
```
Masalah: Jawaban tidak lengkap
Solusi: Tambahkan lebih banyak sumber, sesuaikan parameter pencarian
```

## 📚 Dokumentasi Terkait

- **[RAG-RULES.md](RAG-RULES.md)** - Spesifikasi teknis dan algoritma
- **[settings.json](settings.json)** - Opsi konfigurasi
- **[../../memory-rules/README.md](../../memory-rules/README.md)** - Fungsi memori pelengkap
- **[../../../../docs/CORE-RULES.id.md](../../../../docs/CORE-RULES.id.md)** - Ikhtisar framework

## 🤝 Berkontribusi

Ada saran untuk peningkatan fungsi RAG?

- **Laporan Bug**: [GitHub Issues](../../issues)
- **Permintaan Fitur**: [GitHub Discussions](../../discussions)
- **Kontribusi Kode**: Kirim pull request dengan peningkatan RAG

---

**📚 Aturan RAG**: Memberikan agen kekuatan pencarian dan pemrosesan informasi yang cerdas.

*Hak Cipta (c) 2025 Paulus Ery Wasito Adhi. Dilisensikan di bawah Lisensi MIT.*