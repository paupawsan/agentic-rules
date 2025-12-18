# 🧠 Plugin Aturan Memori (Bahasa Indonesia)

## Ikhtisar

**Plugin Aturan Memori** memberikan kemampuan **memori persisten lokal** untuk agen AI, memungkinkan mereka untuk mengingat konteks, belajar dari interaksi, dan membangun pengetahuan seiring waktu. Plugin ini mengimplementasikan sistem memori canggih dengan beberapa kategori dan pengorganisasian cerdas.

## 📖 Kisah di Balik Proyek Ini

Ini adalah ekstensi praktis dari format panduan agen AI yang ada. Ini bukan teknologi tinggi—ini adalah solusi praktis yang lahir dari kebutuhan dunia nyata.

**Catatan**: Format panduan agen AI memberikan konteks dan instruksi untuk membantu agen AI bekerja secara efektif di proyek, mirip dengan bagaimana file README memandu pengembang manusia.

### Mengapa Ini Ada

Saya telah menggunakan banyak alat memori, termasuk server MCP memori. Mereka cepat dan efisien, tetapi ada masalah fundamental: **data yang mereka simpan terlalu minimal dan saya tidak bisa melihatnya dengan mata manusia biasa tanpa ekstraksi data yang tepat.**

Jadi saya memutuskan untuk membuat **sistem memori lokal** ini—pendekatan sederhana yang dapat dibaca manusia yang memberi Anda visibilitas dan kontrol penuh atas memori agen AI Anda.

### Apa yang Membantu Anda Lakukan

📊 **Analisis Harian**: Membantu agen menganalisis temuan harian Anda, hambatan, perjuangan, dan kelemahan secara lokal
📝 **Laporan Harian**: Secara otomatis menghasilkan laporan harian dari sesi kerja Anda
🔍 **Analisis Basis Kode**: Analisis basis kode Anda sekali, simpan di memori, lalu agen akan memperbarui secara tepat saat Anda mengubah cabang atau melakukan refactoring besar—tidak perlu menganalisis ulang semuanya

### ⚠️ Penyangkalan Penting

#### Pertimbangan Privasi
Jika Anda peduli dengan privasi, **jangan berikan konten sensitif privasi pada awalnya.**

Meskipun data Anda disimpan dengan aman secara lokal, agen yang Anda gunakan tidak bersifat pribadi. Ini tergantung pada pengaturan Anda jika berlaku untuk mencegah agen mengumpulkan atau belajar dari prompt yang Anda berikan.

Cara yang aman: Gunakan model lokal dengan layanan lokal seperti:

Ollama
llama.cpp
LM Studio

#### Keterbatasan Sistem
- Sistem ini adalah template dengan upaya terbaik—dikuratori sebisa mungkin agar generik
- **Anda perlu aktif**: Anda yang perlu meminta agen untuk melakukan apa pun
- **Perluas sendiri**: Berdasarkan preferensi Anda, Anda perlu memperluas sistem sendiri
- **Gunakan model berkualitas tinggi untuk hasil terbaik** saat membuat aturan dan preferensi Anda sendiri:
  Gemini 3 Pro (Thinking)
  Cursor Composer 1
  GPT-5.1 (Thinking)

## 🎯 Yang Dilakukan

**Aturan Memori** menciptakan sistem memori terstruktur yang melampaui riwayat obrolan sederhana:

- **Penyimpanan Persisten**: Informasi bertahan di seluruh sesi dan percakapan
- **Pengorganisasian Cerdas**: Secara otomatis mengkategorikan dan menautkan informasi terkait
- **Pengenalan Konteks**: Mengingat preferensi pengguna, pola, dan detail penting
- **Pembelajaran Antar-Sesi**: Membangun pengetahuan dari interaksi ganda seiring waktu

## ✨ Kemampuan Utama

### Kategori Memori

