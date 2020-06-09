"""remove-sipauthentication

Revision ID: d47f295009dd
Revises: d90ff200ae53

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd47f295009dd'
down_revision = 'd90ff200ae53'

secret_mode_type = sa.Enum(
    'md5',
    'clear',
    name='sipauthentication_secretmode',
)


def upgrade():
    op.drop_table('sipauthentication')
    secret_mode_type.drop(op.get_bind(), checkfirst=False)


def downgrade():
    op.create_table(
        'sipauthentication',
        sa.Column('id', sa.types.INTEGER, primary_key=True),
        sa.Column('usersip_id', sa.types.INTEGER),
        sa.Column('user', sa.types.String(255), nullable=False),
        sa.Column('secretmode', secret_mode_type, nullable=False),
        sa.Column('secret', sa.types.String(255), nullable=False),
        sa.Column('realm', sa.types.String(1024), nullable=False),
    )
