#!/usr/bin/env python3
# Copyright (c) 2025-2026 Paulus Ery Wasito Adhi
#
# Licensed under the MIT License. See LICENSE file for details.
#
# Agentic Rules Framework - Enhanced Setup Launcher
# ================================================
#
# Launches enhanced setup interface with full file system access.
#
# Usage:
#     python setup-launcher.py              # Launch with full file access
#     python setup-launcher.py --port 8080  # Launch on specific port
#     python setup-launcher.py --web        # Launch with basic file saving
#
# Features:
# - Enhanced interface with full file system access (no browser restrictions)
# - Web interface can directly create/modify files (like setup.py does)
# - Automatic file cleanup when switching between AGENTS.md/GEMINI.md/CLAUDE.md
# - Real-time file operations with immediate feedback
# - Server shutdown button in the web interface for clean termination

import argparse
import http.server
import json
import os
import socketserver
import sys
import threading
import time
import urllib.parse
import webbrowser
from pathlib import Path

# Fallback when plugins.json is missing or invalid; must list every module directory
FALLBACK_PLUGIN_DIRS = [
    'modules/memory-rules',
    'modules/rag-rules',
    'modules/critical-thinking-rules',
    'modules/agent-interaction-unit-test',
]

def load_plugin_dirs(server_directory):
    """Load plugin directories from plugins.json, falling back to the known module list."""
    try:
        plugins_file = Path(server_directory) / 'plugins.json'
        with open(plugins_file, 'r', encoding='utf-8') as f:
            plugins_data = json.load(f)
            return plugins_data.get('plugins', FALLBACK_PLUGIN_DIRS)
    except (FileNotFoundError, json.JSONDecodeError):
        return FALLBACK_PLUGIN_DIRS

class SetupHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Custom HTTP request handler with file creation capabilities."""

    def __init__(self, *args, directory=None, **kwargs):
        self.server_directory = Path(directory or Path(__file__).parent)
        super().__init__(*args, directory=str(self.server_directory), **kwargs)

    def do_POST(self):
        """Handle POST requests for file operations."""
        if self.path.startswith('/api/create-file'):
            self.handle_create_file()
        elif self.path.startswith('/api/cleanup-files'):
            self.handle_cleanup_files()
        elif self.path.startswith('/api/shutdown'):
            self.handle_shutdown()
        else:
            self.send_error(404, "Endpoint not found")

    def handle_create_file(self):
        """Handle file creation requests."""
        try:
            # Read request body
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))

            filename = data.get('filename', '')
            content = data.get('content', '')

            if not filename or not content:
                self.send_error(400, "Missing filename or content")
                return

            # Security check - only allow specific file types and locations
            allowed_extensions = ['.md', '.json']

            # Load allowed plugin directories from plugins.json
            plugins_from_json = load_plugin_dirs(self.server_directory)

            # Validate plugins exist as directories and add to allowed_dirs
            allowed_dirs = ['.']  # Root directory is always allowed
            for plugin_name in plugins_from_json:
                plugin_path = self.server_directory / plugin_name
                if plugin_path.is_dir() and plugin_path.exists():
                    allowed_dirs.append(plugin_name)
                else:
                    # Log warning for plugins that don't exist as directories
                    print(f"Warning: Plugin '{plugin_name}' listed in plugins.json but directory not found", file=sys.stderr)

            if not any(filename.endswith(ext) for ext in allowed_extensions):
                self.send_error(400, "Invalid file type")
                return

            # Check if file is in allowed directory
            file_path = self.server_directory / filename
            
            # Files directly in root are always allowed
            if file_path.parent == self.server_directory:
                is_allowed = True
            else:
                # Check if file is within any allowed plugin directory
                is_allowed = False
                for allowed_dir in allowed_dirs:
                    if allowed_dir == '.':
                        # Skip root directory check here (already handled above)
                        continue
                    allowed_path = self.server_directory / allowed_dir
                    try:
                        # Check if file_path is within allowed_path
                        file_path.relative_to(allowed_path)
                        is_allowed = True
                        break
                    except ValueError:
                        # file_path is not within allowed_path, continue checking
                        continue

            if not is_allowed:
                self.send_error(400, f"Invalid file location: {filename} must be in root or within allowed plugin directories")
                return

            # Create parent directories if they don't exist
            file_path.parent.mkdir(parents=True, exist_ok=True)

            # Create backup if file exists
            if file_path.exists():
                backup_path = file_path.with_suffix(f"{file_path.suffix}.backup")
                import shutil
                shutil.copy2(file_path, backup_path)

            # Write the file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({
                'success': True,
                'message': f'File {filename} created successfully'
            }).encode('utf-8'))

        except Exception as e:
            self.send_error(500, f"File creation failed: {str(e)}")

    def handle_cleanup_files(self):
        """Handle cleanup of other file types when switching."""
        try:
            # Read request body
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))

            keep_file = data.get('keep_file', '')
            if not keep_file:
                self.send_error(400, "Missing keep_file parameter")
                return

            # Define all possible file types
            all_file_types = ['AGENTS.md', 'GEMINI.md', 'CLAUDE.md']

            cleaned_files = []

            # Clean up root directory
            for file_type in all_file_types:
                if file_type != keep_file:
                    for ext_variant in [file_type, file_type.replace('.md', '.MD')]:
                        file_path = self.server_directory / ext_variant
                        if file_path.exists():
                            # Create backup
                            backup_path = file_path.with_suffix(f"{file_path.suffix}.backup")
                            import shutil
                            shutil.copy2(file_path, backup_path)
                            # Remove file
                            file_path.unlink()
                            cleaned_files.append(f"{ext_variant}")

            # Clean up rule directories
            rule_dirs = load_plugin_dirs(self.server_directory)
            for rule_dir in rule_dirs:
                rule_path = self.server_directory / rule_dir
                if rule_path.exists():
                    for file_type in all_file_types:
                        if file_type != keep_file:
                            for ext_variant in [file_type, file_type.replace('.md', '.MD')]:
                                file_path = rule_path / ext_variant
                                if file_path.exists():
                                    # Create backup
                                    backup_path = file_path.with_suffix(f"{file_path.suffix}.backup")
                                    import shutil
                                    shutil.copy2(file_path, backup_path)
                                    # Remove file
                                    file_path.unlink()
                                    cleaned_files.append(f"{rule_dir}/{ext_variant}")

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({
                'success': True,
                'message': f'Cleaned up {len(cleaned_files)} conflicting files',
                'cleaned_files': cleaned_files
            }).encode('utf-8'))

        except Exception as e:
            self.send_error(500, f"Cleanup failed: {str(e)}")

    def handle_shutdown(self):
        """Handle server shutdown requests."""
        try:
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({
                'success': True,
                'message': 'Server shutting down...'
            }).encode('utf-8'))

            # Signal the server to shutdown
            import threading
            import os
            # Schedule shutdown in a separate thread to allow response to complete
            def shutdown_server():
                import time
                time.sleep(0.1)  # Brief delay to send response
                os._exit(0)  # Force exit the process

            shutdown_thread = threading.Thread(target=shutdown_server, daemon=True)
            shutdown_thread.start()

        except Exception as e:
            self.send_error(500, f"Shutdown failed: {str(e)}")

    def end_headers(self):
        """Add CORS headers for API requests."""
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

def start_enhanced_setup(port=8000, directory=None):
    """Start enhanced setup interface with file system access."""

    if directory is None:
        directory = Path(__file__).parent

    class CustomHTTPRequestHandler(SetupHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=str(directory), **kwargs)

    try:
        with socketserver.TCPServer(("", port), CustomHTTPRequestHandler) as httpd:
            print(f"🚀 Agentic Rules Enhanced Setup started on port {port}")
            print(f"📁 Working directory: {directory.absolute()}")
            print(f"🌐 Open your browser to: http://localhost:{port}/setup.html")
            print("🛑 Use 'Stop Server' button in browser OR press Ctrl+C to stop")

            # Auto-open browser
            url = f"http://localhost:{port}/setup.html"
            try:
                webbrowser.open(url)
            except Exception as e:
                print(f"⚠️ Could not open browser automatically: {e}")
                print(f"Please manually open: {url}")

            print("\n📋 Instructions:")
            print("1. Configure your rules and settings in the web interface")
            print("2. Click 'Generate Configuration Files'")
            print("3. Choose your save method:")
            print("   📋 Copy: Copy to clipboard for manual editing")
            print("   💾 Save: Open save dialog to choose location")
            print("   📥 Download: Download directly to Downloads folder")
            print("   📁 Create: Direct file creation (available in server mode)")
            print("4. When done, click '🛑 Stop Server' to cleanly shut down")

            print("\n🚀 Enhanced Mode: All four buttons available!")
            print("💡 Tip: Use 'Create' for instant file generation!")
            print("💡 Tip: Click 'Stop Server' when finished to clean up")

            httpd.serve_forever()

    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user")
    except OSError as e:
        if e.errno == 48:  # Address already in use
            print(f"❌ Port {port} is already in use. Try a different port with --port")
        else:
            print(f"❌ Server error: {e}")
        return 1

    return 0

def main():
    parser = argparse.ArgumentParser(
        description='Launch Agentic Rules Framework enhanced setup with full file access'
    )
    parser.add_argument(
        '--port',
        type=int,
        default=8000,
        help='Port to run on (default: 8000)'
    )
    parser.add_argument(
        '--web',
        action='store_true',
        help='Launch with basic file saving (download with guidance)'
    )

    args = parser.parse_args()

    script_dir = Path(__file__).parent
    setup_html = script_dir / "setup.html"

    if not setup_html.exists():
        print(f"❌ Error: setup.html not found at {script_dir}")
        return 1

    if args.web:
        # Regular web mode - basic download functionality
        url = f"file://{setup_html.absolute()}"
        print("🌐 Launching setup.html in basic web mode...")
        print("📁 File creation: Manual download with guidance")
        print(f"URL: {url}")
        webbrowser.open(url)
        return 0
    else:
        # Enhanced mode - full file access
        return start_enhanced_setup(port=args.port, directory=script_dir)

if __name__ == '__main__':
    sys.exit(main())
