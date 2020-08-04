@echo off
cd /d %~dp0
sc create bio-cache binPath= "%CD%\redis-server.exe --service-run %CD%\redis.conf" DisplayName= "bio-redis" start= auto depend= TCPIP
sc description bio-cache "ZKTECO CO.,LTD."
net start bio-cache
pause



