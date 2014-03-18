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

ALTER TABLE ONLY dialaction
    DROP CONSTRAINT IF EXISTS dialaction_pkey;

ALTER TABLE ONLY dialaction
    ADD CONSTRAINT dialaction_pkey PRIMARY KEY (event, category, categoryval);

DROP INDEX IF EXISTS phonefunckey__idx__typeextenumbersright_typevalextenumbersright;

CREATE INDEX phonefunckey__idx__typeextenumbersright_typevalextenumbersright ON phonefunckey 
    USING btree (typeextenumbersright, typevalextenumbersright);

ALTER TABLE cel ALTER COLUMN appdata TYPE varchar(512);

ALTER TABLE dialaction
    ALTER COLUMN event SET NOT NULL;

ALTER TABLE "general"
    ALTER COLUMN exchange_exten SET DEFAULT NULL::character varying;

ALTER TABLE linefeatures
    ALTER COLUMN protocol SET NOT NULL;

ALTER TABLE trunkfeatures
    ALTER COLUMN protocol SET NOT NULL;

ALTER TABLE usercustom
    ALTER COLUMN protocol SET DEFAULT 'custom',
    ALTER COLUMN protocol SET NOT NULL;

ALTER TABLE useriax
    ALTER COLUMN type SET NOT NULL,
    ALTER COLUMN protocol SET DEFAULT 'iax',
    ALTER COLUMN protocol SET NOT NULL;

ALTER TABLE usersip
    ALTER COLUMN type SET NOT NULL,
    ALTER COLUMN protocol SET DEFAULT 'sip',
    ALTER COLUMN protocol SET NOT NULL;

COMMIT;
