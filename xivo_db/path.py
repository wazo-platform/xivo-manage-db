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

import os.path

USR_LIB = '/usr/lib/xivo-manage-db'
VAR_LIB = '/var/lib/xivo-manage-db'
USR_SHARE = '/usr/share/xivo-manage-db'

AST_LAST = os.path.join(VAR_LIB, 'update-db', 'asterisk-last')
XIVO_LAST = os.path.join(VAR_LIB, 'update-db', 'xivo-last')

PG_DROP_DB = os.path.join(USR_LIB, 'pg-drop-db')
PG_INIT_DB = os.path.join(USR_LIB, 'pg-init-db')
PG_MERGE_DB = os.path.join(USR_LIB, 'pg-drop-db')
PG_POPULATE_DB = os.path.join(USR_LIB, 'pg-populate-db')

XIVO_CHECK_DB_OLD = os.path.join(USR_LIB, 'xivo-check-db-old')
XIVO_UPDATE_DB_OLD = os.path.join(USR_LIB, 'xivo-update-db-old')
