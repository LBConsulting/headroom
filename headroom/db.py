import simplejson as json
import os
from settings import CONFIG_ROOT

# DBUTILS (MAY BE MOVED)
# may be needed

## from __future__ import with

def slideload(configfile='slides.json'):
    slide_filepath = os.path.join(CONFIG_ROOT, configfile)
    with open(slide_filepath, 'r') as slides_file:
        slidesjson = slides_file.read()
    slides = json.loads(slidesjson)
    return slides


