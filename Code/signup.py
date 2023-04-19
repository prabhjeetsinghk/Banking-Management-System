from dbConnection import DBCONNECT
from encdecString import encdec


class user_signup:
    @staticmethod
    def add_user_details():
        db = DBCONNECT(host='localhost', user='root', password='Cos@Uni#786125', database='bankdb')
        db.connect()

        user_name = input("Enter your name:\n")
        user_email = input("Enter your email:\n")
        user_pwd = input("Enter your password:\n")

        cursor = db.getkeyvalue("select keyValue from keytable")
        for x in cursor:
            key = x[0]
        
        print(key)
        
        enc = encdec(key=key)
        hashed = enc.strEncoder(user_pwd)
       
        sql_query = "INSERT INTO user_data (user_id, user_name, user_pwd) VALUES (%s, %s, %s)"
        params = (user_email, user_name, hashed)
        result = db.add_user_details(query=sql_query,param=params)
        if result:
            print('Record Added Successfully')
        else:
            print("Error occurred while adding user account")
