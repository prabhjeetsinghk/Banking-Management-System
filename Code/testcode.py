from dbConnection1 import UserDatabase

db = UserDatabase()

user_email = 'prabhjeet3@test.com'
# user_name = 'prabhjeet'
# user_pwd = 'Prabh@123'
# admin_type = 0


# sql_query = "INSERT INTO user_data (user_id, user_name, user_pwd, admin_type) VALUES (?, ?, ?, ?)"
# params = (user_email, user_name, user_pwd, admin_type)
# result = db.add_user_details(query=sql_query,param=params)


sql_query = "select user_pwd, admin_type from user_data where user_id = (?)"
params = (user_email,)
cursor = db.login_execute_query(query=sql_query, param=params)
rows = cursor.fetchall()

for i in rows:
    print(i[0])
    print(i[1])


       
# if (user_pwd == userPwd):
#     print('\n\nLogin successful\n')
#     now = datetime.now()
    
#     #Update User Status
#     sql_query = "UPDATE user_data SET logged_in = 1, last_logged_time = (?) WHERE user_id = (?)"
#     params = (now, user_email,)
#     db.upadte_user_status(query=sql_query, param=params)
#     login_status = True            