@echo off
:: Batch script to run a PowerShell script as administrator

:: Check if the script is running as administrator
net session >nul 2>&1
if %errorLevel% == 0 (
    :: If running as administrator, execute the PowerShell script
    PowerShell -NoProfile -ExecutionPolicy Bypass -File "C:\path\to\yourfile.ps1"
) else (
    :: If not running as administrator, relaunch the batch file as administrator
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
    echo UAC.ShellExecute "cmd.exe", "/c ""%~s0""", "", "runas", 1 >> "%temp%\getadmin.vbs"
    "%temp%\getadmin.vbs"
    del "%temp%\getadmin.vbs"
    exit /B
)
