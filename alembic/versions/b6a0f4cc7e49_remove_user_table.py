"""remove_user_table

Revision ID: b6a0f4cc7e49
Revises: 0720419573a5

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b6a0f4cc7e49'
down_revision = '0720419573a5'


def upgrade():
    op.drop_table('user')
    op.execute('DROP TYPE user_meta')


def downgrade():
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, nullable=False, primary_key=True),
        sa.Column(
            'uuid',
            sa.String(38),
            nullable=False,
            unique=True,
            server_default=sa.text('uuid_generate_v4()'),
        ),
        sa.Column(
            'entity_id',
            sa.Integer,
            sa.ForeignKey('entity.id', ondelete='RESTRICT'),
        ),
        sa.Column('login', sa.String(64), nullable=False, unique=True, server_default=''),
        sa.Column('passwd', sa.String(64), nullable=False, server_default=''),
        sa.Column(
            'meta',
            sa.Enum('user', 'admin', 'root', name='user_meta'),
            nullable=False,
            unique=True,
            server_default='user',
        ),
        sa.Column('valid', sa.Integer, nullable=False, server_default='1'),
        sa.Column('time', sa.Integer, nullable=False, server_default='0'),
        sa.Column('dcreate', sa.Integer, nullable=False, server_default='0'),
        sa.Column('dupdate', sa.Integer, nullable=False, server_default='0'),
        sa.Column('obj', sa.Text, nullable=False),
    )
