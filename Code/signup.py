from dbConnection1 import UserDatabase
from encdecString import encdec
from datetime import datetime

import streamlit as st
class user_signup:

    def render(self):
        st.title("User Registeration Page")

        # Input Name
        user_name = st.text_input("Enter your name", "")

        # Input Email
        user_email = st.text_input("Enter your email", "")

        # Input Password
        user_email = st.text_input("Enter your password", "", type="password")

        # # Number Input
        # age = st.number_input("Enter your age", 0, 100, 25)

        # Date Input
        birth_date = st.date_input("Select your birth date")

    @staticmethod
    def add_user_details():
        db = UserDatabase()
        st.title("Streamlit App")
        user_name = input("Enter your full name:\n")
        user_email = input("Enter your email:\n")
        user_pwd = input("Enter your password:\n")

        cursor = db.getkeyvalue("select keyValue from keytable")
        rows = cursor.fetchall()
        key = rows[0][0]
        
        print(key)
        
        enc = encdec(key=key)
        hashed = enc.strEncoder(user_pwd)
        admin_type = 0
        sql_query = "INSERT INTO user_data (user_id, user_name, user_pwd, admin_type) VALUES (?, ?, ?, ?)"
        params = (user_email, user_name, hashed, admin_type)
        result = db.add_user_details(query=sql_query,param=params)
        if result.rowcount:
            print('Record Added Successfully')
            balance = 0.0

            add_balance_sql_query = "INSERT INTO account_balance (user_id, balance) VALUES (?,?)"
            params = (user_email,balance)

            db.update_balance(query=add_balance_sql_query, param=params)
            
            current_datetime = datetime.now()
            formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

            add_transaction_sql_query = "INSERT INTO transactions (user_id, transaction_time) VALUES (?, ?)"
            params = (user_email, formatted_datetime)

            db.update_trasaction(query=add_transaction_sql_query, param=params)
        else:
            print("Error occurred while adding user account")
