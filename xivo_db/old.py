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

import subprocess

_CHECK_DB_PATH = '/usr/lib/xivo-manage-db/xivo-check-db-old'
_UPDATE_DB_PATH = '/usr/lib/xivo-manage-db/xivo-update-db-old'


def check_db():
    # TODO return exit code / raise exception on error
    subprocess.call([_CHECK_DB_PATH])


def update_db(verbose=False):
    args = [_UPDATE_DB_PATH]
    if verbose:
        args.append('-v')
    # TODO return exit code / raise exception on error
    subprocess.call(args)