#### 1. 🧠 **Memori Teknis**
- Pola kode dan pengetahuan pemrograman
- Solusi teknis dan langkah-langkah pemecahan masalah
- Pola penggunaan alat dan preferensi
- Alur kerja pengembangan dan praktik terbaik

#### 2. 🎭 **Memori Perilaku**
- Pola interaksi pengguna dan preferensi
- Gaya komunikasi dan ekspektasi
- Preferensi respons dan pola umpan balik
- Karakteristik kepribadian dan riwayat interaksi

#### 3. 📍 **Memori Kontekstual**
- Informasi spesifik proyek dan kendala
- Detail lingkungan dan konfigurasi
- Konteks kerja saat ini dan tujuan
- Persyaratan spesifik sesi

#### 4. 💬 **Memori Interaksi Pengguna**
- Permintaan pengguna penting dan persyaratan
- Umpan balik dan koreksi yang diberikan
- Preferensi yang diekspresikan selama percakapan
- Konteks historis dari sesi sebelumnya

#### 5. 📊 **Memori Sesi**
- Alur percakapan dan kemajuan
- Evolusi topik dan transisi
- Titik keputusan dan hasil
- Tujuan sesi dan pencapaian

#### 6. 🎯 **Memori Topik**
- Pendalaman mendalam ke subjek tertentu
- Sesi pemecahan masalah kompleks
- Benang penelitian dan analisis
- Pengembangan pengetahuan jangka panjang

#### 7. 📅 **Memori Riwayat Git**
- Evolusi proyek dan tonggak sejarah
- Perubahan kode dan pola pengembangan
- Riwayat kolaborasi tim
- Pelacakan keputusan proyek

#### 8. 👤 **Memori Pribadi**
- Preferensi pribadi dan gaya kerja
- Tujuan dan motivasi individu
- Konteks pribadi dan latar belakang
- Pembangunan hubungan jangka panjang

#### 9. 🔐 **Memori Kredensial**
- Kunci API, token, dan kredensial akses
- Pola autentikasi dan preferensi
- Informasi terkait keamanan
- Preferensi manajemen akses

#### 10. 🚨 **Memori Sensitif**
- Informasi rahasia dan data pribadi
- Detail sensitif keamanan
- Informasi terlindungi privasi
- Konten akses terbatas

## 🚫 Batasan dan Kendala

### Yang Tidak Dapat Dilakukan
- **Kolaborasi Real-time**: Tidak dapat menyinkronkan memori secara real-time di beberapa instans agen
- **Penyimpanan Tak Terbatas**: Memori memiliki batas praktis berdasarkan konfigurasi penyimpanan
- **Ingatan Sempurna**: Mungkin memprioritaskan informasi terkini atau sering diakses
- **Berbagi Antar-Agen**: Memori biasanya spesifik agen kecuali dikonfigurasi secara eksplisit
- **Pembersihan Otomatis**: Memerlukan kebijakan pembersihan manual atau terkonfigurasi

### Batas Keamanan
- **Penyimpanan Lokal Saja**: Memori tetap dalam jalur penyimpanan yang dikonfigurasi
- **Persetujuan Pengguna Diperlukan**: Semua operasi memori memerlukan izin eksplisit pengguna
- **Enkripsi Tersedia**: Memori sensitif dapat dienkripsi
- **Kontrol Akses**: Kategori memori berbeda memiliki tingkat akses berbeda

## 🎯 Kasus Penggunaan dan Aplikasi

### Peningkatan Alur Kerja Pengembangan
```
Kasus Penggunaan: Asisten Review Kode
Memori menangkap pola pengkodean, konvensi proyek, dan preferensi pengguna
Agen mengingat preferensi gaya kode tertentu dan memberikan umpan balik konsisten
```

### Dukungan Teknis dan Pemecahan Masalah
```
Kasus Penggunaan: Pembantu Administrasi Sistem
Meng ingat konfigurasi server, masalah umum, dan pola penyelesaian
Melacak preferensi pemecahan masalah spesifik pengguna dan solusi yang berhasil
Membangun basis pengetahuan masalah spesifik sistem dan perbaikan
```

