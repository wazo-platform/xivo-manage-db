"""remove_deprecated_cti_tables

Revision ID: cac9af37c973
Revises: 4c1cbf778770

"""

from alembic import op
import sqlalchemy as sa

from sqlalchemy.schema import Column


# revision identifiers, used by Alembic.
revision = 'cac9af37c973'
down_revision = '4c1cbf778770'


def upgrade():
    op.drop_column('userfeatures', 'cti_profile_id')
    op.drop_table('ctistatus')
    op.drop_table('cti_profile_service')
    op.drop_table('cti_profile_preference')
    op.drop_table('cti_profile_xlet')
    op.drop_table('cti_profile')
    op.drop_table('ctiphonehintsgroup')
    op.drop_table('ctiphonehints')
    op.drop_table('ctipresences')
    op.drop_table('cti_preference')
    op.drop_table('cti_service')
    op.drop_table('cti_xlet_layout')
    op.drop_table('cti_xlet')


def downgrade():
    op.create_table(
        'cti_xlet',
        Column('id', sa.Integer, primary_key=True),
        Column('plugin_name', sa.String(40), nullable=False),
    )
    op.create_table(
        'cti_xlet_layout',
        Column('id', sa.Integer, primary_key=True),
        Column('name', sa.String(255), nullable=False),
    )
    op.create_table(
        'cti_service',
        Column('id', sa.Integer, primary_key=True),
        Column('key', sa.String(255), nullable=False),
    )
    op.create_table(
        'cti_preference',
        Column('id', sa.Integer, primary_key=True),
        Column('option', sa.String(255), nullable=False),
    )
    op.create_table(
        'ctipresences',
        Column('id', sa.Integer, primary_key=True),
        Column('name', sa.String(255), nullable=False),
        Column('description', sa.String(255)),
        Column('deletable', sa.Integer),
    )
    op.create_table(
        'ctiphonehints',
        Column('id', sa.Integer, primary_key=True),
        Column('idgroup', sa.Integer),
        Column('number', sa.String(8)),
        Column('name', sa.String(255)),
        Column('color', sa.String(128)),
    )
    op.create_table(
        'ctiphonehintsgroup',
        Column('id', sa.Integer, primary_key=True),
        Column('name', sa.String(255), nullable=False),
        Column('description', sa.String(255)),
        Column('deletable', sa.Integer),
    )
    op.create_table(
        'cti_profile',
        Column('id', sa.Integer, primary_key=True),
        Column('name', sa.String(255), nullable=False),
        Column(
            'presence_id',
            sa.Integer,
            sa.ForeignKey('ctipresences.id', ondelete='RESTRICT'),
        ),
        Column(
            'phonehints_id',
            sa.Integer,
            sa.ForeignKey('ctiphonehintsgroup.id', ondelete='RESTRICT'),
        ),
    )
    op.create_table(
        'cti_profile_xlet',
        Column(
            'xlet_id',
            sa.Integer,
            sa.ForeignKey('cti_xlet.id', ondelete='CASCADE'),
            primary_key=True,
        ),
        Column(
            'profile_id',
            sa.Integer,
            sa.ForeignKey('cti_profile.id', ondelete='CASCADE'),
            primary_key=True,
        ),
        Column(
            'layout_id',
            sa.Integer,
            sa.ForeignKey('cti_xlet_layout.id', ondelete='RESTRICT'),
        ),
        Column('closable', sa.Boolean, server_default='True'),
        Column('movable', sa.Boolean, server_default='True'),
        Column('floating', sa.Boolean, server_default='True'),
        Column('scrollable', sa.Boolean, server_default='True'),
        Column('order', sa.Integer),
    )
    op.create_table(
        'cti_profile_service',
        Column(
            'profile_id',
            sa.Integer,
            sa.ForeignKey('cti_profile.id', ondelete='CASCADE'),
            primary_key=True,
        ),
        Column(
            'service_id',
            sa.Integer,
            sa.ForeignKey('cti_service.id', ondelete='CASCADE'),
            primary_key=True,
        ),
    )
    op.create_table(
        'cti_profile_preference',
        Column(
            'profile_id',
            sa.Integer,
            sa.ForeignKey('cti_profile.id', ondelete='CASCADE'),
            primary_key=True,
        ),
        Column(
            'preference_id',
            sa.Integer,
            sa.ForeignKey('cti_preference.id', ondelete='CASCADE'),
            primary_key=True,
        ),
        Column('value', sa.String(255)),
    )
    op.create_table(
        'ctistatus',
        Column('id', sa.Integer, primary_key=True),
        Column(
            'presence_id',
            sa.Integer,
            sa.ForeignKey('ctipresences.id', ondelete='CASCADE'),
        ),
        Column('name', sa.String(255), nullable=False),
        Column('display_name', sa.String(255)),
        Column('actions', sa.String(255)),
        Column('color', sa.String(20)),
        Column('access_status', sa.String(255)),
        Column('deletable', sa.Integer),
    )
    op.create_unique_constraint(
        'ctistatus_presence_id_name_key',
        'ctistatus',
        ['presence_id', 'name'],
    )
    op.add_column(
        'userfeatures',
        Column(
            'cti_profile_id',
            sa.Integer,
            sa.ForeignKey('cti_profile.id', ondelete='RESTRICT'),
        )
    )
