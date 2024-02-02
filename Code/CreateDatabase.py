import sqlite3
import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv

class UserDatabase:
    def __init__(self):
        load_dotenv()
        database_name = os.getenv('DATABASE_NAME')
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()
        self.create_table()
           
    def create_table(self):
        try:
            result = self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS user_data (
                    user_email TEXT PRIMARY KEY,
                    user_name TEXT NOT NULL,
                    user_pwd TEXT NOT NULL,
                    user_phone TEXT NOT NULL,
                    user_address TEXT NOT NULL,                    
                    balance  FLOAT DEFAULT 0.0,                   
                    admin_type INTEGER DEFAULT 0,
                    logged_in INTEGER DEFAULT 0,
                    last_logged_time TEXT DEFAULT 'Not Logged In'                              
                )
            ''')

            if result.fetchall():
                print("Table 'user_data' created successfully.")
            
            result = self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS transactions (
                    user_email TEXT,
                    transaction_time TEXT,
                    transaction_amount FLOAT,
                    transaction_type TEXT,
                    PRIMARY KEY (user_email, transaction_time)                                                              
                )
            ''')
            if result.fetchall():
                print("Table 'transactions' created successfully.")

            result = self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS keytable (
                    keyValue TEXT NOT NULL              
                )
            ''')

            if result.fetchall():
                try:
                    key = Fernet.generate_key()
                    self.cursor.execute("INSERT INTO keytable (keyValue) VALUES (?)", (key,))
                    print('Key Added Successfully')

                except sqlite3.Error as e:
                    print(f"Error: {e}")
                    self.connection.rollback()                    
                    self.connection.close()

                finally:
                    self.connection.commit()
                    self.connection.close()

        except sqlite3.Error as e:
            print(f"Error: {e}")
            self.connection.rollback()
            self.connection.close()

if __name__ == "__main__":
    db = UserDatabase()    

    # def login_execute_query(self, query, param):
    #     try:
    #         self.cursor.execute(query, param)          
    #         return self.cursor
        
    #     except sqlite3.Error as e:
    #         print(f"Error: {e}")
    #         return False
      
    # def get_user_details(self, query, param):
    #     try:
    #         self.cursor.execute(query,param)
    #         return self.cursor
        
    #     except sqlite3.Error as e:
    #         print(f"Error: {e}")
    #         return False
    
    # def upadte_user_status(self,query,param):
    #     try:
    #         result = self.cursor.execute(query, param)
    #         if result.fetchall():
    #             print(f"User Updated successfully.")
    #             self.connection.commit()
        
    #     except sqlite3.Error as e:
    #         print(f"Error: {e}")
    #         self.connection.rollback()
           
        
    # def add_user_details(self, query, param):
    #     try:
    #         self.cursor.execute(query,param)
    #         self.connection.commit()
    #         return self.cursor
        
    #     except sqlite3.Error as e:
    #         print(f"Error: {e}")
    #         self.connection.rollback()
    #         return False
    
    # def update_balance(self, query, param):
    #     try:
    #         self.cursor.execute(query,param)
    #         self.connection.commit()
    #         return self.cursor
        
    #     except sqlite3.Error as e:
    #         print(f"Error: {e}")
    #         self.connection.rollback()
    #         return False
    
    # def update_trasaction(self, query, param):
    #     try:
    #         self.cursor.execute(query,param)
    #         self.connection.commit()
    #         return self.cursor
        
    #     except sqlite3.Error as e:
    #         print(f"Error: {e}")
    #         self.connection.rollback()
    #         return False
        
    # def update_user_details(self, query, param):
    #     try:
    #         self.cursor.execute(query,param)
    #         self.connection.commit()
    #         return self.cursor
            
    #     except sqlite3.Error as e:
    #         print(f"Error: {e}")
    #         self.connection.rollback()
    #         return False

    # def getkeyvalue(self, query):
    #     try:
    #         self.cursor.execute(query)
    #         return self.cursor
                
    #     except sqlite3.Error as e:
    #         print(f"Error: {e}")
    #         return False

    # def disconnect(self):
    #     self.cursor.close()
    #     self.connection.close()
    
    # def set_key(self, key):
    #     try:
    #         self.cursor.execute("INSERT INTO keytable (keyValue) VALUES (?)", (key,))
    #         print('Key Added Successfully')
        
    #     except sqlite3.Error as e:
    #         print(f"Error: {e}")
    #         self.connection.rollback()

    #     finally:
    #         self.connection.commit()
            