### Tugas Penelitian dan Analisis
```
Kasus Penggunaan: Asisten Penelitian
Mempertahankan konteks penelitian di beberapa sesi
Meng ingat minat pengguna, sumber pilihan, dan metode analisis
Melacak pengembangan hipotesis dan pengumpulan bukti
```

### Kolaborasi Kreatif
```
Kasus Penggunaan: Rekan Pembuatan Konten
Meng ingat preferensi gaya penulisan dan pola kreatif
Melacak tema proyek, pengembangan karakter, dan elemen plot
Mempertahankan konsistensi di seluruh sesi kreatif
```

### Pembelajaran dan Pendidikan
```
Kasus Penggunaan: Tutor yang Dipersonalisasi
Beradaptasi dengan gaya belajar dan kecepatan berdasarkan memori
Meng ingat kemajuan, tantangan, dan pendekatan yang berhasil
Memberikan kesinambungan di seluruh sesi pembelajaran
```

## 📝 Contoh Prompt dan Penggunaan

### Aktivasi Memori Dasar
```
"Ingatkan bahwa saya lebih memilih TypeScript daripada JavaScript dan biasanya bekerja dengan React."
```
→ Aturan Memori akan menyimpan preferensi ini untuk sesi masa depan

### Pembangunan Konteks
```
"Ini adalah proyek backend Node.js. Ingat bahwa kita menggunakan Express, MongoDB, dan autentikasi JWT."
```
→ Memori menangkap konteks proyek dan preferensi stack teknis

### Pembelajaran Pola
```
"Saat saya meminta review kode, fokus pada performa, keamanan, dan pemeliharaan dalam urutan itu."
```
→ Memori mempelajari prioritas pengguna untuk umpan balik review kode

### Kontinuitas Sesi
```
"Melanjutkan dari sesi terakhir kita tentang sistem autentikasi..."
```
→ Memori memberikan konteks dari percakapan sebelumnya

## ⚡ Setup Memori Cepat (5 Menit)

Untuk pengguna yang ingin memori bekerja segera dengan setup minimal:

### Setup Satu-Prompt
```
"AKTIFKAN aturan memori untuk proyek ini dan KONSTRUKSI memori proyek komprehensif. Saya sedang mengembangkan aplikasi [bahasa/kerangka kerja] menggunakan [teknologi utama]. Preferensi saya: [2-3 preferensi utama]. Bangun memori dengan: 1) Ikhtisar dan tujuan proyek, 2) Detail stack teknologi dan arsitektur, 3) Preferensi gaya pengkodean saya, 4) Pola umum dan solusi yang saya gunakan, 5) Persyaratan spesifik proyek dan kendala. EKSEKUSI algoritma Proses Penyimpanan Memori secara tepat seperti yang ditentukan dalam MEMORY-RULES.md untuk MEMBUAT file markdown (.md) lokal yang sebenarnya di struktur direktori yang tepat: [storage.base_path]/projects/[project-id]/[category]/[timestamp]_[category]_memory.md. Gunakan template markdown standar. Verifikasi pembuatan file dan berikan konfirmasi daftar path .md file yang tepat yang dibuat."
```
**Itu saja!** Memori akan diaktifkan dan memori proyek awal akan dibangun segera. Sistem akan mengingat detail proyek dan preferensi Anda di semua sesi masa depan.

### Validasi Cepat
**Buka jendela obrolan baru yang segar** dan tanyakan:
```
"Apa yang Anda ingat tentang proyek ini sejauh ini?"
```
→ Harus menampilkan informasi proyek dasar dan preferensi Anda

### Kapan Menggunakan Setup Cepat
- ✅ **Baru dengan fitur memori** - Mulai tanpa kompleksitas
- ✅ **Proyek kecil/sederhana** - Memori dasar cukup
- ✅ **Kendala waktu** - Perlu memori bekerja segera
- ✅ **Pekerjaan eksplorasi** - Uji kemampuan memori dengan cepat

