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

CREATE OR REPLACE VIEW "user_line" AS
    SELECT
        "id",
        "iduserfeatures" AS "user_id",
        "id" AS "line_id",
        true AS "main_user"
    FROM "linefeatures"
    WHERE "iduserfeatures" <> 0;

GRANT ALL ON TABLE "user_line" TO asterisk;

COMMIT;
