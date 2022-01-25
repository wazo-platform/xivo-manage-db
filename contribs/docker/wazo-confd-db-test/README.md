# wazo-confd-db-test

wazoplatform/wazo-confd-db-test is a [Postgres](http://postgresql.org) image with a minimal database
already configured. It is mainly used for running automated tests. Please note that the database is
preconfigured as if the Wazo wizard has already been run, with default values already set.

## Building the image

This image depends on wazoplatform/wazo-confd-db. Build this image first from the root directory of
xivo-manage-db:

    docker build -t wazoplatform/wazo-confd-db .

Then you can build wazo-confd-db-test:

    docker build -t wazoplatform/wazo-confd-db-test -f contribs/docker/wazo-confd-db-test/Dockerfile .

## Using the image

### Initializing the database

If you would like to execute SQL scripts before postgres starts, place them in ```/pg-init-db```.
For example:

    docker run -v /path/to/sql/scripts:/pg-init-db wazoplatform/wazo-confd-db-test
