# -*- coding: utf-8 -*-
# Copyright 2014-2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

import os
import sys

from xivo_db import alembic
from xivo_db.exception import DBError
from wazo_uuid.uuid_ import get_wazo_uuid


def main():
    os.environ['XIVO_UUID'] = get_wazo_uuid()

    print 'Updating database...'
    try:
        alembic.update_db()
        print 'Updating database done.'
    except DBError:
        sys.exit(1)
