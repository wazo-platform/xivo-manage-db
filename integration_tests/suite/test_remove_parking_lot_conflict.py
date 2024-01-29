# Copyright 2024 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

import os
import os.path
import logging
import sys

import sqlalchemy
import sqlalchemy_utils

from alembic import command as alembic_command  # type: ignore
from alembic.config import Config as AlembicConfig
from pathlib import Path
from sqlalchemy import Connection, sql
from typing import Iterable
from wazo_test_helpers.asset_launching_test_case import AssetLaunchingTestCase

logger = logging.getLogger(__name__)


class BaseAssetLaunchingTestCase(AssetLaunchingTestCase):
    assets_root = os.path.join(os.path.dirname(__file__), '..', 'assets')
    service = 'postgres'
    asset = 'base'


env = BaseAssetLaunchingTestCase


def setup_module() -> None:
    env.setUpClass()


def teardown_module() -> None:
    env.tearDownClass()


def generate_migrated_database(
    postgresql_uri: str, init_script_path: str, target_version: str
) -> None:
    reset_database(postgresql_uri)
    run_script(init_script_path, postgresql_uri)
    run_alembic_migrations(postgresql_uri, target_version)


def reset_database(postgresql_uri: str) -> None:
    drop_database(postgresql_uri)
    create_database(postgresql_uri)
    enable_extensions(postgresql_uri)


def drop_database(postgresql_uri: str) -> None:
    logger.info("dropping database")
    if sqlalchemy_utils.functions.database_exists(postgresql_uri):
        engine = sqlalchemy.create_engine(postgresql_uri)
        engine.execute('DROP OWNED BY asterisk CASCADE;')
        engine.execute('DROP ROLE IF EXISTS asterisk;')
        engine.dispose()

        sqlalchemy_utils.functions.drop_database(postgresql_uri)


def create_database(postgresql_uri: str) -> None:
    logger.info("creating database")

    sqlalchemy_utils.functions.create_database(postgresql_uri)

    engine = sqlalchemy.create_engine(postgresql_uri)
    engine.execute('CREATE ROLE asterisk WITH PASSWORD \'superpass\';')
    engine.dispose()


def enable_extensions(postgresql_uri: str) -> None:
    logger.info("enabling DB extensions")
    engine = sqlalchemy.create_engine(postgresql_uri)
    engine.execute('CREATE EXTENSION IF NOT EXISTS "pgcrypto";')
    engine.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp";')
    engine.dispose()


def run_script(filepath: str, postgresql_uri: str) -> None:
    logger.info("running script %s", filepath)
    postgresql_uri = 'postgresql://postgres:secret@127.0.0.1:5432/asterisk'

    command = [
        'psql',
        '--quiet',
        '--no-psqlrc',
        '--dbname',
        postgresql_uri,
        '--file',
        filepath,
    ]
    errors = env.docker_exec(command, service_name='postgres', return_attr='stderr')

    if errors:
        logger.warning("errors while executing %s: %s", filepath, errors)
        sys.exit(2)


def run_alembic_migrations(postgresql_uri: str, target_version: str) -> None:
    logger.info("running alembic migrations")
    alembic_cfg = build_alembic_config(postgresql_uri)
    os.environ['XIVO_UUID'] = '99999999-9999-9999-9999-999999999999'
    # alembic_command.stamp(alembic_cfg, 'base')
    alembic_command.upgrade(alembic_cfg, target_version)


def build_alembic_config(postgresql_uri: str) -> AlembicConfig:
    alembic_path = Path(env.assets_root) / '../../alembic'
    ini_file = Path(env.assets_root) / '../../alembic.ini'

    alembic_cfg = AlembicConfig(ini_file)
    alembic_cfg.set_main_option('configure_logging', 'false')
    alembic_cfg.set_main_option("script_location", str(alembic_path))
    alembic_cfg.set_main_option("sqlalchemy.url", str(postgresql_uri))
    return alembic_cfg


