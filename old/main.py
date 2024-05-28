import sqlite3
# from resources.archives import dogtuples
from tools.systemTools import metadata
from tools.relational.RelationalActions import Actions as RelationalActions
from tools.constants import Constants
from tools.keyValue.KeyValueActions import Actions as KeyValueActions


relationActions = RelationalActions()
constants = Constants
systemInfo = metadata
keyValueActions = KeyValueActions()








def main():
    global mainConnection
    mainConnection = sqlite3.connect(f"{constants.databasesPath}/keyValue/items.db")
    keyValueActions.connection = mainConnection
    global table
    table = ""
    while True:
        command = input(" $ ").split()
        if command[0] == "use":

            table = command[1]
        
        elif table == "":
            print("Please use a table")
            


        if command[0] == "exit":
            break

        if command[0] == "use":

            table = command[1]

        elif command[0] == "set":
            keyValueActions.set(table,command[1], command[2])
        elif command[0] == "get":
            print(keyValueActions.get(table,command[1]))
        elif command[0] == "del":
            keyValueActions.delete(table,command[1])






if __name__ == "__main__":
    main()
    mainConnection.close()
