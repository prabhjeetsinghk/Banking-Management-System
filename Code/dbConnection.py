# import mysql.connector

# class DBCONNECT:
#     def __init__(self, host, user, password, database):
#         self.host = host
#         self.user = user
#         self.password = password
#         self.database = database
#         self.conn = None

#     def connect(self):
#         self.conn = mysql.connector.connect(
#             host=self.host,
#             user=self.user,
#             password=self.password,
#             database=self.database
#         )

#     def disconnect(self):
#         self.conn.close()
    
#     def login_execute_query(self, query, param):
#         cursor = self.conn.cursor()
#         cursor.execute(query, param)
#         return cursor

#     def upadte_user_status(self,query,param):
#         cursor = self.conn.cursor()
#         cursor.execute(query, param)
#         self.conn.commit()
    
#     def get_user_details(self, query, param):
#         cursor = self.conn.cursor()
#         cursor.execute(query,param)
#         return cursor

#     def add_user_details(self, query, param):
#         cursor = self.conn.cursor()
#         cursor.execute(query,param)
#         self.conn.commit()
#         return cursor

#     def update_user_details(self, query, param):
#         cursor = self.conn.cursor()
#         cursor.execute(query, param)
#         self.conn.commit()
#         return cursor

#     def getkeyvalue(self, query):
#         cursor = self.conn.cursor()
#         cursor.execute(query)
#         return cursor
    