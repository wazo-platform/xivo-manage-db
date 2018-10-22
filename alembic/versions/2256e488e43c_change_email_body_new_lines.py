"""change email body new lines

Revision ID: 2256e488e43c
Revises: 6545d103068c

"""

from alembic import op

# revision identifiers, used by Alembic.
revision = '2256e488e43c'
down_revision = '6545d103068c'


def upgrade():
    _run(r"""UPDATE staticvoicemail
SET var_val = regexp_replace(staticvoicemail.var_val, E'\n', '\n', 'g')
WHERE var_name = 'emailbody'""")


def downgrade():
    _run(r"""UPDATE staticvoicemail
SET var_val = regexp_replace(staticvoicemail.var_val, '\\n', E'\n', 'g')
WHERE var_name = 'emailbody'""")


def _run(qry):
    conn = op.get_bind()
    conn.execute(qry)
