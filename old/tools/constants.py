from typing import Any
class Constants:

    # versions for current formats!!!
    overAllVersion = "0.1"
    keyValueVersion = "0.1"
    relationVersion = "0.1"

    # Paths!!!
    recoursesPath = "resources"
    databasesPath = f"{recoursesPath}/db"
    infoPath = f"./{recoursesPath}/information"
    archivesPath = f"{recoursesPath}/archives"

    def SetKeyValuePairConstant(self,table_name:str,key:str,value:Any): return f"INSERT INTO {table_name} VALUES ({key} , {value} )"

    def GetKeyValuePairConstant(self,table_name:str,key:str): return f"SELECT * FROM {table_name} WHERE KEY = \"{key}\" "

    def DeleteKeyValuePairConstant(self, table_name: str, key: str): return f"DELETE FROM {table_name} WHERE KEY = '{key}'"

    def DropTableConstant(self,table_name:str): return f"DROP TABLE {table_name}"

    def CreateTableConstant(self, table_name:str): return f"CREATE TABLE {table_name} ("

    def InsertConstant(self,table_name:str): return f"INSERT INTO {table_name} VALUES ("

    def SelectFromConstant(self,table_name: str,columns:str): return f"SELECT {columns} FROM {table_name}"

    def WhereConstant(self,where_clause:str): return f"WHERE {where_clause}"

    def UpdateConstant(self,table_name:str): return f"UPDATE {table_name} SET "

    def DeleteConstant(self,table_name:str): return f"DELETE FROM {table_name}"



