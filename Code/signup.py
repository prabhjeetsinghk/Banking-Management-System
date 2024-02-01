from dbConnection1 import UserDatabase
from encdecString import encdec


class user_signup:
    @staticmethod
    def add_user_details():
        db = UserDatabase()

        user_name = input("Enter your full name:\n")
        user_email = input("Enter your email:\n")
        user_pwd = input("Enter your password:\n")

        cursor = db.getkeyvalue("select keyValue from keytable")

        for x in cursor:
            key = x[0]
        
        print(key)
        
        enc = encdec(key=key)
        hashed = enc.strEncoder(user_pwd)
       
        sql_query = "INSERT INTO user_data (user_id, user_name, user_pwd) VALUES (?, ?, ?)"
        params = (user_email, user_name, hashed)
        result = db.add_user_details(query=sql_query,param=params)
        
        print(result)
        
        if result:
            print('Record Added Successfully')
        else:
            print("Error occurred while adding user account")
