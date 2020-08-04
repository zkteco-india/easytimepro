@echo off
cd /d %~dp0
call init.bat
python ConnDb.py
pause
