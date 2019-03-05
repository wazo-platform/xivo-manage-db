FROM wazopbx/wazo-base-db
MAINTAINER Wazo Maintainers <dev@wazo.community>

ADD . /usr/src/xivo-manage-db
WORKDIR /usr/src/xivo-manage-db

RUN true \
    && apt-get update \
    && apt-get install -yq python3-yaml git \
    && pip3 install -r requirements.txt \
    && python3 setup.py install \
    && xivo-configure-uuid \
    && mkdir /usr/share/xivo-manage-db /usr/lib/xivo-manage-db \
    && cp -a alembic alembic.ini populate /usr/share/xivo-manage-db \
    && ln -s /usr/local/bin/pg-populate-db /usr/lib/xivo-manage-db/pg-populate-db \
    && pg_start \
    && xivo-init-db --init \
    && pg_stop \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /usr/src/xivo-manage-db /var/lib/apt/lists/*
USER postgres
