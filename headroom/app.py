from bottle import route, run, view, static_file
from bottle import jinja2_template as template
from db import slideload
import simplejson as json
from settings import STATIC_URL, CONFIG_ROOT

import os

# Constants on initialization

## logging functions
# Static

@route('/')
def index():
    slides = slideload()
    slide = slides['slides'][0]
    ret = dict(slide=slide, config=dict(STATIC_URL=STATIC_URL))
    print ret
    return template("slide.html", page=ret)

@route('/static/<filename>')
def server_static(filename):
    # we use the app.py file itself to determine the location of '/static/'
    return static_file(filename, root=STATIC_ROOT)

# Dynamic

@route('/slide/<slide_id>')
def slide(slide_id="intro"):
    slides = slideload()
    ret = dict(STATIC_URL=STATIC_URL, 
            hello=u"yoyo %s" % slide)
    return template("slide.html", ret=ret)

@route('/admin')
def admin_index():
    ret = dict(hello=u"admin not implemented")
    return template("admin_index.html", ret=ret)

if __name__ =="__main__":
    import bottle
    bottle.debug(True)
    run(host='0.0.0.0', port=8080)

