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

import re
import collections
import subprocess
from xivo_db import path
from xivo_db.exception import DBError

_AlembicCurrentStatus = collections.namedtuple('_AlembicCurrentStatus', ['revision', 'is_head'])


def check_db():
    print 'Checking database...'
    p = _new_alembic_popen(['current', '--head-only'], stdout=subprocess.PIPE)
    output = p.communicate()[0]
    if p.returncode:
        raise Exception('alembic command returned %s' % p.returncode)

    status = _parse_alembic_current_output(output)
    if status.is_head:
        status_msg = 'OK'
    else:
        status_msg = 'NOK (current revision is %s)' % status.revision
    print '\t%s' % status_msg


def _parse_alembic_current_output(output):
    mobj = re.match(r'^(\w+)( \(head\))?$', output)
    if not mobj:
        raise Exception('not a valid alembic current output: %r' % output)

    return _AlembicCurrentStatus(mobj.group(1), True if mobj.group(2) else False)


def update_db():
    if _new_alembic_popen(['upgrade', 'head']).wait():
        raise DBError()


def stamp_head():
    if _new_alembic_popen(['stamp', 'head']).wait():
        raise DBError()


def _new_alembic_popen(args, **kwargs):
    args = ['alembic'] + args
    return subprocess.Popen(args, cwd=path.USR_SHARE, **kwargs)
