@echo off

set VSCODE_PATH="C:\Windows\SysWOW64\WindowsPowerShell\v1.0\powershell.exe"
set WORKSPACE_PATH="C:\Users\dani_\Documents\MEGAsync\UPC\Q9\TFG\Development\TFG-Development"
set SCRIPT_PATH="%WORKSPACE_PATH%\src\main.py"

timeout /t 5 /nobreak > nul
PowerShell -NoProfile -ExecutionPolicy Bypass -Command "& 'C:\Program Files\Microsoft Visual Studio\2022\Community\Common7\Tools\Launch-VsDevShell.ps1'"
