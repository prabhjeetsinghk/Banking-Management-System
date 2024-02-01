import sqlite3

class UserDatabase:
    def __init__(self, database_name="bank.db"):
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
            if not self.cursor.closed:
                self.cursor.close()    
            
    def create_table(self):
        try:
            # Create a table (you can modify this to create additional tables)
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS user_data (
                    user_id INTEGER PRIMARY KEY,
                    user_email TEXT NOT NULL,
                    user_pwd TEXT NOT NULL,
                    admin_type BOOLEAN,
                    logged_in BOOLEAN,
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

        except sqlite3.Error as e:
            print(f"Error: {e}")

        finally:
            self.connection.commit()

    def login_execute_query(self, query, param):
        try:
            self.cursor.execute(query, param)
            print(f"User created successfully.")
        
        except sqlite3.Error as e:
            print(f"Error: {e}")

        finally:
            return self.cursor
        
    def upadte_user_status(self,query,param):
        try:
            self.cursor.execute(query, param)
            print(f"User Updated successfully.")
        
        except sqlite3.Error as e:
            print(f"Error: {e}")
            self.connection.rollback()

        finally:
            self.connection.commit()

    def get_user_details(self, query, param):
        try:
            self.cursor.execute(query,param)
        
        except sqlite3.Error as e:
            print(f"Error: {e}")

        finally:
            return self.cursor
        
    def add_user_details(self, query, param):
        try:
            self.cursor.execute(query,param)
        
        except sqlite3.Error as e:
            print(f"Error: {e}")
            self.connection.rollback()

        finally:
            self.connection.commit()
            return self.cursor
        
    def update_user_details(self, query, param):
        try:
            self.cursor.execute(query,param)
        
        except sqlite3.Error as e:
            print(f"Error: {e}")
            self.connection.rollback()

        finally:
            self.connection.commit()
            return self.cursor

    def getkeyvalue(self, query):
        self.cursor.execute(query)
        return self.cursor


    def disconnect(self):
        self.cursor.close()
        self.connection.close()