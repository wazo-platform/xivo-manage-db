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

-- Create the __switchboard_directory if it does not exist
DO $$
BEGIN
  IF NOT EXISTS (SELECT 1 FROM "context" WHERE "name" = '__switchboard_directory') THEN
    INSERT INTO "context" VALUES ('__switchboard_directory', 'Switchboard', 'xivo_entity', 'others', 0, '');
  END IF;
END $$;

-- Create a new display if the Switchboard display does not exist
DO $$
BEGIN
  IF NOT EXISTS (SELECT 1 FROM "ctidisplays" WHERE "name" = 'switchboard') THEN
    INSERT INTO "ctidisplays" VALUES (DEFAULT, 'switchboard', '{ "10": [ "", "status", "", ""],"20": [ "Name", "name", "", "{db-firstname} {db-lastname}"],"30": [ "Number", "number_office", "", "{db-phone}"]}', 1, '');
  END IF;
END $$;

-- Assign the display to the __switchboard_context
DO $$
BEGIN
  IF NOT EXISTS (SELECT 1 FROM "cticontexts" WHERE "name" = '__switchboard_directory') THEN
    INSERT INTO "cticontexts" VALUES (DEFAULT, '__switchboard_directory', 'xivodir', 'switchboard', '', 1);
  END IF;
END $$;

COMMIT;
