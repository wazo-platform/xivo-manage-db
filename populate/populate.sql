BEGIN;

INSERT INTO "contexttype" VALUES(DEFAULT, 'internal', 0, 0, '');
INSERT INTO "contexttype" VALUES(DEFAULT, 'incall', 0, 0, '');
INSERT INTO "contexttype" VALUES(DEFAULT, 'outcall', 0, 0, '');
INSERT INTO "contexttype" VALUES(DEFAULT, 'services', 0, 0, '');
INSERT INTO "contexttype" VALUES(DEFAULT, 'others', 0, 0, '');


INSERT INTO "feature_extension" (enabled, exten, feature) VALUES (true,'_*31.','agentstaticlogin');
INSERT INTO "feature_extension" (enabled, exten, feature) VALUES (true,'_*32.','agentstaticlogoff');
INSERT INTO "feature_extension" (enabled, exten, feature) VALUES (true,'_*30.','agentstaticlogtoggle');
INSERT INTO "feature_extension" (enabled, exten, feature) VALUES (true,'_*37.','bsfilter');
INSERT INTO "feature_extension" (enabled, exten, feature) VALUES (false,'*34','calllistening');
INSERT INTO "feature_extension" (enabled, exten, feature) VALUES (false,'*26','callrecord');
INSERT INTO "feature_extension" (enabled, exten, feature) VALUES (true,'*36','directoryaccess');
INSERT INTO "feature_extension" (enabled, exten, feature) VALUES (true,'*25','enablednd');
INSERT INTO "feature_extension" (enabled, exten, feature) VALUES (true,'*90','enablevm');
INSERT INTO "feature_extension" (enabled, exten, feature) VALUES (true,'_*90.','enablevmslt');
INSERT INTO "feature_extension" (enabled, exten, feature) VALUES (true,'_*23.','fwdbusy');
INSERT INTO "feature_extension" (enabled, exten, feature) VALUES (true,'_*22.','fwdrna');
INSERT INTO "feature_extension" (enabled, exten, feature) VALUES (true,'_*21.','fwdunc');
INSERT INTO "feature_extension" (enabled, exten, feature) VALUES (true,'*20','fwdundoall');
INSERT INTO "feature_extension" (enabled, exten, feature) VALUES (true,'*48378','autoprov');
INSERT INTO "feature_extension" (enabled, exten, feature) VALUES (true,'*27','incallfilter');
INSERT INTO "feature_extension" (enabled, exten, feature) VALUES (true,'*10','phonestatus');
INSERT INTO "feature_extension" (enabled, exten, feature) VALUES (true,'_*735.','phoneprogfunckey');
INSERT INTO "feature_extension" (enabled, exten, feature) VALUES (false,'_*8.','pickup');
INSERT INTO "feature_extension" (enabled, exten, feature) VALUES (true,'*9','recsnd');
INSERT INTO "feature_extension" (enabled, exten, feature) VALUES (true,'_*99.','vmboxmsgslt');
INSERT INTO "feature_extension" (enabled, exten, feature) VALUES (false,'_*93.','vmboxpurgeslt');
INSERT INTO "feature_extension" (enabled, exten, feature) VALUES (true,'_*97.','vmboxslt');
INSERT INTO "feature_extension" (enabled, exten, feature) VALUES (true,'*98','vmusermsg');
INSERT INTO "feature_extension" (enabled, exten, feature) VALUES (false,'*92','vmuserpurge');
INSERT INTO "feature_extension" (enabled, exten, feature) VALUES (false,'_*92.','vmuserpurgeslt');
INSERT INTO "feature_extension" (enabled, exten, feature) VALUES (true,'_*96.','vmuserslt');
INSERT INTO "feature_extension" (enabled, exten, feature) VALUES (true,'_*11.','paging');
INSERT INTO "feature_extension" (enabled, exten, feature) VALUES (true,'*40','cctoggle');
INSERT INTO "feature_extension" (enabled, exten, feature) VALUES (true,'_*41.','meetingjoin');
INSERT INTO "feature_extension" (enabled, exten, feature) VALUES (true,'_*50.','groupmembertoggle');
INSERT INTO "feature_extension" (enabled, exten, feature) VALUES (true,'_*51.','groupmemberjoin');
INSERT INTO "feature_extension" (enabled, exten, feature) VALUES (true,'_*52.','groupmemberleave');


