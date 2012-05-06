import os
# this should work across platforms
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
CONFIG_ROOT = os.path.join(BASE_DIR, 'config')
CONFIG_FILE = "slides.json"
STATIC_URL = "/static/"
# In the STATIC_ROOT
# The written database. Do not store in version control
DBSUFFIX = "headroom.jsondb"
DBFOLDER = "db"


