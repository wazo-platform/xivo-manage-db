"""add_email_field_in_phonebook

Revision ID: 537774d3845a
Revises: 498f0570ffef

"""

# revision identifiers, used by Alembic.
revision = '537774d3845a'
down_revision = '498f0570ffef'

from alembic import op
from sqlalchemy import sql, and_


directories = sql.table('ctidirectories',
                        sql.column('id'),
                        sql.column('name'))
directory_fields = sql.table('ctidirectoryfields',
                             sql.column('dir_id'),
                             sql.column('fieldname'),
                             sql.column('value'))


def upgrade():
    _add_directory_field('xivodir', 'email', '{phonebook.email}')


def _add_directory_field(directory_name, field_name, value):
    directory_id = _get_directory_id(directory_name)
    if not directory_id:
        return

    if not _have_directory_field(directory_id, field_name):
        _insert_directory_field(directory_id, field_name, value)


def _get_directory_id(directory_name):
    row = op.get_bind().execute(sql.select([directories.c.id])
                                .where(directories.c.name == directory_name)).first()
    return row.id if row else None


def _have_directory_field(directory_id, field_name):
    row = op.get_bind().execute(sql.select([directory_fields.c.dir_id])
                                .where(and_(directory_fields.c.dir_id == directory_id,
                                            directory_fields.c.fieldname == field_name))).first()
    return bool(row)


def _insert_directory_field(directory_id, field_name, value):
    op.execute(directory_fields
               .insert()
               .values(dir_id=directory_id,
                       fieldname=field_name,
                       value=value))


def downgrade():
    pass
