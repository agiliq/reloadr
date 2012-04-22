DESCRIPTION:
------------

reloadr watches your project directory and automatically reloads
all localhost pages in the browser.

DEPENDENCIES:
-------------

[juggernaut](https://github.com/maccman/juggernaut) requires nodejs/redis

[pyinotify](http://pyinotify.sourceforge.net/)

RUN:
----

Setup your redis+juggernaut server and configure `JUGGERNAUT_SERVER`, `JUGGERNAUT_PORT` of `reloadr.js` as well as `REDIS_SERVER` in `watch.py`

Alternatively, you can use the free nano instance of redistogo from heroku (in this case you'll need to export `REDISTOGO_URL` env variable instead of `REDIS_SERVER`)

Run the file monitor:

    python reloadr/watch.py

from your project directory

add the included client scripts:

    <script src="/path/to/application.js" type="text/javascript" charset="utf-8"></script>
    <script src="/path/to/reloadr.js" type="text/javascript" charset="utf-8"></script>

to your base html page.
