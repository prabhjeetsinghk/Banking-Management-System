import sqlite3

class UserDatabase:
    def __init__(self, database_name="pythonbank1.db"):
        self.database_name = database_name
        self.connection = sqlite3.connect(self.database_name)
        self.cursor = self.connection.cursor()
        self.key = b'Fin5yZycv9vs7FkmfuWZwOc9DELDmNJ4QfnzvuoIh78='
        self.create_table()
        self.set_key()

    def set_key(self):
        try:
            self.cursor.execute("INSERT INTO keytable (keyValue) VALUES (?)", (self.key,))
            print('Key Added Successfully')
        
        except sqlite3.Error as e:
            print(f"Error: {e}")
            self.connection.rollback()

        finally:
            self.connection.commit()
            
    def create_table(self):
        try:
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS user_data (
                    user_id TEXT PRIMARY KEY,
                    user_name TEXT NOT NULL,
                    user_pwd TEXT NOT NULL,
                    admin_type BOOLEAN DEFAULT 0,
                    logged_in INTEGER DEFAULT 0,
                    last_logged_time TEXT                              
                )
            ''')
            print("Table 'users' created successfully.")

            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS keytable (
                    keyValue TEXT NOT NULL              
                )
            ''')
            print("Table 'keytable' created successfully.")            
            self.connection.commit()

        except sqlite3.Error as e:
            print(f"Error: {e}")
            self.connection.rollback()


    def login_execute_query(self, query, param):
        try:
            self.cursor.execute(query, param)
            print(f"User created successfully.")            
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
            self.cursor.execute(query, param)
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