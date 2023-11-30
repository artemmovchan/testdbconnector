import pyodbc
import pymssql


'''
connection_string = f"DRIVER={driver};SERVER={host};DATABASE={dbname};UID={username};PWD={password}"
'''

class DBConnector:
    
    def __init__(self, driver: str, host: str, dbname: str, username: str, password: str):
        self.driver = driver
        self.host = host
        self.dbname = dbname
        self.username = username
        self.password = password
    
    def send_sql_query(self, function: str, driver_type: str = 'ODBC'):
        if (driver_type == 'ODBC'):
            connection = pyodbc.connect(f"DRIVER={self.driver};SERVER={self.host};DATABASE={self.dbname};UID={self.username};PWD={self.password}")
        else:
            connection = pymssql.connect(server=self.host, user=self.username, password=self.password, database=self.dbname)
        cursor = connection.cursor()
        cursor.execute(function)
        result = cursor.fetchval()
        cursor.close()
        connection.close()
        return result