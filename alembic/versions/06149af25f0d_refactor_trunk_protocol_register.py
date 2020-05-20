"""refactor_trunk_protocol_register

Revision ID: 06149af25f0d
Revises: e5da3b191742

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '06149af25f0d'
down_revision = 'e5da3b191742'

trunk_protocol = sa.Enum(('sip', 'iax', 'sccp', 'custom'), name='trunk_protocol')

trunkfeatures_tbl = sa.sql.table(
    'trunkfeatures',
    sa.sql.column('id'),
    sa.sql.column('protocol'),
    sa.sql.column('protocolid'),
    sa.sql.column('registerid'),
    sa.sql.column('endpoint_sip_id'),
    sa.sql.column('endpoint_iax_id'),
    sa.sql.column('endpoint_custom_id'),
    sa.sql.column('register_sip_id'),
    sa.sql.column('register_iax_id'),
)
usersip_tbl = sa.sql.table('usersip', sa.sql.column('id'))
useriax_tbl = sa.sql.table('useriax', sa.sql.column('id'))
usercustom_tbl = sa.sql.table('usercustom', sa.sql.column('id'))
staticsip_tbl = sa.sql.table('staticsip', sa.sql.column('id'))
staticiax_tbl = sa.sql.table('staticiax', sa.sql.column('id'))


def upgrade():
    op.add_column(
        'trunkfeatures',
        sa.Column(
            'endpoint_sip_id',
            sa.Integer,
            sa.ForeignKey('usersip.id', ondelete='SET NULL')
        )
    )
    op.add_column(
        'trunkfeatures',
        sa.Column(
            'endpoint_iax_id',
            sa.Integer,
            sa.ForeignKey('useriax.id', ondelete='SET NULL')
        )
    )
    op.add_column(
        'trunkfeatures',
        sa.Column(
            'endpoint_custom_id',
            sa.Integer,
            sa.ForeignKey('usercustom.id', ondelete='SET NULL')
        )
    )
    op.add_column(
        'trunkfeatures',
        sa.Column(
            'register_sip_id',
            sa.Integer,
            sa.ForeignKey('staticsip.id', ondelete='SET NULL')
        )
    )
    op.add_column(
        'trunkfeatures',
        sa.Column(
            'register_iax_id',
            sa.Integer,
            sa.ForeignKey('staticiax.id', ondelete='SET NULL')
        )
    )
    op.create_check_constraint(
        'trunkfeatures_endpoints_check',
        'trunkfeatures',
        '''
        ( CASE WHEN endpoint_sip_id IS NULL THEN 0 ELSE 1 END
        + CASE WHEN endpoint_iax_id IS NULL THEN 0 ELSE 1 END
        + CASE WHEN endpoint_custom_id IS NULL THEN 0 ELSE 1 END
        ) <= 1
        ''',
    )
    op.create_check_constraint(
        'trunkfeatures_registers_check',
        'trunkfeatures',
        '''
        ( CASE WHEN register_sip_id IS NULL THEN 0 ELSE 1 END
        + CASE WHEN register_iax_id IS NULL THEN 0 ELSE 1 END
        ) <= 1
        ''',
    ),
    op.create_check_constraint(
        'trunkfeatures_endpoint_register_check',
        'trunkfeatures',
        '''
        (
            register_sip_id IS NULL AND
            register_iax_id IS NULL
        ) OR (
            register_sip_id IS NOT NULL AND
            endpoint_iax_id IS NULL AND
            endpoint_custom_id IS NULL
        ) OR (
            register_iax_id IS NOT NULL AND
            endpoint_sip_id IS NULL AND
            endpoint_custom_id IS NULL
        )
        ''',
    ),
    query = sa.sql.select([
        trunkfeatures_tbl.c.id,
        trunkfeatures_tbl.c.protocol,
        trunkfeatures_tbl.c.protocolid,
        trunkfeatures_tbl.c.registerid,
    ])
    for trunk in op.get_bind().execute(query):
        if not trunk.protocol:
            continue

        if trunk.protocol == 'sip':
            if trunk.protocolid:
                query = sa.sql.select([usersip_tbl.c.id]).where(usersip_tbl.c.id == trunk.protocolid)
                if op.get_bind().execute(query).scalar():
                    op.execute(
                        trunkfeatures_tbl
                        .update()
                        .where(trunkfeatures_tbl.c.id == trunk.id)
                        .values(endpoint_sip_id=trunk.protocolid)
                    )
            if trunk.registerid:
                query = sa.sql.select([staticsip_tbl.c.id]).where(staticsip_tbl.c.id == trunk.registerid)
                if op.get_bind().execute(query).scalar():
                    op.execute(
                        trunkfeatures_tbl
                        .update()
                        .where(trunkfeatures_tbl.c.id == trunk.id)
                        .values(register_sip_id=trunk.registerid)
                    )

        elif trunk.protocol == 'iax':
            if trunk.protocolid:
                query = sa.sql.select([useriax_tbl.c.id]).where(useriax_tbl.c.id == trunk.protocolid)
                if op.get_bind().execute(query).scalar():
                    op.execute(
                        trunkfeatures_tbl
                        .update()
                        .where(trunkfeatures_tbl.c.id == trunk.id)
                        .values(endpoint_iax_id=trunk.protocolid)
                    )

            if trunk.registerid:
                query = sa.sql.select([staticiax_tbl.c.id]).where(staticiax_tbl.c.id == trunk.registerid)
                if op.get_bind().execute(query).scalar():
                    op.execute(
                        trunkfeatures_tbl
                        .update()
                        .where(trunkfeatures_tbl.c.id == trunk.id)
                        .values(register_iax_id=trunk.registerid)
                    )

        elif trunk.protocol == 'custom':
            if trunk.protocolid:
                query = sa.sql.select([usercustom_tbl.c.id]).where(usercustom_tbl.c.id == trunk.protocolid)
                if op.get_bind().execute(query).scalar():
                    op.execute(
                        trunkfeatures_tbl
                        .update()
                        .where(trunkfeatures_tbl.c.id == trunk.id)
                        .values(endpoint_custom_id=trunk.protocolid)
                    )

    op.drop_column('trunkfeatures', 'protocol')
    op.drop_column('trunkfeatures', 'protocolid')
    op.drop_column('trunkfeatures', 'registerid')


def downgrade():
    op.add_column('trunkfeatures', sa.Column('protocol', trunk_protocol))
    op.add_column('trunkfeatures', sa.Column('protocolid', sa.Integer))
    op.add_column('trunkfeatures', sa.Column('registerid', sa.Integer, nullable=False, server_default='0'))
    op.create_unique_constraint(
        'trunkfeatures_protocol_protocolid_key',
        'trunkfeatures',
        ['protocol', 'protocolid'],
    )

    query = sa.sql.select([
        trunkfeatures_tbl.c.id,
        trunkfeatures_tbl.c.endpoint_sip_id,
        trunkfeatures_tbl.c.endpoint_iax_id,
        trunkfeatures_tbl.c.endpoint_custom_id,
        trunkfeatures_tbl.c.register_sip_id,
        trunkfeatures_tbl.c.register_iax_id,
    ])
    for trunk in op.get_bind().execute(query):
        if trunk.endpoint_sip_id:
            op.execute(
                trunkfeatures_tbl
                .update()
                .where(trunkfeatures_tbl.c.id == trunk.id)
                .values(protocol='sip', protocolid=trunk.endpoint_sip_id)
            )
        elif trunk.endpoint_iax_id:
            op.execute(
                trunkfeatures_tbl
                .update()
                .where(trunkfeatures_tbl.c.id == trunk.id)
                .values(protocol='iax', protocolid=trunk.endpoint_iax_id)
            )
        elif trunk.endpoint_custom_id:
            op.execute(
                trunkfeatures_tbl
                .update()
                .where(trunkfeatures_tbl.c.id == trunk.id)
                .values(protocol='custom', protocolid=trunk.endpoint_custom_id)
            )

        if trunk.register_sip_id:
            op.execute(
                trunkfeatures_tbl
                .update()
                .where(trunkfeatures_tbl.c.id == trunk.id)
                .values(protocol='sip', registerid=trunk.register_sip_id)
            )
        elif trunk.register_iax_id:
            op.execute(
                trunkfeatures_tbl
                .update()
                .where(trunkfeatures_tbl.c.id == trunk.id)
                .values(protocol='iax', registerid=trunk.register_iax_id)
            )

    op.drop_constraint('trunkfeatures_endpoints_check', 'trunkfeatures')
    op.drop_constraint('trunkfeatures_registers_check', 'trunkfeatures')
    op.drop_constraint('trunkfeatures_endpoint_register_check', 'trunkfeatures')
    op.drop_column('trunkfeatures', 'endpoint_sip_id')
    op.drop_column('trunkfeatures', 'endpoint_iax_id')
    op.drop_column('trunkfeatures', 'endpoint_custom_id')
    op.drop_column('trunkfeatures', 'register_sip_id')
    op.drop_column('trunkfeatures', 'register_iax_id')
