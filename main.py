import sqlite3
from typing import Any


con = sqlite3.connect("test.db")
currentTable = ""


def inUsedTable(name: str):
    global currentTable
    currentTable = name


def mkTableKV(name: str):
    con.execute(f"CREATE TABLE IF NOT EXISTS {name} (key TEXT UNIQUE, value ANY )")


def deleteKV(key: str):
    con.execute(f"DELETE FROM {currentTable} WHERE key='{key}'")
    con.commit()


def setKV(key: str, value: Any):
    con.execute("INSERT INTO mole (key, value) VALUES(?, ?)", (key, value))
    # con.execute(f"INSERT INTO {currentTable} (key,value) VALUES ({key},{value})")
    con.commit()


def updateKV(key: str, value: Any):
    print(f"UPDATE {currentTable} SET value = {value} WHERE key = {key}")
    con.execute(f"UPDATE {currentTable} SET value = {value} WHERE key = '{key}'")
    con.commit()


def getKV(key: str) -> Any:
    cur = con.cursor()
    cur.execute(f"SELECT value FROM {currentTable} WHERE key='{key}'")
    row = cur.fetchone()
    if row is None:
        return None
    else:
        return row[0]


def listKV():
    cur = con.cursor()
    cur.execute(f"SELECT * FROM {currentTable}")
    rows = cur.fetchall()
    return rows


mkTableKV("mole")
inUsedTable("mole")
updateKV(key="fish", value=-7)
