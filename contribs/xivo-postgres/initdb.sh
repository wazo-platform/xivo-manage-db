#!/bin/bash
echo "INIT DB"

sed -i 's/@localhost/@/g' /usr/share/xivo-manage-db/alembic.ini

mkdir -p /etc/xivo-dao/conf.d
cat > /etc/xivo-dao/config.yml <<EOC
db_uri: postgresql://asterisk:proformatique@/asterisk
EOC

xivo-init-db --init

sed -i 's/@/@localhost/g' /usr/share/xivo-manage-db/alembic.ini
rm -r /etc/xivo-dao
