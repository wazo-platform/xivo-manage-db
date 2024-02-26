"""remove-queuepenalty-tables

Revision ID: 40c244ac9a97
Revises: 894df9364c4b

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '40c244ac9a97'
down_revision = '894df9364c4b'


def upgrade():
    op.drop_table('queuepenalty')
    op.drop_table('queuepenaltychange')
    op.execute(sa.text('DROP TYPE queuepenaltychange_sign'))


def downgrade():
    op.create_table(
        'queuepenaltychange',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column(
            'seconds',
            sa.Integer,
            primary_key=True,
            server_default='0',
            autoincrement=False,
        ),
        sa.Column('maxp_sign', sa.Enum('=', '+', '-', name='queuepenaltychange_sign')),
        sa.Column('maxp_value', sa.Integer),
        sa.Column('minp_sign', sa.Enum('=', '+', '-', name='queuepenaltychange_sign')),
        sa.Column('minp_value', sa.Integer),
    )
    op.create_table(
        'queuepenalty',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(255), unique=True),
        sa.Column('commented', sa.Integer, nullable=False, server_default='0'),
        sa.Column('description', sa.Text, nullable=False),
    )
