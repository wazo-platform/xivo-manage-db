xivo-postgres Docker image
==========================

xivo-postgres is a [Postgres](http://postgresql.org) image with a minimal database already configured for usage on a
XiVO server. Ideal for running automated tests. Please note that the database is in the same state as a freshly
installed server, meaning that there is ***no data from the installation wizard***.

Prerequisites
=============

 * Docker. Consult their [website](http://docs.docker.com/installation/) for installation instructions

Building the image
==================

Build the docker image from the root of xivo-manage-db:

    cd xivo-manage-db
    docker build -t xivo/xivo-postgres -f contribs/xivo-postgres/Dockerfile .

Using the image
===============

Start a new container with the right port opened:

    docker run --name xivo-postgres -d -p 5432:5432 xivo/xivo-postgres

The image also exposes the port ```5432```, so container linking should work.

You can then connect to the container with a postgres client:

    psql -h localhost -p 5432 -U asterisk asterisk #password: proformatique

Extending the image
===================

If you would like to do additional setup in a derived image, you can use the same entrypoint mecanism
as used in the base [postgres image](https://registry.hub.docker.com/_/postgres/) by placing
a ```*.sh``` script in ```/docker-entrypoint-initdb.d```.

For example, if you would like to create a web access account on initialization, you could write a script that executes
a SQL query in postgres single-user mode:

    gosu postgres postgres --single asterisk <<EOF
    INSERT INTO "accesswebservice" (name, login, passwd, description) VALUES ('webservice', 'username', 'password', '')
    EOF
