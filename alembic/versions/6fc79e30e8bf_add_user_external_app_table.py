"""add_user_external_app_table

Revision ID: 6fc79e30e8bf
Revises: c1d845eb61b4

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6fc79e30e8bf'
down_revision = 'c1d845eb61b4'


def upgrade():
    op.create_table(
        'user_external_app',
        sa.Column('name', sa.Text, primary_key=True),
        sa.Column(
            'user_uuid',
            sa.String(38),
            sa.ForeignKey('userfeatures.uuid', ondelete='CASCADE'),
            primary_key=True
        ),
        sa.Column('label', sa.Text),
        sa.Column('configuration', sa.JSON),
    )


def downgrade():
    op.drop_table('user_external_app')
