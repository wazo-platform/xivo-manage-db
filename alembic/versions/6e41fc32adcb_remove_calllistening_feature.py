"""remove calllistening feature

Revision ID: 6e41fc32adcb
Revises: f3bc803db64e

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '6e41fc32adcb'
down_revision = 'f3bc803db64e'

FEATURE = 'calllistening'
EXTEN = '*34'

feature_extension_table = sa.sql.table(
    'feature_extension',
    sa.sql.column('uuid'),
    sa.sql.column('enabled'),
    sa.sql.column('exten'),
    sa.sql.column('feature'),
)

func_key_dest_service_table = sa.sql.table(
    'func_key_dest_service',
    sa.sql.column('func_key_id'),
    sa.sql.column('destination_type_id'),
    sa.sql.column('feature_extension_uuid'),
)

func_key_table = sa.sql.table(
    'func_key',
    sa.sql.column('id'),
    sa.sql.column('type_id'),
    sa.sql.column('destination_type_id'),
)


def upgrade():
    conn = op.get_bind()

    calllistening_uuids = (
        sa.select([feature_extension_table.c.uuid])
        .where(feature_extension_table.c.feature == FEATURE)
    )

    # Collect func_key IDs before deleting the dest_service rows
    func_key_ids = [
        row[0] for row in conn.execute(
            sa.select([func_key_dest_service_table.c.func_key_id])
            .where(
                func_key_dest_service_table.c.feature_extension_uuid.in_(
                    calllistening_uuids
                )
            )
        )
    ]

    # Remove func_key_dest_service entries referencing calllistening
    conn.execute(
        func_key_dest_service_table
        .delete()
        .where(
            func_key_dest_service_table.c.feature_extension_uuid.in_(
                calllistening_uuids
            )
        )
    )

    # Remove func_key entries that pointed to calllistening destinations
    if func_key_ids:
        conn.execute(
            func_key_table
            .delete()
            .where(func_key_table.c.id.in_(func_key_ids))
        )

    # Remove the feature extension itself
    conn.execute(
        feature_extension_table
        .delete()
        .where(feature_extension_table.c.feature == FEATURE)
    )


def downgrade():
    conn = op.get_bind()

    conn.execute(
        feature_extension_table
        .insert()
        .values(enabled=False, exten=EXTEN, feature=FEATURE)
    )

    conn.execute(
        func_key_table
        .insert()
        .values(type_id=1, destination_type_id=5)
    )

    conn.execute(
        func_key_dest_service_table
        .insert()
        .values(
            func_key_id=sa.func.currval('func_key_id_seq'),
            destination_type_id=5,
            feature_extension_uuid=(
                sa.select([feature_extension_table.c.uuid])
                .where(feature_extension_table.c.feature == FEATURE)
                .scalar_subquery()
            ),
        )
    )
