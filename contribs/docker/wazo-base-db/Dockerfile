FROM debian:jessie
MAINTAINER Wazo Maintainers <dev@wazo.community>

ENV DEBIAN_FRONTEND=noninteractive \
    LC_ALL=C.UTF-8 \
    BUILD_PACKAGES="python-pip python3-pip python-dev python3-dev libpq-dev alembic python-alembic python3-alembic python-psycopg2 python3-psycopg2 python-sqlalchemy python3-sqlalchemy" \
    PYTHON_PACKAGES="https://github.com/wazo-pbx/xivo-lib-python/archive/master.zip" \
    PG_PACKAGES="postgresql-9.4 postgresql-contrib-9.4 postgresql-client"

#Locales must be configured before installing postgres, otherwise the database encoding defaults to SQL_ASCII
RUN true \
    && apt-get update \
    && apt-get install -y sudo locales \
    && dpkg-reconfigure locales \
    && locale-gen C.UTF-8  \
    && /usr/sbin/update-locale LANG=C.UTF-8 \
    && apt-get -y install $PG_PACKAGES \
    && echo "host all  all    0.0.0.0/0  md5" >> /etc/postgresql/9.4/main/pg_hba.conf \
    && echo "listen_addresses='*'" >> /etc/postgresql/9.4/main/postgresql.conf \
    && mkdir -p /var/run/postgresql/9.4-main.pg_stat_tmp \
    && chown -R postgres:postgres /var/run/postgresql \
    && apt-get -y install $BUILD_PACKAGES \
    && pip install $PYTHON_PACKAGES \
    && pip3 install $PYTHON_PACKAGES \
    && true

ADD ./bin/pg_start /usr/local/bin/pg_start
ADD ./bin/pg_stop /usr/local/bin/pg_stop

EXPOSE 5432
CMD ["/usr/lib/postgresql/9.4/bin/postgres", "-D", "/var/lib/postgresql/9.4/main", "--config-file=/etc/postgresql/9.4/main/postgresql.conf"]