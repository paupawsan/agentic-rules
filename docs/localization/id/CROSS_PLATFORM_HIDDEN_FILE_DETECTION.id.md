# Panduan Deteksi File Tersembunyi Lintas Platform
**Versi Framework**: 1.1.0
**Tujuan**: Berikan perintah spesifik dan algoritma untuk deteksi file tersembunyi yang andal
**Cakupan**: Implementasi wajib untuk semua operasi sistem file

## 🎯 **Masalah Kritis yang Ditangani**

**Masalah Saat Ini**: File tersembunyi (dot-file seperti `.env`, `.gitignore`, `.settings`) tidak terdeteksi secara andal di seluruh platform.

**Akar Penyebab**: Deskripsi algoritma generik tanpa perintah spesifik yang berfungsi untuk setiap platform.

**Solusi**: Implementasi perintah platform-spesifik dengan mekanisme fallback.

## 🔧 **Perintah Deteksi File Tersembunyi Spesifik Platform**

### **1. Sistem Unix/Linux/macOS**

#### **Perintah Utama: `find` dengan Dukungan File Tersembunyi**
```bash
# Deteksi file tersembunyi komprehensif
find /path/to/directory -name ".*" -type f 2>/dev/null

# Sertakan file biasa + file tersembunyi
find /path/to/directory \( -name ".*" -o -name "*" \) -type f 2>/dev/null

# Rekursif dengan kontrol kedalaman
find /path/to/directory -maxdepth 3 \( -name ".*" -o -name "*" \) -type f 2>/dev/null
```

#### **Perintah Alternatif: `ls` dengan Flag Tersembunyi**
```bash
# Daftar semua file termasuk tersembunyi
ls -la /path/to/directory

# File tersembunyi saja
ls -ld /path/to/directory/.*

# Pencarian file tersembunyi rekursif
find /path/to/directory -name ".*" -exec ls -ld {} \; 2>/dev/null
```

#### **Implementasi Python (Lintas Platform)**
```python
import os
import glob

def detect_hidden_files_unix(path):
    """Deteksi semua file termasuk tersembunyi di sistem Unix."""
    all_files = []

    # Dapatkan semua file termasuk tersembunyi
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.startswith('.'):
                all_files.append(os.path.join(root, file))
            else:
                all_files.append(os.path.join(root, file))

    return all_files
```

### **2. Sistem Windows**

#### **Perintah Utama: `dir` dengan Atribut Tersembunyi**
```batch
REM Daftar semua file termasuk tersembunyi
dir /a:h /b "C:\path\to\directory"

REM Sertakan kedua file tersembunyi dan terlihat
dir /a /b "C:\path\to\directory"

REM Pencarian file tersembunyi rekursif
for /r "C:\path\to\directory" %i in (.*) do @echo %i
```

#### **Alternatif PowerShell**
```powershell
# Dapatkan semua file termasuk tersembunyi
Get-ChildItem -Path "C:\path\to\directory" -Force -File

# File tersembunyi saja
Get-ChildItem -Path "C:\path\to\directory" -Hidden -File

# Pencarian rekursif
Get-ChildItem -Path "C:\path\to\directory" -Force -File -Recurse
```

#### **Implementasi Python (Windows)**
```python
import os
import glob

def detect_hidden_files_windows(path):
    """Deteksi semua file termasuk tersembunyi di Windows."""
    all_files = []

    # Gunakan os.scandir untuk performa yang lebih baik
    try:
        with os.scandir(path) as entries:
            for entry in entries:
                if entry.is_file():
                    all_files.append(entry.path)
                elif entry.is_dir() and not entry.name.startswith('.'):
                    # Pindai subdirektori secara rekursif
                    all_files.extend(detect_hidden_files_windows(entry.path))
    except PermissionError:
        pass

    return all_files
```

### **3. Implementasi Python Lintas Platform**

#### **Pendeteksi File Tersembunyi Universal**
```python
import os
import platform
import pathlib

class CrossPlatformFileDetector:
    """Pendeteksi file universal untuk semua platform."""

    def __init__(self):
        self.system = platform.system().lower()

    def is_hidden(self, path):
        """Periksa apakah file tersembunyi di platform saat ini."""
        path_obj = pathlib.Path(path)
        name = path_obj.name

        if self.system == 'windows':
            # Periksa atribut tersembunyi Windows
            try:
                import win32api
                import win32con
                attrs = win32api.GetFileAttributes(str(path_obj))
                return bool(attrs & win32con.FILE_ATTRIBUTE_HIDDEN)
            except ImportError:
                # Fallback: periksa apakah nama dimulai dengan titik
                return name.startswith('.')
        else:
            # Sistem mirip Unix: file yang dimulai dengan . tersembunyi
            return name.startswith('.')

    def detect_all_files(self, directory, include_hidden=True, max_depth=3):
        """Deteksi semua file dengan opsi penyertaan file tersembunyi."""
        all_files = []
        directory = pathlib.Path(directory)

        try:
            for root, dirs, files in os.walk(directory, followlinks=False):
                current_depth = len(pathlib.Path(root).relative_to(directory).parts)
                if current_depth > max_depth:
                    dirs[:] = []  # Jangan telusuri lebih dalam
                    continue

                # Filter direktori tersembunyi jika tidak menyertakan tersembunyi
                if not include_hidden:
                    dirs[:] = [d for d in dirs if not d.startswith('.')]

                for file in files:
                    file_path = pathlib.Path(root) / file

                    if include_hidden or not self.is_hidden(file_path):
                        all_files.append(str(file_path))

        except (PermissionError, OSError):
            pass

        return all_files

    def find_specific_hidden_files(self, directory, patterns=None):
        """Temukan jenis file tersembunyi tertentu."""
        if patterns is None:
            patterns = ['.env', '.gitignore', '.git', '.settings']

        hidden_files = []
        all_files = self.detect_all_files(directory, include_hidden=True)

        for file_path in all_files:
            file_name = pathlib.Path(file_path).name
            if any(pattern in file_name for pattern in patterns):
                hidden_files.append(file_path)

        return hidden_files
```

