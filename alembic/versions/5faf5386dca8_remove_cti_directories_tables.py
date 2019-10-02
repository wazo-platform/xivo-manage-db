"""remove cti directories tables

Revision ID: 5faf5386dca8
Revises: 4d80d8106d1e

"""

# revision identifiers, used by Alembic.
revision = '5faf5386dca8'
down_revision = '4d80d8106d1e'


from alembic import op
import sqlalchemy as sa

ldapserver_securitylayer = sa.Enum('tls', 'ssl', name='ldapserver_securitylayer')
ldapserver_protocolversion = sa.Enum('2', '3', name='ldapserver_protocolversion')


def upgrade():
    op.drop_table('ctidisplays')
    op.drop_table('cticontexts')
    op.drop_table('ctidirectoryfields')
    op.drop_table('ctidirectories')
    op.drop_table('ctireversedirectories')
    op.drop_table('directories')
    op.drop_table('ldapfilter')
    op.drop_table('ldapserver')
    ldapserver_securitylayer.drop(op.get_bind())
    ldapserver_protocolversion.drop(op.get_bind())


def downgrade():
    op.create_table(
        'ldapserver',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(64)),
        sa.Column('host', sa.String(255), nullable=False),
        sa.Column('port', sa.Integer, nullable=False),
        sa.Column('securitylayer', ldapserver_securitylayer),
        sa.Column('protocolversion', ldapserver_protocolversion, nullable=False, default=3),
        sa.Column('disable', sa.Integer, nullable=False, default=0),
        sa.Column('dcreate', sa.Integer, nullable=False, default=0),
        sa.Column('description', sa.Text),
    )
    op.create_table(
        'ldapfilter',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('ldapserverid', sa.Integer, nullable=False),
        sa.Column('name', sa.String(128)),
        sa.Column('user', sa.String(255)),
        sa.Column('passwd', sa.String(255)),
        sa.Column('basedn', sa.String(255), nullable=False),
        sa.Column('filter', sa.String(255), nullable=False),
        sa.Column('commented', sa.Integer, nullable=False, default=0),
        sa.Column('description', sa.Text),
    )
    op.create_table(
        'directories',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('uri', sa.String(255)),
        sa.Column('dirtype', sa.String(20), nullable=False),
        sa.Column('name', sa.String(255)),
        sa.Column('description', sa.Text),
        sa.Column('xivo_username', sa.Text),
        sa.Column('xivo_password', sa.Text),
        sa.Column('xivo_verify_certificate', sa.Boolean, nullable=False, default=False),
        sa.Column('xivo_custom_ca_path', sa.Text),
        sa.Column('dird_tenant', sa.Text),
        sa.Column('dird_phonebook', sa.Text),
        sa.Column('auth_host', sa.Text),
        sa.Column('auth_port', sa.Integer),
        sa.Column('auth_backend', sa.Text),
        sa.Column('auth_verify_certificate', sa.Boolean, nullable=False, default=False),
        sa.Column('auth_custom_ca_path', sa.Text),
        sa.Column('ldapfilter_id', sa.Integer, sa.ForeignKey('ldapfilter.id', ondelete='CASCADE')),
        sa.Column('auth_key_file', sa.Text),
    )
    op.create_table(
        'ctidirectoryfields',
        sa.Column('dir_id', sa.Integer, nullable=False),
        sa.Column('fieldname', sa.String(255), nullable=False),
        sa.Column('value', sa.String(255)),
    )
    op.create_table(
        'ctidirectories',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(255)),
        sa.Column('delimiter', sa.String(20)),
        sa.Column('match_direct', sa.Text, nullable=False),
        sa.Column('match_reverse', sa.Text, nullable=False),
        sa.Column('description', sa.String(255)),
        sa.Column('deletable', sa.Integer),
        sa.Column('directory_id', sa.Integer, sa.ForeignKey('directories.id', ondelete='CASCADE')),
    )
    op.create_table(
        'ctireversedirectories',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('directories', sa.Text),
    )
    op.create_table(
        'cticontexts',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50)),
        sa.Column('directories', sa.Text, nullable=False),
        sa.Column('display', sa.Text, nullable=False),
        sa.Column('deletable', sa.Integer),
        sa.Column('description', sa.Text),
    )
    op.create_table(
        'ctidisplays',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50)),
        sa.Column('data', sa.Text, nullable=False),
        sa.Column('deletable', sa.Integer),
        sa.Column('description', sa.Text),
    )
