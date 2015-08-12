FROM postgres:9.1
MAINTAINER XiVO Team "dev@avencall.com"

ENV DEBIAN_FRONTEND noninteractive
ENV POSTGRES_USER asterisk
ENV POSTGRES_PASSWORD proformatique
ENV POSTGRES_DB asterisk

COPY contribs/xivo-postgres/initdb.sh /docker-entrypoint-initdb.d/00_initdb.sh

RUN apt-get -qq update && \
    apt-get -qq -y install \
        apt-utils \
        python-pip \
        python-dev \
        libyaml-dev \
        postgresql-client \
        libpq-dev \
        git

COPY . /usr/src/xivo-manage-db
WORKDIR /usr/src/xivo-manage-db
RUN PATH=/usr/local/bin:$PATH \
    pip install -U pip && \
    pip install -r requirements.txt && \
    python setup.py install && \
    mkdir /usr/share/xivo-manage-db/ && \
    mkdir /usr/lib/xivo-manage-db/ && \
    cp -a alembic alembic.ini migration populate /usr/share/xivo-manage-db && \
    ln -s /usr/local/bin/pg-populate-db /usr/lib/xivo-manage-db/pg-populate-db && \
    ln -s /usr/local/bin/xivo-init-db /usr/lib/xivo-manage-db/pg-init-db

WORKDIR /root
