# Panduan Implementasi Knowledge Graph untuk Agentic Rules Framework
**Versi Framework**: 1.4.0
**Tujuan Dokumen**: Panduan Implementasi Agen untuk Fungsi KG
**Pendekatan Implementasi**: Algoritma Logis & Pseudocode Saja

## 🎯 **Pernyataan Masalah Inti**

Ketika pengguna mengkloning framework aturan agentic, mereka mengharapkan:
- ✅ **Persistensi memori** di seluruh percakapan
- ✅ **Konstruksi Knowledge Graph** untuk memahami hubungan
- ✅ **Penggunaan KG otomatis** dalam percakapan (bukan aktivasi manual)
- ✅ **Mekanisme fallback** ketika fitur lanjutan tidak tersedia

**Tantangan**: Script fisik tidak dapat disertakan. Agen harus mengimplementasikan fungsi KG melalui panduan algoritma logis dan pseudocode.

## 🏗️ **Prinsip Desain Framework**

### **Arsitektur Integrasi KG**
```
Percakapan Pengguna → Sistem Memori → Pemindai KG → Injeksi Konteks → Respons
       ↓               ↓              ↓              ↓              ↓
   Input Natural   Auto-Capture   Pemeriksaan      Auto-Enhance   Enhanced Output
                                   Relevansi
```

### **Kebutuhan Desain Utama**
1. **Zero-Konfigurasi**: Fungsi KG bekerja out-of-the-box
2. **Penemuan Otomatis**: Tidak perlu perintah "gunakan KG" manual
3. **Ketahanan Fallback**: Bekerja dengan memori dasar, ditingkatkan dengan KG
4. **Peningkatan Progresif**: Fitur KG Dasar → Menengah → Lanjutan

## 🤖 **Algoritma Implementasi Agen**

### **Algoritma 1: Pembuatan Memori Sadar KG**
**Tujuan**: Memastikan semua memori secara otomatis mereferensikan KG yang ada

```
Algoritma: Create_KG_Aware_Memory
Input: user_input, conversation_context, memory_category
Output: kg_enhanced_memory_entry

Langkah:
1. Buat entri memori dasar dengan field standar
2. Pindai sistem memori yang ada untuk data KG:
   - Cari memori proyek untuk "kg_data", "kg_analysis", "kg_relationships"
   - Periksa memori umum untuk informasi KG framework
   - Cari file terkait KG dalam struktur direktori memori

3. JIKA data KG ditemukan:
   - Ekstrak entitas dan hubungan yang relevan
   - Hitung skor relevansi berdasarkan:
     * Kemiripan semantik dengan percakapan saat ini
     * Kekenyalan temporal data KG
     * Tumpang tindih topik dengan konteks saat ini
   - Filter item KG di atas ambang relevansi (default: 0.6)

4. Tingkatkan entri memori:
   - Tambahkan field "kg_references" dengan N item KG yang relevan teratas
   - Sertakan field "kg_context" dengan wawasan hubungan
   - Tambahkan field "kg_relationships" untuk konsep terkait

5. Simpan memori yang ditingkatkan dengan referensi silang KG
6. Kembalikan konfirmasi keberhasilan

Fallback: Jika tidak ada data KG yang ditemukan, simpan entri memori standar
```

### **Algoritma 2: Injeksi Konteks KG Percakapan**
**Tujuan**: Secara otomatis menyertakan wawasan KG yang relevan dalam percakapan baru