### Kapan Menggunakan Setup Komprehensif
- 🔧 **Proyek besar/kompleks** - Perlu konteks detail dan pola untuk efektivitas maksimal
- 🔧 **Kolaborasi tim** - Beberapa pengembang dengan preferensi berbeda
- 🔧 **Proyek jangka panjang** - Efektivitas memori maksimal seiring waktu
- 🔧 **Alur kerja kustom** - Persyaratan dan kasus edge tertentu

### Keuntungan Setup Cepat
- ⚡ **Aktivasi segera** - Memori bekerja dalam waktu < 1 menit
- 🎯 **Pembelajaran otomatis** - Meningkat dengan setiap interaksi
- 🔄 **Peningkatan progresif** - Dapat ditingkatkan ke setup komprehensif nanti
- 🛡️ **Default aman** - Pengaturan konservatif mencegah masalah

### Tips Setup Cepat
- **Jadikan stack teknologi spesifik** - Sebutkan bahasa, kerangka kerja, database
- **Sertakan 2-3 preferensi utama** - Fokus pada pengkodean/prioritas alur kerja yang paling penting
- **Sebutkan tipe proyek** - "web app", "API", "mobile app", "analisis data", dll.
- **Mulai sederhana** - Memori akan belajar dan meningkat dengan setiap percakapan
- **Validasi secara teratur** - Tanyakan "apa yang Anda ingat" untuk memeriksa akurasi memori

### Contoh Setup Cepat
```
# Pengembangan Web
"AKTIFKAN aturan memori untuk proyek ini dan KONSTRUKSI memori proyek komprehensif. Saya sedang mengembangkan aplikasi web React/TypeScript menggunakan Next.js dan Tailwind CSS. Preferensi saya: functional components and custom hooks. Bangun memori dengan: ikhtisar proyek, arsitektur React/Next.js, pola TypeScript, preferensi desain komponen, dan pendekatan styling dengan Tailwind. Buat file markdown (.md) di struktur direktori [storage.base_path]/projects/[project-id]/[category]/."

# Ilmu Data
"AKTIFKAN aturan memori untuk proyek ini dan KONSTRUKSI memori proyek komprehensif. Saya sedang mengerjakan proyek analisis data Python menggunakan pandas, numpy, dan matplotlib. Preferensi saya: nama variabel yang jelas dan dokumentasi komprehensif. Bangun memori dengan: tujuan proyek, alur kerja analisis data, praktik terbaik Python, preferensi visualisasi, dan standar dokumentasi. Buat file markdown (.md) di struktur direktori [storage.base_path]/projects/[project-id]/[category]/."

# API Backend
"AKTIFKAN aturan memori untuk proyek ini dan KONSTRUKSI memori proyek komprehensif. Saya sedang membangun API Node.js/Express menggunakan MongoDB. Preferensi saya: async/await, validasi input, dan penanganan kesalahan komprehensif. Bangun memori dengan: arsitektur API, desain database, pendekatan autentikasi, pola penanganan kesalahan, dan pertimbangan performa. Buat file markdown (.md) di struktur direktori [storage.base_path]/projects/[project-id]/[category]/."
```

---

## 🚀 Peningkatan Memori Komprehensif (Setup Lanjutan)

Untuk peningkatan memori komprehensif opsional dengan efektivitas maksimal (meningkatkan memori yang ada):

### ⚠️ Prasyarat
**Sebelum memulai setup komprehensif, Anda harus mengaktifkan memori terlebih dahulu:**

#### Opsi A: Setup Cepat (Direkomendasikan)
Gunakan setup satu-prompt di atas untuk membuat memori bekerja segera, lalu tingkatkan dengan setup komprehensif.

