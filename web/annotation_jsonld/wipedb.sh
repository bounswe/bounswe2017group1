#!/bin/bash

echo 'db.annotations.remove({})' | mongo -u user -p user test
echo 'db.documents.remove({})' | mongo -u user -p user test
echo 'db.idcounters.remove({})' | mongo -u user -p user test
