# -*- coding: utf-8 -*-
# Copyright 2014-2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

import re
import collections
import subprocess
from xivo_db import path
from xivo_db.exception import DBError

_AlembicCurrentStatus = collections.namedtuple('_AlembicCurrentStatus', ['revision', 'is_head'])


def check_db():
    print 'Checking database...'
    p = _new_alembic_popen(['current'], stdout=subprocess.PIPE)
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
