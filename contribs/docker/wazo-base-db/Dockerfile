FROM python:3.7-slim-buster
LABEL maintainer="Wazo Maintainers <dev@wazo.community>"

ENV DEBIAN_FRONTEND=noninteractive
ENV LC_ALL=C.UTF-8
ENV BUILD_PACKAGES="libpq-dev"
ENV PYTHON_PACKAGES="alembic==1.0.0 psycopg2-binary==2.7.7 sqlalchemy==1.2.18 sqlalchemy-utils==0.32.21 https://github.com/wazo-platform/xivo-lib-python/archive/master.zip"
ENV PG_PACKAGES="postgresql-11 postgresql-contrib-11 postgresql-client"

#Locales must be configured before installing postgres, otherwise the database encoding defaults to SQL_ASCII
RUN true \
    && apt-get -q update \
    && apt-get -yq install --no-install-recommends sudo locales \
    && dpkg-reconfigure locales \
    && locale-gen C.UTF-8  \
    && /usr/sbin/update-locale LANG=C.UTF-8 \
    && apt-get -yq install --no-install-recommends $PG_PACKAGES \
    && echo "host all  all    0.0.0.0/0  md5" >> /etc/postgresql/11/main/pg_hba.conf \
    && echo "listen_addresses='*'" >> /etc/postgresql/11/main/postgresql.conf \
    && mkdir -p /run/postgresql/11-main.pg_stat_tmp \
    && chown -R postgres:postgres /run/postgresql \
    && apt-get -yq install --no-install-recommends $BUILD_PACKAGES \
    && pip install $PYTHON_PACKAGES \
    && true

COPY ./pg_start ./pg_stop /usr/local/bin/

EXPOSE 5432
CMD ["/usr/lib/postgresql/11/bin/postgres", "-D", "/var/lib/postgresql/11/main", "--config-file=/etc/postgresql/11/main/postgresql.conf"]
