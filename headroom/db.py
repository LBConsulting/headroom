#-*- coding: utf-8 -*-

import simplejson as json
import os
from operator import itemgetter
from settings import CONFIG_ROOT, CONFIG_FILE, DB_ROOT, DBSUFFIX
import tempfile
from shutil import copy
import datetime
from uuid import uuid1 as uuid

__version__ = "0.2.0"

# required for python <=python2.5
## from __future__ import with

class Model(object):
    def __init__(self, *args, **kwargs):
        self.config = CONFIG_FILE
        try:
            self.objects = self._load()
        except:
            self.objects = {}
        if (kwargs is not None):
            self.objects.update(kwargs)

    def _load(self, **kargs):
        """
        Keeping the kwarg for quick loads
        """
        retpath = os.path.join(CONFIG_ROOT, self.config)
        with open(retpath, 'r') as retfile:
            retjson = retfile.read()
        ret = json.loads(retjson)
        # Just get the slides, not the _doc
        return ret

    def _loaddb(self, dbname="models"):
        retpath = os.path.join(DB_ROOT, "%s.jsondb" % dbname)
        with open(retpath, 'r') as retfile:
            retjson = retfile.read()
        ret = json.loads(retjson)
        # Just get the slides, not the _doc
        return ret

    def _write(self, config):
        """
        Writes to the CONFIG_FILE
        """
        retpath = os.path.join(CONFIG_ROOT, self.config)
        fh, fp = tempfile.mkstemp(suffix=DBSUFFIX, dir=DB_ROOT)
        try:
            configtowrite = json.dumps(config)
        except:
            print "ERROR Dumping Config JSON"
            return False
        try:
            with os.fdopen(fh, 'w') as f:
                f.write(configtowrite)
            f.close()
            return True
        except:
            print "ERROR Writing File"
            return False

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
        self.db = self._loaddb()
        self.tmpon = False
        self.dbfp = ""
        super(Slide, self).__init__(*args, **kwargs)
        if self.config is None:
            self.config = CONFIG_FILE
        if kwargs is not None:
            self.objects.update(kwargs)

    def _load(self):
        return dict(slides=super(Slide, self)._load()['slides'])

    def _loaddb(self):
        return super(Slide, self)._loaddb('slidedb')

    def _tmpdb(self, dbdata=None, db=DB_ROOT):
        """
        make a temporary file to write the db into
        """
        fh, fp = tempfile.mkstemp(suffix=DBSUFFIX, dir=db)
        if dbdata is not None:
            try:
                dbtowrite = json.dumps(dbdata)
            except:
                print 'Could not dump json to db'
                return False
            try:
                with os.fdopen(fh, 'w+') as f:
                    f.write(dbtowrite)
                f.close()
                self.tmpon, self.dbfp, self.dbfh = True, fp, fh
                return True
            except:
                print "Error writing DB"
                return False
        with os.fdopen(fh, 'w+') as f:
            f.write(json.dumps(self.objects))
        f.close()
        self.tmpon, self.dbfp, self.dbfh = True, fp, fh
        return True

    def _dynodb(self, dbname=None, db=DB_ROOT):
        """
        writes all dynamic keys (id, datetime/RT, and slide order)
        to the dynamicdb
        """
        if self.tmpon:
            try:
                incr = 0
                for slide in self.by_weight():
                    incr += 1
                    _metadata = dict(id=incr, uuid=str(uuid()))
                    print slide
                    slide.update(_metadata)
                try:
                    with open(self.dbfp, "w") as f:
                        f.write(json.dumps(slide))
                    f.close()
                    ##self.db = super(Slide, self)._loaddb(self.fp)
                except:
                    print "ERROR, couldn't write file"
                    return False
            except:
                print "ERROR, couldn't insert into file"
                return False


    def _writedb(self, dbname=None, db=DB_ROOT):
        """
        simply copies the tmp file to the db 
        folder and adds a timestamp to the
        filename. 
        """
        if dbname is not None:
            dbname = "%s.jsondb" % dbname
        dbname = "%(dbname)s-%(timestamp)s.jsondb" % dict(dbname='slidedb',
                timestamp=datetime.datetime.strftime(datetime.datetime.now(),
                    format="%Y%m%d-%H%M%S"))
        fp = os.path.join(db, dbname)
        copy(self.dbfp, fp)
        self.tmpon, self.dbfp = False, fp
        return True

    def slides(self):
        return self.objects['slides']

    def by_weight(self):
        return sorted(self.objects['slides'], key=itemgetter('weight'))

    def by_id(self, sid):
        """
        The id <sid> is determined by weight order and is only available to
        items already in the database.
        """
        slide = {}
        for obj in self.objects['slides']:
            if obj['_metadata']['id'] == sid:
                slide.update(obj)
        return slide

    def next(self):
        """
        finds the next slide in relation to the current one
        """
        return

    def previous(self):
        """
        finds the previous slide in relation to the current one
        """
        return



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
