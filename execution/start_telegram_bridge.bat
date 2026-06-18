@echo off
setlocal
set PATH=%APPDATA%\npm;%LOCALAPPDATA%\Programs\Python\Python312;%LOCALAPPDATA%\Programs\Python\Python312\Scripts;%PATH%
cd /d "%~dp0\.."

if not exist ".tmp" mkdir ".tmp"

:loop
echo [watchdog %date% %time%] Arrancando bridge de Telegram... >> .tmp\telegram_bridge.log
python execution\telegram_bridge.py >> .tmp\telegram_bridge.log 2>&1
echo [watchdog %date% %time%] Bridge termino (codigo %errorlevel%), reiniciando en 15s... >> .tmp\telegram_bridge.log
timeout /t 15 /nobreak > nul
goto loop