## 📋 **Pembaruan Algoritma Implementasi**

### **Algoritma Detect_Hidden_Files_Algorithm yang Diperbarui**

```
Algoritma: Detect_Hidden_Files_Algorithm (Ditingkatkan dengan Perintah Spesifik Platform)
Input: directory_path, include_system_files, recursion_depth, platform
Output: comprehensive_file_list

LANGKAH WAJIB - Agen HARUS mengeksekusi perintah spesifik platform:

1. Deteksi Platform dan Pilih Perintah:
   - IF platform == "windows": Gunakan PowerShell "Get-ChildItem -Force" atau "dir /a:h"
   - IF platform == "linux" OR "darwin": Gunakan "find -name '.*'" atau "ls -la"
   - IF platform == "unknown": Gunakan implementasi Python lintas platform

2. Eksekusi Perintah Spesifik Platform:

   UNTUK Sistem Windows:
   - Perintah Utama: PowerShell "Get-ChildItem -Path $directory -Force -File -Recurse"
   - Perintah Fallback: Command Prompt "dir /a:h /b /s $directory"
   - Darurat: Python implementation dengan pemeriksaan atribut tersembunyi

   UNTUK Sistem Unix/Linux/macOS:
   - Perintah Utama: find $directory -name ".*" -type f 2>/dev/null
   - Perintah Fallback: ls -la $directory | grep "^-"
   - Darurat: Python implementation

3. Proses Hasil dengan Kesadaran Platform:
   - Windows: Periksa flag FILE_ATTRIBUTE_HIDDEN melalui win32api
   - Unix-like: File yang dimulai dengan '.' tersembunyi secara konvensi
   - Lintas platform: Gunakan Python pathlib untuk perilaku konsisten
```

### **Algoritma Select_File_Discovery_Tool yang Diperbarui**

```
Algoritma: Select_File_Discovery_Tool (Ditingkatkan dengan Perintah Platform)
Input: search_target, search_context, file_types_needed, platform
Output: specific_command_with_fallbacks

ANALISIS WAJIB - Agen HARUS mengevaluasi semua kondisi:

1. Deteksi Platform dan Analisis Persyaratan:
   - platform = detect_current_platform()  # windows/linux/darwin/unknown
   - Jika hidden_files_needed ATAU starts_with_dot: Eksekusi Detect_Hidden_Files_Algorithm (WAJIB)
   - Jika system_status_check: Sertakan .agentic_initialized, .bootstrap.json (WAJIB)

2. Tentukan cakupan pencarian - HARUS verifikasi:
   - project_root: Gunakan relative_path_resolution
   - system_wide: Gunakan absolute_path_resolution dengan permissions_check
   - network_shares: Gunakan network_mount_detection

3. Eksekusi Perintah Spesifik Platform - IMPLEMENTASI WAJIB:

   UNTUK Sistem Windows:
   - File tersembunyi: PowerShell "Get-ChildItem -Path $directory -Force -File -Recurse"
   - Fallback: CMD "dir /a:h /b /s $directory"
   - Direktori besar: Gunakan pemindaian berbasis iterator untuk mencegah masalah memori

   UNTUK Sistem Unix/Linux/macOS:
   - File tersembunyi: find $directory -name ".*" -type f 2>/dev/null
   - Fallback: ls -la $directory | grep "^\."
   - Direktori besar: find dengan batas -maxdepth dan indikator kemajuan

   UNTUK Platform Tidak Dikenal:
   - Universal: Python pathlib.Path.glob('**/.*') dengan penanganan error
   - Fallback: os.scandir() dengan deteksi file tersembunyi manual

4. Terapkan filter keamanan - HARUS kecualikan:
   - Direktori sistem (/proc, /sys, /dev di Unix; System32, Windows di Windows)
   - Direktori tidak sah berdasarkan izin
   - Hormati pola .gitignore jika berlaku
   - Batasi kedalaman rekursi untuk mencegah loop tak terbatas (maksimal 10 level)

5. Kembalikan command_chain dengan fallback - HARUS berikan:
   - Utama: Perintah native platform untuk deteksi file tersembunyi
   - Fallback: Implementasi Python lintas platform
   - Darurat: Konstruksi path manual dengan os.listdir() dasar

PELANGGARAN: Agen yang menggunakan tool yang tidak tepat atau gagal mendeteksi jenis file yang diperlukan.
```

