#!/bin/bash

HOST=ec2-18-196-2-56.eu-central-1.compute.amazonaws.com
USER=ec2-user
KEYFILE=~/Downloads/cmpe451.pem

echo “Sending backup file...”
scp -i $KEYFILE $1 $USER@$HOST:db.sqlite3