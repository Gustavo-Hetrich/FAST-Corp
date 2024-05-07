@echo off
echo Rodando script de instalação de programas...
echo.

REM Definir o caminho completo para o script PowerShell
set "script_ps1=Y:\SUPORTE TECNICO\Corporativo\Macros\Bot Format\Rede"

REM Verificar se o script PowerShell existe
if not exist "%script_ps1%" (
    echo O script PowerShell não foi encontrado.
    pause
    exit /b
)

REM Executar PowerShell como administrador
powershell.exe -Command "Start-Process powershell.exe -Verb RunAs -ArgumentList '-NoProfile -ExecutionPolicy Bypass -File ""%script_ps1%""'"
