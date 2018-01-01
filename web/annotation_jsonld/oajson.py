#!/usr/bin/env python

"""Open Annotation JSON-LD support functions."""

__author__ = 'Sampo Pyysalo'
__license__ = 'MIT'

from settings import LD_CONTEXT, LD_ITEMTYPE, LD_COLLTYPE, ITEMS

CONTEXT_KEY = '@context'
TYPE_KEY = '@type'

# RFC 6573 link relations. Must be defined in @context to expand to
# "http://www.iana.org/assignments/link-relations/#<RELATION>".
ITEM_KEY = 'item'
COLLECTION_KEY = 'collection'

# backward compatibility (Open Annotation -> Web Annotation @context)
# and variant forms
compatibility_rewrites = [
    ('hasTarget', 'target'),
    ('hasBody', 'body'),
    ('oa:hasTarget', 'target'),
    ('oa:hasBody', 'body'),
]

oa_wa_compatibility_map = dict(compatibility_rewrites)

def normalize(document):
    """Normalize Open Annotation JSON-LD document to the compacted
    form with respect to the preferred @context."""
    # Note: this remapping is a weak approximation for what we should
    # really be doing, namely first expand everything wrt. the
    # @context specified by the caller, and then compact wrt. the
    # preferred @context. TODO: Implement the real thing.
    remap_keys(document, oa_wa_compatibility_map)

def add_context(document, context=LD_CONTEXT):
    """Add JSON-LD @context to given document."""

    if CONTEXT_KEY not in document:
        document[CONTEXT_KEY] = context

def remove_context(document, context=LD_CONTEXT):
    """Remove given JSON-LD context from document."""

    if CONTEXT_KEY in document and document[CONTEXT_KEY] == context:
        del document[CONTEXT_KEY]

def is_collection(document):
    # TODO: more reliable definition of what is a collection
    return isinstance(document, dict) and isinstance(document.get(ITEMS), list)

def add_types(document, itemtype=LD_ITEMTYPE, colltype=LD_COLLTYPE):
    """Add JSON-LD @types to given document."""
    # TODO: recurse
    if is_collection(document):
        type_ = colltype
    else:
        type_ = itemtype
    if TYPE_KEY not in document:
        document[TYPE_KEY] = type_

def remove_types(document, itemtype=LD_ITEMTYPE, colltype=LD_COLLTYPE):
    """Remove given JSON-LD @types from given document."""
    # TODO: recurse
    if is_collection(document):
        type_ = colltype
    else:
        type_ = itemtype
    if TYPE_KEY in document and document[TYPE_KEY] == type_:
        del document[TYPE_KEY]

def _is_atomic(value):
    """Return True if value is of a JSON atomic type, False otherwise."""
    return (value is None or
            isinstance(value, bool),
            isinstance(value, int) or
            isinstance(value, float) or
            isinstance(value, str))

def remap_keys(value, key_map, inplace=True):
    """Remap keys in given JSON value.

    >>> remap_keys({'foo': 1}, {'foo': 'bar'})
    {'bar': 1}

    >>> remap_keys(1, {1: 2})
    1
    """
    if isinstance(value, dict):
        return remap_document_keys(value, key_map, inplace)
    elif isinstance(value, list):
        return [remap_keys(i, key_map, inplace) for i in value]
    else:
        # no-op: atomic value
        assert _is_atomic(value)
    return value

def remap_document_keys(document, key_map, inplace=True):
    """Remap keys in given JSON document.

    >>> remap_keys({'foo': 1}, {'foo': 'bar'})
    {'bar': 1}
    """
    assert isinstance(document, dict)
    if inplace:
        # modify given document
        for key in document.keys():
            new_key = key_map.get(key, key)
            value = remap_keys(document[key], key_map, inplace)
            del document[key]
            assert new_key not in document, 'conflict remapping keys'
            document[new_key] = value
        return document
    else:
        # leave document untouched, create new one
        new_document = {}
        for key in document:
            new_key = key_map.get(key, key)
            assert new_key not in new_document, 'conflict remapping keys'
            new_document[new_key] = remap_keys(document[key], key_map)
        return new_document

if __name__ == "__main__":
    import doctest
    doctest.testmod()
