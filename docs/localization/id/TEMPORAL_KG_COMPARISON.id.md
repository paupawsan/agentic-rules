# Knowledge Graph Temporal — Perbandingan Sebelum/Sesudah

> Pendamping bagian [Model Pengetahuan Sadar-Waktu (Bi-Temporal)](KG_IMPLEMENTATION_GUIDE.id.md)
> pada Panduan Implementasi KG. Dokumen ini menunjukkan perbedaan *perilaku*
> antara KG konvensional (non-temporal) dan model temporal v1.5.0,
> menggunakan uji A/B yang dapat direproduksi dan validasi produksi nyata.

## Mengapa dokumen ini ada

KG yang hanya *menambahkan* fakta pada akhirnya akan memeringkat pengetahuan usang
di atas penggantinya. Kegagalan dunia nyata yang menjadi pemicu: sebuah node aturan
berprioritas tinggi yang sudah usang terus muncul dalam retrieval, dan satu-satunya
perbaikan adalah menyunting isinya secara manual agar bertuliskan "SUPERSEDED" dan
menurunkan prioritasnya secara manual — menulis ulang sejarah untuk mengakali
pemeringkatan. Model temporal memperbaiki hal ini di lapisan data.

## Uji A/B

Kedua server diisi secara identik, melalui tool publiknya masing-masing, dengan
bentuk yang persis sama dengan insiden tersebut:

- sebuah **fakta usang** pada prioritas 9 — `"The deploy target is ALPHA (set up in January)."`
- **penggantinya** pada prioritas 7 — `"The deploy target is BETA since June — alpha was decommissioned."`
- sebuah edge `supersedes` dari pengganti ke fakta usang

Kemudian query yang sama dijalankan terhadap keduanya.

### A — KG konvensional (sebelum)

```
## Results for "… deploy target" (2 matches)

[fact:stale-example] (p:9, scope:project:compare)      ← STALE FACT RANKS FIRST
The deploy target is ALPHA (set up in January).

[fact:current-example] (p:7, scope:project:compare)
The deploy target is BETA since June — alpha was decommissioned.
-> supersedes: stale-example                            (edge exists but is ignored)
```

Fakta yang telah digantikan bukan hanya muncul — prioritasnya yang lebih tinggi
membuatnya berperingkat **di atas** penggantinya sendiri. Agen yang memercayai
hasil teratas akan bertindak berdasarkan pengetahuan usang.

### B — KG temporal (sesudah)

```
## Results for "… deploy target" (1 matches)

[fact:current-example] (p:7, scope:project:compare)     ← ONLY CURRENT KNOWLEDGE
The deploy target is BETA since June — alpha was decommissioned.
-> supersedes: stale-example [invalidated 2026-07-03]
```

Fakta usang disembunyikan dari tampilan default; edge `supersedes` ditampilkan
sebagai penunjuk beranotasi alih-alih menyuntikkan kembali konten yang disembunyikan.

### B — riwayat tetap dapat di-query (tanpa kehilangan data)

```
kg_query("… deploy target", include_expired=True)

[fact:stale-example] (p:9) [SUPERSEDED by current-example]
The deploy target is ALPHA (set up in January).

[fact:current-example] (p:7)
The deploy target is BETA since June — alpha was decommissioned.
```

```
kg_get_node("stale-example")

Status: superseded by current-example at 2026-07-03T21:42Z
Valid: 2026-07-03T21:42Z → 2026-07-03T21:42Z
Supersession chain: stale-example -> current-example (newest last)
```

Tidak ada yang dihapus. Fakta lama tetap menyimpan isi lengkapnya, membawa interval
validitasnya, dan menyebutkan penerusnya.

## Validasi produksi

Model temporal divalidasi terhadap sebuah KG personal berumur panjang (beberapa ratus
node) yang disajikan melalui MCP:

| Pemeriksaan | Hasil |
|-------------|-------|
| Migrasi in-place (murni `ADD COLUMN`): jumlah node/edge/embedding tidak berubah, semua baris di-backfill `valid_at = created_at` | ✅ |
| Node nyata yang dulu diturunkan prioritasnya secara manual, diperbaiki dengan satu link `supersedes`: tersembunyi dari retrieval default, penggantinya yang muncul | ✅ |
| `kg_get_node` pada node tersebut melaporkan `Status: superseded by … at …` beserta interval validitas dan rantai supersession | ✅ |
| Perjalanan waktu: `as_of` yang diatur ke tanggal di dalam jendela validitas lamanya mengembalikan node itu sebagai yang berlaku saat itu, dan menyembunyikan penerusnya (belum valid saat itu) | ✅ |
| Kompatibilitas mundur: setiap signature tool pra-temporal bekerja tanpa perubahan | ✅ |

## Perbandingan kemampuan

| Kemampuan | KG Konvensional | KG Temporal (v1.5.0) |
|-----------|-----------------|----------------------|
| Pengetahuan usang di hasil default | muncul; dapat mengungguli penggantinya | disembunyikan otomatis saat supersession |
| Mengganti sebuah fakta | sunting teks lama secara manual + turunkan prioritas (menulis ulang sejarah) | `kg_add(…, supersedes=old)` — satu panggilan atomik |
| "Apa yang kita ketahui pada tanggal X?" | tidak dapat dijawab | `as_of=<ISO date>` pada query/context |
| Riwayat | hanya konvensi teks manual | tanpa kehilangan data: `include_expired`, penanda `[SUPERSEDED by …]`, rantai supersession |
| Fakta berakhir tanpa pengganti | hapus atau sunting manual | `kg_retire` (invalid / expired / restore — dapat dibalikkan) |
| Jendela validitas | — | `valid_from` / `valid_until`, termasuk fakta retroaktif |
| Kontradiksi | tipe edge ada tetapi tidak berfungsi | dicatat tanpa menyembunyikan kedua sisi; resolusi bersifat saran |
| Deteksi near-duplicate saat penulisan | — | saran KNN embedding mengusulkan supersede/contradict |
| Kesegaran dalam pemeringkatan | — | dorongan recency yang ringan (waktu paruh 90 hari, hanya sebagai pemecah seri) |

## Cakupan pengujian di balik perbandingan ini

- **Suite lokal 59 pemeriksaan** terhadap salinan scratch dari database nyata:
  migrasi in-place yang idempoten, penyelarasan rowid FTS/vektor, parsing format
  timestamp campuran, kompatibilitas signature lama, supersession atomik,
  perhitungan jendela as-of (lima kasus), bolak-balik retire/restore, semantik
  kontradiksi, jendela validitas retroaktif dan masa depan, dorongan recency yang
  dibatasi, serta gerbang ekspansi konteks (edge `supersedes` tidak boleh
  menyuntikkan kembali konten yang disembunyikan).
- **Harness A/B 6 asersi**: baseline konvensional (server sebelumnya yang diekstrak
  dari version control) mereproduksi insiden fakta usang; server temporal
  memperbaikinya tanpa kehilangan riwayat.
- Gerbang framework: suite statis plugin dan `validate.py` sepenuhnya hijau.

## Trade-off

Riwayat terus terakumulasi — tidak ada yang dihapus (dapat diabaikan pada skala
personal/proyek; arsipkan rantai yang telah digantikan jika graf tumbuh sangat
besar). Agen harus mengikuti prinsip *supersede, jangan sunting*; aturan v1.5.0 dan
preamble aktivasi Claude Code mengajarkan persis hal itu. Lihat
[kapan (tidak) menggunakan model temporal](KG_IMPLEMENTATION_GUIDE.id.md).