INSERT INTO "features" VALUES (DEFAULT,0,0,0,'features.conf','general','parkext','700');
INSERT INTO "features" VALUES (DEFAULT,0,0,0,'features.conf','general','parkpos','701-750');
INSERT INTO "features" VALUES (DEFAULT,0,0,0,'features.conf','general','context','parkedcalls');
INSERT INTO "features" VALUES (DEFAULT,0,0,0,'features.conf','general','parkinghints','no');
INSERT INTO "features" VALUES (DEFAULT,0,0,0,'features.conf','general','parkingtime','45');
INSERT INTO "features" VALUES (DEFAULT,0,0,0,'features.conf','general','comebacktoorigin','yes');
INSERT INTO "features" VALUES (DEFAULT,0,0,1,'features.conf','general','courtesytone',NULL);
INSERT INTO "features" VALUES (DEFAULT,0,0,0,'features.conf','general','parkedplay','caller');
INSERT INTO "features" VALUES (DEFAULT,0,0,0,'features.conf','general','parkedcalltransfers','no');
INSERT INTO "features" VALUES (DEFAULT,0,0,0,'features.conf','general','parkedcallreparking','no');
INSERT INTO "features" VALUES (DEFAULT,0,0,0,'features.conf','general','parkedcallhangup','no');
INSERT INTO "features" VALUES (DEFAULT,0,0,0,'features.conf','general','parkedcallrecording','no');
INSERT INTO "features" VALUES (DEFAULT,0,0,0,'features.conf','general','parkeddynamic','no');
INSERT INTO "features" VALUES (DEFAULT,0,0,0,'features.conf','general','findslot','next');
INSERT INTO "features" VALUES (DEFAULT,0,0,0,'features.conf','general','parkedmusicclass','default');
INSERT INTO "features" VALUES (DEFAULT,0,0,0,'features.conf','general','transferdigittimeout','5');
INSERT INTO "features" VALUES (DEFAULT,0,0,1,'features.conf','general','xfersound',NULL);
INSERT INTO "features" VALUES (DEFAULT,0,0,1,'features.conf','general','xferfailsound',NULL);
INSERT INTO "features" VALUES (DEFAULT,0,0,0,'features.conf','general','pickupexten','*8');
INSERT INTO "features" VALUES (DEFAULT,0,0,0,'features.conf','general','featuredigittimeout','1500');
INSERT INTO "features" VALUES (DEFAULT,0,0,0,'features.conf','general','atxfernoanswertimeout','15');
INSERT INTO "features" VALUES (DEFAULT,0,0,0,'features.conf','general','atxferdropcall','no');
INSERT INTO "features" VALUES (DEFAULT,0,0,0,'features.conf','general','atxferloopdelay','10');
INSERT INTO "features" VALUES (DEFAULT,0,0,0,'features.conf','general','atxfercallbackretries','2');
INSERT INTO "features" VALUES (DEFAULT,1,0,0,'features.conf','featuremap','blindxfer','*1');
INSERT INTO "features" VALUES (DEFAULT,1,0,0,'features.conf','featuremap','disconnect','*0');
INSERT INTO "features" VALUES (DEFAULT,1,0,0,'features.conf','featuremap','atxfer','*2');
INSERT INTO "features" VALUES (DEFAULT,1,0,0,'features.conf','applicationmap','togglerecord','*3,self,AGI(agi://${{XIVO_AGID_IP}}/call_recording)');


INSERT INTO "func_key_type" ("id", "name") VALUES (1, 'speeddial'),
                                                  (2, 'transfer'),
                                                  (3, 'dtmf');

SELECT setval('func_key_type_id_seq', (SELECT MAX(id) FROM func_key_type));


INSERT INTO "func_key_destination_type" (id, name) VALUES (1, 'user'),
                                                          (2, 'group'),
                                                          (3, 'queue'),
                                                          (4, 'conference'),
                                                          (5, 'service'),
                                                          (6, 'forward'),
                                                          (7, 'park_position'),
                                                          (8, 'features'),
                                                          (9, 'paging'),
                                                          (10, 'custom'),
                                                          (11, 'agent'),
                                                          (12, 'bsfilter'),
                                                          (13, 'groupmember');


INSERT INTO "func_key" (type_id, destination_type_id) VALUES (1, 5);
INSERT INTO "func_key_dest_service" (func_key_id, destination_type_id, feature_extension_uuid)
VALUES (currval('func_key_id_seq'), 5, (SELECT "uuid" from feature_extension WHERE "feature" = 'enablevm'));

INSERT INTO "func_key" (type_id, destination_type_id) VALUES (1, 5);
INSERT INTO "func_key_dest_service" (func_key_id, destination_type_id, feature_extension_uuid)
VALUES (currval('func_key_id_seq'), 5, (SELECT "uuid" from feature_extension WHERE "feature" = 'vmusermsg'));

INSERT INTO "func_key" (type_id, destination_type_id) VALUES (1, 5);
INSERT INTO "func_key_dest_service" (func_key_id, destination_type_id, feature_extension_uuid)
VALUES (currval('func_key_id_seq'), 5, (SELECT "uuid" from feature_extension WHERE "feature" = 'vmuserpurge'));

INSERT INTO "func_key" (type_id, destination_type_id) VALUES (1, 5);
INSERT INTO "func_key_dest_service" (func_key_id, destination_type_id, feature_extension_uuid)
VALUES (currval('func_key_id_seq'), 5, (SELECT "uuid" from feature_extension WHERE "feature" = 'phonestatus'));

INSERT INTO "func_key" (type_id, destination_type_id) VALUES (1, 5);
INSERT INTO "func_key_dest_service" (func_key_id, destination_type_id, feature_extension_uuid)
VALUES (currval('func_key_id_seq'), 5, (SELECT "uuid" from feature_extension WHERE "feature" = 'recsnd'));

INSERT INTO "func_key" (type_id, destination_type_id) VALUES (1, 5);
INSERT INTO "func_key_dest_service" (func_key_id, destination_type_id, feature_extension_uuid)
VALUES (currval('func_key_id_seq'), 5, (SELECT "uuid" from feature_extension WHERE "feature" = 'calllistening'));

