"""directories: migration xivo directory

Revision ID: b8f8ba046d25
Revises: c22356e22a13

"""

# revision identifiers, used by Alembic.
revision = 'b8f8ba046d25'
down_revision = 'c22356e22a13'

from alembic import op
from sqlalchemy import sql, and_

directories = sql.table(
    'directories',
    sql.column('id'),
    sql.column('name'),
    sql.column('uri'),
    sql.column('dirtype'),
    sql.column('description'),
    sql.column('xivo_username'),
    sql.column('xivo_password'),
    sql.column('xivo_verify_certificate'),
    sql.column('xivo_custom_ca_path'),
    sql.column('auth_backend'),
    sql.column('auth_host'),
    sql.column('auth_port'),
    sql.column('auth_verify_certificate'),
    sql.column('auth_custom_ca_path'),
)
webservice = sql.table(
    'accesswebservice',
    sql.column('login'),
    sql.column('passwd'),
)
old_uri = 'http://localhost:9487'
new_uri = 'https://localhost:9486'
username = 'wazo-dird-xivo-backend'
default_ca_path = '/usr/share/xivo-certs/server.crt'
dirtype = 'xivo'

def find_ws_password(conn, username):
    password = None
    query = sql.select([webservice.c.passwd]).where(webservice.c.login == username)
    for row in conn.execute(query):
        password = row.passwd

    if not password:
        raise Exception(f'failed to find a password for user {username}')

    return password


def upgrade():
    password = find_ws_password(op.get_bind(), username)
    op.execute(directories.update().values(
        uri=new_uri,
        xivo_username=username,
        xivo_password=password,
        xivo_verify_certificate=True,
        xivo_custom_ca_path=default_ca_path,
        auth_backend='xivo_service',
        auth_host='localhost',
        auth_port=9497,
        auth_verify_certificate=True,
        auth_custom_ca_path=default_ca_path,
    ).where(and_(directories.c.dirtype == dirtype, directories.c.uri == old_uri)))


def downgrade():
    op.execute(directories.update().values(
        uri=old_uri,
        xivo_username=None,
        xivo_password=None,
        xivo_verify_certificate=False,
        xivo_custom_ca_path=None,
        auth_backend=None,
        auth_host=None,
        auth_port=None,
        auth_verify_certificate=False,
        auth_custom_ca_path=None,
    ).where(and_(directories.c.dirtype == dirtype, directories.c.uri == new_uri)))
