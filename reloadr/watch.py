#!/usr/bin/python

import os

import redis
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

class EventHandler(pyinotify.ProcessEvent):
    def process_IN_MODIFY(self, event):
        if any([True for ext in EXTENSIONS if event.pathname.endswith(ext)]):
            msg = "Modified: %s" % (event.pathname)
            print msg
            r = redis.Redis(REDIS_SERVER)
            jug = Juggernaut(r)
            jug.publish("channel1", msg)

handler = EventHandler()
notifier = pyinotify.Notifier(wm, handler)
wdd = wm.add_watch(cwd, mask, rec=True)

notifier.loop()
