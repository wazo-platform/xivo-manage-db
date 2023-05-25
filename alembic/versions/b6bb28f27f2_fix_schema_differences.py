"""fix schema differences

Revision ID: b6bb28f27f2
Revises: 27f83f39e031

"""

# revision identifiers, used by Alembic.
revision = 'b6bb28f27f2'
down_revision = '27f83f39e031'

from alembic import op


def drop_constraint(constraint, table):
    op.execute(f'ALTER TABLE {table} DROP CONSTRAINT IF EXISTS {constraint}')


def upgrade():
    drop_constraint('fk_entity_id', 'callfilter')
    drop_constraint('callfilter_entity_id_fkey', 'callfilter')
    op.create_foreign_key('callfilter_entity_id_fkey', 'callfilter',
                          'entity', ['entity_id'], ['id'],
                          ondelete='RESTRICT')

    drop_constraint('pickup_entity_id_fkey', 'pickup')
    op.create_foreign_key('pickup_entity_id_fkey', 'pickup',
                          'entity', ['entity_id'], ['id'],
                          ondelete='RESTRICT')

    drop_constraint('schedule_entity_id_fkey', 'schedule')
    op.create_foreign_key('schedule_entity_id_fkey', 'schedule',
                          'entity', ['entity_id'], ['id'],
                          ondelete='RESTRICT')

    drop_constraint('userfeatures_entity_id_fkey', 'userfeatures')
    drop_constraint('userfeatures_entityid_fkey', 'userfeatures')
    op.create_foreign_key('userfeatures_entityid_fkey', 'userfeatures',
                          'entity', ['entityid'], ['id'],
                          ondelete='RESTRICT')

    drop_constraint('fk_user_id', 'user_contact')
    drop_constraint('user_contact_user_id_fkey', 'user_contact')
    op.create_foreign_key('user_contact_user_id_fkey', 'user_contact',
                          'userfeatures', ['user_id'], ['id'],
                          ondelete='CASCADE')

    drop_constraint('fk_phonebook_id', 'user_contact')
    drop_constraint('user_contact_phonebook_id_fkey', 'user_contact')
    op.create_foreign_key('user_contact_phonebook_id_fkey', 'user_contact',
                          'phonebook', ['phonebook_id'], ['id'],
                          ondelete='CASCADE')

    drop_constraint('fk_phonebook_id', 'phonebooknumber')
    drop_constraint('phonebooknumber_phonebookid_fkey', 'phonebooknumber')
    op.create_foreign_key('phonebooknumber_phonebookid_fkey', 'phonebooknumber',
                          'phonebook', ['phonebookid'], ['id'],
                          ondelete='CASCADE')

    drop_constraint('fk_phonebook_id', 'phonebookaddress')
    drop_constraint('phonebookaddress_phonebookid_fkey', 'phonebookaddress')
    op.create_foreign_key('phonebookaddress_phonebookid_fkey', 'phonebookaddress',
                          'phonebook', ['phonebookid'], ['id'],
                          ondelete='CASCADE')


def downgrade():
    drop_constraint('fk_entity_id', 'callfilter')
    drop_constraint('callfilter_entity_id_fkey', 'callfilter')
    op.create_foreign_key('fk_entity_id', 'callfilter',
                          'entity', ['entity_id'], ['id'])

    drop_constraint('pickup_entity_id_fkey', 'pickup')
    op.create_foreign_key('pickup_entity_id_fkey', 'pickup',
                          'entity', ['entity_id'], ['id'])

    drop_constraint('schedule_entity_id_fkey', 'schedule')
    op.create_foreign_key('schedule_entity_id_fkey', 'schedule',
                          'entity', ['entity_id'], ['id'])

    drop_constraint('userfeatures_entity_id_fkey', 'userfeatures')
    drop_constraint('userfeatures_entityid_fkey', 'userfeatures')
    op.create_foreign_key('userfeatures_entityid_fkey', 'userfeatures',
                          'entity', ['entityid'], ['id'])

    drop_constraint('fk_user_id', 'user_contact')
    drop_constraint('user_contact_user_id_fkey', 'user_contact')
    op.create_foreign_key('fk_user_id', 'user_contact',
                          'userfeatures', ['user_id'], ['id'],
                          ondelete='CASCADE')

    drop_constraint('fk_phonebook_id', 'user_contact')
    drop_constraint('user_contact_phonebook_id_fkey', 'user_contact')
    op.create_foreign_key('fk_phonebook_id', 'user_contact',
                          'phonebook', ['phonebook_id'], ['id'],
                          ondelete='CASCADE')

    drop_constraint('fk_phonebook_id', 'phonebooknumber')
    drop_constraint('phonebooknumber_phonebookid_fkey', 'phonebooknumber')
    op.create_foreign_key('fk_phonebook_id', 'phonebooknumber',
                          'phonebook', ['phonebookid'], ['id'],
                          ondelete='CASCADE')

    drop_constraint('fk_phonebook_id', 'phonebookaddress')
    drop_constraint('phonebookaddress_phonebookid_fkey', 'phonebookaddress')
    op.create_foreign_key('fk_phonebook_id', 'phonebookaddress',
                          'phonebook', ['phonebookid'], ['id'],
                          ondelete='CASCADE')
