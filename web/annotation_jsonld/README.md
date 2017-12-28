# RESTful Open Annotation store in Eve

RESTful annotation storage using the Open Annotation model and
JSON-LD, implemented in Eve and backed by MongoDB.

This is a pre-alpha, proof-of-concept implementation and should not be
used for anything serious.

For more information, see

* http://www.openannotation.org/
* http://www.w3.org/annotation/
* http://json-ld.org/
* http://en.wikipedia.org/wiki/REST
* http://python-eve.org/
* http://www.mongodb.org/

## Installation

### MongoDB

After initial installation, you can set up the user for the server as
follows:

    $ mongo <DBNAME>
    db.addUser({user: "<NAME>", pwd: "<PASSWORD>", roles: ["readWrite"]})

where `<DBNAME>`, `<NAME>` and `<PASSWORD>` are set up to match your
settings.
