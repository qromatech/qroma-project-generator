CALL poetry run python -m PyInstaller qroma-cli.spec

copy dist\qroma.exe %UserProfile%\.qroma

cd "%~dp0"
