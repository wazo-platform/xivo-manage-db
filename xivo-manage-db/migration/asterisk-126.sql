/*
 * Copyright (C) 2013-2014  Avencall
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

BEGIN;

UPDATE "staticsip" SET "var_val" = 'force_rport,comedia' WHERE "var_name" = 'nat' and "var_val" = 'yes';

/* Prepare migration */
ALTER TYPE "usersip_nat" RENAME TO "usersip_nat_old";
CREATE TYPE "usersip_nat" as enum ('no','force_rport','comedia','force_rport,comedia');
ALTER TABLE "usersip" RENAME COLUMN "nat" to "nat_old";
ALTER TABLE "usersip" ADD COLUMN "nat" usersip_nat;

/* Copy data to new type */
UPDATE "usersip" SET "nat" = 'force_rport,comedia' WHERE "nat_old" = 'yes';
UPDATE "usersip" SET "nat" = nat_old::text::usersip_nat WHERE "nat_old" <> 'yes';

/* Clean unused objects */
ALTER TABLE "usersip" DROP COLUMN "nat_old";
DROP TYPE "usersip_nat_old";

COMMIT;
