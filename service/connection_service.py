

import os
from time import sleep
from source.mysql_source import MysqlSource
from destination.mysql_destination import MysqlDestination
from dotenv import load_dotenv
load_dotenv()
CONNECTION_MYSQL_DB_HOST = os.environ.get("CONNECTION_MYSQL_DB_HOST")
CONNECTION_MYSQL_DB_PORT = os.environ.get("CONNECTION_MYSQL_DB_PORT")
MYSQL_ROOT_PASSWORD = os.environ.get("MYSQL_ROOT_PASSWORD")

class ConnectionService:
    def __init__(self, sourceId, credentials):
        self.host = credentials.host
        self.port = credentials.port
        self.database = credentials.database
        self.username = credentials.username
        self.password = credentials.password
        self.sourceId = sourceId
        self.source_db = MysqlSource(
            self.host,
            self.port, 
            self.database, 
            self.username,
            self.password
        )
        self.destination_db = MysqlDestination(
            CONNECTION_MYSQL_DB_HOST,
            CONNECTION_MYSQL_DB_PORT, 
            None, 
            "root",
            MYSQL_ROOT_PASSWORD
        )
    
    def get_table_schema(self):
        self.source_db.connect()
        result = self.source_db.get_table_schema()
        self.source_db.close()
        return result
    
    def create_connection(self):
        self.source_db.connect()
        self.destination_db.connect()
        if self.source_db.connection is not None and self.source_db.connection.is_connected():
            self.tables = self.source_db.get_table_schema()
        
        if self.destination_db.connection is not None and self.destination_db.connection.is_connected():
            cursor = self.destination_db.connection.cursor()
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.database}_{self.sourceId}")
            cursor.execute(f"USE {self.database}_{self.sourceId}")

            for create_table_stmt in self.tables:
                try:
                    cursor.execute(create_table_stmt)
                except Exception as e:
                    print(f"Failed insert schema: {e}")
            cursor.close()

        return self.tables
