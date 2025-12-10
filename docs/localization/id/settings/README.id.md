# Konfigurasi Pengaturan

## Ikhtisar

Pengaturan mengontrol aktivasi dan perilaku aturan agentic. Setiap kategori aturan memiliki file pengaturan sendiri, dengan file pengaturan global yang mengkoordinasi perilaku keseluruhan.

## Hierarki Konfigurasi

```
global-settings.json (kontrol utama)
├── memory-rules/settings.json
├── critical-thinking-rules/settings.json
└── rag-rules/settings.json
```

## Pengaturan Global

### Kategori Aturan
- **memory_rules**: Mengontrol penyimpanan pemahaman persisten
- **critical_thinking_rules**: Mengelola verifikasi dan perilaku penalaran
- **rag_rules**: Menangani optimasi pemrosesan informasi

### Dukungan Platform
- **cursor_support**: Integrasi IDE Cursor
- **vscode_support**: Integrasi Visual Studio Code
- **ci_systems_support**: Integrasi pipeline CI/CD
- **custom_platforms**: Sistem agentic pihak ketiga

## Pengaturan Khusus Aturan

### Pengaturan Aturan Memori
```json
{
  "memory_rules": {
    "enabled": true,
    "storage_path": "./memory",
    "max_entries_per_category": 100,
    "categories": {
      "technical": {"enabled": true},
      "behavioral": {"enabled": true},
      "contextual": {"enabled": true}
    }
  }
}
```

### Pengaturan Aturan Berpikir Kritis
```json
{
  "critical_thinking_rules": {
    "enabled": true,
    "verification_level": "standard",
    "error_admission": {"enabled": true},
    "ground_check": {"enabled": true}
  }
}
```

### Pengaturan Aturan RAG
```json
{
  "rag_rules": {
    "enabled": true,
    "context_window_optimization": {"enabled": true},
    "hierarchical_reading": {"enabled": true},
    "log_analysis": {"enabled": true}
  }
}
```

## Instruksi Penggunaan

1. **Aktifkan/Nonaktifkan Aturan**: Atur `enabled: true/false` di global-settings.json atau pengaturan aturan individual
2. **Sesuaikan Parameter**: Modifikasi nilai di file pengaturan masing-masing
3. **Adaptasi Platform**: Aktifkan flag dukungan platform yang relevan
4. **Pantau Performa**: Sesuaikan batas berdasarkan kemampuan sistem

## Fitur Keamanan

- **Shutdown Darurat**: Secara otomatis nonaktifkan aturan jika konflik terdeteksi
- **Override Pengguna**: Izinkan kontrol manual saat diperlukan
- **Resolusi Konflik**: Penanganan konflik aturan berbasis prioritas
- **Backup**: Backup pengaturan otomatis sebelum perubahan

## Logging

Semua penerapan aturan dicatat saat `logging_enabled: true`. Log mencakup:
- Peristiwa aktivasi/deaktivasi aturan
- Perubahan parameter
- Metrik performa
- Kondisi kesalahan

---

Hak Cipta (c) 2025 Paulus Ery Wasito Adhi. Dilisensikan di bawah Lisensi MIT (lihat file LICENSE).