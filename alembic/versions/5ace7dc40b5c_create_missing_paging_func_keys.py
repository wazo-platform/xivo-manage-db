"""create_missing_paging_func_keys

Revision ID: 5ace7dc40b5c
Revises: 13692a692d44

"""

from alembic import op
from sqlalchemy import sql

# revision identifiers, used by Alembic.
revision = '5ace7dc40b5c'
down_revision = '13692a692d44'

paging = sql.table('paging',
                   sql.column('id'))

dest_paging = sql.table('func_key_dest_paging',
                        sql.column('func_key_id'),
                        sql.column('paging_id'))

funckey = sql.table('func_key',
                    sql.column('id'),
                    sql.column('type_id'),
                    sql.column('destination_type_id'))

destination_type = sql.table('func_key_destination_type',
                             sql.column('id'),
                             sql.column('name'))

funckey_type = sql.table('func_key_type',
                         sql.column('id'),
                         sql.column('name'))


def upgrade():
    speeddial = (sql.select([funckey_type.c.id])
                 .where(funckey_type.c.name == 'speeddial')
                 ).as_scalar()

    paging_type = (sql.select([destination_type.c.id])
                   .where(destination_type.c.name == 'paging')
                   ).as_scalar()

    create_funckey = (funckey
                      .insert()
                      .values(type_id=speeddial,
                              destination_type_id=paging_type)
                      .returning(funckey.c.id)
                      )

    missing_pagings = (sql.select([paging.c.id])
                       .select_from(
                           paging.outerjoin(dest_paging,
                                            dest_paging.c.paging_id == paging.c.id))
                       .where(
                           dest_paging.c.paging_id == None))

    for row in op.get_bind().execute(missing_pagings):
        func_key_id = op.get_bind().execute(create_funckey).scalar()
        create_paging = (dest_paging
                         .insert()
                         .values(paging_id=row.id,
                                 func_key_id=func_key_id)
                         )
        op.get_bind().execute(create_paging)


def downgrade():
    pass
