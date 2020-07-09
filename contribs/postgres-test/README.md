# Wazo postgres-test

wazopbx/postgres-test is a [Postgres](http://postgresql.org) image with a minimal database already
configured.
It is mainly used for running automated tests. Please note that the database is preconfigured as if
the Wazo wizard has already been run, with default values already set.

## Building the image

This image depends on wazopbx/postgres. Build this image first from the root directory of
xivo-manage-db:

    docker build -t wazopbx/postgres .

Then you can build postgres-test:

    docker build -t wazopbx/postgres-test -f contribs/postgres-test/Dockerfile .

## Using the image

### Initializing the database

If you would like to execute SQL scripts before postgres starts, place them in ```/pg-init-db```.
For example:

    docker run -v /path/to/sql/scripts:/pg-init-db wazopbx/postgres-test
