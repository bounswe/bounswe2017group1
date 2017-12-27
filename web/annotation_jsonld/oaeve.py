#!/usr/bin/env python

"""Open Annotation JSON-LD support functions for Eve."""

__author__ = 'Sampo Pyysalo'
__license__ = 'MIT'

import json
import urlparse
import hashlib
import re

import flask
import mimeparse

import oajson
import seqid

from settings import TARGET_RESOURCE

# whether to expand @id values to absolute URLs
ABSOLUTE_ID_URLS = True

# mapping from Eve JSON keys to JSON-LD ones
jsonld_key_rewrites = [
    ('_id', '@id'),
]

eve_to_jsonld_key_map = dict(jsonld_key_rewrites)
jsonld_to_eve_key_map = dict([(b,a) for a,b in jsonld_key_rewrites])

def dump_json(document, prettyprint=True):
    if not prettyprint:
        return json.dumps(document)
    else:
        return json.dumps(document, indent=2, sort_keys=True,
                          separators=(',', ': '))+'\n'

def setup_callbacks(app):
    # annotations
    app.on_pre_POST_annotations += convert_incoming_jsonld
    app.on_pre_PUT_annotations += convert_incoming_jsonld
    app.on_post_GET_annotations += convert_outgoing_jsonld
    app.on_post_PUT_annotations += convert_outgoing_jsonld
    app.on_post_POST_annotations += convert_outgoing_jsonld
    # annotations by document (separate Eve endpoint)
    app.on_post_GET_annbydoc += convert_outgoing_jsonld
    app.on_post_GET_annbydoc += rewrite_annbydoc_ids
    # documents
    app.on_post_GET_documents += rewrite_outgoing_document
    # TODO: this doesn't seem to be firing, preventing the use of ETag
    # in HEAD response to avoid roundtrips.
    app.on_post_HEAD_documents += rewrite_outgoing_document

def eve_to_jsonld(document):
    document = oajson.remap_keys(document, eve_to_jsonld_key_map)
    if ABSOLUTE_ID_URLS:
        ids_to_absolute_urls(document)
    oajson.add_context(document)
    oajson.add_types(document)
    remove_meta(document)
    remove_status(document)
    remove_target_resources(document)
    rewrite_links(document)
    return document

def eve_from_jsonld(document):
    document = oajson.remap_keys(document, jsonld_to_eve_key_map)
    # TODO: invert ids_to_absolute_urls() here
    oajson.normalize(document)
    oajson.remove_context(document)
    oajson.remove_types(document)
    add_target_resources(document)
    return document

def add_target_resources(document):
    """Add fragmentless target URL values to make search easier."""
    if oajson.is_collection(document):
        for item in document.get(oajson.ITEMS, []):
            add_target_resources(item)
    else:
        target = document.get('target')
        if target is None:
            return
        assert TARGET_RESOURCE not in document
        # TODO: support multiple and structured targets
        if not isinstance(target, basestring):
            raise NotImplementedError('multiple/structured targets')
        document[TARGET_RESOURCE] = urlparse.urldefrag(target)[0]

def remove_target_resources(document):
    """Remove fragmentless target URL values added to make search easier."""
    if oajson.is_collection(document):
        for item in document.get(oajson.ITEMS, []):
            remove_target_resources(item)
    else:
        try:
            del document[TARGET_RESOURCE]
        except KeyError:
            pass

def is_jsonld_response(response):
    """Return True if the given Response object should be treated as
    JSON-LD, False otherwise."""
    # TODO: reconsider "application/json" here
    return response.mimetype in ['application/json', 'application/ld+json']

def convert_outgoing_jsonld(request, payload):
    """Event hook to run after executing a GET method.

    Converts Eve payloads that should be interpreted as JSON-LD into
    the Open Annotation JSON-LD representation.
    """
    if not is_jsonld_response(payload):
        return
    doc = json.loads(payload.get_data())
    jsonld_doc = eve_to_jsonld(doc)
    payload.set_data(dump_json(jsonld_doc))

def _collection_ids_to_absolute_urls(document):
    """Rewrite @id values from relative to absolute URL form for collection."""
    base = flask.request.base_url
    # Eve responds to both "collection" and "collection/" variants
    # of the same endpoint, but the join only works for the latter.
    # We have to make sure the separator is present in the base.
    if base and base[-1] != '/':
        base = base + '/'
    for item in document.get(oajson.ITEMS, []):
        _item_ids_to_absolute_urls(item)

