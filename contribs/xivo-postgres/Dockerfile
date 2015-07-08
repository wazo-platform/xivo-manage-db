FROM postgres:9.1
MAINTAINER XiVO Team "dev@avencall.com"

ENV DEBIAN_FRONTEND noninteractive
ENV POSTGRES_USER asterisk
ENV POSTGRES_PASSWORD proformatique
ENV POSTGRES_DB asterisk

RUN apt-get -qq update
RUN apt-get -qq -y install \
    apt-utils \
    python-pip \
    python-dev \
    libyaml-dev \
    postgresql-client \
    libpq-dev \
    git

ADD . /usr/src/xivo-manage-db
WORKDIR /usr/src/xivo-manage-db
RUN pip install -r requirements.txt
RUN python setup.py install

RUN mkdir /usr/share/xivo-manage-db/
RUN mkdir /usr/lib/xivo-manage-db/
RUN cp -a alembic alembic.ini migration populate /usr/share/xivo-manage-db
RUN ln -s /usr/local/bin/pg-populate-db /usr/lib/xivo-manage-db/pg-populate-db
RUN ln -s /usr/local/bin/xivo-init-db /usr/lib/xivo-manage-db/pg-init-db

ADD contribs/xivo-postgres/initdb.sh /docker-entrypoint-initdb.d/00_initdb.sh
WORKDIR /root
