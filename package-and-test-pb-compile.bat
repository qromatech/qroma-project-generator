pyinstaller qroma-cli.spec

copy dist\qroma.exe test

cd test
cd abc

CALL ..\qroma pb

cd "%~dp0"
