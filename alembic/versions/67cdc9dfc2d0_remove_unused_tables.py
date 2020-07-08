"""remove-unused-tables

Revision ID: 67cdc9dfc2d0
Revises: eddc1df1d57c

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '67cdc9dfc2d0'
down_revision = 'eddc1df1d57c'


def upgrade():
    op.drop_table('attachment')
    op.drop_table('ctisheetactions')
    op.drop_table('ctisheetevents')
    op.drop_column('agentfeatures', 'numgroup')
    op.drop_table('agentgroup')


def downgrade():
    op.create_table(
        'attachment',
        sa.Column('id', sa.Integer, nullable=False, primary_key=True),
        sa.Column('name', sa.String(64), nullable=False),
        sa.Column('object_type', sa.String(16), nullable=False),
        sa.Column('object_id', sa.Integer, nullable=False),
        sa.Column('file', sa.Binary),
        sa.Column('size', sa.Integer, nullable=False),
        sa.Column('mime', sa.String(64), nullable=False),
    )
    op.create_unique_constraint(
        'attachment_object_type_object_id_key',
        'attachment',
        ['object_type', 'object_id']
    )

    op.create_table(
        'ctisheetactions',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50)),
        sa.Column('description', sa.Text, nullable=False),
        sa.Column('whom', sa.String(50)),
        sa.Column('sheet_info', sa.Text),
        sa.Column('systray_info', sa.Text),
        sa.Column('sheet_qtui', sa.Text),
        sa.Column('action_info', sa.Text),
        sa.Column('focus', sa.Integer),
        sa.Column('deletable', sa.Integer),
        sa.Column('disable', sa.Integer),
    )

    op.create_table(
        'ctisheetevents',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('incomingdid', sa.String(50)),
        sa.Column('hangup', sa.String(50)),
        sa.Column('dial', sa.String(50)),
        sa.Column('link', sa.String(50)),
        sa.Column('unlink', sa.String(50)),
    )

    op.create_table(
        'agentgroup',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('groupid', sa.Integer, nullable=False),
        sa.Column('name', sa.String(128), nullable=False, server_default=''),
        sa.Column('groups', sa.String(255), nullable=False, server_default=''),
        sa.Column('commented', sa.Integer, nullable=False, server_default='0'),
        sa.Column('deleted', sa.Integer, nullable=False, server_default='0'),
        sa.Column('description', sa.Text),
    )

    op.add_column('agentfeatures', sa.Column('numgroup', sa.Integer, nullable=True))
