#!/usr/bin/env python
#coding=utf-8
import os,sys
p=os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
if sys.version[0]=='3':
    os.environ['PATH']="%(p)s\\Python37;"%{"p":p}+os.environ['PATH']
    newpath="%INSTALL_PATH%\\Python37;%INSTALL_PATH%\\Python37\\Lib\\site-packages;%INSTALL_PATH%".replace('%INSTALL_PATH%',p).split(";")
else:
    os.environ['PATH']="%(p)s\\Python37;"%{"p":p}+os.environ['PATH']
    newpath="%INSTALL_PATH%\\Python37;%INSTALL_PATH%\\Python37\\Lib\\site-packages;%INSTALL_PATH%".replace('%INSTALL_PATH%',p).split(";")
for t in newpath:
    if t not in sys.path:
        sys.path.append(t)
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
import django
django.setup()
from mysite.cloud_kafka import *


if __name__ == '__main__':
    Run_kafka()


