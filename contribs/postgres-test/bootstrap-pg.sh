#!/bin/bash

PG_CTL="sudo -u postgres /usr/lib/postgresql/9.4/bin/pg_ctl -D /var/lib/postgresql/9.4/main"
PG_CONF="/etc/postgresql/9.4/main/postgresql.conf"
SCRIPTS="/pg-init-db"

if [ "$1" != "postgres" ]; then
    exec "$@"
fi

if [ "$(ls -A $SCRIPTS)" ]; then
    $PG_CTL -w -o "--config-file=$PG_CONF -c listen_addresses=''" start
    for filepath in $SCRIPTS/*
    do
        sudo -u postgres psql asterisk < "$filepath"
    done
    $PG_CTL -w -o "--config-file=$PG_CONF" stop
fi

gosu postgres \
    /usr/lib/postgresql/9.4/bin/postgres \
    -D /var/lib/postgresql/9.4/main \
    --config-file=/etc/postgresql/9.4/main/postgresql.conf
