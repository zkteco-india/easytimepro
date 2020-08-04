cls
@echo off
cd /d %~dp0
call init.bat
rem python manage.py makemigrations
python manage.py migrate
pause
