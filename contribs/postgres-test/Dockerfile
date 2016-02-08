FROM xivo/postgres
MAINTAINER XiVO Team "dev@avencall.com"
USER root

#Insert data required for running integration tests
COPY contribs/postgres-test/initdb.sql /usr/src/initdb.sql
COPY alembic /usr/share/xivo-manage-db/alembic
COPY contribs/postgres-test/bootstrap-pg.sh /bootstrap-pg.sh

ADD https://github.com/tianon/gosu/releases/download/1.7/gosu-amd64 /usr/local/bin/gosu

RUN \
    mkdir -p /pg-init-db \
    && sed -i 's/#fsync.*/fsync = off/g' $PG_CONF \
    && $PG_CTL -w -o "--config-file=$PG_CONF" start \
    && sudo -u postgres psql asterisk < /usr/src/initdb.sql \
    && xivo-update-db \
    && sudo -u postgres psql asterisk -c "CREATE DATABASE xivotemplate TEMPLATE asterisk;" \
    && $PG_CTL -w -o "--config-file=$PG_CONF" stop \
    && chmod +x /usr/local/bin/gosu

ENTRYPOINT ["/bootstrap-pg.sh"]

CMD ["postgres"]
