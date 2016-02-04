FROM xivo/postgres
MAINTAINER XiVO Team "dev@avencall.com"
USER root

#Insert data required for running integration tests
COPY contribs/postgres-test/initdb.sql /usr/src/initdb.sql
COPY alembic /usr/share/xivo-manage-db/alembic
RUN \
    sed -i 's/#fsync.*/fsync = off/g' $PG_CONF \
    && $PG_CTL -o "--config-file=$PG_CONF" start \
    && sudo -u postgres psql asterisk < /usr/src/initdb.sql \
    && xivo-update-db \
    && $PG_CTL -o "--config-file=$PG_CONF" stop

USER postgres
