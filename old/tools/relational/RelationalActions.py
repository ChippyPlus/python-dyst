import sqlite3
from tools.constants import Constants
from typing import Any
class Actions:
    def __init__(self):
        self.connection:sqlite3.Connection # This needs to be set manually
        self.constants = Constants()
        self._  = "This is a 100% waste of time"

    def createTable(self,table_name:str, columns:tuple[str]):

        sql = self.constants.CreateTableConstant(table_name) # ' f"CREATE TABLE {table_name} ("    '
        for column, data_type in columns:
            sql += f"{column} {data_type},"
        sql = sql[:-1] + ")"

        self.connection.execute(sql)
        self.connection.commit()

    def insert(self,table_name:str, data:tuple[Any]):
        sql = self.constants.InsertConstant(table_name) # ' f"INSERT INTO {table_name} VALUES (" '
        for index,_ in enumerate(data):
            if isinstance(data[index], str):
                sql += f"\"{data[index]}\","
            elif isinstance(data[index], int):
                sql += f"{data[index]},"
            elif isinstance(data[index], float):
                sql += f"{data[index]},"
            else:
                sql += f"\"{data[index]}\","
        sql = sql.removesuffix(",") + ")"

        self.connection.execute(sql)
        self.connection.commit()

    def select(self,table_name:str, _columns:tuple[str] = ("*",), where_clause:str = ""):
        columns = ",".join(_columns)
        sql = self.constants.SelectFromConstant(table_name,columns) # ' f"SELECT {columns} FROM {table_name}" '
        if where_clause:
            sql += self.constants.WhereConstant(where_clause) #  ' f" WHERE {where_clause}" '

        cursor = self.connection.execute(sql)
        self.connection.commit()
        return cursor.fetchall()

    def update(self,table_name:str, data:dict[Any,Any], where_clause:str):
        sql = self.constants.UpdateConstant(table_name) # ' f"UPDATE {table_name} SET " '
        for column, _ in data.items():
            sql += f"{column} = ?, "
        sql = sql[:-2] + self.constants.WhereConstant(where_clause) # ' f" WHERE {where_clause}" '
        self.connection.execute(sql, list(data.values()))
        self.connection.commit()


    def delete(self,table_name:str, where_clause:str):
        sql = f"{self.constants.DeleteConstant(table_name)} {self.constants.WhereConstant(where_clause)}" # '   f"DELETE FROM {table_name} WHERE {where_clause}" ' 
        self.connection.execute(sql)
        self.connection.commit()


    def delete_table(self,table_name:str):
        sql = self.constants.DropTableConstant(table_name) # ' f"DROP TABLE {table_name}" '
        self.connection.execute(sql)
        self.connection.commit()


    def execute(self,sql:str):
        self.connection.execute(sql)
        self.connection.commit()
    def close(self):
        self.connection.close()