INSERT INTO "func_key" (type_id, destination_type_id) VALUES (1, 5);
INSERT INTO "func_key_dest_service" (func_key_id, destination_type_id, feature_extension_uuid)
VALUES (currval('func_key_id_seq'), 5, (SELECT "uuid" from feature_extension WHERE "feature" = 'directoryaccess'));

INSERT INTO "func_key" (type_id, destination_type_id) VALUES (1, 5);
INSERT INTO "func_key_dest_service" (func_key_id, destination_type_id, feature_extension_uuid)
VALUES (currval('func_key_id_seq'), 5, (SELECT "uuid" from feature_extension WHERE "feature" = 'fwdundoall'));

INSERT INTO "func_key" (type_id, destination_type_id) VALUES (1, 5);
INSERT INTO "func_key_dest_service" (func_key_id, destination_type_id, feature_extension_uuid)
VALUES (currval('func_key_id_seq'), 5, (SELECT "uuid" from feature_extension WHERE "feature" = 'pickup'));

INSERT INTO "func_key" (type_id, destination_type_id) VALUES (1, 5);
INSERT INTO "func_key_dest_service" (func_key_id, destination_type_id, feature_extension_uuid)
VALUES (currval('func_key_id_seq'), 5, (SELECT "uuid" from feature_extension WHERE "feature" = 'callrecord'));

INSERT INTO "func_key" (type_id, destination_type_id) VALUES (1, 5);
INSERT INTO "func_key_dest_service" (func_key_id, destination_type_id, feature_extension_uuid)
VALUES (currval('func_key_id_seq'), 5, (SELECT "uuid" from feature_extension WHERE "feature" = 'incallfilter'));

INSERT INTO "func_key" (type_id, destination_type_id) VALUES (1, 5);
INSERT INTO "func_key_dest_service" (func_key_id, destination_type_id, feature_extension_uuid)
VALUES (currval('func_key_id_seq'), 5, (SELECT "uuid" from feature_extension WHERE "feature" = 'enablednd'));

INSERT INTO "func_key" (type_id, destination_type_id) VALUES (2, 8);
INSERT INTO "func_key_dest_features" (func_key_id, destination_type_id, features_id)
VALUES (
    currval('func_key_id_seq'),
    8,
    (SELECT id FROM features WHERE filename = 'features.conf'
                                AND category = 'general'
                                AND var_name = 'parkext')
);

INSERT INTO "func_key" (type_id, destination_type_id) VALUES (3, 8);
INSERT INTO "func_key_dest_features" (func_key_id, destination_type_id, features_id)
VALUES (
    currval('func_key_id_seq'),
    8,
    (SELECT id FROM features WHERE filename = 'features.conf'
                                AND category = 'featuremap'
                                AND var_name = 'blindxfer')
);

INSERT INTO "func_key" (type_id, destination_type_id) VALUES (3, 8);
INSERT INTO "func_key_dest_features" (func_key_id, destination_type_id, features_id)
VALUES (
    currval('func_key_id_seq'),
    8,
    (SELECT id FROM features WHERE filename = 'features.conf'
                                AND category = 'featuremap'
                                AND var_name = 'atxfer')
);

INSERT INTO "func_key" (type_id, destination_type_id) VALUES (3, 8);
INSERT INTO "func_key_dest_features" (func_key_id, destination_type_id, features_id)
VALUES (
    currval('func_key_id_seq'),
    8,
    (SELECT id FROM features WHERE filename = 'features.conf'
                                AND category = 'applicationmap'
                                AND var_name = 'togglerecord')
);

INSERT INTO "pjsip_transport" (name) VALUES
  ('transport-udp'),
  ('transport-wss');
INSERT INTO "pjsip_transport_option" (key, value, pjsip_transport_uuid) VALUES
  ('protocol', 'udp', (SELECT uuid FROM pjsip_transport WHERE name = 'transport-udp')),
  ('bind', '0.0.0.0:5060', (SELECT uuid FROM pjsip_transport WHERE name = 'transport-udp'));
INSERT INTO "pjsip_transport_option" (key, value, pjsip_transport_uuid) VALUES
  ('protocol', 'wss', (SELECT uuid FROM pjsip_transport WHERE name = 'transport-wss')),
  ('bind', '0.0.0.0:5060', (SELECT uuid FROM pjsip_transport WHERE name = 'transport-wss'));

