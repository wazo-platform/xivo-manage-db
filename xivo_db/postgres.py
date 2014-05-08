# -*- coding: UTF-8 -*-

# Copyright (C) 2014 Avencall
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

import os
import subprocess
from xivo_db import path
from xivo_db.exception import DBError


def init_db():
    _call_as_postgres(path.PG_INIT_DB)


def drop_db():
    _call_as_postgres(path.PG_DROP_DB)


def merge_db():
    _call_as_postgres(path.PG_MERGE_DB)


def populate_db():
    _call_as_postgres(path.PG_POPULATE_DB)


def _call_as_postgres(pathname):
    args = ['su', '-c', pathname, 'postgres']
    with open(os.devnull) as fobj:
        if subprocess.call(args, stdout=fobj, cwd='/tmp'):
            raise DBError()
