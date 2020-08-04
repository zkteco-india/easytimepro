@echo off
cd /d %~dp0
set path=%windir%\system32;%path%
taskkill /im bioCat.exe /f
net stop AttServer
net stop bio-server

net stop bio-proxy

for /l %%i in (0,1,7) do net stop bio-apache%%i