#### Opsi B: Aktivasi Manual
Jika Anda lebih suka melewatkan setup cepat, aktifkan memori secara manual terlebih dahulu:
```
"Aktifkan aturan memori untuk proyek ini. Saya sedang mengerjakan [deskripsi proyek singkat]."
```
→ Ini mengaktifkan sistem memori sehingga setup komprehensif akan bekerja.

#### Opsi C: Melalui Setup Framework
**Konstruksi memori juga dapat terjadi selama inisialisasi jika aturan memori sudah diaktifkan:**

1. **Menggunakan setup.py:** Jalankan `python setup.py` dan aktifkan memory-rules dalam konfigurasi
2. **Menggunakan setup.html:** Buka setup.html, konfigurasikan memory-rules, dan hasilkan file konfigurasi
3. **Pengaturan manual:** Edit `memory-rules/settings.json` dan atur `"enabled": true`

→ Setelah diaktifkan melalui sistem setup, memori akan dibangun selama inisialisasi agen berikutnya. Lihat halaman setup utama untuk opsi konfigurasi.

### Langkah 1: Setup Konteks Proyek Awal
Mulai dengan pengenalan proyek komprehensif:

```
Ini adalah proyek [Tipe Proyek] bernama [Nama Proyek]. Ingat detail penting berikut:

STACK TEKNIS:
- Bahasa: [Python/Node.js/dll.]
- Kerangka Kerja: [Django/React/dll.]
- Database: [PostgreSQL/MongoDB/dll.]
- Deployment: [Docker/AWS/dll.]

TIM & ALUR KERJA:
- Gaya kode: [PEP8/ESLint/dll.]
- Alur kerja Git: [GitFlow/trunk-based/dll.]
- Testing: [pytest/Jest/dll.]
- Dokumentasi: [Sphinx/JSDoc/dll.]

TUJUAN PROYEK:
- Tujuan utama: [tujuan utama]
- Pengguna target: [tipe pengguna/demografi]
- Fitur utama: [fungsi utama]
- Metrik sukses: [KPI/tujuan]

KENDALA & PREFERENSI:
- Persyaratan performa: [waktu respons/dll.]
- Persyaratan keamanan: [standar kepatuhan]
- Anggaran/timeline: [kendala]
- Preferensi saya: [gaya pengkodean Anda, alat, pendekatan]
```
→ Ini menetapkan konteks dasar di semua kategori memori

### Langkah 2: Pemahaman Kodebasis
Pandukan agen untuk memahami basis kode Anda:

```
Mari kita jelajahi struktur proyek. Ingat direktori utama ini dan tujuannya:

DIREKTORI INTI:
- src/components: Komponen React mengikuti [konvensi penamaan]
- src/utils: Utilitas bersama, lebih suka [gaya fungsional/pemrograman]
- tests/: Tes unit menggunakan [kerangka kerja testing]
- docs/: Dokumentasi dalam [Markdown/reStructuredText]

POLA PENTING:
- Penanganan kesalahan: Selalu gunakan [try/catch/async-await/dll.]
- Manajemen state: [Redux/Context/Zustand/dll.] untuk state global
- Panggilan API: [Axios/Fetch/dll.] dengan [pola penanganan kesalahan]
- Penamaan file: [kebab-case/camelCase/dll.]
```
→ Memori membangun pemahaman teknis dan pola pengkodean

### Langkah 3: Setup Alur Kerja Pribadi
Tetapkan preferensi kerja Anda:

```
Ingat preferensi alur kerja pengembangan saya:

GAYA PENGKODEAN:
- Indentasi: [spasi/tab] dengan [lebar]
- Panjang baris: Maksimum [80/100/120] karakter
- Komentar: [JSDoc/docstring/dll.] untuk API publik
- Penamaan: [deskriptif/self-documenting] nama variabel

PREFERENSI REVIEW:
- Area fokus: [performa > keamanan > pemeliharaan]
- Gaya umpan balik: [konstruktif/langsung/seimbang]
- Contoh kode: [selalu/kadang-kadang/tidak pernah] sertakan contoh
- Prioritas: [bug > fitur > refactoring]

KOMUNIKASI:
- Pembaruan status: [teratur/sesuai kebutuhan/atas permintaan]
- Format pertanyaan: [langsung/terbuka/terstruktur]
- Dokumentasi: [komprehensif/esensial/minimal]
```
→ Memori mempelajari preferensi pribadi dan gaya kerja Anda

