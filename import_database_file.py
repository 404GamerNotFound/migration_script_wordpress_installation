import subprocess

# Database credentials
DB_USER = "XXXX"
DB_PASSWORD = "XXXX"
DB_NAME = "XXXX"
DB_HOST = "localhost"

# Path to your SQL dump file
SQL_DUMP_PATH = "livewww-all-data.sql"

def run_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
        print(f'Successfully executed: {command}')
    except subprocess.CalledProcessError as e:
        print(f'An error occurred: {e}')
        exit(1)  # Exit the script if command fails

def import_sql_dump():
    # 1. Überprüfen, ob die Datenbank existiert, falls nicht, erstellen
    command_check_create_db = f'mysql -h {DB_HOST} -u {DB_USER} -p{DB_PASSWORD} -e "CREATE DATABASE IF NOT EXISTS {DB_NAME};"'
    run_command(command_check_create_db)

    # 2. Berechtigungen setzen (optional, wenn nötig)
    command_grant_permissions = f'mysql -h {DB_HOST} -u {DB_USER} -p{DB_PASSWORD} -e "GRANT ALL PRIVILEGES ON {DB_NAME}.* TO \'{DB_USER}\'@\'localhost\'; FLUSH PRIVILEGES;"'
    run_command(command_grant_permissions)

    # 3. Command to import .sql file
    command_import = f'mysql -h {DB_HOST} -u {DB_USER} -p{DB_PASSWORD} {DB_NAME} < {SQL_DUMP_PATH}'
    run_command(command_import)

    print(f'Successfully imported {SQL_DUMP_PATH} into {DB_NAME} database.')

import_sql_dump()
