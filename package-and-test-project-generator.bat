pyinstaller qroma-cli.spec
@REM pyinstaller --onefile --paths venv\Lib\site-packages src/qroma-cli.py

rmdir /S /Q test
mkdir test

copy dist\qroma.exe test

cd test

CALL qroma new :abc --do-build --build-ignore-www --dev-board-platforms platformio --dev-board-platforms arduino
REM --replace-existing

cd /D %UserProfile%
cd qroma-projects
cd abc
cd device-boards\esp32\abc

CALL code .
cd "%~dp0"
