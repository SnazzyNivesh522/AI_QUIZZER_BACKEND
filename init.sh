#!/bin/bash
service mysql start
sleep 10
mysql -u root -e "source ../db/schema.sql"
mysql -u root -e "SHOW DATABASES;"
exec "$@"

