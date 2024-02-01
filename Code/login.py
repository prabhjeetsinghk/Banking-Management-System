# from Code.dbConnection1 import DBCONNECT
from dbConnection1 import UserDatabase
from encdecString import encdec
from datetime import datetime

class LOGIN:
    @staticmethod
    def user_login():
        login_status = False
        adminType = 0
        db = UserDatabase()
        # db = DBCONNECT(host='localhost', user='root', password='Cos@Uni#786125', database='bankdb')
        # db.connect()  
        print("\n+++ Application Login Menu +++")
        user_email = str(input("> Enter your email: "))
        user_pwd = str(input("> Enter your Password: "))
        sql_query = "select user_pwd, admin_type from user_data where user_id = %s"
        params = (user_email,)
        cursor = db.login_execute_query(query=sql_query, param=params)

        for x in cursor:
            data = x
            pwd= data[0]
            adminType = data[1]
        
        cursor = db.getkeyvalue("select keyValue from keytable")
        for x in cursor:
            key = x[0]
        
        dec = encdec(key=key)    
        userPwd = dec.strDecorder(pwd)
        
        if (user_pwd == userPwd):
            print('\n\nLogin successful\n')
            now = datetime.now()
            #Update User Status
            sql_query = "UPDATE user_data SET logged_in = 1, last_logged_time = %s WHERE user_id = %s"
            params = (now, user_email,)
            cursor = db.upadte_user_status(query=sql_query, param=params)
            login_status = True            
        else:
            print('Please enter correct email or password')
        
        return adminType, login_status, user_email