### Langkah 4: Pembangunan Pola Masalah-Penyelesaian
Tetapkan masalah umum dan solusi:

```
Masalah umum yang perlu diingat dalam proyek ini:

MASALAH YANG SERING:
1. Timeout koneksi database → Periksa pengaturan connection pool
2. Batasan rate API → Implementasi backoff eksponensial
3. Kebocoran memori → Profile dengan [tool] dan perbaiki [penyebab umum]

POLA PENYELESAIAN:
- Kesalahan autentikasi → Verifikasi format token dan kedaluwarsa
- Kegagalan validasi → Periksa sanitasi input dan skema
- Masalah performa → Profile dengan [tool] dan optimalkan [bottleneck]

PENDekatan DEBUGGING:
- Mulai dengan [log/stack trace/pesan kesalahan]
- Periksa [konfigurasi/variabel lingkungan]
- Verifikasi [dependensi/versi/kompatibilitas]
- Test [komponen terisolasi/titik integrasi]
```
→ Memori membangun basis pengetahuan pemecahan masalah

### Langkah 5: Validasi dan Testing
Verifikasi setup memori bekerja dan file dibuat:

```
Mari kita test apakah Anda mengingat detail proyek utama DAN file memori dibuat:

1. Bahasa pemrograman dan kerangka kerja apa yang kita gunakan?
2. Apa direktori utama dan tujuannya?
3. Apa prioritas review kode saya?
4. Apa yang harus saya periksa pertama kali saat ada kesalahan database?
5. File lokal apa yang dibuat selama konstruksi memori? (Periksa direktori penyimpanan yang dikonfigurasi)

Jika Anda mengingat ini dengan benar DAN dapat mengonfirmasi file sebenarnya ada, maka setup memori selesai!"
```
→ Memvalidasi retensi memori dan pemahaman

## 🔧 Pemecahan Masalah Memori

### Gejala: Memori Tidak Bertahan Antar Sesi

**Penyebab Mungkin dan Solusi:**

1. **Masalah Jalur Penyimpanan**
   ```
   Gejala: Setelan reset setiap sesi
   Solusi: Periksa izin jalur penyimpanan memori dan ruang disk
   Perintah: Verifikasi akses tulis ke direktori memori yang dikonfigurasi
   ```

2. **Setelan Tidak Disimpan**
   ```
   Gejala: Setelan memori tidak dipertahankan
   Solusi: Pastikan memory_rules.enabled = true di settings.json
   Periksa: Pastikan settings.json berisi konfigurasi memori
   ```

3. **Masalah Penyimpanan Browser**
   ```
   Gejala: Antarmuka web kehilangan setelan memori
   Solusi: Hapus cache browser, coba mode incognito, periksa localStorage
   Alternatif: Gunakan setup-launcher.py untuk penyimpanan server persisten
   ```

### Gejala: Memori Tidak Menggunakan Informasi yang Dipelajari

**Penyebab Mungkin dan Solusi:**

1. **Konteks Tidak Cukup**
   ```
   Gejala: Agen tidak mengingat detail proyek
   Solusi: Berikan prompt setup proyek awal yang lebih komprehensif
   Tambahkan: Contoh spesifik, cuplikan kode, dan preferensi detail
   ```

2. **Ketidakcocokan Kategori**
   ```
   Gejala: Informasi disimpan tetapi tidak diambil
   Solusi: Periksa pemetaan kategori memori
   Verifikasi: Detail teknis → kategori teknis
   Preferensi pribadi → kategori perilaku/pribadi
   ```