```
Algoritma: Inject_Conversation_KG_Context
Input: new_conversation_request, user_context, project_context
Output: kg_enhanced_conversation_context

Langkah:
1. Analisis permintaan percakapan:
   - Ekstrak entitas, topik, dan maksud utama
   - Identifikasi konteks proyek dan tujuan pengguna
   - Tentukan domain pengetahuan yang relevan dengan permintaan

2. Query sistem memori untuk data KG:
   - Cari memori proyek untuk KG yang relevan dengan topik
   - Periksa memori umum untuk KG framework umum
   - Cari pola KG spesifik pengguna

3. Hitung relevansi KG:
   UNTUK setiap item KG yang ditemukan:
     relevance_score = calculate_relevance(
       conversation_entities,
       kg_entities,
       temporal_recency,
       topic_overlap
     )
   ENDFOR

4. Pilih item konteks KG teratas:
   - Urutkan berdasarkan skor relevansi menurun
   - Batasi hingga max_context_items (default: 5)
   - Prioritaskan hubungan dampak tinggi

5. Format konteks KG untuk injeksi:
   - Konversi hubungan KG ke bahasa natural
   - Buat ringkasan kontekstual dari koneksi yang relevan
   - Hasilkan pernyataan wawasan tentang hubungan

6. Injeksi konteks KG ke dalam percakapan:
   - Tambahkan wawasan KG yang relevan ke konteks sistem
   - Sertakan ringkasan hubungan dalam konteks yang tersedia
   - Buat data KG dapat diakses untuk generasi respons

Fallback: Jika tidak ada data KG yang tersedia, lanjutkan dengan konteks percakapan standar
```

### **Algoritma 3: Konstruksi KG Progresif**
**Tujuan**: Bangun KG secara bertahap tanpa memerlukan scripting lanjutan

```
Algoritma: Progressive_KG_Construction
Input: conversation_data, memory_entries, project_context
Output: incrementally_built_kg

Langkah:
1. Mulai dengan ekstraksi entitas dasar:
   - Identifikasi kata benda, nama proper, istilah teknis
   - Ekstrak konsep utama dari percakapan
   - Bangun daftar entitas sederhana

2. Tetapkan hubungan dasar:
   - Hubungkan entitas yang disebutkan bersama
   - Catat hubungan temporal (sebelum/sesudah)
   - Rekam pola interaksi

3. Tingkatkan dengan integrasi memori:
   - Referensi silang dengan entri memori yang ada
   - Identifikasi kombinasi entitas berulang
   - Perkuat hubungan melalui frekuensi

4. Simpan KG secara bertahap:
   - Simpan sebagai file markdown terstruktur
   - Gunakan penamaan konsisten: YYYYMMDD_entity_relationships.md
   - Sertakan metadata untuk pengambilan di masa depan

5. Peningkatan progresif:
   - Mulai dengan ko-okuren entitas
   - Tambahkan hubungan semantik
   - Sertakan metadata kontekstual
   - Bangun skor kekuatan hubungan

Fallback: Simpan data percakapan sebagai memori yang ditingkatkan bahkan jika konstruksi KG gagal
```

### **Algoritma 4: Peningkatan Query KG**
**Tujuan**: Tingkatkan pengambilan informasi menggunakan hubungan KG

```
Algoritma: KG_Enhanced_Query_Processing
Input: user_query, available_context, memory_system
Output: kg_enhanced_response_context

Langkah:
1. Proses query standar:
   - Ekstrak kata kunci dan maksud
   - Cari informasi relevan dalam sistem memori
   - Kumpulkan konteks tradisional

2. Tingkatkan dengan hubungan KG:
   JIKA data KG tersedia:
     - Temukan entitas yang disebutkan dalam query
     - Jelajahi hubungan KG untuk menemukan konsep terkait
     - Ambil informasi terkait tidak langsung
     - Sertakan konteks hubungan

3. Peringkat hasil dengan wawasan KG:
   - Dorong hasil yang terhubung dengan entitas query
   - Sertakan penjelasan hubungan
   - Berikan pemahaman kontekstual

4. Hasilkan respons yang ditingkatkan KG:
   - Sertakan wawasan hubungan dalam respons
   - Jelaskan koneksi antara konsep
   - Berikan pemahaman konteks yang lebih luas

Fallback: Kembalikan hasil query standar jika peningkatan KG tidak tersedia
```

## 🔧 **Strategi Implementasi Fallback**

