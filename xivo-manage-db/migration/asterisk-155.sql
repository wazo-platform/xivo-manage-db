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

CREATE OR REPLACE FUNCTION protocol_context(protocol trunk_protocol, protocolid integer)
  RETURNS SETOF varchar AS
$body$
BEGIN

RETURN QUERY EXECUTE 'SELECT "context" FROM user' || protocol || ' WHERE "id" = ' || protocolid;

END;
$body$
  LANGUAGE plpgsql STABLE;

UPDATE "linefeatures" 
SET "context" = protocol_context("protocol", "protocolid")
WHERE "context" is NULL;


DROP FUNCTION protocol_context(protocol trunk_protocol, protocolid integer);

COMMIT;
