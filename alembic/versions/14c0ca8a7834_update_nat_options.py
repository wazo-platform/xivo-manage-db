"""update_nat_options

Revision ID: 14c0ca8a7834
Revises: 57461905b7e6

"""

# revision identifiers, used by Alembic.
revision = '14c0ca8a7834'
down_revision = '57461905b7e6'

from alembic import op


def upgrade():
    qry ="""
    ALTER TYPE "usersip_nat" RENAME TO "usersip_nat_old";
    CREATE TYPE "usersip_nat" as enum ('no', 'force_rport', 'comedia', 'force_rport,comedia', 'auto_force_rport','auto_comedia');
    ALTER TABLE "usersip" RENAME COLUMN "nat" to "nat_old";
    ALTER TABLE "usersip" ADD COLUMN "nat" usersip_nat;
    UPDATE "usersip" SET "nat" = 'auto_force_rport' WHERE "nat_old" = 'no';
    ALTER TABLE "usersip" DROP COLUMN "nat_old";
    DROP TYPE "usersip_nat_old";
    """
    op.execute(qry)


def downgrade():
    qry ="""
    ALTER TYPE "usersip_nat" RENAME TO "usersip_nat_old";
    CREATE TYPE "usersip_nat" as enum ('no', 'force_rport', 'comedia', 'force_rport,comedia');
    ALTER TABLE "usersip" RENAME COLUMN "nat" to "nat_old";
    ALTER TABLE "usersip" ADD COLUMN "nat" usersip_nat;
    UPDATE "usersip" SET "nat" = 'no' WHERE "nat_old" = 'auto_force_rport';
    ALTER TABLE "usersip" DROP COLUMN "nat_old";
    DROP TYPE "usersip_nat_old";
    """
    op.execute(qry)