### **Tier 1: Integrasi Memori Dasar**
```
Ketika fitur KG tidak tersedia:
- Simpan percakapan sebagai memori yang ditingkatkan
- Sertakan ekstraksi entitas dan kategorisasi dasar
- Referensi silang dengan entri memori yang ada
- Berikan pelacakan hubungan dasar
```

### **Tier 2: Fitur KG Menengah**
```
Ketika scripting dasar tersedia:
- Implementasikan pelacakan ko-okuren entitas
- Bangun graf hubungan sederhana
- Simpan data KG dalam format terstruktur
- Aktifkan query KG dasar
```

### **Tier 3: Fitur KG Lanjutan**
```
Ketika implementasi penuh memungkinkan:
- Analisis hubungan kompleks
- Pemahaman semantik
- Algoritma graf dan penjelajahan
- Optimasi query lanjutan
```

## 📁 **Desain Struktur Memori**

### **Organisasi Memori Kompatibel KG**
```
memory/
├── common/                    # Dibagikan di seluruh proyek
│   ├── technical/            # Pengetahuan teknis
│   ├── behavioral/           # Pola perilaku framework
│   └── kg_data/              # Data KG umum
├── private/                  # Data spesifik pengguna
│   ├── personal/             # Informasi pengguna
│   └── kg_patterns/          # Pola KG pribadi
└── projects/
    └── [project_name]/
        ├── contextual/       # Konteks proyek
        ├── sessions/         # Sesi percakapan
        ├── technical/        # Tek proyek-spesifik
        ├── topics/           # Organisasi berbasis topik
        │   ├── kg_data/      # Data KG proyek
        │   ├── kg_analysis/  # Hasil analisis KG
        │   └── kg_relationships/  # Data hubungan
        ├── user_interactions/ # Memori interaksi pengguna
        └── kg_index/         # Indeks KG proyek
```

### **Format File Memori KG**
```markdown
# Entri Memori KG: [topik] - [timestamp]

**Proyek**: [project_name]
**Tipe KG**: [entity_relationships|analysis|query_patterns]
**Kategori**: kg_data
**Penyimpanan**: project
**Retensi**: 365 hari

## Metadata KG
- **Entitas**: [daftar entitas yang diekstrak]
- **Hubungan**: [jumlah hubungan]
- **Komunitas**: [jumlah komunitas yang terdeteksi]
- **Terakhir Diperbarui**: [timestamp]

## Wawasan Utama
- [Hubungan 1]: [deskripsi]
- [Hubungan 2]: [deskripsi]

## Pola Query
- [Pola 1]: [contoh penggunaan]
- [Pola 2]: [contoh penggunaan]

## Catatan Integrasi
- Secara otomatis direferensikan dalam percakapan
- Di-cross-link dengan entri memori
- Diperbarui melalui analisis percakapan
```

## 🔄 **Alur Kerja Integrasi**

### **Alur Pemrosesan Percakapan**
```
1. Input Pengguna → Ekstraksi Entitas → Pemeriksaan Relevansi KG
2. Pemindaian Memori → Pengambilan Data KG → Peningkatan Konteks
3. Generasi Respons → Integrasi Wawasan KG → Output
4. Penyimpanan Memori → Penambahan Referensi KG → Update Pembelajaran
```

### **Alur Evolusi KG**
```
Memori Dasar → Pelacakan Entitas → Pembentukan Hubungan → Konstruksi KG → Query Lanjutan
     ↓             ↓                ↓                   ↓                 ↓
  Penyimpanan   Pengenalan     Analisis         Peningkatan       Optimasi
```

## 🎯 **Daftar Periksa Implementasi Agen**

### **Fase 1: Kesadaran KG Dasar**
- [ ] Implementasikan Algoritma 1: Pembuatan Memori Sadar KG
- [ ] Buat struktur memori kompatibel KG
- [ ] Aktifkan pemindaian referensi KG otomatis
- [ ] Test penyimpanan memori KG dasar

