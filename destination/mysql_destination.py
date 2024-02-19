import mysql.connector
from mysql.connector import Error

class MysqlDestination:
    def __init__(self, host, port, database, user, password):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password

    def connect(self):
        """Establish a connection to the MySQL database."""
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password
            )
            if self.connection.is_connected():
                print("MySQL Database connection successful")
        except Error as e:
            print(f"Error connecting to MySQL Database: {e}")
            self.connection = None

    def execute_query(self, query):
        """Execute a SQL query."""
        if self.connection is not None and self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                cursor.execute(query)
                if query.strip().lower().startswith('select'):
                    results = cursor.fetchall()
                    return results
                else:
                    self.connection.commit()  # Commit changes for INSERT/UPDATE/DELETE
                    return {"success": True}
            except Error as e:
                print(f"Failed to execute query: {e}")
            finally:
                cursor.close()
        else:
            print("Connection is not established. Call connect() before executing queries.")
    
    def get_table_schema(self):

        if self.connection is not None and self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                cursor.execute("SHOW TABLES")
                tables = cursor.fetchall()
                table_create_statements = []
                for (table_name,) in tables:
                    # Retrieve the CREATE TABLE statement for each table
                    cursor.execute(f"SHOW CREATE TABLE {table_name}")
                    create_table_stmt = cursor.fetchone()[1]
                    print(create_table_stmt)
                    table_create_statements.append(create_table_stmt)
                cursor.close()
                return table_create_statements
            except Error as e:
                print(f"Failed to execute query: {e}")
            finally:
                cursor.close()
        else:
            print("Connection is not established. Call connect() before executing queries.")
        

    def close(self):
        """Close the database connection."""
        if self.connection is not None and self.connection.is_connected():
            self.connection.close()
            print("MySQL connection is closed")