INSERT INTO "staticiax" VALUES (DEFAULT,0,0,0,'iax.conf','general','bindport',4569);
INSERT INTO "staticiax" VALUES (DEFAULT,0,0,0,'iax.conf','general','bindaddr','0.0.0.0');
INSERT INTO "staticiax" VALUES (DEFAULT,0,0,0,'iax.conf','general','iaxthreadcount',10);
INSERT INTO "staticiax" VALUES (DEFAULT,0,0,0,'iax.conf','general','iaxmaxthreadcount',100);
INSERT INTO "staticiax" VALUES (DEFAULT,0,0,0,'iax.conf','general','iaxcompat','no');
INSERT INTO "staticiax" VALUES (DEFAULT,0,0,0,'iax.conf','general','authdebug','yes');
INSERT INTO "staticiax" VALUES (DEFAULT,0,0,0,'iax.conf','general','delayreject','no');
INSERT INTO "staticiax" VALUES (DEFAULT,0,0,0,'iax.conf','general','trunkfreq',20);
INSERT INTO "staticiax" VALUES (DEFAULT,0,0,0,'iax.conf','general','trunktimestamps','yes');
INSERT INTO "staticiax" VALUES (DEFAULT,0,0,1,'iax.conf','general','regcontext',NULL);
INSERT INTO "staticiax" VALUES (DEFAULT,0,0,0,'iax.conf','general','minregexpire',60);
INSERT INTO "staticiax" VALUES (DEFAULT,0,0,0,'iax.conf','general','maxregexpire',60);
INSERT INTO "staticiax" VALUES (DEFAULT,0,0,0,'iax.conf','general','bandwidth','high');
INSERT INTO "staticiax" VALUES (DEFAULT,0,0,1,'iax.conf','general','tos',NULL);
INSERT INTO "staticiax" VALUES (DEFAULT,0,0,0,'iax.conf','general','jitterbuffer','no');
INSERT INTO "staticiax" VALUES (DEFAULT,0,0,0,'iax.conf','general','forcejitterbuffer','no');
INSERT INTO "staticiax" VALUES (DEFAULT,0,0,0,'iax.conf','general','maxjitterbuffer',1000);
INSERT INTO "staticiax" VALUES (DEFAULT,0,0,0,'iax.conf','general','maxjitterinterps',10);
INSERT INTO "staticiax" VALUES (DEFAULT,0,0,0,'iax.conf','general','resyncthreshold',1000);
INSERT INTO "staticiax" VALUES (DEFAULT,0,0,1,'iax.conf','general','accountcode',NULL);
INSERT INTO "staticiax" VALUES (DEFAULT,0,0,0,'iax.conf','general','amaflags','default');
INSERT INTO "staticiax" VALUES (DEFAULT,0,0,0,'iax.conf','general','adsi','no');
INSERT INTO "staticiax" VALUES (DEFAULT,0,0,0,'iax.conf','general','transfer','yes');
INSERT INTO "staticiax" VALUES (DEFAULT,0,0,0,'iax.conf','general','language','fr_FR');
INSERT INTO "staticiax" VALUES (DEFAULT,0,0,0,'iax.conf','general','mohinterpret','default');
INSERT INTO "staticiax" VALUES (DEFAULT,0,0,1,'iax.conf','general','mohsuggest',NULL);
INSERT INTO "staticiax" VALUES (DEFAULT,0,0,0,'iax.conf','general','encryption','no');
INSERT INTO "staticiax" VALUES (DEFAULT,0,0,0,'iax.conf','general','maxauthreq',3);
INSERT INTO "staticiax" VALUES (DEFAULT,0,0,0,'iax.conf','general','codecpriority','host');
INSERT INTO "staticiax" VALUES (DEFAULT,0,0,1,'iax.conf','general','disallow',NULL);
INSERT INTO "staticiax" VALUES (DEFAULT,0,0,1,'iax.conf','general','allow',NULL);
INSERT INTO "staticiax" VALUES (DEFAULT,0,0,0,'iax.conf','general','rtcachefriends','yes');
INSERT INTO "staticiax" VALUES (DEFAULT,0,0,0,'iax.conf','general','rtupdate','yes');
INSERT INTO "staticiax" VALUES (DEFAULT,0,0,0,'iax.conf','general','rtignoreregexpire','yes');
INSERT INTO "staticiax" VALUES (DEFAULT,0,0,0,'iax.conf','general','rtautoclear','no');
INSERT INTO "staticiax" VALUES (DEFAULT,0,0,0,'iax.conf','general','pingtime',20);
INSERT INTO "staticiax" VALUES (DEFAULT,0,0,0,'iax.conf','general','lagrqtime',10);
INSERT INTO "staticiax" VALUES (DEFAULT,0,0,0,'iax.conf','general','nochecksums','no');
INSERT INTO "staticiax" VALUES (DEFAULT,0,0,0,'iax.conf','general','autokill','yes');
INSERT INTO "staticiax" VALUES (DEFAULT,0,0,0,'iax.conf','general','calltokenoptional','0.0.0.0');
INSERT INTO "staticiax" VALUES (DEFAULT,0,0,0,'iax.conf','general','srvlookup',NULL);
INSERT INTO "staticiax" VALUES (DEFAULT,0,0,0,'iax.conf','general','jittertargetextra',NULL);
INSERT INTO "staticiax" VALUES (DEFAULT,0,0,0,'iax.conf','general','forceencryption',NULL);
INSERT INTO "staticiax" VALUES (DEFAULT,0,0,0,'iax.conf','general','trunkmaxsize',NULL);
INSERT INTO "staticiax" VALUES (DEFAULT,0,0,0,'iax.conf','general','trunkmtu',NULL);
INSERT INTO "staticiax" VALUES (DEFAULT,0,0,0,'iax.conf','general','cos',NULL);
INSERT INTO "staticiax" VALUES (DEFAULT,0,0,0,'iax.conf','general','allowfwdownload',NULL);
INSERT INTO "staticiax" VALUES (DEFAULT,0,0,0,'iax.conf','general','parkinglot',NULL);
INSERT INTO "staticiax" VALUES (DEFAULT,0,0,0,'iax.conf','general','maxcallnumbers',NULL);
INSERT INTO "staticiax" VALUES (DEFAULT,0,0,0,'iax.conf','general','maxcallnumbers_nonvalidated',NULL);
INSERT INTO "staticiax" VALUES (DEFAULT,0,0,0,'iax.conf','general','shrinkcallerid',NULL);


