# クロスプラットフォーム隠しファイル検出実装ガイド
**フレームワークバージョン**: 1.2.0
**目的**: 信頼できる隠しファイル検出のための特定コマンドとアルゴリズムを提供
**範囲**: すべてのファイルシステム操作の必須実装

## 🎯 **対処する重要な問題**

**現在の問題**: 隠しファイル（.env、.gitignore、.settingsなどのドットファイル）がプラットフォーム全体で確実に検出されない。

**根本原因**: 各プラットフォームで動作する具体的なコマンドなしの汎用アルゴリズム記述。

**解決策**: プラットフォーム固有のコマンド実装とフォールバックメカニズム。

## 🔧 **プラットフォーム固有の隠しファイル検出コマンド**

### **1. Unix/Linux/macOSシステム**

#### **主要コマンド: `find` と隠しファイルサポート**
```bash
# 包括的な隠しファイル検出
find /path/to/directory -name ".*" -type f 2>/dev/null

# 通常ファイル + 隠しファイルを含む
find /path/to/directory \( -name ".*" -o -name "*" \) -type f 2>/dev/null

# 深さ制御付き再帰的
find /path/to/directory -maxdepth 3 \( -name ".*" -o -name "*" \) -type f 2>/dev/null
```

#### **代替コマンド: `ls` と隠しフラグ**
```bash
# 隠しファイルを含むすべてのファイルをリスト
ls -la /path/to/directory

# 隠しファイルのみ
ls -ld /path/to/directory/.*

# 再帰的な隠しファイル検索
find /path/to/directory -name ".*" -exec ls -ld {} \; 2>/dev/null
```

#### **Python実装（クロスプラットフォーム）**
```python
import os
import glob

def detect_hidden_files_unix(path):
    """Unixシステムで隠しファイルを含むすべてのファイルを検出。"""
    all_files = []

    # 隠しファイルを含むすべてのファイルを取得
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.startswith('.'):
                all_files.append(os.path.join(root, file))
            else:
                all_files.append(os.path.join(root, file))

    return all_files
```

### **2. Windowsシステム**

#### **主要コマンド: `dir` と隠し属性**
```batch
REM 隠しファイルを含むすべてのファイルをリスト
dir /a:h /b "C:\path\to\directory"

REM 隠しファイルと表示ファイルの両方を含む
dir /a /b "C:\path\to\directory"

REM 再帰的な隠しファイル検索
for /r "C:\path\to\directory" %i in (.*) do @echo %i
```

#### **PowerShell代替**
```powershell
# 隠しファイルを含むすべてのファイルを取得
Get-ChildItem -Path "C:\path\to\directory" -Force -File

# 隠しファイルのみ
Get-ChildItem -Path "C:\path\to\directory" -Hidden -File

# 再帰的検索
Get-ChildItem -Path "C:\path\to\directory" -Force -File -Recurse
```

#### **Python実装（Windows）**
```python
import os
import glob

def detect_hidden_files_windows(path):
    """Windowsで隠しファイルを含むすべてのファイルを検出。"""
    all_files = []

    # より良いパフォーマンスのためにos.scandirを使用
    try:
        with os.scandir(path) as entries:
            for entry in entries:
                if entry.is_file():
                    all_files.append(entry.path)
                elif entry.is_dir() and not entry.name.startswith('.'):
                    # サブディレクトリを再帰的にスキャン
                    all_files.extend(detect_hidden_files_windows(entry.path))
    except PermissionError:
        pass

    return all_files
```

### **3. クロスプラットフォームPython実装**

#### **ユニバーサル隠しファイル検出器**
```python
import os
import platform
import pathlib

class CrossPlatformFileDetector:
    """すべてのプラットフォーム用のユニバーサルファイル検出器。"""

    def __init__(self):
        self.system = platform.system().lower()

    def is_hidden(self, path):
        """現在のプラットフォームでファイルが隠されているかをチェック。"""
        path_obj = pathlib.Path(path)
        name = path_obj.name

        if self.system == 'windows':
            # Windows隠し属性をチェック
            try:
                import win32api
                import win32con
                attrs = win32api.GetFileAttributes(str(path_obj))
                return bool(attrs & win32con.FILE_ATTRIBUTE_HIDDEN)
            except ImportError:
                # フォールバック: 名前の先頭にドットがあるかチェック
                return name.startswith('.')
        else:
            # Unixライクシステム: .で始まるファイルは隠しファイル
            return name.startswith('.')

    def detect_all_files(self, directory, include_hidden=True, max_depth=3):
        """オプションの隠しファイル包含ですべてのファイルを検出。"""
        all_files = []
        directory = pathlib.Path(directory)

        try:
            for root, dirs, files in os.walk(directory, followlinks=False):
                current_depth = len(pathlib.Path(root).relative_to(directory).parts)
                if current_depth > max_depth:
                    dirs[:] = []  # それ以上深く探索しない
                    continue

                # 隠しを含まない場合は隠しディレクトリをフィルタリング
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
        """特定の種類の隠しファイルを検索。"""
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

## 📋 **実装アルゴリズム更新**

### **更新された: Detect_Hidden_Files_Algorithm**

```
アルゴリズム: Detect_Hidden_Files_Algorithm (プラットフォーム固有コマンドで強化)
Input: directory_path, include_system_files, recursion_depth, platform
Output: comprehensive_file_list

