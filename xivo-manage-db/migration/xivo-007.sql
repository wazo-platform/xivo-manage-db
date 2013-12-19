/*
 * Copyright (C) 2013  Avencall
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

CREATE OR REPLACE LANGUAGE plpythonu;

CREATE OR REPLACE FUNCTION create_move_acl_script() RETURNS void AS $$

import os

script = '''\
<?php

$acl = unserialize($argv[1]);


if (isset($acl["acl"]["service"]["cti"]["control_system"]["restart"])
   && $acl["acl"]["service"]["cti"]["control_system"]["restart"] == 1) {

    $acl["acl"]["service"]["ipbx"]["control_system"]["cti_restart"] = 1;

    unset($acl["acl"]["service"]["cti"]["control_system"]["restart"]);
    if (empty($acl["acl"]["service"]["cti"]["control_system"]["restart"]))
        unset($acl["acl"]["service"]["cti"]["control_system"]);
    if (empty($acl["acl"]["service"]["cti"]["control_system"]))
        unset($acl["acl"]["service"]["cti"]);

}

$raw_acl = serialize($acl);
print $raw_acl . "\n";

?>
'''

filename = '/tmp/migrate_acl.php'

if os.path.exists(filename):
    os.remove(filename)

with open(filename, 'w') as script_file:
     script_file.write(script)

$$ LANGUAGE plpythonu;

CREATE OR REPLACE FUNCTION move_cti_restart_acl(raw_acl text) RETURNS text AS $$

import subprocess

command = ['/usr/bin/php', '/tmp/migrate_acl.php', raw_acl]
p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
new_acl = p.communicate()

return new_acl[0].strip()

$$ LANGUAGE plpythonu;

SELECT "create_move_acl_script"();
UPDATE "user" SET "obj" = "move_cti_restart_acl"("obj") WHERE "obj" <> '';

DROP FUNCTION IF EXISTS "move_cti_restart_acl"(text);
DROP FUNCTION IF EXISTS "create_move_acl_script"();

COMMIT;
