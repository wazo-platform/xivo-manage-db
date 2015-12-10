FROM debian:jessie
MAINTAINER XiVO Team "dev@avencall.com"

# Add dependencies
RUN apt-get -qq update
RUN apt-get -qq -y install \
    git \
    apt-utils \
    python-pip \
    python-dev \
    libyaml-dev \
    postgresql-client \
    libpq-dev


WORKDIR /usr/src
ADD . /usr/src/xivo-manage-db
WORKDIR xivo-manage-db
RUN pip install -r requirements.txt
RUN python setup.py install
RUN mkdir /usr/share/xivo-manage-db
RUN mkdir /usr/lib/xivo-manage-db/
RUN cp -a alembic alembic.ini migration populate /usr/share/xivo-manage-db
RUN ln -s /usr/local/bin/pg-populate-db /usr/lib/xivo-manage-db/pg-populate-db
RUN ln -s /usr/local/bin/xivo-init-db /usr/lib/xivo-manage-db/pg-init-db

RUN adduser --disabled-password --gecos '' postgres

WORKDIR /root

RUN rm -rf /usr/src/*
RUN apt-get clean