## 🚀 **Catatan Implementasi Agen**

### **Fase 1: Deteksi Platform (Wajib)**
```python
import platform

def get_platform():
    """Deteksi platform saat ini untuk perintah yang sesuai."""
    system = platform.system().lower()
    if system == 'windows':
        return 'windows'
    elif system == 'darwin':
        return 'macos'
    elif system == 'linux':
        return 'linux'
    else:
        return 'unknown'
```

### **Fase 2: Eksekusi Perintah (Wajib)**
```python
import subprocess

def execute_hidden_file_detection(directory, platform):
    """Eksekusi perintah yang sesuai berdasarkan platform."""

    if platform == 'windows':
        cmd = ['powershell', 'Get-ChildItem', '-Path', directory, '-Force', '-File', '-Recurse']
    elif platform in ['linux', 'macos']:
        cmd = ['find', directory, '-name', '.*', '-type', 'f']
    else:
        # Fallback ke Python
        return detect_files_python(directory)

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        return parse_command_output(result.stdout, platform)
    except (subprocess.TimeoutExpired, subprocess.CalledProcessError):
        return detect_files_python(directory)
```

### **Fase 3: Pemrosesan Hasil (Wajib)**
```python
def parse_command_output(output, platform):
    """Parse output perintah menjadi daftar file terstruktur."""

    files = []
    lines = output.strip().split('\n')

    for line in lines:
        line = line.strip()
        if line and not line.startswith('#'):  # Lewati komentar
            # Validasi file ada dan dapat diakses
            if os.path.isfile(line):
                files.append({
                    'path': line,
                    'hidden': line.split('/')[-1].startswith('.') if platform != 'windows' else None,
                    'accessible': True
                })

    return files
```

## 🧪 **Pengujian & Validasi**

### **Perintah Pengujian berdasarkan Platform**

#### **Pengujian Windows:**
```batch
REM Uji deteksi file tersembunyi
dir /a:h /b "C:\test\directory"

REM Uji alternatif PowerShell
powershell "Get-ChildItem -Path 'C:\test\directory' -Hidden -File"
```

#### **Pengujian Unix:**
```bash
# Uji perintah find
find /test/directory -name ".*" -type f

# Uji alternatif ls
ls -la /test/directory | grep "^-"
```

### **Daftar Periksa Validasi:**
- [ ] Deteksi file `.env`
- [ ] Temukan `.gitignore`
- [ ] Cari file `.settings`
- [ ] Temukan direktori `.git`
- [ ] Tangani kesalahan izin dengan baik
- [ ] Bekerja di berbagai direktori pengguna

## 🔧 **Penyelesaian Masalah Umum**

### **Masalah: Perintah Tidak Ditemukan**
**Solusi**: Selalu sertakan fallback ke implementasi Python
```python
try:
    result = subprocess.run(cmd, ...)
except FileNotFoundError:
    return python_fallback(directory)
```

### **Masalah: Izin Ditolak**
**Solusi**: Lewati direktori tidak dapat diakses, catat peringatan
```python
except PermissionError:
    logging.warning(f"Izin ditolak: {directory}")
    return []
```

### **Masalah: Waktu Perintah Habis**
**Solusi**: Terapkan timeout dan fallback
```python
try:
    result = subprocess.run(cmd, timeout=30)
except subprocess.TimeoutExpired:
    return python_fallback(directory)
```

## 📊 **Optimasi Performa**

### **Strategi Caching:**
- Cache daftar direktori selama 5-10 menit
- Simpan pola file tersembunyi untuk digunakan kembali
- Terapkan pemindaian inkremental

### **Manajemen Sumber Daya:**
- Batasi kedalaman rekursi (default: 3 level)
- Gunakan streaming untuk direktori besar
- Terapkan paginasi untuk set hasil besar

## 🎯 **Metrik Kesuksesan**

### **Akurasi Deteksi:**
- ✅ Temukan 100% dot-file (`.env`, `.gitignore`, dll.)
- ✅ Tangani atribut tersembunyi platform-spesifik
- ✅ Sertakan .env, .gitignore, .settings, .agentic_initialized
- ✅ Proses symbolic link dengan benar

### **Target Performa:**
- ✅ Respons sub-1 detik untuk direktori kecil
- ✅ Respons sub-10 detik untuk direktori besar
- ✅ Tingkat kegagalan <1% untuk direktori dapat diakses
- ✅ Penanganan yang baik untuk masalah izin

---

**Catatan Implementasi**: Panduan ini memberikan perintah spesifik dan logika yang HARUS digunakan agen untuk deteksi file tersembunyi yang andal di semua platform. Algoritma abstrak dalam dokumentasi utama harus digantikan dengan implementasi konkret ini.
