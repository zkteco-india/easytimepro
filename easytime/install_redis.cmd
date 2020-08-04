@echo off
cd /d %~dp0
call init.bat
set path=%windir%\system32;%path%
sc create bio-cache binPath= "\"%CD%\redis\redis-server.exe\" --service-run \"%CD%\redis\redis.conf\"" DisplayName= "bio-redis" start= auto depend= TCPIP
sc description bio-redis "ZKTeco Biometrics India Pvt.Ltd"
net start bio-cache



