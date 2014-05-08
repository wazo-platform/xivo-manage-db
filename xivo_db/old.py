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
from xivo_db import path
from xivo_db.exception import DBError


def check_db():
    subprocess.call([path.XIVO_CHECK_DB_OLD])


def update_db(verbose=False):
    args = [path.XIVO_UPDATE_DB_OLD]
    if verbose:
        args.append('-v')
    if subprocess.call(args):
        raise DBError()


def is_active():
    return os.path.exists(path.AST_LAST) or os.path.exists(path.XIVO_LAST)


def deactivate():
    _force_unlink(path.AST_LAST)
    _force_unlink(path.XIVO_LAST)


def _force_unlink(pathname):
    try:
        os.unlink(pathname)
    except OSError as e:
        if e.errno != errno.ENOENT:
            raise
