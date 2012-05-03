import os
# this should work across platforms
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
CONFIG_ROOT = os.path.join(BASE_DIR, 'config')
STATIC_URL = "/static/"
# In the STATIC_ROOT
SLIDES_FILE = "slides.json"


