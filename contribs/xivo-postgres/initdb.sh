#!/bin/bash
echo "STARTING POSTGRES"
gosu postgres pg_ctl -o "-h 127.0.0.1" start

echo "INIT DB"
xivo-init-db --init

echo "STOPPING POSTGRES"
gosu postgres pg_ctl stop
