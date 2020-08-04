import os
import sys
from ctypes import *
p=os.path.split(os.path.realpath(__file__))[0]

os.environ['PATH']="%s/%s"%(p,"zkeco_dlls;")+"%s/%s"%(p,"django;")+"%(p)s\\Python37;"%{"p":p}+os.environ['PATH']

new_sys_path = [p]
virtualenv=['%s/Python37','%s/zkeco_dlls','%s/python37/dlls','%s/python37/scripts','%s/python37/lib','%s/Python37/lib/site-packages']
for d in virtualenv:
    new_sys_path.append(d%p)

sys.path = new_sys_path

os.chdir(p)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

 