3. **Masalah Konteks Query**
   ```
   Gejala: Agen memiliki info tetapi tidak menerapkan
   Solusi: Jadikan lebih eksplisit dalam query
   Coba: "Meng ingat setup proyek kita..." atau "Berdasarkan diskusi terakhir kita..."
   ```

### Gejala: Konflik atau Inkonsistensi Memori

**Penyebab Mungkin dan Solusi:**

1. **Kebingungan Proyek Berganda**
   ```
   Gejala: Agen mencampur informasi dari proyek berbeda
   Solusi: Tentukan konteks proyek dengan jelas dalam prompt
   Gunakan: "[Nama Proyek] proyek..." awalan
   ```

2. **Informasi Kedaluwarsa**
   ```
   Gejala: Agen menggunakan pola lama setelah perubahan proyek
   Solusi: Perbarui memori secara eksplisit dengan informasi baru
   Perintah: "Perbarui memori: kita beralih dari [lama] ke [baru]"
   ```

3. **Masalah Kebijakan Retensi**
   ```
   Gejala: Informasi penting dibersihkan
   Solusi: Sesuaikan setelan retensi dalam konfigurasi memori
   Tingkatkan: retention_days untuk kategori penting
   ```

### Gejala: Masalah Performa Memori

**Penyebab Mungkin dan Solusi:**

1. **Ukuran Memori Terlalu Besar**
   ```
   Gejala: Waktu respons lambat, penggunaan memori tinggi
   Solusi: Kurangi max_entries_per_category di setelan
   Aktifkan: kebijakan kompresi dan pembersihan
   ```

2. **Pola Akses yang Sering**
   ```
   Gejala: Operasi memori memperlambat
   Solusi: Aktifkan caching dan optimalkan pengindeksan
   Periksa: setelan performa memori dalam konfigurasi
   ```

3. **Kebotakan I/O Penyimpanan**
   ```
   Gejala: Operasi memori menyebabkan penundaan
   Solusi: Pindahkan penyimpanan memori ke media penyimpanan yang lebih cepat
   Periksa: SSD vs HDD, lokal vs penyimpanan jaringan
   ```

### Gejala: Memori Tidak Belajar dari Koreksi

**Penyebab Mungkin dan Solusi:**

1. **Masalah Format Koreksi**
   ```
   Gejala: Agen mengulangi kesalahan yang sama
   Solusi: Jadikan eksplisit tentang koreksi
   Gunakan: "Ingat untuk referensi di masa depan: [kesalahan] harus [koreksi]"
   ```

2. **Loop Umpan Balik Dinonaktifkan**
   ```
   Gejala: Koreksi tidak dipertahankan
   Solusi: Aktifkan pembelajaran kesalahan dalam setelan memori
   Periksa: error_correction_learning = true
   ```

### Pemecahan Masalah Lanjutan

#### Inspeksi Memori
```
Untuk memeriksa apa yang ada di memori, tanyakan agen:
"Apa yang Anda ingat tentang stack teknologi proyek ini?"
"Apa preferensi saya untuk review kode?"
"Bisakah Anda membuat daftar masalah umum yang kita temui?"
```

#### Reset Memori
```
Jika memori perlu direset:
1. Hentikan agen/sesi
2. Hapus direktori penyimpanan memori
3. Mulai ulang dengan setup memori segar
4. Jalankan ulang prompt setup proyek awal
```

#### Validasi Konfigurasi
```
Periksa konfigurasi memori:
- settings.json ada dan JSON valid
- memory_rules.enabled = true
- jalur penyimpanan dapat ditulisi
- kebijakan retensi masuk akal
- batas kategori sesuai dengan ukuran proyek
```

### Mendapatkan Bantuan

Jika pemecahan masalah tidak menyelesaikan masalah:

1. **Periksa Log**: Cari pesan kesalahan terkait memori
2. **Validasi Setelan**: Pastikan semua setelan dikonfigurasi dengan benar
3. **Test Isolasi**: Coba setup memori di lingkungan bersih
4. **Dukungan Komunitas**: Periksa masalah GitHub untuk masalah serupa
5. **Laporan Bug Detail**: Sertakan konfigurasi, log, dan langkah reproduksi

