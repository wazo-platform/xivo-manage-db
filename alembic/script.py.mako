"""${message}

Revision ID: ${up_revision}
Revises: ${down_revision}

"""

from alembic import op
import sqlalchemy as sa
${imports if imports else ""}

# revision identifiers, used by Alembic.
revision = ${repr(up_revision)}
down_revision = ${repr(down_revision)}

<%
    kwargs = {}
    if config.cmd_opts.x:
        kwargs = dict(arg.split('=', 1) for arg in config.cmd_opts.x)
%>
def upgrade():
% if kwargs.get('wazo_version'):
    infos = sa.sql.table('infos', sa.sql.column('wazo_version'))
    op.execute(infos.update().values(wazo_version='${kwargs['wazo_version']}'))
% else:
    ${upgrades if upgrades else "pass"}
% endif


def downgrade():
    ${downgrades if downgrades else "pass"}
