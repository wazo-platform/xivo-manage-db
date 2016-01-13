FROM debian:jessie
MAINTAINER XiVO Team "dev@avencall.com"

# Add dependencies
RUN apt-get -qq update
RUN apt-get update -qq && apt-get install -y locales -qq && locale-gen en_US.UTF-8 en_us && dpkg-reconfigure locales && dpkg-reconfigure locales && locale-gen C.UTF-8 && /usr/sbin/update-locale LANG=C.UTF-8
ENV LANG C.UTF-8
ENV LANGUAGE C.UTF-8
ENV LC_ALL C.UTF-8
RUN apt-get -qq -y install \
    git \
    apt-utils \
    python-pip \
    python-dev \
    libyaml-dev \
    postgresql-client \
    postgresql \
    postgresql-contrib \
    postgresql-plpython \
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
RUN echo "host all  all    0.0.0.0/0  md5" >> /etc/postgresql/9.4/main/pg_hba.conf
RUN echo "listen_addresses='*'" >> /etc/postgresql/9.4/main/postgresql.conf
EXPOSE 5432
USER postgres
RUN /etc/init.d/postgresql start && pg-init-db && xivo-init-db --init && /etc/init.d/postgresql stop
CMD ["/usr/lib/postgresql/9.4/bin/postgres", "-D", "/var/lib/postgresql/9.4/main", "-c", "config_file=/etc/postgresql/9.4/main/postgresql.conf"]
