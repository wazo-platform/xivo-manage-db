"""remove_invalid_user_email

Revision ID: 27040433c098
Revises: 1747774cead4

"""

import re

from alembic import op
from sqlalchemy import sql

# revision identifiers, used by Alembic.
revision = '27040433c098'
down_revision = '1747774cead4'


userfeatures = sql.table(
    'userfeatures',
    sql.column('id'),
    sql.column('email'),
)

# the following code is copy/paste from python-marshmallow Email validator
USER_REGEX = re.compile(
    r"(^[-!#$%&'*+/=?^`{}|~\w]+(\.[-!#$%&'*+/=?^`{}|~\w]+)*$"  # dot-atom
    # quoted-string
    r'|^"([\001-\010\013\014\016-\037!#-\[\]-\177]'
    r'|\\[\001-\011\013\014\016-\177])*"$)', re.IGNORECASE | re.UNICODE
)

DOMAIN_REGEX = re.compile(
    # domain
    r'(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+'
    r'(?:[A-Z]{2,6}|[A-Z0-9-]{2,})$'
    # literal form, ipv4 address (SMTP 4.1.3)
    r'|^\[(25[0-5]|2[0-4]\d|[0-1]?\d?\d)'
    r'(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}\]$', re.IGNORECASE | re.UNICODE
)

DOMAIN_WHITELIST = ('localhost',)


def _list_users():
    query = sql.select([userfeatures.c.id, userfeatures.c.email])
    return op.get_bind().execute(query).fetchall()


def _remove_user_email(user_id):
    query = userfeatures.update().where(userfeatures.c.id == user_id).values(email=None)
    return op.execute(query)


def _is_valid_email(email):
    if not email or '@' not in email:
        return False

    user_part, domain_part = email.rsplit('@', 1)

    if not USER_REGEX.match(user_part):
        return False

    if domain_part in DOMAIN_WHITELIST:
        return True

    if not DOMAIN_REGEX.match(domain_part):
        return False

    return True


def upgrade():
    users = _list_users()
    for user in users:
        if user.email and not _is_valid_email(user.email):
            _remove_user_email(user.id)


def downgrade():
    pass
