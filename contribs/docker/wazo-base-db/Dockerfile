FROM debian:buster
LABEL maintainer="Wazo Maintainers <dev@wazo.community>"

ENV DEBIAN_FRONTEND=noninteractive
ENV LC_ALL=C.UTF-8
ENV BUILD_PACKAGES="python3-pip python3-dev libpq-dev alembic python3-alembic python3-psycopg2 python3-sqlalchemy python3-sqlalchemy-utils"
ENV PYTHON_PACKAGES="https://github.com/wazo-platform/xivo-lib-python/archive/master.zip"
ENV PG_PACKAGES="postgresql-11 postgresql-contrib-11 postgresql-client"

#Locales must be configured before installing postgres, otherwise the database encoding defaults to SQL_ASCII
RUN true \
    && apt-get update \
    && apt-get install -y sudo locales \
    && dpkg-reconfigure locales \
    && locale-gen C.UTF-8  \
    && /usr/sbin/update-locale LANG=C.UTF-8 \
    && apt-get -y install $PG_PACKAGES \
    && echo "host all  all    0.0.0.0/0  md5" >> /etc/postgresql/11/main/pg_hba.conf \
    && echo "listen_addresses='*'" >> /etc/postgresql/11/main/postgresql.conf \
    && mkdir -p /run/postgresql/11-main.pg_stat_tmp \
    && chown -R postgres:postgres /run/postgresql \
    && apt-get -y install $BUILD_PACKAGES \
    && pip3 install $PYTHON_PACKAGES \
    && true

COPY ./pg_start ./pg_stop /usr/local/bin/

EXPOSE 5432
CMD ["/usr/lib/postgresql/11/bin/postgres", "-D", "/var/lib/postgresql/11/main", "--config-file=/etc/postgresql/11/main/postgresql.conf"]
