"""refactor-line-protocol-to-endpoint

Revision ID: e5da3b191742
Revises: 7d91d22133a9v

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e5da3b191742'
down_revision = '7d91d22133a9'

trunk_protocol = sa.Enum(('sip', 'iax', 'sccp', 'custom'), name='trunk_protocol')

linefeatures_tbl = sa.sql.table(
    'linefeatures',
    sa.sql.column('id'),
    sa.sql.column('protocol'),
    sa.sql.column('protocolid'),
    sa.sql.column('endpoint_sip_id'),
    sa.sql.column('endpoint_sccp_id'),
    sa.sql.column('endpoint_custom_id'),
)
usersip_tbl = sa.sql.table('usersip', sa.sql.column('id'))
sccpline_tbl = sa.sql.table('sccpline', sa.sql.column('id'))
usercustom_tbl = sa.sql.table('usercustom', sa.sql.column('id'))


def upgrade():
    op.add_column(
        'linefeatures',
        sa.Column(
            'endpoint_sip_id',
            sa.Integer,
            sa.ForeignKey('usersip.id', ondelete='SET NULL')
        )
    )
    op.add_column(
        'linefeatures',
        sa.Column(
            'endpoint_sccp_id',
            sa.Integer,
            sa.ForeignKey('sccpline.id', ondelete='SET NULL')
        )
    )
    op.add_column(
        'linefeatures',
        sa.Column(
            'endpoint_custom_id',
            sa.Integer,
            sa.ForeignKey('usercustom.id', ondelete='SET NULL')
        )
    )

    op.create_check_constraint(
        'linefeatures_endpoints_check',
        'linefeatures',
        '''
        ( CASE WHEN endpoint_sip_id IS NULL THEN 0 ELSE 1 END
        + CASE WHEN endpoint_sccp_id IS NULL THEN 0 ELSE 1 END
        + CASE WHEN endpoint_custom_id IS NULL THEN 0 ELSE 1 END
        ) <= 1
        ''',
    )
    query = sa.sql.select([
        linefeatures_tbl.c.id,
        linefeatures_tbl.c.protocol,
        linefeatures_tbl.c.protocolid,
    ])
    for line in op.get_bind().execute(query):
        if not line.protocol or not line.protocolid:
            continue

        if line.protocol == 'sip':
            query = sa.sql.select([usersip_tbl.c.id]).where(usersip_tbl.c.id == line.protocolid)
            if op.get_bind().execute(query).scalar():
                op.execute(
                    linefeatures_tbl
                    .update()
                    .where(linefeatures_tbl.c.id == line.id)
                    .values(endpoint_sip_id=line.protocolid)
                )
        elif line.protocol == 'sccp':
            query = sa.sql.select([sccpline_tbl.c.id]).where(sccpline_tbl.c.id == line.protocolid)
            if op.get_bind().execute(query).scalar():
                op.execute(
                    linefeatures_tbl
                    .update()
                    .where(linefeatures_tbl.c.id == line.id)
                    .values(endpoint_sccp_id=line.protocolid)
                )
        elif line.protocol == 'custom':
            query = sa.sql.select([usercustom_tbl.c.id]).where(usercustom_tbl.c.id == line.protocolid)
            if op.get_bind().execute(query).scalar():
                op.execute(
                    linefeatures_tbl
                    .update()
                    .where(linefeatures_tbl.c.id == line.id)
                    .values(endpoint_custom_id=line.protocolid)
                )

    op.drop_column('linefeatures', 'protocol')
    op.drop_column('linefeatures', 'protocolid')


def downgrade():
    op.add_column('linefeatures', sa.Column('protocol', trunk_protocol))
    op.add_column('linefeatures', sa.Column('protocolid', sa.Integer))
    op.create_unique_constraint(
        'linefeatures_protocol_protocolid_key',
        'linefeatures',
        ['protocol', 'protocolid'],
    )

    query = sa.sql.select([
        linefeatures_tbl.c.id,
        linefeatures_tbl.c.endpoint_sip_id,
        linefeatures_tbl.c.endpoint_sccp_id,
        linefeatures_tbl.c.endpoint_custom_id,
    ])
    for line in op.get_bind().execute(query):
        if line.endpoint_sip_id:
            op.execute(
                linefeatures_tbl
                .update()
                .where(linefeatures_tbl.c.id == line.id)
                .values(protocol='sip', protocolid=line.endpoint_sip_id)
            )
        elif line.endpoint_sccp_id:
            op.execute(
                linefeatures_tbl
                .update()
                .where(linefeatures_tbl.c.id == line.id)
                .values(protocol='sccp', protocolid=line.endpoint_sccp_id)
            )
        elif line.endpoint_custom_id:
            op.execute(
                linefeatures_tbl
                .update()
                .where(linefeatures_tbl.c.id == line.id)
                .values(protocol='custom', protocolid=line.endpoint_custom_id)
            )

    op.drop_constraint('linefeatures_endpoints_check', 'linefeatures')
    op.drop_column('linefeatures', 'endpoint_sip_id')
    op.drop_column('linefeatures', 'endpoint_sccp_id')
    op.drop_column('linefeatures', 'endpoint_custom_id')
