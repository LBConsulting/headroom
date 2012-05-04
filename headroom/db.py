#-*- coding: utf-8 -*-

import simplejson as json
import os
from operator import itemgetter
from settings import CONFIG_ROOT, SLIDES_FILE, DBFOLDER, DBSUFFIX
import tempfile

## SLIDES_FILE = 'testing-3.json'

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
    fh, fp = tempfile.mkstemp(suffix=DBSUFFIX, dir=DBFOLDER)
    try:
        jsontowrite = json.dumps(writein)
    except:
        print "ERROR Dumping JSON"
        return False
    try:
        with os.fdopen(fh, 'w') as jsonfile:
            jsonfile.write(jsontowrite)
        jsonfile.close()
        return True
    except:
        print "ERROR Writing File"
        return False


class Model(object):
    def __init__(self, *args, **kwargs):
        self.jsonfile = SLIDES_FILE
        try:
            self.objects = self._load()
        except:
            self.objects = {}
        if (kwargs is not None):
            self.objects.update(kwargs)

    def _load(self):
        """
        Keeping the kwarg for quick loads
        """
        retpath = os.path.join(CONFIG_ROOT, self.jsonfile)
        with open(retpath, 'r') as retfile:
            retjson = retfile.read()
        ret = json.loads(retjson)
        # Just get the slides, not the _doc
        return ret

    def _write(self, writeme):
        """
        TODO: Locking
        """
        try:
            towrite = json.dumps(writeme)
        except:
            return -1
        slide_filepath = os.path.join(CONFIG_ROOT, self.jsonfile)
        with open(slide_filepath, 'w') as slides_file:
            slides_file.write(towrite)
        slides_file.close()
        return True

    def objects(self):
        return self.objects

    def by_field(self, slide_id):
        return [x[str(slide_id)] for x in self.objects]

    def fields(self):
        ret = []
        fields = [x.keys() for x in self.objects]
        for field in fields:
            ret.extend(field)
        return set(ret)

    def find(self, query):
        ret = []
        for field in self.fields():
            try:
                ret.extend([x['title'] for x in self.objects if x.get(field, 0).lower() == query.lower()])
            except KeyError:
                print "No such key 'title'"
                return False
        return ret
        
class Slide(Model):
    def __init__(self, *args, **kwargs):
        super(Slide, self).__init__(*args, **kwargs)
        if self.jsonfile is None:
            self.jsonfile = SLIDES_FILE
        if kwargs is not None:
            self.objects.update(kwargs)

    def _load(self, slidesfile=SLIDES_FILE):
        return dict(slides=super(Slide, self)._load()['slides'])

    def by_weight(self):
        return sorted(self.slides, key=itemgetter('weight'))

class Config(Model):
    """
    A config model for taking in configured files
    """
    pass

class Result(Model):
    """
    A result model for writing, computing, and displaying results
    """
    pass
