INSERT INTO "entity" (name, displayname, description) VALUES ('xivotest', 'xivotest', '');

INSERT INTO "accesswebservice" (name, login, passwd, description) VALUES ('admin', 'admin', 'proformatique', '');

INSERT INTO "context" (name, displayname, contexttype, description, entity) 
VALUES 
('default', 'Default', 'internal', '', 'xivotest'),
('from-extern', 'Incalls', 'incall', '', 'xivotest'),
('to-extern', 'Outcalls', 'incall', '', 'xivotest');

INSERT INTO "contextinclude" (context, include) VALUES ('default', 'to-extern');

INSERT INTO "contextnumbers" (context, type, numberbeg, numberend, didlength)
VALUES
('default', 'user', '1000', '1999', 0),
('default', 'group', '2000', '2999', 0),
('default', 'queue', '3000', '3999', 0),
('default', 'meetme', '4000', '4999', 0),
('from-extern', 'incall', '1000', '9999', 0);

INSERT INTO "netiface" (ifname, networktype, type, family, options) VALUES ('eth0', 'voip', 'iface', 'inet', '');

UPDATE provisioning set net4_ip_rest='provd';

ALTER ROLE asterisk WITH SUPERUSER;
