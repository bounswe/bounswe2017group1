"""Settings for Eve and RESTful OA support functionality."""

__author__ = 'Sampo Pyysalo'
__license__ = 'MIT'

# The port on the server to listen to
PORT = 5005

# CORS settings
X_DOMAINS = '*'  # Access-Control-Allow-Origin: * (open to all)

# Never render responses as XML (RDF/XML support TODO)
XML = False

# Name for target resource field to add for search
TARGET_RESOURCE = 'target_resource'

# Maximum document size in characters. (Note: some PMC docs go over 1M)
MAX_DOC_SIZE = 100 * 1024

# TODO: the LD_ settings really belong in oajson.py
# Default JSON-LD @context.
LD_CONTEXT = 'http://www.w3.org/ns/oa.jsonld'

# Default JSON-LD @type for items.
LD_ITEMTYPE = 'oa:Annotation'

# Default JSON-LD @type for collections. 
# TODO: make sure we want to use this spec
LD_COLLTYPE = 'http://www.w3.org/ns/hydra/core#Collection'

# Open Annotation requires xsd:dateTime (ISO 8601), such as
# "1997-07-16T19:20:30.45+01:00". TODO: time zone
DATE_FORMAT = '%Y-%m-%dT%H:%M:%S'

# Eve HATEOAS controls are not part of JSON-LD, and partially
# rendudant with general use of link relations and URIs inherent in
# JSON-LD. However, they can be used to generate links for traversing
# paginated collections.
HATEOAS = True

# Return entire document on PUT, POST and PATCH.
BANDWIDTH_SAVER = False

# Eve ITEMS list largely matches for the "@graph" of JSON-LD named
# graphs http://www.w3.org/TR/json-ld/#named-graphs
ITEMS = '@graph'

# Eve DATE_CREATED is essentially the same thing as oa:annotatedAt
# ("annotatedAt" for short in the @context of both OA and Web
# Annotation specs).
DATE_CREATED = 'annotatedAt'

# Eve LAST_UPDATED is NOT actually the same as oa:serializedAt, but
# the approximation is not unreasonable (think "serialized into the
# database") and so used here.
LAST_UPDATED = 'serializedAt'

# For simplicity, disable concurrency control for the moment, removing
# the "_etag" attribute and the checking for If-Match headers
# (see http://python-eve.org/features.html#concurrency)
IF_MATCH = False

# TODO: disable (setting to Null doesn't work) or rewrite '_meta'
#META = None

# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
# individual items  (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

# Maximum value allowed for QUERY_MAX_RESULTS query parameter.
PAGINATION_LIMIT = 10000

# Default value for QUERY_MAX_RESULTS.
PAGINATION_DEFAULT = 10000

# Schemata for validating representations. See Cerberus
# (https://github.com/nicolaiarocci/cerberus) for syntax and docs.
document_schema = {
    'text': {
        'type': 'string',
        'minlength': 1,
        'maxlength': MAX_DOC_SIZE,
        'required': True,
    },
    'name': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 100,
        'required': True,
        'unique': True,
    },
}

annotation_schema = {
    '_id': {
        'type': 'string',
    },
    '@context': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 1024,
    },
    '@type': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 1024,
    },
    'body': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 1024,
    },
    'target': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 1024,
        'required': True,
    },
    'annotatedBy': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 1024,
    },
    # added to aid in search; target without fragment identifiers (etc.)
    TARGET_RESOURCE: {
        'type': 'string',
        'minlength': 1,
        'maxlength': 1024,
        'required': True,
    },
}

DOMAIN = {
    'documents': {
        'schema': document_schema,
        # allow lookup by document name
        'additional_lookup': {
            # TODO: add schema constraint that "name" must match this
            'url': 'regex("[\w.-]+")',
            'field': 'name'
        },
    },
    'annotations': {
        'url': 'annotations',
        'item_url': 'regex("[0-9]+")',
        'schema': annotation_schema,
    },
    'annbydoc': {
        # http://python-eve.org/features.html#sub-resources
        'datasource': {
            'source': 'annotations'
        },
        'url': 'documents/<regex(".+"):'+TARGET_RESOURCE+'>/annotations',
        'schema': annotation_schema,
        'resource_methods': ['GET'],
    },
}

# Please note that MONGO_HOST and MONGO_PORT could very well be left
# out as they already default to a bare bones local 'mongod' instance.
MONGO_HOST = 'localhost'
MONGO_PORT = 8000
MONGO_USERNAME = 'admin'
MONGO_PASSWORD = 'admin12345'
MONGO_DBNAME = 'annotation_db'
