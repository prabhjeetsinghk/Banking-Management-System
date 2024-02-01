from dbConnection1 import UserDatabase

db = UserDatabase()

db.disconnect()
cursor = db.getkeyvalue("select keyValue from keytable")

keys = cursor.fetchall()

for x in keys:
    print(x)
