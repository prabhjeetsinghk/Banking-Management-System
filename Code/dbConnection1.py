import sqlite3

class UserDatabase:
    def __init__(self, database_name="pythonbank.db"):
        self.database_name = database_name
        self.connection = sqlite3.connect(self.database_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def set_key(self, key):
        try:
            self.cursor.execute("INSERT INTO keytable (keyValue) VALUES (?)", (key))
            print('Key Added Successfully')
        
        except sqlite3.Error as e:
            print(f"Error: {e}")
            self.connection.rollback()

        finally:
            self.connection.commit()
            
    def create_table(self):
        try:
            result = self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS user_data (
                    user_id TEXT PRIMARY KEY,
                    user_name TEXT NOT NULL,
                    user_pwd TEXT NOT NULL,
                    admin_type BOOLEAN DEFAULT 0,
                    logged_in INTEGER DEFAULT 0,
                    last_logged_time TEXT                              
                )
            ''')
            if result.fetchall():
                print("Table 'users' created successfully.")
            
            result = self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS account_balance (
                    user_id TEXT PRIMARY KEY,
                    balance  FLOAT default 0.0                             
                )
            ''')
            if result.fetchall():
                print("Table 'account_balance' created successfully.")
            
            result = self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS transactions (
                    user_id TEXT,
                    transaction_time TEXT,
                    primary key (user_id, transaction_time)                        
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
                print("Table 'keytable' created successfully.")            
            self.connection.commit()

        except sqlite3.Error as e:
            print(f"Error: {e}")
            self.connection.rollback()


    def login_execute_query(self, query, param):
        try:
            self.cursor.execute(query, param)          
            return self.cursor
        
        except sqlite3.Error as e:
            print(f"Error: {e}")
            return False
      
    def get_user_details(self, query, param):
        try:
            self.cursor.execute(query,param)
            return self.cursor
        
        except sqlite3.Error as e:
            print(f"Error: {e}")
            return False
    
    def upadte_user_status(self,query,param):
        try:
            result = self.cursor.execute(query, param)
            if result.fetchall():
                print(f"User Updated successfully.")
                self.connection.commit()
        
        except sqlite3.Error as e:
            print(f"Error: {e}")
            self.connection.rollback()
           
        
    def add_user_details(self, query, param):
        try:
            self.cursor.execute(query,param)
            self.connection.commit()
            return self.cursor
        
        except sqlite3.Error as e:
            print(f"Error: {e}")
            self.connection.rollback()
            return False
    
    def update_balance(self, query, param):
        try:
            self.cursor.execute(query,param)
            self.connection.commit()
            return self.cursor
        
        except sqlite3.Error as e:
            print(f"Error: {e}")
            self.connection.rollback()
            return False
    
    def update_trasaction(self, query, param):
        try:
            self.cursor.execute(query,param)
            self.connection.commit()
            return self.cursor
        
        except sqlite3.Error as e:
            print(f"Error: {e}")
            self.connection.rollback()
            return False
        
    def update_user_details(self, query, param):
        try:
            self.cursor.execute(query,param)
            self.connection.commit()
            return self.cursor
            
        except sqlite3.Error as e:
            print(f"Error: {e}")
            self.connection.rollback()
            return False

    def getkeyvalue(self, query):
        try:
            self.cursor.execute(query)
            return self.cursor
                
        except sqlite3.Error as e:
            print(f"Error: {e}")
            return False

    def disconnect(self):
        self.cursor.close()
        self.connection.close()