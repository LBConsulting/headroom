#-*- coding: utf-8 -*-

import simplejson as json
import os
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

class Slide():
    def __init__(self, slidesfile=SLIDES_FILE):
        self.slides = slideload(slidesfile)

    def objects(self):
        return self.slides

    def by_weight(self):
        return sorted(self.slides, key=lambda slide: slide['weight'])




