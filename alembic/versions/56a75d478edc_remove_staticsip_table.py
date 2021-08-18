"""remove_staticsip_table

Revision ID: 56a75d478edc
Revises: 06e9e3483fec

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56a75d478edc'
down_revision = '06e9e3483fec'


def upgrade():
    op.drop_table('staticsip')


def downgrade():
    op.create_table(
        'staticsip',
        sa.Column('id', sa.Integer, nullable=False, primary_key=True),
        sa.Column('cat_metric', sa.Integer,
                  nullable=False, server_default='0'),
        sa.Column('var_metric', sa.Integer,
                  nullable=False, server_default='0'),
        sa.Column('commented', sa.Integer, nullable=False, server_default='0'),
        sa.Column('filename', sa.String(128), nullable=False),
        sa.Column('category', sa.String(128), nullable=False),
        sa.Column('var_name', sa.String(128), nullable=False),
        sa.Column('var_val', sa.String(255))
    )
    op.create_index('staticsip__idx__category', 'staticsip', ['category'])
