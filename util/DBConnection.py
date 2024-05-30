import pyodbc
from .PropertyUtil import PropertyUtil


class DBConnection:
    @staticmethod
    def get_db_connection():
        connection_string = PropertyUtil.getPropertyString()
        try:
            return pyodbc.connect(connection_string)
        except pyodbc.Error as e:
            print(f"Error while connecting to SQL database: {e}")
            return None
