from bottle import route, run, view, static_file, post, get, redirect
from bottle import jinja2_template as template
from db import Slide
from settings import STATIC_URL, CONFIG_ROOT
from forms import DemographicsForm

import os

__version__ = "0.2.0"

# Homebrewed JSONDB Manager on initialization
s = Slide()
s._tmpdb()
s._dynodb()

## logging functions
# Static

#files
@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root=STATIC_ROOT)

#the homepage just uses the first slide (based on weight)
@route('/')
def index():
    # get the first slide
    slide = s.by_id(1)
    ret = dict(STATIC_URL=STATIC_URL, 
            slide=slide,
            nxt=s.nxt()['_metadata']['url'],
            previous=s.previous()['_metadata']['url']
            )
    return template("slide.html", page=ret)


    slide = s.by_weight()[0]
    slide['_url'] = '/'
    page = dict(slide=slide,config=dict(STATIC_URL=STATIC_URL))
    return template("slide.html", page=page)

# Dynamic

#forms are pumped through here
#this probably needs to be worked on after the urls
@get('/input')
def posted_slide():
    form = DemographicsForm()
    ret = {}
    ## get this query into db
    for slide in s.objects():
        if slide['kind'] == 'InputSlide':
            ret = slide
    next_slide_id = "testing"
    next_slide = "/slide/%s" % next_slide_id
    return template("input.html", page=ret, form=form)
    ##redirect(next_slide)

@post('/input')
def posted_input():
    form = DemographicsForm(request.forms)
    if form.validate():
        return "Posted month: %s" % form.birth_month.data
    else:
        return "Error..."

@route('/s/<slide_id:int>')
def slide(slide_id=None):
    if slide_id is None or 0:
        return redirect('/')
    slide = s.by_id(slide_id)
    nxt, previous = '', ''
    try:
        nxt=s.nxt()['_metadata']['url'],
        previous=s.previous()['_metadata']['url']
    except:
        pass
    ret = dict(STATIC_URL=STATIC_URL, 
            slide=slide,
            nxt=nxt,
            previous=previous
            )
    return template("slide.html", page=ret)

# admin for version 2.0
@route('/admin')
def admin_index():
    ret = dict(hello=u"admin not implemented")
    return template("admin_index.html", ret=ret)

# This is where the conductor taps her wand.
if __name__ =="__main__":
    import bottle
    bottle.debug(True)
    bottle.TEMPLATES.clear()
    run(host='0.0.0.0', port=8080)

