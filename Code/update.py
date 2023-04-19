from dbConnection import DBCONNECT
from login import LOGIN
from encdecString import encdec

class user_update:
    @staticmethod
    def update_user_details(user_email):
        db = DBCONNECT(host='localhost', user='root', password='Cos@Uni#786125', database='bankdb')
        db.connect()
        cursor = db.getkeyvalue("select keyValue from keytable")
        for x in cursor:
            key = x[0]
        
        enc = encdec(key=key) 
        option = int(input("Select the option you want to update:\n1. Name\n2. Password\n3. Both Name and Password\n\n"))
        if option == 1:
            user_name = input("Enter your new name")
            sql_query = "UPDATE user_data SET user_name=%s where user_id=%s"
            params = (user_name, user_email)
            db.update_user_details(query=sql_query,param=params)
            # db.disconnect()
            status = True
        elif option == 2:
            user_pwd = input("Enter your new password")
            
            hashed = enc.strEncoder(user_pwd)

            sql_query = "UPDATE user_data SET user_pwd=%s where user_id=%s"
            params = (hashed, user_email)            
            db.update_user_details(query=sql_query,param=params)
            # db.disconnect()
            status = True
        elif option == 3:
            user_name = input("Enter your new name")            
            user_pwd = input("Enter your new password")
            hashed = enc.strEncoder(user_pwd)
            sql_query = "UPDATE user_data SET user_name=%s, user_pwd=%s where user_id=%s"
            params = (user_name, hashed, user_email)
            db.update_user_details(query=sql_query,param=params)
            # db.disconnect()
            status = True
        else:
            print("You entered wrong option, Please choose correct one")
            status = False
        return status

    @staticmethod
    def update_user(user_email):
        obj1 = user_update()
        obj2 = LOGIN()
        db = DBCONNECT(host='localhost', user='root', password='Cos@Uni#786125', database='bankdb')
        db.connect()
        sql_query = "select logged_in from user_data where user_id = %s"
        params = (user_email,)
        cursor = db.get_user_details(query=sql_query,param=params)
        # db.disconnect()
        for i in cursor:
            login_status = i[0]
        if login_status:
            result =  obj1.update_user_details(user_email)        
            if result:
                print('Record Updated Successfully')
            else:
                obj1.update_user_details(user_email)
        else:
            print("Your session has expired, Please login again")
            obj2.user_login()
        
