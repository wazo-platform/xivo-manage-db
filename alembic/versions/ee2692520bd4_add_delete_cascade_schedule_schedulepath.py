"""add_delete_cascade_schedule_schedulepath.py

Revision ID: ee2692520bd4
Revises: 0d7b3f6ecde3

"""

from alembic import op

# revision identifiers, used by Alembic.
revision = 'ee2692520bd4'
down_revision = '0d7b3f6ecde3'


def upgrade():
    op.drop_constraint("schedule_path_schedule_id_fkey", "schedule_path", type_="foreignkey")
    op.create_foreign_key(
        None,
        "schedule_path",
        "schedule",
        ["schedule_id"],
        ["id"],
        ondelete="CASCADE",
    )
    op.drop_constraint("outcalltrunk_outcallid_fkey", "outcalltrunk", type_="foreignkey")
    op.create_foreign_key(
        None,
        "outcalltrunk",
        "outcall",
        ["outcallid"],
        ["id"],
        ondelete="CASCADE",
    )
    op.drop_constraint("ivr_choice_ivr_id_fkey", "ivr_choice", type_="foreignkey")
    op.create_foreign_key(
        None,
        "ivr_choice",
        "ivr",
        ["ivr_id"],
        ["id"],
        ondelete="CASCADE",
    )
    op.drop_constraint("rightcallexten_rightcallid_fkey", "rightcallexten", type_="foreignkey")
    op.create_foreign_key(
        None,
        "rightcallexten",
        "rightcall",
        ["rightcallid"],
        ["id"],
        ondelete="CASCADE",
    )

def downgrade():
    op.drop_constraint("schedule_path_schedule_id_fkey", "schedule_path", type_="foreignkey")
    op.create_foreign_key(
        None,
        "schedule_path",
        "schedule",
        ["schedule_id"],
        ["id"],
    )
    op.drop_constraint("outcalltrunk_outcallid_fkey", "outcalltrunk", type_="foreignkey")
    op.create_foreign_key(
        None,
        "outcalltrunk",
        "outcall",
        ["outcallid"],
        ["id"],
    )
    op.drop_constraint("ivr_choice_ivr_id_fkey", "ivr_choice", type_="foreignkey")
    op.create_foreign_key(
        None,
        "ivr_choice",
        "ivr",
        ["ivr_id"],
        ["id"],
    )
    op.drop_constraint("rightcallexten_rightcallid_fkey", "rightcallexten", type_="foreignkey")
    op.create_foreign_key(
        None,
        "rightcallexten",
        "rightcall",
        ["rightcallid"],
        ["id"],
    )
