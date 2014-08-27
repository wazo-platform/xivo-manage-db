"""add directmedia outgoing option

Revision ID: 379d2e0c5e51
Revises: 50cfb10bd01d
XiVO Version: <version>

"""

revision = '379d2e0c5e51'
down_revision = '50cfb10bd01d'


from alembic import op
import sqlalchemy as sa
from sqlalchemy.types import VARCHAR

old_options = ('no', 'yes', 'nonat', 'update', 'update,nonat')

old_type = sa.Enum(*old_options, name='usersip_directmedia')

usersip_table = sa.sql.table('usersip',
                             sa.Column('directmedia', old_type, nullable=False))

staticsip_table = sa.sql.table('staticsip',
                               sa.Column('var_name', VARCHAR(128), nullable=False),
                               sa.Column('var_val', VARCHAR(255)))


def upgrade():
    qry = """
    ALTER TABLE usersip
    ALTER COLUMN directmedia TYPE varchar(20);
    """
    op.execute(qry)

    qry = """
    ALTER TABLE usersip
    ADD CONSTRAINT usersip_directmedia
    CHECK ( directmedia IN
        ('no', 'yes', 'nonat', 'update', 'update,nonat', 'outgoing')
    );
    """
    op.execute(qry)

    old_type.drop(op.get_bind(), checkfirst=False)


def downgrade():
    op.execute(usersip_table.update().
               where(usersip_table.c.directmedia == u'outgoing').
               values(directmedia='no'))

    op.execute(staticsip_table.update().
               where(sa.sql.and_(
                   staticsip_table.c.var_name == u'directmedia',
                   staticsip_table.c.var_val == u'outgoing')).
               values(var_val='no'))

    qry = """
    ALTER TABLE usersip
    DROP CONSTRAINT usersip_directmedia;
    """
    op.execute(qry)

    old_type.create(op.get_bind(), checkfirst=False)

    qry = """
    ALTER TABLE usersip
    ALTER COLUMN directmedia
    TYPE usersip_directmedia
    USING (directmedia::usersip_directmedia);
    """
    op.execute(qry)
