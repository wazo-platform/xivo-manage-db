"""add the pjsip transport tables

Revision ID: edca430a8373
Revises: 2cbd52dd69e1

"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = 'edca430a8373'
down_revision = '2cbd52dd69e1'


def upgrade():
    op.create_table(
        'pjsip_transport',
        sa.Column(
            'uuid',
            postgresql.UUID,
            server_default=sa.text('uuid_generate_v4()'),
            primary_key=True,
        ),
        sa.Column('name', sa.Text, nullable=False),
    )
    op.create_unique_constraint('pjsip_transport_name_key', 'pjsip_transport', ['name'])

    op.create_table(
        'pjsip_transport_option',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('key', sa.Text, nullable=False),
        sa.Column('value', sa.Text, nullable=False),
        sa.Column(
            'pjsip_transport_uuid',
            postgresql.UUID,
            sa.ForeignKey('pjsip_transport.uuid', ondelete='CASCADE'),
            nullable=False,
        ),
    )


def downgrade():
    op.drop_table('pjsip_transport_option')
    op.drop_constraint('pjsip_transport_name_key', 'pjsip_transport')
    op.drop_table('pjsip_transport')
