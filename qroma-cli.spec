# -*- mode: python ; coding: utf-8 -*-

print("IN PYINSTALLER SPEC")

# PyInstaller should run from poetry
import subprocess
result = subprocess.run(["poetry", "env", "info", "-p"], shell=True, stdout=subprocess.PIPE, text=True)
poetry_venv = result.stdout.strip()
print(poetry_venv)
poetry_venv_site_packages = os.path.join(poetry_venv, "Lib", "site-packages")
print(poetry_venv_site_packages)


import tomllib
import datetime

pyproject_toml_path = os.path.join(os.getcwd(), 'pyproject.toml')
with open(pyproject_toml_path, 'rb') as f:
    py_project = tomllib.load(f)
    qroma_app_version = py_project['tool']['poetry']['version']
qroma_build_time = datetime.datetime.now().isoformat(timespec="seconds")

build_info_out_file_path = os.path.join(os.getcwd(), 'src', 'build_info.py')
with open(build_info_out_file_path, "w") as build_info_file:
    build_info_str = f'''
qroma_build_info = {{
    "app_version": "{qroma_app_version}",
    "build_time": "{qroma_build_time}",
}}
'''
    build_info_file.write(build_info_str)


block_cipher = None


a = Analysis(
    ['src\\qroma-cli.py'],
    pathex=[poetry_venv_site_packages],
    binaries=[],
    datas=[],
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
