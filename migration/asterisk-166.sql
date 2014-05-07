/*
 * Copyright (C) 2014  Avencall
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

DROP TABLE IF EXISTS "operator" CASCADE;
DROP TABLE IF EXISTS "operator_destination" CASCADE;
DROP TABLE IF EXISTS "operator_trunk" CASCADE;
DROP TABLE IF EXISTS "outcalldundipeer" CASCADE;
DROP TABLE IF EXISTS "parkinglot" CASCADE;
DROP TABLE IF EXISTS "voicemenu" CASCADE;


ALTER TABLE "accessfeatures" RENAME COLUMN "feature" to "feature_old";
ALTER TABLE "accessfeatures" ADD COLUMN "feature" VARCHAR(64) DEFAULT 'phonebook' NOT NULL CHECK("feature"='phonebook');
ALTER TABLE "accessfeatures" DROP COLUMN "feature_old";
DROP TYPE IF EXISTS "accessfeatures_feature";
ALTER TABLE "accessfeatures" ADD CONSTRAINT "accessfeatures_host_feature_key" UNIQUE ("host", "feature");


ALTER TABLE "serverfeatures" RENAME COLUMN "feature" to "feature_old";
ALTER TABLE "serverfeatures" ADD COLUMN "feature" VARCHAR(64) DEFAULT 'phonebook' NOT NULL CHECK("feature"='phonebook');
ALTER TABLE "serverfeatures" DROP COLUMN "feature_old";
DROP TYPE IF EXISTS "serverfeatures_feature";


ALTER TABLE "trunkfeatures" ALTER "description" DROP NOT NULL;

COMMIT;
