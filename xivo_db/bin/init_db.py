# -*- coding: UTF-8 -*-
#
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
import logging

from sqlalchemy.schema import MetaData

from xivo_dao import alchemy # imports all the sqlalchemy model
from xivo_dao.helpers import db_manager
from xivo_dao.helpers.db_manager import Base
from xivo_db import alembic
from xivo_db import postgres

logger = logging.getLogger(__name__)


def expensive_setup():
    logger.info('Connecting to database...')
    session = db_manager.DaoSession()
    engine = session.bind
    logger.info('Connected to database')
    return engine


def _drop_tables(engine):
    metadata = MetaData(bind=engine)
    metadata.reflect()
    logger.info('Dropping all tables...')
    metadata.drop_all()


def _create_tables(engine):
    logger.info('Creating all tables...')
    Base.metadata.create_all(bind=engine)


def close():
    logger.info('Closing connection...')
    db_manager.close()


def _populate_db():
    logger.info('Populating database...')
    postgres.populate_db()


def _drop_db():
    logger.info('Dropping database...')
    postgres.drop_db()


def _init_db():
    logger.info('Initializing database...')
    postgres.init_db()
    alembic.stamp_head()


def main():
    parsed_args = _parse_args()

    _init_logging(parsed_args.verbose)

    engine = expensive_setup()

    if parsed_args.reset:
        _drop_db()
        _init_db()
        _create_tables(engine)

    if parsed_args.drop:
        _drop_db()

    if parsed_args.init:
        _init_db()
        _create_tables(engine)
        _populate_db()

    close()


def _parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='increase verbosity')
    parser.add_argument('--init', action='store_true',
                        help='Initialize role and database')
    parser.add_argument('--reset', action='store_true',
                        help='reset database')
    parser.add_argument('--drop', action='store_true',
                        help='drop tables')
    return parser.parse_args()


def _init_logging(verbose):
    logger = logging.getLogger()
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter('%(message)s'))
    logger.addHandler(handler)
    if verbose:
        logger.setLevel(logging.INFO)
    else:
        logger.setLevel(logging.ERROR)
