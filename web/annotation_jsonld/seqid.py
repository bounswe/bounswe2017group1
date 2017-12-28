#!/usr/bin/env python

"""Sequential ID support with MongoDB."""

__author__ = 'Sampo Pyysalo'
__license__ = 'MIT'

import pymongo

import settings

# Name of DB collection to use for counters
DEFAULT_COLLECTION = 'idcounters'

# Name of the default sequence to take IDs from.
DEFAULT_SEQUENCE = 'annotations'

def next_id(sequence=DEFAULT_SEQUENCE, collection=DEFAULT_COLLECTION):
    """Return next ID from sequence in collection."""
    return next_ids(1, sequence, collection)[0]

def next_ids(n, sequence=DEFAULT_SEQUENCE, collection=DEFAULT_COLLECTION):
    """Return list of n next IDs from sequence in collection."""
    database = default_database()
    collection = database[collection]
    # http://docs.mongodb.org/manual/tutorial/create-an-auto-incrementing-field/
    result = collection.find_and_modify(query={ '_id':  sequence },
                                        update={ '$inc': { 'seq': n } },
                                        upsert=True,
                                        new=True)
    max_seq = result['seq']
    return list(range(max_seq-n+1, max_seq+1))
    
def default_database():
    """Connect, authenticate, and return DB based on global settings."""
    if default_database._cache is None:
        database = get_database()
        authenticate(database)
        default_database._cache = database
    return default_database._cache
default_database._cache = None

def get_client(host=None, port=None):
    """Return MongoClient, defaulting to global settings."""
    if host is None:
        host = settings.MONGO_HOST
    if port is None:
        port = settings.MONGO_PORT
    return pymongo.MongoClient(host, port)

def get_database(client=None, dbname=None):
    """Return database, defaulting to global settings."""
    if client is None:
        client = get_client()
    if dbname is None:
        dbname = settings.MONGO_DBNAME
    return client[dbname]

def authenticate(database, username=None, password=None):
    """Authenticate to use database, defaulting to global settings."""
    if username is None:
        username = settings.MONGO_USERNAME
    if password is None:
        password = settings.MONGO_PASSWORD
    return database.authenticate(username, password)
