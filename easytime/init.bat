SET INSTALL_PATH=%CD%

if {%1}=={} GOTO noparms
SET INSTALL_PATH=%1

:noparms

SET PRJ_NAME=mysite
path = %INSTALL_PATH%\Python37;%INSTALL_PATH%\Utilities\;%PATH%;%INSTALL_PATH%\zkeco_dlls
set PYTHONPATH=%INSTALL_PATH%\Python37;%INSTALL_PATH%\Python37\Lib\site-packages;%INSTALL_PATH%;%INSTALL_PATH%\zkeco_dlls
SET DJANGO_SETTINGS_MODULE=%PRJ_NAME%.settings
ECHO %INSTALL_PATH%