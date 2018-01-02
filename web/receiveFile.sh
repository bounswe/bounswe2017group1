#!/bin/bash

HOST=ec2-18-196-2-56.eu-central-1.compute.amazonaws.com
USER=ec2-user
KEYFILE=~/Downloads/cmpe451.pem


scp -i $KEYFILE $USER@$HOST:bounswe2017group1/web/db.sqlite3 db.sqlite3
echo “Database dump successfully downloaded.”