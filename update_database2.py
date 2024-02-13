import mysql.connector
from mysql.connector import Error

def replace_string_in_db(host, database, user, password):
    connection = None  # Initialize connection variable
    try:
        # Establish a connection to the database
        connection = mysql.connector.connect(host=host, user=user, password=password)
        if connection.is_connected():
            # Create the database if it doesn't exist
            cursor = connection.cursor()
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{database}`")
            cursor.close()

            # Connect to the specific database
            connection.database = database

            cursor = connection.cursor()

            # Get the names of all tables in the database
            cursor.execute("SHOW TABLES")
            tables = cursor.fetchall()

            for table in tables:
                table_name = table[0]
                print(f"Working on table: {table_name}")  # Log which table is currently being processed

                # Get the names of all columns for the current table
                cursor.execute(f"DESCRIBE `{table_name}`")  # Added backticks for table name
                columns = cursor.fetchall()

                for column in columns:
                    column_name = column[0]
                    column_type = column[1]

                    # Check if the column type is text-like
                    if 'char' in column_type or 'text' in column_type:
                        # Prepare SQL command to replace the string
                        # Added LOWER() to ignore case sensitivity
                        sql = f"UPDATE `{table_name}` SET `{column_name}` = REPLACE(`{column_name}`, 'datactics.com', 'sandbox2.datactics.net') WHERE LOWER(`{column_name}`) LIKE '%datactics.com%'"
                        try:
                            cursor.execute(sql)
                        except Error as e:
                            print(f"Error in table: {table_name}, column: {column_name}, Error: {e}")

            # Commit changes to the database
            connection.commit()

    except Error as e:
        print("Error connecting to the MySQL database", e)
    finally:
        if connection is not None and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

# Database access credentials
host = 'localhost'
database = 'XXXX'  # Change to the desired database name
user = 'XXXX'
password = 'XXXX'
replace_string_in_db(host, database, user, password)