### **Fase 2: Integrasi Percakapan**
- [ ] Implementasikan Algoritma 2: Injeksi Konteks KG Percakapan
- [ ] Tambahkan perhitungan relevansi KG
- [ ] Aktifkan peningkatan konteks otomatis
- [ ] Test injeksi KG percakapan

### **Fase 3: Peningkatan Progresif**
- [ ] Implementasikan Algoritma 3: Konstruksi KG Progresif
- [ ] Tambahkan pembentukan KG bertahap
- [ ] Aktifkan pelacakan hubungan
- [ ] Test kemampuan evolusi KG

### **Fase 4: Peningkatan Query**
- [ ] Implementasikan Algoritma 4: Peningkatan Query KG
- [ ] Tambahkan pengambilan berbasis hubungan
- [ ] Aktifkan pemahaman kontekstual
- [ ] Test kemampuan query yang ditingkatkan

## 🔒 **Keamanan & Kompatibilitas**

### **Degradasi yang Baik**
- Selalu berikan fungsionalitas dasar tanpa fitur KG
- Peningkatan KG harus aditif, bukan wajib
- Jelas fallback path untuk semua operasi KG
- Pengalaman pengguna tidak terpengaruh oleh status implementasi KG

### **Kompatibilitas Memori**
- Memori yang ditingkatkan KG bekerja dengan sistem memori dasar
- Memori standar tetap dapat dibaca dalam sistem yang ditingkatkan KG
- Jalur migrasi untuk upgrade sistem memori
- Kompatibilitas mundur dipertahankan

### **Pertimbangan Performa**
- Operasi KG tidak boleh memblokir alur percakapan
- Pemrosesan latar belakang untuk konstruksi KG berat
- Caching untuk data KG yang sering diakses
- Batas sumber daya untuk operasi KG

## 📚 **Sumber Daya Implementasi**

### **Kemampuan Agen yang Diperlukan**
1. **Akses Sistem Memori**: Baca/tulis entri memori
2. **Operasi Sistem File**: Buat/kelola file memori
3. **Pemrosesan Teks**: Ekstraksi entitas, identifikasi hubungan
4. **Manajemen Konteks**: Penilaian relevansi, injeksi konteks

### **Pola yang Direkomendasikan**
- Implementasikan algoritma secara bertahap
- Test setiap fase sebelum melanjutkan
- Pertahankan logging komprehensif
- Berikan feedback pengguna tentang status KG

### **Metrik Kesuksesan**
- Memori secara otomatis mereferensikan KG
- Percakapan menyertakan konteks KG yang relevan
- Data KG berkembang melalui penggunaan
- Mekanisme fallback bekerja dengan andal

---

## ⏳ **Model Pengetahuan Sadar-Waktu (Bi-Temporal)** *(v1.5.0)*

Pengetahuan berubah. Target deploy berpindah, sebuah konvensi digantikan, sebuah keputusan dibatalkan. KG yang hanya *menambahkan* fakta pada akhirnya akan menempatkan pengetahuan usang di atas penggantinya — jawaban dengan prioritas tertinggi bisa jadi jawaban yang salah. Model temporal memperbaiki hal ini di lapisan data: **pengetahuan tidak pernah dihapus; pengetahuan digantikan (superseded).**

### **Modelnya**

Setiap node membawa dua dimensi waktu yang saling independen:

| Field | Dimensi | Arti |
|-------|---------|------|
| `created_at` | waktu transaksi | kapan rekaman masuk ke KG |
| `expired_at` | waktu transaksi | kapan rekaman dipensiunkan sebagai *pencatatan yang keliru* (`NULL` = aktif) |
| `valid_at` | waktu peristiwa | kapan fakta menjadi benar di dunia nyata (default: `created_at`) |
| `invalid_at` | waktu peristiwa | kapan fakta berhenti menjadi benar — diisi otomatis saat supersession (`NULL` = masih benar) |

Aturan model:

