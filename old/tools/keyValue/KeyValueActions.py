import sqlite3
from tools.constants import Constants

"""
FORMAT
KEY   | VALUE
hello | world
"""

class Actions:
    def __init__(self):
        self.connection: sqlite3.Connection  # This needs to be set manually
        self.constants = Constants()

    def createTable(self, table_name: str):
        sql = f"{self.constants.CreateTableConstant(table_name)} KEY TEXT PRIMARY KEY, VALUE ANY)"
        self.connection.execute(sql) #? I think this is a very bad None function!!!!!!!!!!!!!!

        self.connection.commit()

    def set(self,table_name: str, key: str, value: str):
        sql = f"INSERT INTO {table_name} VALUES (?, ?)"
        self.connection.execute(sql, (key, value))
        self.connection.commit()


    def get(self, table_name: str, key: str):
        sql = f"{self.constants.GetKeyValuePairConstant(table_name, key)}"
        print(sql+";")
        out = self.connection.execute(sql)
        self.connection.commit()
        return out.fetchone()[0]

    def delete(self, table_name: str, key: str):
        sql = f"{self.constants.DeleteKeyValuePairConstant(table_name, key)}"
        self.connection.execute(sql)
        self.connection.commit()
    
    def execute(self, sql: str):
        self.connection.execute(sql)
        self.connection.commit()

    def close(self):
        self.connection.close()
