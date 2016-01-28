FROM debian:jessie
MAINTAINER XiVO Team "dev@avencall.com"

ENV DEBIAN_FRONTEND noninteractive
ENV PGDATA /var/lib/postgresql/9.4/main
ENV PGCONF /etc/postgresql/9.4/main/postgresql.conf
ENV PGBIN /usr/lib/postgresql/9.4/bin

RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get install -y \
        locales \
        python-pip \
        python-dev \
        libyaml-dev \
        git \
        sudo


#Locales must be configured before installing postgres, otherwise the database encoding defaults to SQL_ASCII
RUN \
    dpkg-reconfigure locales && \
    locale-gen C.UTF-8 && \
    /usr/sbin/update-locale LANG=C.UTF-8
ENV LC_ALL C.UTF-8

RUN \
    apt-get -y install \
        postgresql-9.4 \
        postgresql-contrib-9.4 \
        postgresql-client \
        libpq-dev

#Prepare dependencies for initializing database
COPY . /usr/src/xivo-manage-db
COPY ./contribs/xivo-postgres/initdb.sql /usr/src/initdb/initdb.sql
WORKDIR /usr/src/xivo-manage-db
RUN \
    pip install -r requirements.txt && \
    python setup.py install && \
    mkdir /usr/share/xivo-manage-db/ && \
    mkdir /usr/lib/xivo-manage-db/ && \
    cp -a alembic alembic.ini migration populate /usr/share/xivo-manage-db && \
    ln -s /usr/local/bin/pg-populate-db /usr/lib/xivo-manage-db/pg-populate-db && \
    ln -s /usr/local/bin/xivo-init-db /usr/lib/xivo-manage-db/pg-init-db && \
    echo "host all  all    0.0.0.0/0  md5" >> /etc/postgresql/9.4/main/pg_hba.conf && \
    echo "listen_addresses='*'" >> $PGCONF && \
    sed -i 's/#fsync.*/fsync = off/g' $PGCONF && \
    mkdir -p /var/run/postgresql/9.4-main.pg_stat_tmp && \
    chown -R postgres:postgres /var/run/postgresql

#Initialize database and insert initial data
RUN \
    sudo -u postgres $PGBIN/pg_ctl -D $PGDATA -o "-c config_file=$PGCONF" start && \
    sudo -u postgres pg-init-db && \
    xivo-init-db --init && \
    sudo -u postgres psql asterisk < /usr/src/initdb/initdb.sql && \
    sudo -u postgres $PGBIN/pg_ctl -D $PGDATA -o "-c config_file=$PGCONF" stop

EXPOSE 5432
USER postgres
CMD $PGBIN/postgres -D $PGDATA --config-file=$PGCONF
