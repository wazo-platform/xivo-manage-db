FROM wazopbx/postgres
MAINTAINER Wazo Maintainers <dev@wazo.community>
USER root
ENV PG_CONF="/etc/postgresql/9.6/main/postgresql.conf"

#Insert data required for running integration tests
COPY contribs/postgres-test/initdb.sql /usr/src/initdb.sql
COPY alembic /usr/share/xivo-manage-db/alembic
COPY contribs/postgres-test/bootstrap-pg.sh /bootstrap-pg.sh

ADD https://github.com/tianon/gosu/releases/download/1.7/gosu-amd64 /usr/local/bin/gosu

RUN \
    mkdir -p /pg-init-db \
    && sed -i 's/#fsync.*/fsync = off/g' $PG_CONF \
    && pg_start \
    && sudo -u postgres psql asterisk < /usr/src/initdb.sql \
    && cd /usr/share/xivo-manage-db \
    && alembic -c alembic.ini branches \
    && alembic -c alembic.ini show head \
    && xivo-update-db \
    && alembic -c alembic.ini branches \
    && alembic -c alembic.ini show head \
    && sudo -u postgres psql asterisk -c "CREATE DATABASE xivotemplate TEMPLATE asterisk;" \
    && pg_stop \
    && chmod +x /usr/local/bin/gosu

ENTRYPOINT ["/bootstrap-pg.sh"]
