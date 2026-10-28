@echo off
py -m pip install -r requirements.txt pyinstaller
py -m PyInstaller --noconfirm --onefile --noconsole --name Oz12E_Moylash --collect-submodules uvicorn --hidden-import main --hidden-import ui --add-data "data.json;." --hidden-import multipart --hidden-import python_multipart desktop.py
echo.
echo Tayyor: dist\Oz12E_Moylash.exe
pause