INSERT INTO "staticqueue" VALUES (DEFAULT,0,0,0,'queues.conf','general','persistentmembers','yes');
INSERT INTO "staticqueue" VALUES (DEFAULT,0,0,0,'queues.conf','general','autofill','no');
INSERT INTO "staticqueue" VALUES (DEFAULT,0,0,0,'queues.conf','general','monitor-type','no');
INSERT INTO "staticqueue" VALUES (DEFAULT,0,0,0,'queues.conf','general','updatecdr','no');
INSERT INTO "staticqueue" VALUES (DEFAULT,0,0,0,'queues.conf','general','shared_lastcall','yes');


INSERT INTO "asterisk_file" (name) VALUES ('confbridge.conf');
INSERT INTO "asterisk_file_section" (name, priority, asterisk_file_id) VALUES ('general', 0, (SELECT id FROM asterisk_file WHERE name = 'confbridge.conf'));
INSERT INTO "asterisk_file_section" (name, priority, asterisk_file_id) VALUES ('wazo_default_bridge', NULL, (SELECT id FROM asterisk_file WHERE name = 'confbridge.conf'));
INSERT INTO "asterisk_file_variable" (key, value, asterisk_file_section_id) VALUES ('type', 'bridge', (SELECT id FROM asterisk_file_section
                                                                                                       WHERE name = 'wazo_default_bridge'
                                                                                                       AND asterisk_file_id = (SELECT id FROM asterisk_file WHERE name = 'confbridge.conf')));
INSERT INTO "asterisk_file_section" (name, priority, asterisk_file_id) VALUES ('wazo_default_user', NULL, (SELECT id FROM asterisk_file WHERE name = 'confbridge.conf'));
INSERT INTO "asterisk_file_variable" (key, value, asterisk_file_section_id) VALUES ('type', 'user', (SELECT id FROM asterisk_file_section
                                                                                                     WHERE name = 'wazo_default_user'
                                                                                                     AND asterisk_file_id = (SELECT id FROM asterisk_file WHERE name = 'confbridge.conf')));
INSERT INTO "asterisk_file_variable" (key, value, asterisk_file_section_id) VALUES ('dsp_drop_silence', 'yes', (SELECT id FROM asterisk_file_section
                                                                                                                WHERE name = 'wazo_default_user'
                                                                                                                AND asterisk_file_id = (SELECT id FROM asterisk_file WHERE name = 'confbridge.conf')));
INSERT INTO "asterisk_file_variable" (key, value, asterisk_file_section_id) VALUES ('talk_detection_events', 'yes', (SELECT id FROM asterisk_file_section
                                                                                                                     WHERE name = 'wazo_default_user'
                                                                                                                     AND asterisk_file_id = (SELECT id FROM asterisk_file WHERE name = 'confbridge.conf')));


INSERT INTO "asterisk_file" (name) VALUES ('rtp.conf');
INSERT INTO "asterisk_file_section" (name, priority, asterisk_file_id) VALUES ('general', 0, (SELECT id FROM asterisk_file WHERE name = 'rtp.conf'));
INSERT INTO "asterisk_file_variable" (key, value, asterisk_file_section_id) VALUES ('rtpstart', '10000', (SELECT id FROM asterisk_file_section
                                                                                                          WHERE name = 'general'
                                                                                                          AND asterisk_file_id = (SELECT id FROM asterisk_file WHERE name = 'rtp.conf')));
INSERT INTO "asterisk_file_variable" (key, value, asterisk_file_section_id) VALUES ('rtpend', '20000', (SELECT id FROM asterisk_file_section
                                                                                                          WHERE name = 'general'
                                                                                                          AND asterisk_file_id = (SELECT id FROM asterisk_file WHERE name = 'rtp.conf')));
INSERT INTO "asterisk_file_section" (name, priority, asterisk_file_id) VALUES ('ice_host_candidates', NULL, (SELECT id FROM asterisk_file WHERE name = 'rtp.conf'));
INSERT INTO "asterisk_file" (name) VALUES ('hep.conf');
INSERT INTO "asterisk_file_section" (name, priority, asterisk_file_id) VALUES ('general', 0, (SELECT id FROM asterisk_file WHERE name = 'hep.conf'));
INSERT INTO "asterisk_file_variable" (key, value, asterisk_file_section_id) VALUES ('enabled', '0', (SELECT id FROM asterisk_file_section
                                                                                                          WHERE name = 'general'
                                                                                                          AND asterisk_file_id = (SELECT id FROM asterisk_file WHERE name = 'hep.conf')));

INSERT INTO "asterisk_file" (name) VALUES ('pjsip.conf');
INSERT INTO "asterisk_file_section" (name, priority, asterisk_file_id) VALUES
  ('global', 0, (SELECT id FROM asterisk_file WHERE name = 'pjsip.conf')),
  ('system', 0, (SELECT id FROM asterisk_file WHERE name = 'pjsip.conf'));
