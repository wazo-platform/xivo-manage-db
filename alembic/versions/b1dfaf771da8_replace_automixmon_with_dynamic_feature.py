"""replace automixmon with dynamic feature

Revision ID: b1dfaf771da8
Revises: b62e1eba7869

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b1dfaf771da8'
down_revision = 'b62e1eba7869'

features_table = sa.sql.table('features',
                              sa.sql.column('id'),
                              sa.sql.column('filename'),
                              sa.sql.column('category'),
                              sa.sql.column('var_name'),
                              sa.sql.column('var_val'))

func_key_dest_features_table = sa.sql.table('func_key_dest_features',
                                            sa.sql.column('func_key_id'),
                                            sa.sql.column('destination_type_id'),
                                            sa.sql.column('features_id'))


def upgrade():
    feature_id, dtmf = _get_feature_value('featuremap', 'automixmon')
    if dtmf:
        application_map = f'{dtmf},self,AGI(agi://${{XIVO_AGID_IP}}/call_recording)'
        new_feature_id = _insert_feature('applicationmap', 'togglerecord', application_map)
        _move_funckey_dest_feature(feature_id, new_feature_id)
        _remove_feature('featuremap', 'automixmon')


def downgrade():
    feature_id, dtmf = applicationmap_dtmf(*_get_feature_value('applicationmap', 'togglerecord'))
    if dtmf:
        new_feature_id = _insert_feature('featuremap', 'automixmon', dtmf)
        _move_funckey_dest_feature(feature_id, new_feature_id)
        _remove_feature('applicationmap', 'togglerecord')


def applicationmap_dtmf(feature_id, applicationmap_value):
    if not applicationmap_value:
        return feature_id, None
    dtmf = applicationmap_value.split(',', 1)[0]
    return feature_id, dtmf


def _get_feature_value(category, var_name):
    features_query = (
        sa.sql.select(
            [features_table.c.id,
             features_table.c.var_val])
        .where(
            sa.sql.and_(
                features_table.c.category == category,
                features_table.c.var_name == var_name)))
    return op.get_bind().execute(features_query).first()


def _insert_feature(category, var_name, var_val):
    query = (features_table
             .insert()
             .returning(features_table.c.id)
             .values(filename='features.conf',
                     category=category,
                     var_name=var_name,
                     var_val=var_val))

    return op.get_bind().execute(query).scalar()


def _remove_feature(category, var_name):
    query = (features_table
             .delete()
             .where(
                 sa.sql.and_(
                     features_table.c.category == category,
                     features_table.c.var_name == var_name,
                 ),
             ))

    op.execute(query)


def _move_funckey_dest_feature(old_feature_id, new_feature_id):
    query = (func_key_dest_features_table
             .update()
             .values(
                 features_id=new_feature_id
             )
             .where(
                 func_key_dest_features_table.c.features_id == old_feature_id
             ))

    op.execute(query)
