FROM wazopbx/wazo-base-db
LABEL maintainer="Wazo Maintainers <dev@wazo.community>"

ADD . /usr/src/xivo-manage-db
WORKDIR /usr/src/xivo-manage-db

RUN true \
    && apt-get -q update \
    && apt-get -yq install python3-yaml \
    && pip3 install -r requirements.txt \
    && python3 setup.py install \
    && xivo-configure-uuid \
    && mkdir /usr/share/xivo-manage-db /usr/lib/xivo-manage-db \
    && cp -a alembic alembic.ini populate /usr/share/xivo-manage-db \
    && ln -s /usr/local/bin/pg-populate-db /usr/lib/xivo-manage-db/pg-populate-db \
    && pg_start \
    && alembic -c alembic.ini branches \
    && alembic -c alembic.ini show head \
    && xivo-init-db --init \
    && alembic -c alembic.ini branches \
    && alembic -c alembic.ini show head \
    && pg_stop \
    && apt-get -y autoremove \
    && apt-get clean \
    && rm -rf /usr/src/xivo-manage-db /var/lib/apt/lists/*
USER postgres
