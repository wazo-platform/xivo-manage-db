# Copyright 2014-2025 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import annotations

import os
import sys

from wazo_uuid.uuid_ import get_wazo_uuid

from xivo_db import alembic
from xivo_db.exception import DBError


def main() -> None:
    os.environ['XIVO_UUID'] = get_wazo_uuid()

    print('Updating database...')
    try:
        alembic.update_db()
        print('Updating database done.')
    except DBError:
        sys.exit(1)