def _item_ids_to_absolute_urls(document, base=None):
    """Rewrite @id values from relative to absolute URL form for item."""
    if base is None:
        base = flask.request.base_url
    try:
        id_ = document['@id']
        document['@id'] = urlparse.urljoin(base, id_)
    except KeyError, e:
        print 'Warning: no @id: %s' % str(document)

def ids_to_absolute_urls(document):
    """Rewrite @id value from relative to absolute URL form."""
    if oajson.is_collection(document):
        return _collection_ids_to_absolute_urls(document)
    else:
        return _item_ids_to_absolute_urls(document)

def remove_meta(document):
    """Remove Eve pagination meta-information ("_meta") if present."""
    try:
        del document['_meta']
    except KeyError:
        pass

def remove_status(document):
    """Remove Eve status information ("_status") if present."""
    try:
        del document['_status']
    except KeyError:
        pass

def _rewrite_collection_links(document):
    """Rewrite Eve HATEOAS-style "_links" to JSON-LD for a collection.

    Also rewrites links for items in the collection."""
    links = document.get('_links')
    assert links is not None, 'internal error'

    # Eve generates RFC 5988 link relations ("next", "prev", etc.)
    # for collections when appropriate. Move these to the collection
    # level.
    for key in ['start', 'last', 'next', 'prev', 'previous']:
        if key not in links:
            pass
        elif 'href' not in links[key]:
            print 'Warning: no href in Eve _links[%s]' % key
        else:
            assert key not in document, \
                'Error: redundant %s links: %s' % (key, str(document))
            # fill in relative links (e.g. "people?page=2")
            url = links[key]['href']
            url = urlparse.urljoin(flask.request.url_root, url)
            # TODO: don't assume the RESTful OA keys match Eve ones. In
            # particular, consider normalizing 'prev' vs. 'previous'.
            document[key] = url

    # Others assumed to be redundant with JSON-LD information and safe
    # to delete.
    del document['_links']

    # Process _links in collection items. (At the moment, just
    # delete them.)
    for item in document.get(oajson.ITEMS, []):
        try:
            del item['_links']
        except KeyError:
            pass

    return document

def _rewrite_item_links(document):
    """Rewrite Eve HATEOAS-style "_links" to JSON-LD for non-collection."""
    links = document.get('_links')
    assert links is not None, 'internal error'

    # Eve is expected to provide "collection" as a refererence back to
    # the collection of which the item is a member. We'll move this to
    # the item level with the collection link relation (RFC 6573)
    if 'collection' not in links or 'href' not in links['collection']:
        print 'Warning: no collection in Eve _links.' # TODO use logging
    else:
        assert oajson.COLLECTION_KEY not in document, \
            'Error: redundant collection links: %s' % str(document)
        document[oajson.COLLECTION_KEY] = links['collection']['href']

    # Eve also generates a "self" links, which is redundant with
    # JSON-LD "@id", and "parent", which is not defined in the RESTful
    # OA spec. These can simply be removed.
    del document['_links']
    return document

def rewrite_links(document):
    """Rewrite Eve HATEOAS-style "_links" to JSON-LD."""
    # HATEOAS is expected but not required, so _links may be absent.
    if not '_links' in document:
        print "Warning: no _links in Eve document." # TODO use logging
        return document
    if oajson.is_collection(document):
        return _rewrite_collection_links(document)
    else:
        return _rewrite_item_links(document)

def is_jsonld_request(request):
    """Return True if the given Request object should be treated as
    JSON-LD, False otherwise."""
    content_type = request.headers['Content-Type'].split(';')[0]
    # TODO: reconsider "application/json" here
    return content_type in ['application/json', 'application/ld+json']

def rewrite_content_type(request):
    """Rewrite JSON-LD content type to assure compatibility with Eve.""" 
    if request.headers['Content-Type'].split(';')[0] != 'application/ld+json':
        return # OK
    # Eve doesn't currently support application/ld+json, so we'll
    # pretend it's just json by changing the content-type header.
    # werkzeug EnvironHeaders objects are immutable and disallow
    # copy(), so hack around that. (This is probably a bad idea.)
    headers = { key: value for key, value in request.headers }
    parts = headers['Content-Type'].split(';')
    if parts[0] == 'application/ld+json':
        parts[0] = 'application/json'
    headers['Content-Type'] = ';'.join(parts)
    request.headers = headers

