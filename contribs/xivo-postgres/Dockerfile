FROM xivo/xivo-postgres
MAINTAINER XiVO Team "dev@avencall.com"
USER root

# makes db operations run slightly faster on older hard drives
RUN \
    sed -i 's/#fsync.*/fsync = off/g' $PGCONF 

#Insert data required for running integration tests
COPY ./initdb.sql /usr/src/initdb.sql
RUN \
    sudo -u postgres $PGBIN/pg_ctl -D $PGDATA -o "-c config_file=$PGCONF" start && \
    sudo -u postgres psql asterisk < /usr/src/initdb.sql && \
    sudo -u postgres $PGBIN/pg_ctl -D $PGDATA -o "-c config_file=$PGCONF" stop

USER postgres
