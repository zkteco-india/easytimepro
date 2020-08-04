@echo off
cd /d %~dp0
call init.bat
"%cd%/Python37/python.exe" "%cd%/ConnDb.py" clear_cache
pause
