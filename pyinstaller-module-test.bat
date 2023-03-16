pyinstaller pyinstaller_module_test.spec
@REM pyinstaller --onefile --paths venv\Lib\site-packages src/qroma-cli.py

rmdir /S /Q test
mkdir test-installer

copy dist\pyinstaller_test.exe test-installer

cd test-installer

CALL pyinstaller_test env

cd "%~dp0"