- **Gantikan, jangan edit.** Saat pengetahuan berubah, tambahkan node baru dengan edge `supersedes` ke node lama. Node lama diinvalidasi secara otomatis dan keluar dari hasil pengambilan default — tetapi isinya tidak tersentuh.
- **Tampilan default = saat ini.** Query hanya mengembalikan pengetahuan yang valid *sekarang*. Node yang sudah digantikan, sudah dipensiunkan, atau belum berlaku disaring keluar; edge `supersedes` ditampilkan sebagai pointer beranotasi (`-> supersedes: old-id [invalidated <date>]`) alih-alih menyuntikkan kembali konten yang tersembunyi.
- **Perjalanan waktu.** `as_of=<ISO date>` merekonstruksi apa yang benar pada saat itu — berguna untuk mengaudit *mengapa* sebuah keputusan masa lalu diambil dengan pengetahuan yang tersedia saat itu. `include_expired=true` menampilkan semuanya, dengan penanda `[SUPERSEDED by …]` / `[expired]`.
- **Pensiun tanpa pengganti.** Saat sebuah fakta sekadar berhenti menjadi benar (tidak ada yang menggantikannya), pensiunkan sebagai `invalid`; saat sebuah rekaman salah sejak awal, pensiunkan sebagai `expired` (disembunyikan dari tampilan historis setelah saat itu). Keduanya dapat dibatalkan (`restore`) — tidak ada yang pernah dimusnahkan.
- **Kebaruan sebagai pemecah seri (tie-breaker).** Pemeringkatan boleh menambahkan peluruhan eksponensial yang *lembut* berdasarkan waktu pembaruan terakhir (default waktu paruh 90 hari), dibatasi agar hanya menata ulang hasil yang nyaris seri dan tidak pernah mengalahkan relevansi.

### **Mengapa memakainya — dan kapan tidak**

**Manfaat:**
- **Pengetahuan usang berhenti menang.** Kegagalan yang memotivasi model ini: sebuah fakta usang berprioritas tinggi terus mengungguli penggantinya sampai seseorang mengedit teks dan prioritasnya secara manual. Dengan supersession, fakta terkini muncul ke permukaan dan fakta lama menjadi pointer beranotasi — tanpa penurunan peringkat manual, tanpa menulis ulang sejarah.
- **Auditabilitas.** "Apa yang kita yakini pada 10 Juni?" punya jawaban yang bisa di-query. Keputusan masa lalu dapat dinilai berdasarkan pengetahuan pada zamannya.
- **Kontradiksi yang aman.** Dua fakta yang saling bertentangan dapat hidup berdampingan (edge `contradicts` mencatat konfliknya) sampai salah satunya menang lewat supersession — tidak ada penghapusan prematur atas pengetahuan yang mungkin saja benar.
- **Reversibilitas.** Pensiun yang keliru cukup dipulihkan dengan satu `restore`; node yang dihapus hilang selamanya.

**Biaya / kapan melewatkannya:**
- **Disiplin jalur tulis.** Agen harus mempelajari "gantikan, jangan edit" — aturan dalam framework ini mengajarkannya, tetapi skrip ad-hoc yang menulis langsung ke penyimpanan dapat melewatinya.
- **Pertumbuhan.** Riwayat terus menumpuk (tidak ada yang dihapus). Untuk KG skala personal/proyek (ratusan hingga puluhan ribu node) hal ini dapat diabaikan; pada skala yang lebih besar, arsipkan rantai supersession lama alih-alih menghapusnya.
- **Tidak diperlukan untuk domain yang hanya bertambah (append-only).** Jika pengetahuan Anda tidak pernah berubah (mis. korpus referensi statis), penyaringan temporal hanya menambah field yang tidak akan pernah Anda isi — nilai default (`valid_at = created_at`, semuanya terkini) lalu berperilaku persis seperti KG non-temporal, jadi biayanya kecil, tetapi manfaatnya pun tidak ada.

### **Asal-usul & Kredit**