INSERT INTO "asterisk_file_variable" (key, value, asterisk_file_section_id) VALUES
  ('user_agent', 'Wazo PBX', (SELECT id FROM asterisk_file_section WHERE name = 'global' AND asterisk_file_id = (SELECT id FROM asterisk_file WHERE name = 'pjsip.conf'))),
  ('endpoint_identifier_order', 'auth_username,username,ip', (SELECT id FROM asterisk_file_section WHERE name = 'global' AND asterisk_file_id = (SELECT id FROM asterisk_file WHERE name = 'pjsip.conf')));

INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,0,'voicemail.conf','general','maxmsg',100);
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,0,'voicemail.conf','general','silencethreshold',256);
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,0,'voicemail.conf','general','minsecs',0);
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,0,'voicemail.conf','general','maxsecs',0);
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,0,'voicemail.conf','general','maxsilence',15);
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,0,'voicemail.conf','general','review','yes');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,0,'voicemail.conf','general','operator','yes');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,0,'voicemail.conf','general','format','wav');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,0,'voicemail.conf','general','maxlogins',3);
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,0,'voicemail.conf','general','envelope','yes');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,0,'voicemail.conf','general','saycid','no');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,1,'voicemail.conf','general','cidinternalcontexts',NULL);
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,0,'voicemail.conf','general','sayduration','yes');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,0,'voicemail.conf','general','saydurationm',2);
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,0,'voicemail.conf','general','forcename','no');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,0,'voicemail.conf','general','forcegreetings','no');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,0,'voicemail.conf','general','tempgreetwarn','yes');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,0,'voicemail.conf','general','maxgreet',0);
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,0,'voicemail.conf','general','skipms',3000);
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,0,'voicemail.conf','general','sendvoicemail','no');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,0,'voicemail.conf','general','usedirectory','yes');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,0,'voicemail.conf','general','nextaftercmd','yes');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,1,'voicemail.conf','general','dialout',NULL);
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,1,'voicemail.conf','general','callback',NULL);
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,1,'voicemail.conf','general','exitcontext',NULL);
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,0,'voicemail.conf','general','attach','yes');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,0,'voicemail.conf','general','volgain',0);
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,0,'voicemail.conf','general','mailcmd','/usr/sbin/sendmail -t');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,0,'voicemail.conf','general','serveremail','wazo');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,0,'voicemail.conf','general','charset','UTF-8');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,0,'voicemail.conf','general','fromstring','Wazo PBX');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,0,'voicemail.conf','general','emaildateformat','%Y-%m-%d à %H:%M:%S');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,0,'voicemail.conf','general','pbxskip','no');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,0,'voicemail.conf','general','emailsubject','Messagerie Wazo');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,0,'voicemail.conf','general','emailbody','Bonjour ${VM_NAME},\n\nVous avez reçu un message d''une durée de ${VM_DUR} minute(s), il vous reste actuellement ${VM_MSGNUM} message(s) non lu(s) sur votre messagerie vocale : ${VM_MAILBOX}.\n\nLe dernier a été envoyé par ${VM_CALLERID}, le ${VM_DATE}. Si vous le souhaitez vous pouvez l''écouter ou le consulter en tapant le *98 sur votre téléphone.\n\nMerci.\n\n-- Messagerie Wazo --');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,0,'voicemail.conf','general','pagerfromstring','Wazo PBX');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,1,'voicemail.conf','general','pagersubject',NULL);
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,1,'voicemail.conf','general','pagerbody',NULL);
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,0,'voicemail.conf','general','adsifdn','0000000F');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,0,'voicemail.conf','general','adsisec','9BDBF7AC');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,0,'voicemail.conf','general','adsiver',1);
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,0,'voicemail.conf','general','searchcontexts','no');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,0,'voicemail.conf','general','externpass','/usr/share/asterisk/bin/change-pass-vm');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,1,'voicemail.conf','general','externnotify',NULL);
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,1,'voicemail.conf','general','smdiport',NULL);
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,1,'voicemail.conf','general','odbcstorage',NULL);
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,1,'voicemail.conf','general','odbctable',NULL);
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','eu-fr','Europe/Paris|''vm-received'' q ''digits/at'' kM');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','na-newfoundland','America/St_Johns|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','na-atlantic','America/Halifax|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','na-eastern','America/New_York|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','na-central','America/Chicago|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','na-mountain','America/Denver|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','na-pacific','America/Los_Angeles|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','na-alaska','America/Anchorage|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','be-brussels','Europe/Brussels|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','it-rome','Europe/Rome|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','ca-glace_bay','America/Glace_Bay|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','ca-moncton','America/Moncton|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','ca-goose_bay','America/Goose_Bay|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','ca-blanc-sablon','America/Blanc-Sablon|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','ca-toronto','America/Toronto|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','ca-nipigon','America/Nipigon|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','ca-thunder_bay','America/Thunder_Bay|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','ca-iqaluit','America/Iqaluit|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','ca-pangnirtung','America/Pangnirtung|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','ca-atikokan','America/Atikokan|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','ca-winnipeg','America/Winnipeg|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','ca-rainy_river','America/Rainy_River|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','ca-resolute','America/Resolute|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','ca-rankin_inlet','America/Rankin_Inlet|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','ca-regina','America/Regina|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','ca-swift_current','America/Swift_Current|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','ca-edmonton','America/Edmonton|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','ca-cambridge_bay','America/Cambridge_Bay|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','ca-yellowknife','America/Yellowknife|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','ca-inuvik','America/Inuvik|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','ca-creston','America/Creston|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','ca-dawson_creek','America/Dawson_Creek|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','ca-fort_nelson','America/Fort_Nelson|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','ca-whitehorse','America/Whitehorse|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','ca-dawson','America/Dawson|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','ca-vancouver','America/Vancouver|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','de-berlin','Europe/Berlin|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','de-busingen','Europe/Busingen|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','il-jerusalem','Asia/Jerusalem|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','lu-luxembourg','Europe/Luxembourg|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','my-kuala_lumpur','Asia/Kuala_Lumpur|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','my-kuching','Asia/Kuching|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','mc-monaco','Europe/Monaco|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','nl-amsterdam','Europe/Amsterdam|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','pl-warsaw','Europe/Warsaw|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','pt-lisbon','Europe/Lisbon|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','pt-madeira','Atlantic/Madeira|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','pt-azores','Atlantic/Azores|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','gb-london','Europe/London|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','us-detroit','America/Detroit|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','us-kentucky-louisville','America/Kentucky/Louisville|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','us-kentucky-monticello','America/Kentucky/Monticello|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','us-indiana-indianapolis','America/Indiana/Indianapolis|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','us-indiana-vincennes','America/Indiana/Vincennes|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','us-indiana-winamac','America/Indiana/Winamac|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','us-indiana-marengo','America/Indiana/Marengo|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','us-indiana-petersburg','America/Indiana/Petersburg|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','us-indiana-vevay','America/Indiana/Vevay|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','us-indiana-tell_city','America/Indiana/Tell_City|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','us-indiana-knox','America/Indiana/Knox|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','us-menominee','America/Menominee|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','us-north_dakota-center','America/North_Dakota/Center|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','us-north_dakota-new_salem','America/North_Dakota/New_Salem|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','us-north_dakota-beulah','America/North_Dakota/Beulah|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','us-boise','America/Boise|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','us-phoenix','America/Phoenix|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','us-juneau','America/Juneau|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','us-sitka','America/Sitka|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','us-metlakatla','America/Metlakatla|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','us-yakutat','America/Yakutat|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','us-nome','America/Nome|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','us-adak','America/Adak|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','us-honolulu','Pacific/Honolulu|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','es-madrid','Europe/Madrid|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','es-ceuta','Africa/Ceuta|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','es-canary','Atlantic/Canary|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,1,0,0,'voicemail.conf','zonemessages','ch-zurich','Europe/Zurich|''vm-received'' q ''digits/at'' IMp');
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,1,'voicemail.conf','general','moveheard',NULL);
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,1,'voicemail.conf','general','forward_urgent_auto',NULL);
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,1,'voicemail.conf','general','userscontext',NULL);
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,1,'voicemail.conf','general','smdienable',NULL);
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,1,'voicemail.conf','general','externpassnotify',NULL);
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,1,'voicemail.conf','general','externpasscheck',NULL);
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,1,'voicemail.conf','general','directoryinfo',NULL);
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,1,'voicemail.conf','general','pollmailboxes',NULL);
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,1,'voicemail.conf','general','pollfreq',NULL);
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,1,'voicemail.conf','general','imapgreetings',NULL);
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,1,'voicemail.conf','general','greetingsfolder',NULL);
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,1,'voicemail.conf','general','imapparentfolder',NULL);
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,1,'voicemail.conf','general','tz',NULL);
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,1,'voicemail.conf','general','hidefromdir',NULL);
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,1,'voicemail.conf','general','messagewrap',NULL);
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,1,'voicemail.conf','general','minpassword',NULL);
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,1,'voicemail.conf','general','vm-password',NULL);
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,1,'voicemail.conf','general','vm-newpassword',NULL);
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,1,'voicemail.conf','general','vm-passchanged',NULL);
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,1,'voicemail.conf','general','vm-reenterpassword',NULL);
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,1,'voicemail.conf','general','vm-mismatch',NULL);
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,1,'voicemail.conf','general','vm-invalid-password',NULL);
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,1,'voicemail.conf','general','vm-pls-try-again',NULL);
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,1,'voicemail.conf','general','listen-control-forward-key',NULL);
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,1,'voicemail.conf','general','listen-control-reverse-key',NULL);
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,1,'voicemail.conf','general','listen-control-pause-key',NULL);
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,1,'voicemail.conf','general','listen-control-restart-key',NULL);
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,1,'voicemail.conf','general','listen-control-stop-key',NULL);
INSERT INTO "staticvoicemail" VALUES (DEFAULT,0,0,1,'voicemail.conf','general','backupdeleted',NULL);


