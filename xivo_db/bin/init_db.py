# -*- coding: UTF-8 -*-
# Copyright 2014-2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

import argparse
import logging
import xivo_dao.alchemy.all  # imports all the sqlalchemy model

from xivo_dao.helpers import db_manager
from xivo_dao.helpers.db_manager import Base
from xivo_db import alembic
from xivo_db import postgres

logger = logging.getLogger(__name__)


def _create_tables():
    logger.info('Creating all tables...')
    Base.metadata.create_all()


def _enable_extensions():
    logger.info('Enabling extensions...')
    extensions = ['pgcrypto', 'uuid-ossp']
    for extension in extensions:
        postgres.enable_extension(extension)


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
    db_manager.init_db_from_config()


def main():
    parsed_args = _parse_args()

    _init_logging(parsed_args.verbose)

    if parsed_args.drop:
        _drop_db()

    if parsed_args.init:
        _init_db()
        _enable_extensions()
        _create_tables()
        _populate_db()


def _parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='increase verbosity')
    parser.add_argument('--drop', action='store_true',
                        help='drop database')
    parser.add_argument('--init', action='store_true',
                        help='initialize database')
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
