pyinstaller qroma-cli.spec
@REM pyinstaller --onefile --paths venv\Lib\site-packages src/qroma-cli.py

rmdir /S /Q test
mkdir test

copy dist\qroma.exe test

cd test

CALL qroma init abc

cd "%~dp0"
