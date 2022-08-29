"""
DbPy Offical
~~~~~~~~~~~~~~~~
Some data is maybe messed up idk
"""

import pymysql
connection = pymysql.connect(host="host", port=int("port"), user="user", passwd="passwd", database="database")
cursor = connection.cursor()
debug = True
print("Debug (db.py) : Database Connection Online") 
 
def debug(oneoroff):
    if oneoroff == "on":
        print("Debug mode enabled succesfully")
        debug = True
    elif oneoroff == "off":
        debug = False
    else:
        return print("Error: Not a valid value for 'oneoroff'") 

def get(name,table):
    """
    Get data out of a table in the database
    """
    retrive = f"Select * from {table};" 
    cursor.execute(retrive)
    rows = cursor.fetchall()
    connection.commit()
    if debug == True:
        print("Debug (db.py) : returned data ")
    for row in rows:
        rowname = str(row[1])
        name = str(name)
        if name == rowname:
            return row[2]
    raise Exception("Error (db.py) : Could not retrieve data from database")
         
def createtable(name):
    """
    Create a table with the given name
    """
    try:
        create = f"""CREATE TABLE {str(name)}(
        ID INT(30) PRIMARY KEY AUTO_INCREMENT,
        NAME  CHAR(30) NOT NULL,
        VALUE CHAR(30))""" 
        cursor.execute(create) 
        if debug == True: 
               return print("Debug (db.py) : Created table ") 
    except:
      return print("Error (db.py) : Table already exists")

def createnew(name,data,table):
    try:
        if debug == True:
                print("Debug (db.py) : Creating new Entry")
        insert1 = f"INSERT INTO {table}(Name, VALUE) VALUES('{str(name)}', '{str(data)}' );"
        cursor.execute(insert1) 
        connection.commit()
        return "Created new Entry"
    except:
        return "Error (db.py) : Could not create entry"

def set(name,data,table):
    """
    Create or Set a value in a given Table
    """
    try:
        get(str(name),str(table))
        cursor.execute(f"UPDATE {table} SET VALUE = '{data}' WHERE NAME = '{name}'")
        if debug == True:
            print("Success (db.py) : Updated value")
        connection.commit()
        return "Updated Value"
    except Exception:
        if debug == True:
            print("Debug (db.py) : Creating new Entry")
        createnew(name,data,table)
        return "Created new Entry"

def remove(name,table):
    """
    Remove a value from a given Table
    """
    try:
        cursor.execute(f"DELETE FROM {table} WHERE 'NAME' = '{name}'")
        connection.commit()
        if debug == True:
            return print("Debug (db.py) : remove table succesfully")
        return "Removed Value"
    except:
        raise Exception("Error (db.py) : failed to remove data from table")

def rmtable(tabel):
    """
    Remove a Table with the given name
    """
    try:
        cursor.execute(f"DROP TABLE IF EXISTS {tabel}")
        connection.commit()
        if debug == True:
            print("Debug (db.py) : remove table succesfully")
    except:
        print("Debug (db.py) : remove table failed")