def _is_create_annotation_request(document, request):
    # TODO: better logic for deciding if a document is an annotation.
    return (request.method == 'POST' and
            (request.url.endswith('/annotations') or
             request.url.endswith('/annotations/')))

def add_new_annotation_id(document, request):
    """Add IDs for annotation documents when necessary."""
    if _is_create_annotation_request(document, request):
        # Creating new annotation; fill ID if one is not provided.
        if '_id' not in document:
            document['_id'] = str(seqid.next_id())
    return document

def convert_incoming_jsonld(request, lookup=None):
    # force=True because older versions of flask don't recognize the
    # content type application/ld+json as JSON.
    doc = request.get_json(force=True)
    assert doc is not None, 'get_json() failed for %s' % request.mimetype
    # NOTE: it's important that the following are in-place
    # modifications of the JSON dict, as assigning to request.data
    # doesn't alter the JSON (it's cached) and there is no set_json().
    doc = eve_from_jsonld(doc)
    # If the request is a post and no ID is provided, make one
    doc = add_new_annotation_id(doc, request)
    # Also, we'll need to avoid application/ld+json.
    rewrite_content_type(request)

def accepts_mimetype(request, mimetype):
    """Return True if requests accepts mimetype, False otherwise."""
    accepted = request.headers.get('Accept')
    return mimeparse.best_match([mimetype], accepted) == mimetype

def is_document_collection_request(request):
    parsed = urlparse.urlparse(request.url)
    return parsed.path in ('/documents', '/documents/')

def text_etag(text):
    return hashlib.sha1(text.encode('utf-8')).hexdigest()

def rewrite_outgoing_document_collection(request, payload):
    collection = json.loads(payload.get_data())
    for document in collection.get(oajson.ITEMS, []):
        # Only include the bare minimum in collection-level requests
        id_, modified = document['name'], document['serializedAt']
        document.clear()
        document['@id'], document['serializedAt'] = id_, modified
    collection = eve_to_jsonld(collection)
    payload.set_data(dump_json(collection))

def rewrite_outgoing_document(request, payload):
    if not is_jsonld_response(payload):
        pass # Can only rewrite JSON
    elif is_document_collection_request(request):
        rewrite_outgoing_document_collection(request, payload)
    elif not accepts_mimetype(request, 'text/plain'):
        pass # Just return whatever is prepared
    else:
        # Return the text of the document as text/plain
        doc = json.loads(payload.get_data())
        try:
            text = doc['text']
        except KeyError, e:
            text = 'Error: failed to load text: %s' % dump_json(doc)
        payload.set_data(text)
        payload.headers['Content-Type'] = 'text/plain; charset=utf-8'
        payload.headers['ETag'] = text_etag(text)

def _rewrite_annbydoc_collection_ids(collection):
    for item in collection.get(oajson.ITEMS, []):
        _rewrite_annbydoc_item_id(item)

def _rewrite_annbydoc_item_id(document):
    id_ = document['@id']
    parts = urlparse.urlparse(id_)
    m = re.match(r'^.*(/annotations/[^\/]+)$', parts.path)
    if not m:
        # TODO
        print 'failed to rewrite ann-by-doc id %s' % id_
        return
    new_path = m.group(1)
    rewritten = urlparse.urlunparse((parts.scheme, parts.netloc, new_path,
                                     parts.params, parts.query, parts.fragment))
    document['@id'] = rewritten

def rewrite_annbydoc_ids(request, payload):
    """Event hook to run after GET on annotations-by-document endpoint.

    Removes extra "/documents/.../" from @id values. For example, an
    @id of "http://ex.org/documents/1.txt/annotations/1" would be
    rewritten as "http://ex.org/annotations/1".
    """
    if not is_jsonld_response(payload):
        return
    doc = json.loads(payload.get_data())
    if oajson.is_collection(doc):
        _rewrite_annbydoc_collection_ids(doc)
    else:
        _rewrite_annbydoc_item_id(doc)
    payload.set_data(dump_json(doc))
