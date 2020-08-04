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
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
from django.db import connection
from django.conf import settings
#from mysite.utils import saveToFile

def saveToFile(text, fn=None, append=True, ctlsize=False):
    """/files/conn_logs.zk dont rename or change,this file is used by bioCat to check result"""
    if not fn:
        fn = os.path.join(settings.ADDITION_FILE_ROOT , 'conn_logs.zk')
    with open(fn, "w") as f:
        try:
            f.write(text)
        except:
            pass
    return fn



def conn_db():
    LMAC = uuid.uuid1().hex[-12:].lower()
    print("mac=%s" % LMAC)
    s = ''
    try:
        cursor = connection.cursor()
        s = "connect successfully"
        tables = connection.introspection.table_names(cursor)
        if len(tables) > 30:
            s='%s,Table is ok'%(s)
        else:
            s='%s,No tables'%(s)

    except Exception as e:
        s = '%s' % e

        s = "connect failed:" + s
    print(s)
    saveToFile(s)


def check_db():
    s = 'create tables failed:'
    try:
        with connection.cursor() as cursor:
            tables = connection.introspection.table_names(cursor)
            if len(tables) > 30:
                s = 'create tables successfully'
            else:
                s = 'create tables failed:'
    except Exception:
        pass
    print(s)
    saveToFile(s)


def clear_cache():
    from django.core.cache import cache
    if 'django_redis' in settings.CACHES['default']['BACKEND']:
        from django_redis import get_redis_connection
        get_redis_connection("default").flushall()
    cache.clear()
    print('Cache cleanup completed')


if __name__ == '__main__':
    import sys

    if len(sys.argv) == 1 or (len(sys.argv) > 1 and sys.argv[1] == 'conndb'):
        conn_db()
    elif len(sys.argv) > 1 and sys.argv[1] == 'checkdb':
        check_db()
    elif len(sys.argv) > 1 and sys.argv[1] == 'clear_cache':
        clear_cache()
