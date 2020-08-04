import os
import sys
p=os.path.split(os.path.realpath(__file__))[0]
sys.path.append(p)
sys.path.append("%s\\%s"%(p,"zkeco_dlls"))

#sys.stdout = sys.stderr
#print "sys.path==",sys.path
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")


from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

