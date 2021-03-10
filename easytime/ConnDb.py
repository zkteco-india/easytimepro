#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: michael.wang
# datetime: 2020/03/20 18:08
# last modified by:
"""
This file is very important to serve the console program
"""
import uuid
import os
PROJECT_PATH = os.path.abspath(os.path.dirname(os.path.dirname('__file__')))
def saveToFile(text, fn=None, append=True, ctlsize=False):
    """/files/conn_logs.zk dont rename or change,this file is used by bioCat to check result"""
    if not fn:
        fn = os.path.join(PROJECT_PATH+'/files/' , 'conn_logs.zk')
    with open(fn, "w") as f:
        try:
            f.write(text)
        except:
            pass
    return fn



def conn_db():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    from django.db import connection
    from django.conf import settings
    LMAC = uuid.uuid1().hex[-12:].lower()
    print("mac=%s" % LMAC)
    s = ''
    import time
    try:
        t1=time.time()
        cursor = connection.cursor()
        t=(time.time()-t1)*1000
        s = "connection is successful"
        tables = connection.introspection.table_names(cursor)
        if len(tables) < 5:
            s='%s,No tables'%(s)

    except Exception as e:
        s = '%s' % e

        s = "connection failed:" + s

    s = '%s %s'%(settings.DATABASE_ENGINE,s)
    print(s)
    saveToFile(s)


def check_db():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    from django.db import connection
    s = 'create tables failed:'
    try:
        with connection.cursor() as cursor:
            tables = connection.introspection.table_names(cursor)
            if len(tables) > 50:
                s = 'create tables successfully'
            else:
                s = 'create tables failed:'
    except Exception:
        pass
    print(s)
    saveToFile(s)


def clear_cache():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    from django.conf import settings
    from django.core.cache import cache
    if 'django_redis' in settings.CACHES['default']['BACKEND']:
        from django_redis import get_redis_connection
        get_redis_connection("default").flushall()
    cache.clear()
    print('Cache cleanup completed')
    
def upgrade_software():
    p=os.path.split(os.path.realpath(__file__))[0]

    os.environ['PATH']="%s/%s"%(p,"zkeco_dlls;")+"%(p)s\\Python37;"%{"p":p}+os.environ['PATH']

    new_sys_path = [p]
    virtualenv=['%s/Python37','%s/zkeco_dlls','%s/python37/dlls','%s/python37/scripts','%s/python37/lib','%s/Python37/lib/site-packages']
    for d in virtualenv:
        new_sys_path.append(d%p)

    sys.path = new_sys_path

    from zkeco_dlls import easy_upgrade
    easy_upgrade.upgrade_software()


if __name__ == '__main__':
    import sys

    if len(sys.argv) == 1 or (len(sys.argv) > 1 and sys.argv[1] == 'conndb'):
        conn_db()
    elif len(sys.argv) > 1 and sys.argv[1] == 'checkdb':
        check_db()
    elif len(sys.argv) > 1 and sys.argv[1] == 'clear_cache':
        clear_cache()
    elif len(sys.argv) > 1 and sys.argv[1] == 'upgrade_software':
        upgrade_software()