INSERT INTO "agentglobalparams" VALUES (DEFAULT,'general','multiplelogin','no');
INSERT INTO "agentglobalparams" VALUES (DEFAULT,'general','persistentagents','yes');
INSERT INTO "agentglobalparams" VALUES (DEFAULT,'agents','autologoffunavail','no');
INSERT INTO "agentglobalparams" VALUES (DEFAULT,'agents','maxlogintries','3');
INSERT INTO "agentglobalparams" VALUES (DEFAULT,'agents','endcall','no');


INSERT INTO "sccpgeneralsettings" VALUES (DEFAULT, 'directmedia', 'no');
INSERT INTO "sccpgeneralsettings" VALUES (DEFAULT, 'dialtimeout', '5');
INSERT INTO "sccpgeneralsettings" VALUES (DEFAULT, 'keepalive', '10');
INSERT INTO "sccpgeneralsettings" VALUES (DEFAULT, 'language', 'en_US');
INSERT INTO "sccpgeneralsettings" VALUES (DEFAULT, 'allow', '');
INSERT INTO "sccpgeneralsettings" VALUES (DEFAULT, 'guest', 'no');
INSERT INTO "sccpgeneralsettings" VALUES (DEFAULT, 'max_guests', '100');


DROP TYPE IF EXISTS "queue_statistics" CASCADE;
CREATE TYPE "queue_statistics" AS (
    received_call_count bigint,
    answered_call_count bigint,
    answered_call_in_qos_count bigint,
    abandonned_call_count bigint,
    received_and_done bigint,
    max_hold_time integer,
    mean_hold_time integer
);
ALTER TYPE "queue_statistics" OWNER TO asterisk;


