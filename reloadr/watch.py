#!/usr/bin/python

import os
import redis
import urlparse
import pyinotify

from juggernaut import Juggernaut

wm = pyinotify.WatchManager()  # Watch Manager
mask = pyinotify.IN_MODIFY
cwd = os.getcwd()

EXTENSIONS = [
    '.py',
    '.html',
    '.css',
    '.js',
]

REDIS_SERVER = "localhost"

if os.environ.has_key('REDISTOGO_URL'):
    urlparse.uses_netloc.append('redis')
    url = urlparse.urlparse(os.environ['REDISTOGO_URL'])
    REDIS = redis.Redis(host=url.hostname, port=url.port, db=0, password=url.password)
else:
    REDIS = redis.Redis(REDIS_SERVER)

class EventHandler(pyinotify.ProcessEvent):
    def process_IN_MODIFY(self, event):
        if any([True for ext in EXTENSIONS if event.pathname.endswith(ext)]):
            msg = "Modified: %s" % (event.pathname)
            print msg
            jug = Juggernaut(REDIS)
            jug.publish("channel1", msg)

handler = EventHandler()
notifier = pyinotify.Notifier(wm, handler)
wdd = wm.add_watch(cwd, mask, rec=True)

notifier.loop()
