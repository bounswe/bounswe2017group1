#!/usr/bin/env python

"""RESTful Open Annotation server based on Eve.

The RESTful Open Annotation API is primarily implemented using two
ways of modifying the Eve default API: 

1. global configuration of keys in settings.py to use OA names,
e.g. "annotatedAt" instead of the default "_created".

2. event hooks to modify incoming and outcoming documents in more
complex ways, such as removing the default "@context" value on POST
and adding it to the top-level graph on GET.
"""

__author__ = 'Sampo Pyysalo'
__license__ = 'MIT'

import sys
import os

from eve import Eve

from oaeve import setup_callbacks

from settings import PORT

# TODO: I think we need this for mod_wsgi, but make sure.
appdir = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(appdir))

try:
    from development import DEBUG
    print >> sys.stderr, '########## Devel, DEBUG %s ##########' % DEBUG
except ImportError:
    DEBUG = False

# Eve's "settings.py application folder" default fails with wsgi
app = Eve(settings=os.path.join(appdir, 'settings.py'))

setup_callbacks(app)

def main(argv):
    if not DEBUG:
        app.run(host='0.0.0.0', port=PORT, debug=False)
    else:
        app.run(debug=DEBUG, port=PORT)
    return 1

if __name__ == '__main__':
    sys.exit(main(sys.argv))
