#-*- coding: utf-8 -*-

import simplejson as json
import os
from operator import itemgetter
from settings import CONFIG_ROOT, SLIDES_FILE

SLIDES_FILE = 'testing-3.json'

# DBUTILS (MAY BE MOVED)
# may be needed

## from __future__ import with

def jsonfileload(config):
    """
    Keeping the kwarg for quick loads
    """
    retpath = os.path.join(CONFIG_ROOT, config)
    with open(retpath, 'r') as retfile:
        retjson = retfile.read()
    ret = json.loads(retjson)
    # Just get the slides, not the _doc
    return ret

def jsonfilewrite(writein, config):
    """
    writes and entire key into one file
    """
    retpath = os.path.join(CONFIG_ROOT, config)
    try:
        jsontowrite = json.dumps(writein)
    except:
        print "ERROR Dumping JSON"
        return False
    try:
        with open(retpath, 'w') as jsonfile:
            jsonfile.write(jsontowrite)
        jsonfile.close()
        return True
    except:
        print "ERROR Writing File"
        return False


class Model(object):
    def __init__(self, **kwargs):
        self.slidesfile = SLIDES_FILE
        self.slides = self._load()

    def _load():
        """
        Keeping the kwarg for quick loads
        """
        retpath = os.path.join(CONFIG_ROOT, self.slidesfile)
        with open(retpath, 'r') as retfile:
            retjson = retfile.read()
        ret = json.loads(retjson)
        # Just get the slides, not the _doc
        return ret

    def _write(writeme):
        """
        TODO: Locking
        """
        try:
            towrite = json.dumps(writeme)
        except:
            return -1
        slide_filepath = os.path.join(CONFIG_ROOT, slidesfile)
        with open(slide_filepath, 'w') as slides_file:
            slides_file.write(towrite)
        slides_file.close()
        return True

    def objects(self):
        return self.slides

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
    def _load(slidesfile=SLIDES_FILE):
        """
        Keeping the kwarg for quick loads
        """
        slide_filepath = os.path.join(CONFIG_ROOT, slidesfile)
        with open(slide_filepath, 'r') as slides_file:
            slidesjson = slides_file.read()
        slides = json.loads(slidesjson)
        # Just get the slides, not the _doc
        slides = slides['slides']
        return slides

    def by_weight(self):
        return sorted(self.slides, key=itemgetter('weight'))
