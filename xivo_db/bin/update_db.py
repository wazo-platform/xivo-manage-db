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

import argparse
import sys
from xivo_db import old
from xivo_db.exception import DBError


def main():
    parsed_args = _parse_args()

    if old.is_active():
        try:
            old.update_db(parsed_args.verbose)
            old.merge_db()
        except DBError:
            sys.exit(1)

        old.deactivate()


def _parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='increase verbosity')
    return parser.parse_args()
