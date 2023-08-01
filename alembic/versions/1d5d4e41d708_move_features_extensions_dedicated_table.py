"""move_features_extensions_dedicated_table

Revision ID: 1d5d4e41d708
Revises: 1ec7cdef9eeb

"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision = '1d5d4e41d708'
down_revision = '1ec7cdef9eeb'


def upgrade():
    # create 'feature_extension' table
    op.create_table(
        'feature_extension',
        sa.Column('uuid', UUID, server_default=sa.text('uuid_generate_v4()'),
                  primary_key=True),
        sa.Column('enabled', sa.Boolean, nullable=False, server_default='true'),
        sa.Column('exten', sa.String(40), nullable=False),
        sa.Column('feature', sa.String(255), nullable=False),
    )

    op.create_index(
        index_name='feature_extension__idx__uuid',
        table_name='feature_extension',
        columns=['uuid'],
    )

    # move extensions having context=xivo-features from 'extensions' table into 'feature_extension' table
    op.execute('''
    INSERT INTO feature_extension (enabled, exten, feature) 
      SELECT 
        CASE commented WHEN 1 THEN False ELSE True END as enabled,
        exten,
        typeval as feature
      FROM extensions
      WHERE context = 'xivo-features';
    ''')

    # for func keys having a 'extension_id' column
    for t in ('func_key_dest_agent', 'func_key_dest_forward', 'func_key_dest_groupmember', 'func_key_dest_service'):
        # add new column 'feature_extension_uuid'
        op.execute(f'''
        ALTER TABLE {t}
        ADD feature_extension_uuid UUID REFERENCES feature_extension(uuid);
        ''')

        # populate feature_extension_uuid column
        op.execute(f'''
        UPDATE {t} t
        SET feature_extension_uuid=fe.uuid
        FROM feature_extension fe
        WHERE 
        fe.feature=(
          SELECT extensions.typeval FROM extensions WHERE t.extension_id=extensions.id
        );
        ''')

        # remove old column 'extension_id'
        op.execute(f"ALTER TABLE {t} DROP COLUMN extension_id;")

    # old features extensions in 'extensions' table removed
    op.execute("DELETE FROM extensions where context = 'xivo-features';")


def downgrade():
    op.execute('''
    INSERT INTO extensions (commented, context, exten, type, typeval)
      SELECT 
        CASE enabled WHEN False THEN 1 ELSE 0 END as commented,
        TEXT 'xivo-features' as context,
        exten,
        TEXT 'extenfeatures' as type
        feature as typeval,
      FROM feature_extension;
    ''')

    # for func keys having a 'feature_extension_uuid' column
    for t in ('func_key_dest_agent', 'func_key_dest_forward', 'func_key_dest_groupmember',
              'func_key_dest_service'):
        # add new column 'extension_id'
        op.execute(f'''
            ALTER TABLE {t}
            ADD extension_id integer REFERENCES extensions(id);
            ''')

        # populate feature_extension_uuid column
        op.execute(f'''
            UPDATE {t} t
            SET extension_id=e.id
            FROM extensions e
            WHERE 
            e.typeval=(
              SELECT feature_extension.feature FROM feature_extension WHERE t.feature_extension_uuid=feature_extension.uuid
            );
            ''')

        # remove previous column 'feature_extension_uuid'
        op.execute(f"ALTER TABLE {t} DROP COLUMN feature_extension_uuid;")

    op.execute("DROP TABLE feature_extension;")