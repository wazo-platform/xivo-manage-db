# -*- coding: utf-8 -*-
# Copyright 2014-2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

import time
import sys
import os

from pwd import getpwnam

import subprocess
import getpass
import psycopg2

from wazo_uuid.uuid_ import get_wazo_uuid
from xivo import db_helper
from xivo_db import path
from xivo_db.exception import DBError


def run_as(user_name):
    def wrapper(f):
        def decorator(*args, **kwargs):
            starting_uid = os.geteuid()
            user = getpwnam(user_name)
            os.seteuid(user.pw_uid)
            res = f(*args, **kwargs)
            os.seteuid(starting_uid)
            return res
        return decorator
    return wrapper


@run_as('postgres')
def init_db(db_name, db_user, db_user_password, pg_db_uri):
    for _ in xrange(40):
        try:
            conn = psycopg2.connect(pg_db_uri)
            break
        except psycopg2.OperationalError:
            time.sleep(0.25)
    else:
        print >> sys.stderr, 'Failed to connect to postgres'

    conn.autocommit = True
    with conn:
        with conn.cursor() as cursor:
            if not db_helper.db_user_exists(cursor, db_user):
                db_helper.create_db_user(cursor, db_user, db_user_password)
            if not db_helper.db_exists(cursor, db_name):
                db_helper.create_db(cursor, db_name, db_user)


@run_as('postgres')
def enable_extension(extension, app_db_uri):
    with psycopg2.connect(app_db_uri) as conn:
        with conn.cursor() as cursor:
            cursor.execute('CREATE EXTENSION IF NOT EXISTS "{}"'.format(extension))


def drop_db(pg_db_uri, app_db_name):
    _call_as_postgres(path.PG_DROP_DB.format(pg_db_uri=pg_db_uri, app_db_name=app_db_name))


def populate_db(app_db_uri):
    _call_as_postgres(path.PG_POPULATE_DB.format(wazo_uuid=get_wazo_uuid(), app_db_uri=app_db_uri))


def _call_as_postgres(pathname):
    user = 'postgres'
    if getpass.getuser() == user:
        args = [pathname]
    else:
        args = ['su', '-c', pathname, user]

    if subprocess.call(args, cwd='/tmp'):
        raise DBError()
