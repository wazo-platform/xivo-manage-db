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

    op.execute('''
    INSERT INTO feature_extension (enabled, exten, feature) 
      SELECT 
        CASE commented WHEN 1 THEN False ELSE True END as enabled,
        exten,
        typeval as feature
      FROM extensions
      WHERE context = 'xivo-features';
    ''')


def downgrade():
    op.execute('''
    INSERT INTO extensions (commented, context, exten, type, typeval)
      SELECT 
        CASE enabled WHEN False THEN 1 ELSE 0 END as commented,
        'xivo-features' as context,
        exten,
        TEXT 'extenfeatures' as type
        feature as typeval,
      FROM feature_extension;
    ''')
    op.drop_table('feature_extension')