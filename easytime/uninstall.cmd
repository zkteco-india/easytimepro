@echo off
cd /d %~dp0
set path=%windir%\system32;%path%
taskkill /im bioCat.exe /f
net stop AttServer
sc delete AttServer
net stop bio-server
sc delete bio-server

net stop bio-proxy
sc delete bio-proxy

for /l %%i in (0,1,7) do net stop bio-apache%%i
for /l %%i in (0,1,7) do sc delete bio-apache%%i

net stop bio-mysql
sc delete bio-mysql

net stop bio-pgsql
sc delete bio-pgsql

net stop bio-cache
sc delete bio-cache

net stop bio-redis
sc delete bio-redis

