# -*- mode: python ; coding: utf-8 -*-

print("IN PYINSTALLER SPEC")

# PyInstaller should run from poetry
import subprocess
result = subprocess.run(["poetry", "env", "info", "-p"], shell=True, stdout=subprocess.PIPE, text=True)
poetry_venv = result.stdout.strip()
print(poetry_venv)
poetry_venv_site_packages = os.path.join(poetry_venv, "Lib", "site-packages")
print(poetry_venv_site_packages)


added_files = [('pyproject.toml', 'pyproject.toml')]


block_cipher = None


a = Analysis(
    ['src\\qroma-cli.py'],
    pathex=[poetry_venv_site_packages],
    binaries=[],
    datas=added_files,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='qroma',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
