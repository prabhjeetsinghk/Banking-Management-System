import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()
database_name = os.getenv('DATABASE_NAME')

user_email = 'prabh1@test.com'


# sql_query = "INSERT INTO user_data (user_id, user_name, user_pwd, admin_type) VALUES (?, ?, ?, ?)"
# params = (user_email, user_name, user_pwd, admin_type)
# result = db.add_user_details(query=sql_query,param=params)

conn = sqlite3.connect(database_name)
sql_query = "select * from user_data where user_email = (?)"
params = (user_email,)
# fetch_data_query = f'''
#     SELECT t1.user_name, t2.balance, t3.transaction_time FROM user_data as t1
#     INNER JOIN account_balance as t2 ON t1.user_id = t2.user_id
#     INNER JOIN transactions as t3 ON t1.user_id = t3.user_id
#     WHERE t1.user_id = (?)
# '''
# cursor = conn.execute(query=sql_query, param=params)

cursor = conn.execute('''
            select * from user_data where user_email = (?)
        ''', (user_email, ))
rows = cursor.fetchall()

for i in rows:
    print(i)

# for i in rows:
#     print(i[0])
#     print(i[1])

# print(rows[0][0])

       
# if (user_pwd == rows[0][0]):
#     print('\n\nLogin successful\n')
#     now = datetime.now()
    
#     #Update User Status
#     sql_query = "UPDATE user_data SET logged_in = 1, last_logged_time = (?) WHERE user_id = (?)"
#     params = (now, user_email,)
#     db.upadte_user_status(query=sql_query, param=params)
#     login_status = True 

#     sql_query = "select * from user_data where user_id = (?)"
#     params = (user_email,)
#     cursor = db.login_execute_query(query=sql_query, param=params)
#     rows = cursor.fetchall()

#     for i in rows[0]:
#         print(i)
# def selection_after_login(adminType, user_email):
#     adminType = adminType
#     email = user_email
#     if adminType == 0:
#         print("\t\t\t*******Select the o2peration to perform******\n")
#         option = int(input("1. Credit\n2. Debit\n3. Update User Profile\n\n"))
#         if option == 3:
#             d3 = user_update()
#             d3.update_user(email)
#         else:
#             print("Please select only from given options\n")
#             selection_after_login(email)
#     else:
#         print("Hello Admin, Choose below operations")
#         option = int(input("1. Add new user\n2. Update existing user"))

# selection_after_login(0, user_email)