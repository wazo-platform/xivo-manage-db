FROM debian:jessie
MAINTAINER XiVO Team "dev@avencall.com"

ENV DEBIAN_FRONTEND=noninteractive \
    LC_ALL=C.UTF-8 \
    BUILD_PACKAGES="python-pip python-dev libyaml-dev git libpq-dev" \
    PG_PACKAGES="postgresql-9.4 postgresql-contrib-9.4 postgresql-client" \
    PG_CTL="sudo -u postgres /usr/lib/postgresql/9.4/bin/pg_ctl -D /var/lib/postgresql/9.4/main" \
    PG_CONF="/etc/postgresql/9.4/main/postgresql.conf"

#Locales must be configured before installing postgres, otherwise the database encoding defaults to SQL_ASCII
RUN apt-get update \
    && apt-get install -y \
        sudo \
        locales \
    && dpkg-reconfigure locales \
    && locale-gen C.UTF-8  \
    && /usr/sbin/update-locale LANG=C.UTF-8


COPY . /usr/src/xivo-manage-db
WORKDIR /usr/src/xivo-manage-db

#Regrouping all commands into a single one avoids creating extra layers and reduces image size
RUN \
    apt-get -y install $BUILD_PACKAGES $PG_PACKAGES \
    && echo "host all  all    0.0.0.0/0  md5" >> /etc/postgresql/9.4/main/pg_hba.conf \
    && echo "listen_addresses='*'" >> /etc/postgresql/9.4/main/postgresql.conf \
    && mkdir -p /var/run/postgresql/9.4-main.pg_stat_tmp \
    && chown -R postgres:postgres /var/run/postgresql \
    && pip install -r requirements.txt \
    && python setup.py install \
    && mkdir /usr/share/xivo-manage-db /usr/lib/xivo-manage-db \
    && cp -a alembic alembic.ini migration populate /usr/share/xivo-manage-db \
    && ln -s /usr/local/bin/pg-populate-db /usr/lib/xivo-manage-db/pg-populate-db \
    && ln -s /usr/local/bin/xivo-init-db /usr/lib/xivo-manage-db/pg-init-db \
    && $PG_CTL -o "--config-file=$PG_CONF" start \
    && while [ "$($PG_CTL status)" = "pg_ctl: no server running" ]; do sleep 1; done \
    && sudo -u postgres pg-init-db \
    && xivo-init-db --init \
    && $PG_CTL -o "--config-file=$PG_CONF" stop \
    && apt-get remove --purge -y $BUILD_PACKAGES \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /usr/src/xivo-manage-db /var/lib/apt/lists/*


EXPOSE 5432
USER postgres
CMD ["/usr/lib/postgresql/9.4/bin/postgres", "-D", "/var/lib/postgresql/9.4/main", "--config-file=/etc/postgresql/9.4/main/postgresql.conf"]
