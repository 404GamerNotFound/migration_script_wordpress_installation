#!/bin/bash

# Setze Datenbankverbindungsinformationen
DB_NAME="XXXX"
DB_USER="XXXX"
DB_PASSWORD="XXXX"
DB_HOST="localhost"

# Setze alte und neue Domain
OLD_DOMAIN="datactics.com"
NEW_DOMAIN="sandbox2.datactics.com"

# SQL-Befehl, um die erforderlichen UPDATE-Befehle zu generieren
SQL="SELECT CONCAT('UPDATE \`', table_schema, '\`.\`', table_name, '\` SET \`', column_name, '\` = REPLACE(\`', column_name, '\`, ''', '${OLD_DOMAIN}', ''', ''', '${NEW_DOMAIN}', ''') WHERE \`', column_name, '\` LIKE ''%', '${OLD_DOMAIN}', '%'';') AS query FROM information_schema.columns WHERE table_schema = '${DB_NAME}' AND data_type IN ('char', 'varchar', 'text', 'mediumtext', 'longtext');"

# Führe SQL-Befehl aus und speichere die Ergebnisse in einer Variablen
QUERIES=$(mysql -u${DB_USER} -p${DB_PASSWORD} -h ${DB_HOST} --database=${DB_NAME} -e "${SQL}")

# Entferne die erste Zeile (Spaltennamen)
QUERIES=$(echo "${QUERIES}" | sed '1d')

# Führe jede generierte SQL-Query aus
while read -r QUERY; do
    if [ ! -z "$QUERY" ]; then
        mysql -u${DB_USER} -p${DB_PASSWORD} -h ${DB_HOST} --database=${DB_NAME} -e "${QUERY}"
    fi
done <<< "${QUERIES}"

echo "Ersetzung abgeschlossen."
