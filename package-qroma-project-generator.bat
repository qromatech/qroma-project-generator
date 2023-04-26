CALL poetry run python -m PyInstaller qroma-cli.spec

copy dist\qroma.exe %UserProfile%\.qroma

CALL poetry run python copy_to_downloads_directory.py

cd "%~dp0"