DROP FUNCTION IF EXISTS "fill_simple_calls" (timestamptz, timestamptz);
CREATE FUNCTION "fill_simple_calls"(period_start timestamptz, period_end timestamptz)
  RETURNS void AS
$$
  INSERT INTO "stat_call_on_queue" (callid, "time", stat_queue_id, status)
    SELECT
      callid,
      time,
      (SELECT id FROM stat_queue WHERE name=queuename) as stat_queue_id,
      CASE WHEN event = 'FULL' THEN 'full'::call_exit_type
           WHEN event = 'DIVERT_CA_RATIO' THEN 'divert_ca_ratio'
           WHEN event = 'DIVERT_HOLDTIME' THEN 'divert_waittime'
           WHEN event = 'CLOSED' THEN 'closed'
           WHEN event = 'JOINEMPTY' THEN 'joinempty'
      END as status
    FROM queue_log
    WHERE event IN ('FULL', 'DIVERT_CA_RATIO', 'DIVERT_HOLDTIME', 'CLOSED', 'JOINEMPTY') AND
          "time" BETWEEN $1 AND $2;
$$
LANGUAGE SQL;
ALTER FUNCTION "fill_simple_calls" (period_start timestamptz, period_end timestamptz) OWNER TO asterisk;


DROP FUNCTION IF EXISTS "fill_leaveempty_calls" (timestamptz, timestamptz);
CREATE OR REPLACE FUNCTION "fill_leaveempty_calls" (period_start timestamptz, period_end timestamptz)
RETURNS void AS
$$
WITH 
leave_call as (
    SELECT main.id, main.callid, main.time AS leave_time, main.queuename, 
        (SELECT time FROM queue_log 
        WHERE callid = main.callid AND queuename = main.queuename 
        AND time <= main.time AND event = 'ENTERQUEUE' 
        ORDER BY time DESC LIMIT 1) AS enter_time, 
        stat_queue.id as stat_queue_id 
    FROM queue_log AS main 
    LEFT JOIN stat_queue ON stat_queue.name = main.queuename
    WHERE event='LEAVEEMPTY'
),
leave_call_in_range AS (
    SELECT *
    FROM leave_call
    WHERE enter_time BETWEEN $1 AND $2 
)
INSERT INTO stat_call_on_queue (callid, time, waittime, stat_queue_id, status)
SELECT
    callid,
    enter_time AS time,
    EXTRACT(EPOCH FROM (leave_time - enter_time))::INTEGER AS waittime,
    stat_queue_id,
    'leaveempty' AS status
FROM leave_call_in_range;
$$
LANGUAGE SQL;
ALTER FUNCTION "fill_leaveempty_calls" (period_start timestamptz, period_end timestamptz) OWNER TO asterisk;

DROP FUNCTION IF EXISTS "set_agent_on_pauseall" ();
CREATE FUNCTION "set_agent_on_pauseall" ()
  RETURNS trigger AS
$$
DECLARE
    "number" text;
BEGIN
    SELECT "agent_number" INTO "number" FROM "agent_login_status" WHERE "interface" = NEW."agent";
    IF FOUND THEN
        NEW."agent" := 'Agent/' || "number";
    END IF;

    RETURN NEW;
END;
$$
LANGUAGE plpgsql;
ALTER FUNCTION "set_agent_on_pauseall" () OWNER TO asterisk;


CREATE TRIGGER "change_queue_log_agent"
    BEFORE INSERT ON "queue_log"
    FOR EACH ROW
    WHEN (NEW."event" = 'PAUSEALL' OR NEW."event" = 'UNPAUSEALL')
    EXECUTE PROCEDURE "set_agent_on_pauseall"();



INSERT INTO "resolvconf" VALUES(DEFAULT, '', '', NULL, NULL, NULL, NULL, '');


INSERT INTO "dhcp" VALUES (DEFAULT,0,'','','');


INSERT INTO "mail" VALUES (DEFAULT,'','example.wazo.community','','','');


INSERT INTO "monitoring" VALUES (DEFAULT,0,NULL,NULL);


INSERT INTO "provisioning" VALUES(DEFAULT, '', '', 0, 8667);

/* The UUID "populate-uuid" will be replaced by pg-populate-db */
/* The version is bumped automatically during the release process */
INSERT INTO "infos" (uuid, wazo_version, live_reload_enabled, timezone, configured) VALUES ('populate-uuid', '23.16', 'True', 'Europe/Paris', 'False');

COMMIT;
