"""remove custom moh directory

Revision ID: 3196befc4753
Revises: 6bfd932df2c
XiVO Version: <version>

"""

# revision identifiers, used by Alembic.
revision = '3196befc4753'
down_revision = '6bfd932df2c'

from alembic import op
from sqlalchemy import sql

musiconhold = sql.table('musiconhold',
                        sql.column('id'),
                        sql.column('category'),
                        sql.column('var_name'),
                        sql.column('var_val'),
                        sql.column('filename'))


def upgrade():
    custom_moh_query = sql.select(
        [musiconhold.c.category]
    ).where(
        sql.and_(
            musiconhold.c.var_name == 'mode',
            musiconhold.c.var_val == 'custom'
        ))

    query = (musiconhold.delete()
             .where(
                 sql.and_(
                     musiconhold.c.var_name == 'directory',
                     musiconhold.c.category.in_(custom_moh_query))))

    op.execute(query)


def downgrade():
    directory_query = sql.select(
        [musiconhold.c.category.label('category'),
         sql.literal_column("'directory'").label('var_name'),
         sql.literal_column("'/var/lib/xivo/moh/' || category").label('var_val'),
         sql.literal_column("'musiconhold.conf'").label('filename')]
    ).where(
        sql.and_(
            musiconhold.c.var_name == 'mode',
            musiconhold.c.var_val == 'custom'))

    query = (musiconhold
             .insert()
             .returning(musiconhold.c.id)
             .from_select(
                 [musiconhold.c.category,
                  musiconhold.c.var_name,
                  musiconhold.c.var_val,
                  musiconhold.c.filename],
                 directory_query))

    op.execute(query)
