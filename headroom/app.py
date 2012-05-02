from bottle import route, run, view, static_file
from bottle import jinja2_template as template

import os

# Constants on initialization

# this should work across platforms
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = "/static/"

# Static

@route('/')
def index():
    ret = dict(hello=u'howdy')
    return template("index.html", ret=ret)

@route('/static/<filename>')
def server_static(filename):
    # we use the app.py file itself to determine the location of '/static/'
    return static_file(filename, root=STATIC_ROOT)

# Dynamic

@route('/ts/<slide>')
def text_slide(slide="intro"):
    ret = dict(STATIC_URL=STATIC_URL, hello=u"yoyo %s" % slide)
    return template("slide.html", ret=ret)

@route('/admin')
def admin_index():
    ret = dict(hello=u"admin. hello there. <h2>unce</h2>")
    return template("admin_index.html", ret=ret)

if __name__ =="__main__":
    import bottle
    bottle.debug(True)
    run(host='0.0.0.0', port=8080)