## ⚙️ Opsi Konfigurasi

### Konfigurasi Penyimpanan
```json
{
  "memory_rules": {
    "enabled": true,
    "max_entries_per_category": 100,
    "retention_days": 90,
    "auto_cleanup": true
  }
}
```

### Setelan Khusus Kategori
```json
{
  "categories": {
    "technical": {
      "enabled": true,
      "retention_days": 180,
      "priority": "high"
    },
    "personal": {
      "enabled": true,
      "retention_days": 365,
      "encryption": true
    }
  }
}
```

## 🔄 Integrasi dengan Aturan Lain

### Efek Sinergi dengan Aturan RAG
- Memori memberikan konteks yang dipersonalisasi untuk pencarian informasi
- RAG mengoptimalkan pencarian memori dan penilaian relevansi
- Sistem gabungan menciptakan pengambilan pengetahuan yang cerdas

### Peningkatan Aturan Berpikir Kritis
- Memori menyimpan koreksi kesalahan dan wawasan pembelajaran
- Berpikir kritis memvalidasi akurasi dan konsistensi memori
- Sistem perbaikan diri melalui pembaruan memori yang divalidasi

### Koordinasi Bootstrap
- Inisialisasi memori mengikuti urutan pemuatan bootstrap
- Terhubung dengan aturan lain melalui konteks bersama
- Mempertahankan konsistensi dan kohesi seluruh sistem

## 📊 Performa dan Penyimpanan

### Persyaratan Penyimpanan
- **Memori Dasar**: ~10MB untuk penggunaan umum
- **Penggunaan Diperluas**: Skalasi dengan volume percakapan
- **Kompresi**: Kompresi otomatis untuk memori besar
- **Backup**: Backup otomatis sebelum operasi pembersihan

### Karakteristik Performa
- **Kecepatan Akses**: Pencarian sub-detik untuk memori terkini
- **Performa Pencarian**: Pencarian teks lengkap cepat di semua kategori
- **Pengindeksan**: Pengindeksan otomatis untuk pencarian cepat
- **Pembersihan**: Pembersihan latar belakang tidak mempengaruhi performa

## 🔧 Pemecahan Masalah

### Memori Tidak Bertahan
```
Gejala: Informasi hilang antar sesi
Solusi: Periksa izin jalur penyimpanan dan ruang disk yang tersedia
```

### Performa Rendah
```
Gejala: Operasi memori terlalu lambat
Solusi: Kurangi max_entries_per_category atau aktifkan kompresi
```

### Konflik Memori
```
Gejala: Informasi tidak konsisten atau bertentangan
Solusi: Tinjau kebijakan retensi dan frekuensi pembersihan
```

## 📚 Dokumentasi Terkait

- **[RULES.md.id](RULES.md.id)** - Spesifikasi algoritma teknis
- **[settings.json](settings.json)** - Referensi opsi konfigurasi
- **[../../../../docs/CORE-RULES.id.md](../../../../docs/CORE-RULES.id.md)** - Ikhtisar arsitektur framework
- **[../../../../docs/localization/id/USER-GUIDE.id.md](../../../../docs/localization/id/USER-GUIDE.id.md)** - Instruksi setup dasar

## 🤝 Berkontribusi

Temukan masalah atau punya saran untuk fungsi memori?

- **Laporan Bug**: [GitHub Issues](../../issues)
- **Permintaan Fitur**: [GitHub Discussions](../../discussions)
- **Kontribusi Kode**: Kirim pull request dengan peningkatan memori

---

**🧠 Aturan Memori**: Memberikan agen AI hadiah mengingat, belajar, dan tumbuh dengan setiap interaksi.

*Hak Cipta (c) 2025 Paulus Ery Wasito Adhi. Dilisensikan di bawah Lisensi MIT.*