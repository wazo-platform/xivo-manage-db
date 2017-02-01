# -*- coding: UTF-8 -*-

# Copyright 2014-2017 The Wazo Authors  (see the AUTHORS file)
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

import argparse
import os
import sys

from xivo_db import alembic
from xivo_db import old
from xivo_db import postgres
from xivo_db.exception import DBError
from wazo_uuid.uuid_ import get_wazo_uuid


def main():
    parsed_args = _parse_args()
    os.environ['XIVO_UUID'] = get_wazo_uuid()

    print 'Updating database...'
    try:
        if old.is_active():
            old.update_db(parsed_args.verbose)
            postgres.merge_db()
            old.deactivate()

        alembic.update_db()
        print 'Updating database done.'
    except DBError:
        sys.exit(1)


def _parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='increase verbosity')
    return parser.parse_args()
