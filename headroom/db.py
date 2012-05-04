#-*- coding: utf-8 -*-

import simplejson as json
import os
from operator import itemgetter
from settings import CONFIG_ROOT, SLIDES_FILE

# DBUTILS (MAY BE MOVED)
# may be needed

## from __future__ import with

def slideload(slidesfile=SLIDES_FILE):
    slide_filepath = os.path.join(CONFIG_ROOT, slidesfile)
    with open(slide_filepath, 'r') as slides_file:
        slidesjson = slides_file.read()
    slides = json.loads(slidesjson)
    # Just get the slides, not the _doc
    slides = slides['slides']
    return slides


class Model(object):
    def __init__(self, slidesfile=SLIDES_FILE):
        self.slides = slideload(slidesfile)

    def objects(self):
        return self.slides

    def by_weight(self):
        return sorted(self.slides, key=itemgetter('weight'))

    def by_field(self, slide_id):
        return [x[str(slide_id)] for x in self.slides]

    def fields(self):
        ret = []
        fields = [x.keys() for x in self.slides]
        for field in fields:
            ret.extend(field)
        return set(ret)

    def find(self, query):
        ret = []
        for field in self.fields():
            ret.extend([x['title'] for x in self.slides if x.get(field, 0).lower() == query.lower()])
        return ret
        

class Slide(Model):
    pass
