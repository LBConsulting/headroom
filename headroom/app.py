from bottle import route, run, view, static_file, post, get, redirect
from bottle import jinja2_template as template
from db import slideload, Slide
import simplejson as json
from settings import STATIC_URL, CONFIG_ROOT
from forms import DemographicsForm

import os

# DB Constants on initialization
s = Slide()

## logging functions
# Static

@route('/')
def index():
    slide = s.by_weight()[0]
    ret = dict(slide=slide, config=dict(STATIC_URL=STATIC_URL))
    print ret
    return template("slide.html", page=ret)

@route('/static/<filename>')
def server_static(filename):
    # we use the app.py file itself to determine the location of '/static/'
    return static_file(filename, root=STATIC_ROOT)

# Dynamic

@get('/input')
def posted_slide():
    ret = {}
    ## get this query into db
    for slide in s.objects():
        if slide['kind'] == 'InputSlide':
            ret = slide
    next_slide_id = "testing"
    next_slide = "/slide/%s" % next_slide_id
    redirect(next_slide)

@post('/input')
def posted_input():
    form = DemographicsForm(request.POST)
    if form.validate():
        return "Posted month: %s" % form.birth_month.data
    else:
        return "Error..."

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