Ini adalah **adaptasi, bukan penemuan proyek ini**. Pemodelan bi-temporal (memisahkan *waktu valid* dari *waktu transaksi*) adalah praktik lama dalam basis data temporal (lihat mis. tabel temporal SQL:2011). Penerapannya pada KG memori agen AI — edge supersession, invalidasi tanpa kehilangan data, pengambilan point-in-time — dipopulerkan oleh mesin **Graphiti dari Zep**, yang menginspirasi desain ini. Framework ini hanya mengadaptasi *konsepnya*: tidak ada kode, skema, atau teks Graphiti yang digunakan ulang, itulah sebabnya tidak ada lisensi pihak ketiga yang menyertainya. Arah riset yang terkait tetapi berbeda adalah *penalaran/peramalan* KG temporal berbasis embedding (mis. RE-GCN, [arXiv:2104.10353](https://arxiv.org/abs/2104.10353)), yang memprediksi fakta masa depan dari snapshot KG; framework ini dengan sengaja tetap berada di lapisan penyimpanan/pengambilan — pengetahuan terkurasi masuk, pengambilan sadar-waktu yang deterministik keluar.

### **Implementasi Berbasis Database (alih-alih markdown)**

KG markdown (Tier di atas) adalah default tanpa infrastruktur. Ketika graf tumbuh melampaui apa yang masih nyaman ditangani dengan grep-and-read — atau ketika lebih dari satu proyek atau agen membutuhkan pengetahuan yang sama — pindahkan penyimpanan ke database. SQLite sudah cukup; tidak perlu proses server untuk memulai.

**Skema** (SQLite; field temporalnya adalah tiga kolom nullable):

```sql
CREATE TABLE nodes (
    id TEXT PRIMARY KEY,
    type TEXT NOT NULL CHECK(type IN ('rule','pattern','fact','procedure','gotcha')),
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    scope TEXT NOT NULL DEFAULT 'global',
    tags TEXT DEFAULT '',
    priority INTEGER DEFAULT 5 CHECK(priority BETWEEN 1 AND 10),
    source TEXT DEFAULT '',
    created_at TEXT DEFAULT (datetime('now')),
    updated_at TEXT DEFAULT (datetime('now')),
    valid_at TEXT,      -- event time: fact became true (NULL -> treat as created_at)
    invalid_at TEXT,    -- event time: fact stopped being true (set on supersession)
    expired_at TEXT     -- transaction time: record retired as erroneous
);

CREATE TABLE edges (
    source_id TEXT NOT NULL REFERENCES nodes(id) ON DELETE CASCADE,
    target_id TEXT NOT NULL REFERENCES nodes(id) ON DELETE CASCADE,
    relation TEXT NOT NULL CHECK(relation IN
        ('applies_to','depends_on','part_of','related_to','supersedes','contradicts')),
    weight REAL DEFAULT 0.5,
    PRIMARY KEY (source_id, target_id, relation)
);

CREATE INDEX idx_nodes_invalid ON nodes(invalid_at);
CREATE INDEX idx_nodes_expired ON nodes(expired_at);
-- Optional retrieval upgrades: an FTS5 table over (title, content, tags) for BM25,
-- and a vector table (e.g. sqlite-vec) for semantic search.
```

**Predikat visibilitas** (jantung dari perilaku temporal):

```
current view (default):   expired_at IS NULL AND invalid_at IS NULL
                           AND (valid_at IS NULL OR valid_at <= now)
as-of view (as_of = T):   (expired_at IS NULL OR expired_at > T)
                           AND (valid_at IS NULL OR valid_at <= T)
                           AND (invalid_at IS NULL OR invalid_at > T)
```

Terapkan predikat ini sebagai post-filter pada kandidat di kode aplikasi, bukan sebagai perbandingan string SQL ad-hoc — format timestamp yang campur aduk (`datetime('now')` vs ISO-8601 dengan offset) merusak pengurutan leksikografis. Normalisasikan semua penulisan melalui satu helper timestamp.

**Semantik jalur tulis:**
- `add(..., supersedes=old_id)` — dalam satu transaksi: sisipkan node baru, sisipkan edge `supersedes`, dan atur `old.invalid_at = new.valid_at` *hanya jika nilainya NULL* (jangan pernah menimpa riwayat yang sudah ada).
- Edge `supersedes` yang dibuat sendirian menginvalidasi targetnya dengan cara yang sama; edge `contradicts` tidak menginvalidasi apa pun (catat konfliknya, selesaikan nanti).
- `retire(id, mode)` — atur `invalid_at` (fakta berakhir) atau `expired_at` (rekaman salah); `restore` mengosongkan keduanya.

**Memigrasikan database non-temporal yang sudah ada, di tempat:** gunakan murni `ALTER TABLE nodes ADD COLUMN …` (jangan pernah drop/buat ulang tabel — pembangunan ulang menetapkan ulang rowid SQLite dan diam-diam membuat tabel FTS/vektor yang di-join lewat rowid kehilangan sinkronisasi), lalu lakukan backfill satu kali: `UPDATE nodes SET valid_at = created_at WHERE valid_at IS NULL`. Buat migrasinya idempoten (periksa `PRAGMA table_info` terlebih dahulu) dan cadangkan file database sebelum eksekusi pertama.

### **Meng-upgrade KG menjadi Server MCP — jalur yang direkomendasikan**

Tangga kematangan yang alami adalah: **file markdown → database SQLite → server MCP** di depan database tersebut. Konversi ke MCP menjadi pilihan yang benar-benar baik begitu salah satu dari ini terpenuhi: (a) lebih dari satu proyek, mesin, atau agen membutuhkan pengetahuan yang sama, atau (b) Anda menginginkan kualitas pengambilan (BM25/semantik/reranking) yang lebih baik daripada grep. Alasan mengapa ini sepadan:

- **Satu otak, banyak sesi.** Setiap proyek dan setiap sesi agen berbicara ke penyimpanan yang sama melalui set tool yang sama (`kg_context`, `kg_query`, `kg_add`, `kg_link`, `kg_retire`, `kg_get_node`, `kg_list`) — tidak ada salinan per proyek yang perlahan saling menyimpang.
- **Aturannya sudah berbicara MCP.** File aturan framework ini menginstruksikan agen untuk mengutamakan tool MCP `kg` saat terhubung dan kembali (fallback) ke penyimpanan markdown saat tidak — konversi membutuhkan **nol perubahan aturan**, cukup konfigurasikan endpoint-nya (`kg_mcp_url` di plugin Claude Code).
- **Peningkatan pengambilan tetap di sisi server.** Pencarian hibrida BM25+vektor, reranking, penyaringan temporal, peluruhan kebaruan — semuanya membaik di balik antarmuka tool tanpa menyentuh satu pun teks yang dilihat agen.
- **Penulisan tervalidasi skema.** Parameter tool (tipe, relasi yang valid, batas prioritas) ditegakkan di batas sistem, alih-alih sekadar diharapkan terjaga pada penyuntingan file.

Kapan *tidak* perlu konversi: satu proyek dengan KG kecil dan tanpa keinginan menjalankan sebuah proses — penyimpanan markdown berada dalam kontrol versi bersama repo, dapat di-diff saat code review, dan tidak memerlukan instalasi apa pun. Kesederhanaan itu layak dipertahankan sampai kebutuhan berbagi atau kualitas pengambilan benar-benar menjadi masalah.

---

**Catatan Implementasi**: Panduan ini menyediakan algoritma logis dan pseudocode untuk implementasi KG. Agen harus menyesuaikan pola ini dengan kemampuan dan kendala lingkungan spesifik mereka. Tujuannya adalah memastikan fungsi KG bekerja seamlessly untuk pengguna akhir terlepas dari pendekatan implementasi agen yang mendasari.
