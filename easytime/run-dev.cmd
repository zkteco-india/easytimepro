cls
@echo off
echo service is running ...
cd /d %~dp0
call init.bat
@for /L %%i IN (0,1,2000) DO @python manage.py runserver 0.0.0.0:80
