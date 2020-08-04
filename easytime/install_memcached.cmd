@echo off
cd /d %~dp0
call init.bat
sc create bio-cache binPath= "%CD%\memcached\memcached.exe -p 11211 -l 127.0.0.1 -m 1024 -d runservice" DisplayName= "bio-cache" start= auto depend= TCPIP
sc description bio-cache "ZKTECO CO.,LTD."
net start bio-cache


