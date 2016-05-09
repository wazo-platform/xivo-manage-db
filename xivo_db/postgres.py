# -*- coding: UTF-8 -*-

# Copyright (C) 2014-2016 Avencall
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

import subprocess
import getpass
import psycopg2
import time
import sys
import os

from pwd import getpwnam

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
def init_db():
    db_name = 'asterisk'
    db_user = 'asterisk'
    db_user_password = 'proformatique'

    for _ in xrange(40):
        try:
            conn = psycopg2.connect('postgresql:///postgres')
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


def drop_db():
    _call_as_postgres(path.PG_DROP_DB)


def merge_db():
    _call_as_postgres(path.PG_MERGE_DB)


def populate_db():
    _call_as_postgres(path.PG_POPULATE_DB)


def _call_as_postgres(pathname):
    user = 'postgres'
    if getpass.getuser() == user:
        args = [pathname]
    else:
        args = ['su', '-c', pathname, user]

    if subprocess.call(args, cwd='/tmp'):
        raise DBError()
