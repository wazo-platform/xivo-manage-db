#!/bin/bash
echo "STARTING POSTGRES"
gosu postgres pg_ctl start

echo "INIT DB"
xivo-init-db --init

echo "STOPPING POSTGRES"
gosu postgres pg_ctl stop