context_table = sql.table(
    'context',
    sql.column('name'),
    sql.column('tenant_uuid'),
)
extensions_table = sql.table(
    'extensions',
    sql.column('id'),
    sql.column('exten'),
    sql.column('context'),
    sql.column('type'),
    sql.column('typeval'),
)
parking_lot_table = sql.table(
    'parking_lot',
    sql.column('id'),
    sql.column('slots_start'),
    sql.column('slots_end'),
    sql.column('tenant_uuid'),
)
tenant_table = sql.table(
    'tenant',
    sql.column('uuid'),
)


def insert_parking_lot(
    connection: Connection,
    exten: str,
    context: str,
    slots_start: str,
    slots_end: str,
    tenant_uuid: str,
) -> int:
    query = (
        parking_lot_table.insert()
        .returning(parking_lot_table.c.id)
        .values(slots_start=slots_start, slots_end=slots_end, tenant_uuid=tenant_uuid)
    )
    parking_lot_id = connection.execute(query).scalar()
    query = extensions_table.insert().values(
        exten=exten,
        context=context,
        type='parking',
        typeval=str(parking_lot_id),
    )
    connection.execute(query)
    return parking_lot_id


def list_parking_lot_ids(connection: Connection) -> Iterable[int]:
    query = sql.select([parking_lot_table.c.id])
    return list(row.id for row in connection.execute(query))


def list_extensions(connection: Connection) -> Iterable[tuple[str, str, str, str]]:
    query = sql.select(
        [
            extensions_table.c.exten,
            extensions_table.c.context,
            extensions_table.c.type,
            extensions_table.c.typeval,
        ]
    ).order_by(extensions_table.c.id)
    return list(connection.execute(query))


def test_parking_remove_conflicts() -> None:
    port = env.service_port(5432, 'postgres')
    pg_uri = f'postgresql://postgres:secret@127.0.0.1:{port}/asterisk'

    db_init_script = (
        '/usr/src/xivo-manage-db/integration_tests/assets/database-before-migration.sql'
    )
    generate_migrated_database(pg_uri, db_init_script, 'f64ea9c1a1d3')

    engine = sqlalchemy.create_engine(pg_uri)
    with engine.connect() as connection:
        query = tenant_table.insert().returning(tenant_table.c.uuid)
        tenant_uuid = connection.execute(query).scalar()
        connection.execute(
            context_table.insert().values(name='default', tenant_uuid=tenant_uuid)
        )
        connection.execute(
            context_table.insert().values(
                name='other-context', tenant_uuid=tenant_uuid
            ),
        )
        # unconflicting parking lot
        remaining_parking_lot_id = insert_parking_lot(
            connection,
            exten='100',
            context='default',
            slots_start='101',
            slots_end='150',
            tenant_uuid=tenant_uuid,
        )
        # unconflicting parking lot in another context
        remaining_parking_lot_id2 = insert_parking_lot(
            connection,
            exten='100',
            context='other-context',
            slots_start='101',
            slots_end='150',
            tenant_uuid=tenant_uuid,
        )
        # conflicting with 699
        insert_parking_lot(
            connection,
            exten='700',
            context='default',
            slots_start='701',
            slots_end='750',
            tenant_uuid=tenant_uuid,
        )
        # conflicting with 700
        insert_parking_lot(
            connection,
            exten='699',
            context='default',
            slots_start='701',
            slots_end='750',
            tenant_uuid=tenant_uuid,
        )
        # conflicting with 799
        insert_parking_lot(
            connection,
            exten='800',
            context='default',
            slots_start='801',
            slots_end='850',
            tenant_uuid=tenant_uuid,
        )
        # conflicting with 800 on the last number
        insert_parking_lot(
            connection,
            exten='799',
            context='default',
            slots_start='850',
            slots_end='859',
            tenant_uuid=tenant_uuid,
        )

    run_alembic_migrations(pg_uri, 'cc3dd7adbd56')

    with engine.connect() as connection:
        remaining_parking_lots = list_parking_lot_ids(connection)
        assert list(remaining_parking_lots) == [
            remaining_parking_lot_id,
            remaining_parking_lot_id2,
        ]

        remaining_extensions = list_extensions(connection)
        assert remaining_extensions == [
            ('100', 'default', 'parking', str(remaining_parking_lot_id)),
            ('100', 'other-context', 'parking', str(remaining_parking_lot_id2)),
        ]
