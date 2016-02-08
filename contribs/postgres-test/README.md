XiVO Postgres test
==================

xivo/postgres-test is a [Postgres](http://postgresql.org) image with a minimal database already configured.
It is mainly used for running automated tests. Please note that the database is preconfigured as if
the XiVO wizard has already been run, with default values already set.

Prerequisites
=============

 * Docker. Consult their [website](http://docs.docker.com/installation/) for installation instructions

Building the image
==================

This image depends on xivo/postgres. Build this image first from the root directory of xivo-manage-db:

    cd xivo-manage-db
    docker build -t xivo/postgres .

Then you can build postgres-test:

    cd contribs/xivo-postgres
    docker build -t xivo/postgres-test -f contribs/postgres-test/Dockerfile .

Using the image
===============

Initializing the database
-------------------------

If you would like to execute SQL scripts before postgres starts, place them in ```/pg-init-db```. For example:

    docker run -v /path/to/sql/scripts:/pg-init-db xivo/postgres-test

Starting the database
---------------------

Start a new container with the right port opened:

    docker run --name xivo-postgres-test -d -p 5432:5432 xivo/postgres-test

The image also exposes the port ```5432```, so container linking should work.

You can then connect to the container with a postgres client:

    psql -h localhost -p 5432 -U asterisk asterisk #password: proformatique
