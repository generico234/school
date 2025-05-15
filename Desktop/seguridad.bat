@echo off
setlocal enabledelayedexpansion
set a=0

:menu
set /a a+=1

if %a% gtr 3 (
    goto exit
)

echo =========== MENU ==============
set /p usuario=Ingrese el nombre de usuario: 
set /p contraseña=Ingrese la contraseña: 
echo ===============================

if /i "%usuario%"=="Rosi" (
    goto program
) else (
    goto menu
)

:program
if "%contraseña%"=="123" (
    start "" "C:\Users\%username%\Desktop\confidencial.txt"
    goto fin
) else (
    echo Contraseña incorrecta.
    goto menu
)

:exit
echo Le erraste 3 veces, la policia esta en camino.
pause
exit

:fin
echo Programa abierto con esisto.
pause
exit
