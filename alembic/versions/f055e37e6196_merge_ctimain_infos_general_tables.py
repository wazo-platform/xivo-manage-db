"""merge-ctimain-infos-general-tables

Revision ID: f055e37e6196
Revises: 67cdc9dfc2d0

"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'f055e37e6196'
down_revision = '67cdc9dfc2d0'

ctimain_tbl = sa.sql.table(
    'ctimain',
    sa.sql.column('live_reload_conf'),
)
general_tbl = sa.sql.table(
    'general',
    sa.sql.column('timezone'),
    sa.sql.column('configured'),
)
infos_tbl = sa.sql.table(
    'infos',
    sa.sql.column('live_reload_enabled'),
    sa.sql.column('timezone'),
    sa.sql.column('configured'),
)


def upgrade():
    op.add_column(
        'infos',
        sa.Column(
            'live_reload_enabled',
            sa.Boolean,
            nullable=False,
            server_default='True',
        )
    )
    op.add_column('infos', sa.Column('timezone', sa.String(128)))
    op.add_column(
        'infos',
        sa.Column(
            'configured',
            sa.Boolean,
            nullable=False,
            server_default='False',
        )
    )
    ctimain = op.get_bind().execute(sa.sql.select([ctimain_tbl])).first()
    general = op.get_bind().execute(sa.sql.select([general_tbl])).first()
    op.execute(
        infos_tbl
        .update()
        .values(
            timezone=general.timezone,
            configured=general.configured,
            live_reload_enabled=ctimain.live_reload_conf == 1,
        )
    )
    op.drop_table('ctimain')
    op.drop_table('general')


def downgrade():
    op.create_table(
        'ctimain',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('ctis_active', sa.Integer, nullable=False, server_default='1'),
        sa.Column('tlscertfile', sa.String(128)),
        sa.Column('tlsprivkeyfile', sa.String(128)),
        sa.Column('context_separation', sa.Integer),
        sa.Column('live_reload_conf', sa.Integer),
    )
    op.create_table(
        'general',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('timezone', sa.String(128)),
        sa.Column('configured', sa.Boolean, nullable=False, server_default='False'),
    )
    infos = op.get_bind().execute(sa.sql.select([infos_tbl])).first()
    op.execute(
        ctimain_tbl
        .insert()
        .values(live_reload_conf=1 if infos.live_reload_enabled else 0)
    )
    op.execute(
        general_tbl
        .insert()
        .values(
            timezone=infos.timezone,
            configured=infos.configured,
        )
    )
    op.drop_column('infos', 'live_reload_enabled')
    op.drop_column('infos', 'timezone')
    op.drop_column('infos', 'configured')
