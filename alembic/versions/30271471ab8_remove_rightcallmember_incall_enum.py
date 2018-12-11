"""remove_rightcallmember_incall_enum

Revision ID: 30271471ab8
Revises: e4f459f58795

"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '30271471ab8'
down_revision = 'e4f459f58795'

rightcallmember_type = sa.Enum('user', 'group', 'incall', 'outcall', name='rightcallmember_type')
rightcallmember = sa.sql.table('rightcallmember', sa.Column('type'))


def upgrade():
    op.execute(
        rightcallmember
        .delete()
        .where(rightcallmember.c.type == 'incall')
    )
    op.alter_column('rightcallmember', 'type', type_=sa.String(64))

    op.create_check_constraint(
        'rightcallmember_type_check',
        'rightcallmember',
        sa.sql.column('type').in_([
            'group',
            'outcall',
            'user'
        ])
    )
    rightcallmember_type.drop(op.get_bind(), checkfirst=False)


def downgrade():
    rightcallmember_type.create(op.get_bind())
    op.drop_constraint('rightcallmember_type_check', 'rightcallmember')
    op.execute('ALTER TABLE rightcallmember ALTER COLUMN type TYPE rightcallmember_type USING type::text::rightcallmember_type')