必須ステップ - エージェントはプラットフォーム固有コマンドを実行しなければならない：

1. プラットフォームを検出し、コマンドを選択：
   - IF platform == "windows": PowerShell "Get-ChildItem -Force" または "dir /a:h" を使用
   - IF platform == "linux" OR "darwin": "find -name '.*'" または "ls -la" を使用
   - IF platform == "unknown": クロスプラットフォームPython実装を使用

2. プラットフォーム固有コマンドを実行：

   Windowsシステムの場合：
   - 主要コマンド: PowerShell "Get-ChildItem -Path $directory -Force -File -Recurse"
   - フォールバックコマンド: CMD "dir /a:h /b /s $directory"
   - 緊急時: Python実装と隠し属性チェック

   Unix/Linux/macOSシステムの場合：
   - 主要コマンド: find $directory -name ".*" -type f 2>/dev/null
   - フォールバックコマンド: ls -la $directory | grep "^-"
   - 緊急時: Python実装

3. プラットフォーム認識で結果を処理：
   - Windows: win32api経由でFILE_ATTRIBUTE_HIDDENフラグをチェック
   - Unixライク: 慣例により.で始まるファイルは隠しファイル
   - クロスプラットフォーム: 一貫した動作のためにPython pathlibを使用
```

### **更新された: Select_File_Discovery_Tool**

```
アルゴリズム: Select_File_Discovery_Tool (プラットフォームコマンドで強化)
Input: search_target, search_context, file_types_needed, platform
Output: specific_command_with_fallbacks

必須分析 - エージェントはすべての条件を評価しなければならない：

1. プラットフォームを検出し、要件を分析：
   - platform = detect_current_platform()  # windows/linux/darwin/unknown
   - If hidden_files_needed OR starts_with_dot: Detect_Hidden_Files_Algorithmを実行 (必須)
   - If system_status_check: .agentic_initialized, .bootstrap.jsonを含む (必須)

2. 検索範囲を決定 - 検証しなければならない：
   - project_root: relative_path_resolutionを使用
   - system_wide: permissions_check付きabsolute_path_resolutionを使用
   - network_shares: network_mount_detectionを使用

3. プラットフォーム固有コマンドを実行 - 必須実装：

   Windowsシステムの場合：
   - 隠しファイル: PowerShell "Get-ChildItem -Path $directory -Force -File -Recurse"
   - フォールバック: CMD "dir /a:h /b /s $directory"
   - 大きなディレクトリ: メモリ問題を防ぐためにイテレータベーススキャンを使用

   Unix/Linux/macOSシステムの場合：
   - 隠しファイル: find $directory -name ".*" -type f 2>/dev/null
   - フォールバック: ls -la $directory | grep "^\."
   - 大きなディレクトリ: -maxdepth制限と進行状況インジケーター付きfind

   不明なプラットフォームの場合：
   - ユニバーサル: エラーハンドリング付きPython pathlib.Path.glob('**/.*')
   - フォールバック: 手動隠しファイル検出付きos.scandir()

4. 安全フィルターを適用 - 除外しなければならない：
   - システムディレクトリ (Unixの/proc、/sys、/dev; WindowsのSystem32、Windows)
   - 権限に基づく不正ディレクトリ
   - 該当する場合.gitignoreパターンを尊重
   - 無限ループを防ぐために再帰深度を制限 (最大10レベル)

5. フォールバック付きtool_chainを返す - 提供しなければならない：
   - 主要: 隠しファイル検出のためのプラットフォームネイティブコマンド
   - フォールバック: クロスプラットフォームPython実装
   - 緊急時: 基本os.listdir()付き手動パス構築

