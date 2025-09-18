FROM python:3.11-slim-bookworm
LABEL maintainer="Wazo Maintainers <dev@wazo.community>"

ENV DEBIAN_FRONTEND=noninteractive
ENV LC_ALL=C.UTF-8
ENV BUILD_PACKAGES="libpq-dev"
ENV PYTHON_PACKAGES="alembic==1.4.3 psycopg2-binary==2.8.6 sqlalchemy==1.3.22 sqlalchemy-utils==0.36.8 https://github.com/wazo-platform/xivo-lib-python/archive/master.zip"
ENV PG_PACKAGES="postgresql-13 postgresql-contrib-13 postgresql-client"

#Locales must be configured before installing postgres, otherwise the database encoding defaults to SQL_ASCII
RUN true \
    && apt-get -q update \
    && apt-get -yq install --no-install-recommends sudo locales \
    && dpkg-reconfigure locales \
    && locale-gen C.UTF-8  \
    && /usr/sbin/update-locale LANG=C.UTF-8 \
    && apt-get -yq install --no-install-recommends $PG_PACKAGES \
    && echo "host all  all    0.0.0.0/0  md5" >> /etc/postgresql/13/main/pg_hba.conf \
    && echo "listen_addresses='*'" >> /etc/postgresql/13/main/postgresql.conf \
    && mkdir -p /run/postgresql/13-main.pg_stat_tmp \
    && chown -R postgres:postgres /run/postgresql \
    && apt-get -yq install --no-install-recommends $BUILD_PACKAGES \
    && pip install $PYTHON_PACKAGES \
    && true

COPY ./pg_start ./pg_stop /usr/local/bin/

EXPOSE 5432
ENTRYPOINT ["/usr/lib/postgresql/13/bin/postgres", "-D", "/var/lib/postgresql/13/main", "--config-file=/etc/postgresql/13/main/postgresql.conf"]
