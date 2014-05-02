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

import errno
import os
import subprocess

_CHECK_DB_PATH = '/usr/lib/xivo-manage-db/xivo-check-db-old'
_UPDATE_DB_PATH = '/usr/lib/xivo-manage-db/xivo-update-db-old'
_AST_LAST_PATH = '/var/lib/xivo-manage-db/update-db/asterisk-last'
_XIVO_LAST_PATH = '/var/lib/xivo-manage-db/update-db/xivo-last'


class UpdateFailedException(Exception):
    pass


def check_db():
    subprocess.call([_CHECK_DB_PATH])


def update_db(verbose=False):
    args = [_UPDATE_DB_PATH]
    if verbose:
        args.append('-v')
    if subprocess.call(args):
        raise UpdateFailedException()


def is_active():
    return os.path.exists(_AST_LAST_PATH) or os.path.exists(_XIVO_LAST_PATH)


def deactivate():
    _force_unlink(_AST_LAST_PATH)
    _force_unlink(_XIVO_LAST_PATH)


def _force_unlink(path):
    try:
        os.unlink(path)
    except OSError as e:
        if e.errno != errno.ENOENT:
            raise