違反: 不適切なツールを使用したり、必要なファイルタイプを検出できないエージェント。
```

## 🚀 **エージェント実装要件**

### **フェーズ1: プラットフォーム検出（必須）**
```python
import platform

def get_platform():
    """適切なコマンドのために現在のプラットフォームを検出。"""
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

### **フェーズ2: コマンド実行（必須）**
```python
import subprocess

def execute_hidden_file_detection(directory, platform):
    """プラットフォームに基づいて適切なコマンドを実行。"""

    if platform == 'windows':
        cmd = ['powershell', 'Get-ChildItem', '-Path', directory, '-Force', '-File', '-Recurse']
    elif platform in ['linux', 'macos']:
        cmd = ['find', directory, '-name', '.*', '-type', 'f']
    else:
        # Pythonにフォールバック
        return detect_files_python(directory)

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        return parse_command_output(result.stdout, platform)
    except (subprocess.TimeoutExpired, subprocess.CalledProcessError):
        return detect_files_python(directory)
```

### **フェーズ3: 結果処理（必須）**
```python
def parse_command_output(output, platform):
    """コマンド出力を構造化ファイルリストに解析。"""

    files = []
    lines = output.strip().split('\n')

    for line in lines:
        line = line.strip()
        if line and not line.startswith('#'):  # コメントをスキップ
            # ファイルが存在しアクセス可能かを検証
            if os.path.isfile(line):
                files.append({
                    'path': line,
                    'hidden': line.split('/')[-1].startswith('.') if platform != 'windows' else None,
                    'accessible': True
                })

    return files
```

## 🧪 **テストと検証**

### **プラットフォーム別テストコマンド**

#### **Windowsテスト：**
```batch
REM 隠しファイル検出をテスト
dir /a:h /b "C:\test\directory"

REM PowerShell代替をテスト
powershell "Get-ChildItem -Path 'C:\test\directory' -Hidden -File"
```

#### **Unixテスト：**
```bash
# findコマンドをテスト
find /test/directory -name ".*" -type f

# ls代替をテスト
ls -la /test/directory | grep "^-"
```

### **検証チェックリスト：**
- [ ] `.env`ファイルを検出
- [ ] `.gitignore`を見つける
- [ ] `.settings`ファイルを検索
- [ ] `.git`ディレクトリを発見
- [ ] 権限エラーを適切に処理
- [ ] さまざまなユーザーディレクトリで動作

## 🔧 **一般的な問題のトラブルシューティング**

### **問題: コマンドが見つからない**
**解決策**: Python実装へのフォールバックを常に含める
```python
try:
    result = subprocess.run(cmd, ...)
except FileNotFoundError:
    return python_fallback(directory)
```

### **問題: 権限が拒否された**
**解決策**: アクセスできないディレクトリをスキップし、警告をログ
```python
except PermissionError:
    logging.warning(f"権限拒否: {directory}")
    return []
```

### **問題: コマンドタイムアウト**
**解決策**: タイムアウトを実装し、フォールバック
```python
try:
    result = subprocess.run(cmd, timeout=30)
except subprocess.TimeoutExpired:
    return python_fallback(directory)
```

## 📊 **パフォーマンス最適化**

### **キャッシュ戦略：**
- ディレクトリリストを5-10分間キャッシュ
- 再利用のために隠しファイルパターンを保存
- 増分スキャンを実装

### **リソース管理：**
- 再帰深度を制限 (デフォルト: 3レベル)
- 大きなディレクトリにストリーミングを使用
- 大きな結果セットにページネーションを適用

## 🎯 **成功指標**

### **検出精度：**
- ✅ `.env`、`.gitignore`などの100%ドットファイルを検出
- ✅ プラットフォーム固有の隠し属性を処理
- ✅ `.env`、`.gitignore`、`.settings`、`.agentic_initialized`を含む
- ✅ シンボリックリンクを正しく処理

### **パフォーマンス目標：**
- ✅ 小さなディレクトリのサブ1秒応答
- ✅ 大きなディレクトリのサブ10秒応答
- ✅ アクセス可能なディレクトリの<1%失敗率
- ✅ 権限問題の適切な処理

---

**実装ノート**: このガイドはすべてのプラットフォームで信頼できる隠しファイル検出にエージェントが使用しなければならない具体的なコマンドとロジックを提供します。主要ドキュメントの抽象アルゴリズムはこれらの具体的な実装に置き換えられるべきです。
