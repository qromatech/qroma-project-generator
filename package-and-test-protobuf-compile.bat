pyinstaller qroma-cli.spec

copy dist\qroma.exe test

cd test

CALL qroma protobuf :abc

cd "%~dp0"
