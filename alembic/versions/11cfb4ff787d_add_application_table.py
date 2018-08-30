"""add_application_table

Revision ID: 11cfb4ff787d
Revises: 57ab432bb1c3

"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '11cfb4ff787d'
down_revision = '57ab432bb1c3'


def upgrade():
    op.create_table(
        'application',
        sa.Column(
            'uuid',
            sa.String(36),
            server_default=sa.text('uuid_generate_v4()'),
            primary_key=True
        ),
        sa.Column(
            'tenant_uuid',
            sa.String(36),
            sa.ForeignKey('tenant.uuid', ondelete='CASCADE'),
            nullable=False,
        ),
        sa.Column('name', sa.String(128)),
    )

    op.create_table(
        'application_dest_node',
        sa.Column(
            'application_uuid',
            sa.String(36),
            sa.ForeignKey('application.uuid', ondelete='CASCADE'),
            primary_key=True,
        ),
        sa.Column(
            'type',
            sa.String(32),
            sa.CheckConstraint("type in ('holding', 'mixing')")
        ),
        sa.Column('music_on_hold', sa.String(128)),
    )


def downgrade():
    op.drop_table('application')
    op.drop_table('application_dest_node')
